#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# ///
"""Verify the repo-local MCP server setup for the Ink workspace."""

from __future__ import annotations

import argparse
import json
import os
import select
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
MCP_CONFIG_PATH = REPO_ROOT / ".mcp.json"
PROTOCOL_VERSION = "2024-11-05"
DEFAULT_TIMEOUT_SECONDS = 20.0

CONFIG_CHECKS: dict[str, tuple[Path, tuple[str, ...]]] = {
    "blog-image-finder": (
        REPO_ROOT / ".secrets" / "image-provider.json",
        ("provider", "access_key"),
    ),
    "blog-image-uploader": (
        REPO_ROOT / ".secrets" / "blog-image-s3.json",
        ("bucket", "region", "access_key_id", "secret_access_key"),
    ),
}


class VerificationError(RuntimeError):
    """Raised when a verification step fails."""


def print_status(level: str, message: str) -> None:
    print(f"{level:<5} {message}")


def load_mcp_servers() -> dict[str, Any]:
    if not MCP_CONFIG_PATH.exists():
        raise VerificationError(f"Missing MCP config: {MCP_CONFIG_PATH}")

    try:
        payload = json.loads(MCP_CONFIG_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise VerificationError(f"Invalid JSON in {MCP_CONFIG_PATH}: {exc}") from exc

    servers = payload.get("mcpServers")
    if not isinstance(servers, dict) or not servers:
        raise VerificationError(f"{MCP_CONFIG_PATH} does not contain a non-empty mcpServers object")
    return servers


def normalize_server_names(available: dict[str, Any], selected: list[str]) -> list[str]:
    if not selected:
        return list(available.keys())

    missing = [name for name in selected if name not in available]
    if missing:
        joined = ", ".join(missing)
        raise VerificationError(f"Unknown MCP server(s): {joined}")
    return selected


def validate_command_entry(name: str, entry: Any) -> tuple[list[str], Path]:
    if not isinstance(entry, dict):
        raise VerificationError(f"{name}: .mcp.json entry must be an object")

    command = entry.get("command")
    if command != "uv":
        raise VerificationError(f"{name}: expected command 'uv', found {command!r}")

    args = entry.get("args")
    if not isinstance(args, list) or not all(isinstance(arg, str) for arg in args):
        raise VerificationError(f"{name}: expected args to be a string array")
    if "run" not in args:
        raise VerificationError(f"{name}: expected args to contain 'run'")

    run_index = args.index("run")
    script_arg = next((arg for arg in args[run_index + 1 :] if arg.endswith(".py")), "")
    if not script_arg:
        raise VerificationError(f"{name}: could not find a Python entry script after 'run'")

    script_path = Path(script_arg)
    if not script_path.is_absolute():
        script_path = (REPO_ROOT / script_arg).resolve()
    if not script_path.exists():
        raise VerificationError(f"{name}: entry script not found at {script_path}")
    return [command, *args], script_path


def validate_optional_config(name: str) -> list[tuple[str, str]]:
    check = CONFIG_CHECKS.get(name)
    if not check:
        return []

    path, required_fields = check
    if not path.exists():
        return [("WARN", f"{name}: local config not found at {path}")]

    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [("FAIL", f"{name}: config file is not valid JSON: {exc}")]

    if not isinstance(payload, dict):
        return [("FAIL", f"{name}: config file must be a JSON object")]

    missing_fields = [field for field in required_fields if not isinstance(payload.get(field), str) or not payload.get(field, "").strip()]
    if missing_fields:
        joined = ", ".join(missing_fields)
        return [("FAIL", f"{name}: config is missing required string fields: {joined}")]

    return [("OK", f"{name}: config looks present at {path}")]


def send_message(stdin: Any, payload: dict[str, Any]) -> None:
    body = json.dumps(payload).encode("utf-8")
    stdin.write(f"Content-Length: {len(body)}\r\n\r\n".encode("utf-8"))
    stdin.write(body)
    stdin.flush()


def _remaining_seconds(deadline: float) -> float:
    return max(0.0, deadline - time.monotonic())


def _readline(fd: int, deadline: float) -> bytes:
    chunks: list[bytes] = []
    while True:
        timeout = _remaining_seconds(deadline)
        ready, _, _ = select.select([fd], [], [], timeout)
        if not ready:
            raise VerificationError("Timed out while waiting for MCP response headers")
        chunk = os.read(fd, 1)
        if not chunk:
            raise VerificationError("MCP server closed stdout before responding")
        chunks.append(chunk)
        if chunk == b"\n":
            return b"".join(chunks)


def _readexact(fd: int, size: int, deadline: float) -> bytes:
    chunks: list[bytes] = []
    remaining = size
    while remaining > 0:
        timeout = _remaining_seconds(deadline)
        ready, _, _ = select.select([fd], [], [], timeout)
        if not ready:
            raise VerificationError("Timed out while waiting for an MCP response body")
        chunk = os.read(fd, remaining)
        if not chunk:
            raise VerificationError("MCP server closed stdout before the full response body arrived")
        chunks.append(chunk)
        remaining -= len(chunk)
    return b"".join(chunks)


def read_message(stdout_fd: int, timeout_seconds: float) -> dict[str, Any]:
    deadline = time.monotonic() + timeout_seconds
    headers: dict[str, str] = {}

    while True:
        line = _readline(stdout_fd, deadline)
        if line in {b"\r\n", b"\n"}:
            break
        key, _, value = line.decode("utf-8").partition(":")
        headers[key.strip().lower()] = value.strip()

    try:
        content_length = int(headers.get("content-length", "0"))
    except ValueError as exc:
        raise VerificationError("MCP response did not include a valid Content-Length header") from exc
    if content_length <= 0:
        raise VerificationError("MCP response did not include a positive Content-Length header")

    body = _readexact(stdout_fd, content_length, deadline)
    try:
        payload = json.loads(body.decode("utf-8"))
    except json.JSONDecodeError as exc:
        raise VerificationError("MCP response body was not valid JSON") from exc
    if not isinstance(payload, dict):
        raise VerificationError("MCP response body was not a JSON object")
    return payload


def stop_process(process: subprocess.Popen[bytes]) -> str:
    if process.stdin and not process.stdin.closed:
        process.stdin.close()

    if process.poll() is None:
        process.terminate()
        try:
            process.wait(timeout=3)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait(timeout=3)

    stderr = b""
    if process.stderr:
        stderr = process.stderr.read()
    return stderr.decode("utf-8", errors="replace").strip()


def verify_stdio_server(name: str, command: list[str], timeout_seconds: float) -> tuple[str, list[str]]:
    process = subprocess.Popen(
        command,
        cwd=REPO_ROOT,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    try:
        assert process.stdin is not None
        assert process.stdout is not None

        send_message(
            process.stdin,
            {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "initialize",
                "params": {
                    "protocolVersion": PROTOCOL_VERSION,
                    "capabilities": {},
                    "clientInfo": {"name": "ink-mcp-verify", "version": "0.1.0"},
                },
            },
        )
        init_response = read_message(process.stdout.fileno(), timeout_seconds)
        if "error" in init_response:
            raise VerificationError(f"{name}: initialize failed: {init_response['error']}")

        result = init_response.get("result")
        if not isinstance(result, dict):
            raise VerificationError(f"{name}: initialize response did not include a result object")

        server_info = result.get("serverInfo")
        if not isinstance(server_info, dict):
            raise VerificationError(f"{name}: initialize response did not include serverInfo")
        server_label = f"{server_info.get('name', name)} {server_info.get('version', '').strip()}".strip()

        send_message(
            process.stdin,
            {
                "jsonrpc": "2.0",
                "method": "notifications/initialized",
                "params": {},
            },
        )
        send_message(
            process.stdin,
            {
                "jsonrpc": "2.0",
                "id": 2,
                "method": "tools/list",
                "params": {},
            },
        )
        tools_response = read_message(process.stdout.fileno(), timeout_seconds)
        if "error" in tools_response:
            raise VerificationError(f"{name}: tools/list failed: {tools_response['error']}")

        tools_result = tools_response.get("result")
        if not isinstance(tools_result, dict):
            raise VerificationError(f"{name}: tools/list response did not include a result object")

        tools = tools_result.get("tools")
        if not isinstance(tools, list):
            raise VerificationError(f"{name}: tools/list response did not include a tools array")

        tool_names = [tool.get("name", "<unknown>") for tool in tools if isinstance(tool, dict)]
        return server_label, tool_names
    except BrokenPipeError as exc:
        raise VerificationError(f"{name}: server exited before the MCP handshake completed") from exc
    finally:
        stderr = stop_process(process)
        if process.returncode not in {0, -15, -9, None} and stderr:
            print_status("INFO", f"{name}: stderr after shutdown\n{stderr}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("servers", nargs="*", help="Optional MCP server names to verify")
    parser.add_argument(
        "--timeout-seconds",
        type=float,
        default=DEFAULT_TIMEOUT_SECONDS,
        help=f"Seconds to wait for each MCP response (default: {DEFAULT_TIMEOUT_SECONDS:g})",
    )
    args = parser.parse_args()

    if shutil.which("uv") is None:
        print_status("FAIL", "uv is not installed or not on PATH")
        return 1
    print_status("OK", f"uv found on PATH: {shutil.which('uv')}")

    try:
        servers = load_mcp_servers()
        selected = normalize_server_names(servers, args.servers)
    except VerificationError as exc:
        print_status("FAIL", str(exc))
        return 1

    print_status("OK", f"Loaded MCP config from {MCP_CONFIG_PATH}")

    failures = 0
    warnings = 0

    for name in selected:
        print_status("INFO", f"Verifying {name}")

        try:
            command, script_path = validate_command_entry(name, servers[name])
            print_status("OK", f"{name}: registered as {' '.join(command)}")
            print_status("OK", f"{name}: entry script exists at {script_path}")
        except VerificationError as exc:
            print_status("FAIL", str(exc))
            failures += 1
            continue

        config_failed = False
        for level, message in validate_optional_config(name):
            print_status(level, message)
            if level == "FAIL":
                failures += 1
                config_failed = True
            elif level == "WARN":
                warnings += 1

        if config_failed:
            continue

        try:
            server_label, tool_names = verify_stdio_server(name, command, args.timeout_seconds)
            joined_tools = ", ".join(tool_names) if tool_names else "<none>"
            print_status("OK", f"{name}: MCP handshake succeeded with {server_label}")
            print_status("OK", f"{name}: tools = {joined_tools}")
        except VerificationError as exc:
            print_status("FAIL", str(exc))
            failures += 1

    summary = f"Verification complete: {len(selected) - failures} passed, {warnings} warnings, {failures} failed"
    if failures:
        print_status("FAIL", summary)
        return 1

    if warnings:
        print_status("WARN", summary)
    else:
        print_status("OK", summary)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
