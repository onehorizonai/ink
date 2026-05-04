#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# ///
from __future__ import annotations

import hashlib
import hmac
import json
import mimetypes
import re
import sys
import traceback
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any


SERVER_NAME = "blog-image-uploader"
SERVER_VERSION = "0.1.0"
PROTOCOL_VERSION = "2024-11-05"

REPO_ROOT = Path(__file__).resolve().parents[4]
CONFIG_PATH = REPO_ROOT / ".secrets" / "blog-image-s3.json"
SERVICE = "s3"

TOOLS = [
    {
        "name": "upload_image",
        "description": "Upload a local image file into the configured blog image S3 bucket.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "local_path": {"type": "string"},
                "object_key": {"type": "string"},
                "prefix": {"type": "string"},
                "overwrite": {"type": "boolean", "default": False},
                "content_type": {"type": "string"},
            },
            "required": ["local_path"],
            "additionalProperties": False,
        },
    }
]


class ToolError(Exception):
    def __init__(self, error_type: str, message: str, *, details: dict[str, Any] | None = None) -> None:
        super().__init__(message)
        self.error_type = error_type
        self.details = details or {}


@dataclass(frozen=True)
class UploaderConfig:
    bucket: str
    region: str
    access_key_id: str
    secret_access_key: str
    session_token: str | None
    endpoint_url: str | None
    public_base_url: str | None
    key_prefix: str
    history_path: Path
    addressing_style: str
    timeout_seconds: int


class UploadHistory:
    def __init__(self, path: Path) -> None:
        self.path = path

    def load(self) -> dict[str, Any]:
        if not self.path.exists():
            return {"items": {}}

        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise ToolError(
                "invalid_config",
                "The configured upload history file is not valid JSON.",
                details={"path": str(self.path), "reason": str(exc)},
            ) from exc

        if not isinstance(data, dict) or not isinstance(data.get("items", {}), dict):
            raise ToolError(
                "invalid_config",
                "The configured upload history file must contain an object with an items map.",
                details={"path": str(self.path)},
            )
        return data

    def add(self, object_key: str, record: dict[str, Any]) -> None:
        payload = self.load()
        payload.setdefault("items", {})[object_key] = record
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


class S3Client:
    def __init__(self, config: UploaderConfig) -> None:
        self.config = config

    def object_exists(self, object_key: str) -> bool:
        url, host, canonical_uri = self._build_request_target(object_key)
        headers = self._signed_headers("HEAD", host, canonical_uri, "", "", {})
        request = urllib.request.Request(url, method="HEAD", headers=headers)
        try:
            with urllib.request.urlopen(request, timeout=self.config.timeout_seconds):
                return True
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return False
            raise self._map_http_error(exc) from exc
        except urllib.error.URLError as exc:
            raise ToolError(
                "provider_request_failed",
                "The S3 endpoint could not be reached.",
                details={"reason": str(exc.reason)},
            ) from exc

    def upload_object(self, object_key: str, content: bytes, content_type: str) -> dict[str, Any]:
        url, host, canonical_uri = self._build_request_target(object_key)
        payload_hash = hashlib.sha256(content).hexdigest()
        extra_headers = {"content-type": content_type}
        headers = self._signed_headers("PUT", host, canonical_uri, "", payload_hash, extra_headers)
        request = urllib.request.Request(url, method="PUT", data=content, headers=headers)
        try:
            with urllib.request.urlopen(request, timeout=self.config.timeout_seconds) as response:
                return {
                    "etag": response.headers.get("ETag", "").strip('"'),
                    "status": response.status,
                }
        except urllib.error.HTTPError as exc:
            raise self._map_http_error(exc) from exc
        except urllib.error.URLError as exc:
            raise ToolError(
                "upload_failure",
                "The image upload failed before completion.",
                details={"reason": str(exc.reason)},
            ) from exc

    def public_url(self, object_key: str) -> str:
        encoded_key = encode_key(object_key)
        if self.config.public_base_url:
            return f"{self.config.public_base_url.rstrip('/')}/{encoded_key}"

        url, _, _ = self._build_request_target(object_key)
        return url

    def _build_request_target(self, object_key: str) -> tuple[str, str, str]:
        encoded_key = encode_key(object_key)
        if self.config.endpoint_url:
            base = urllib.parse.urlparse(self.config.endpoint_url)
            scheme = base.scheme or "https"
            base_path = base.path.rstrip("/")
            endpoint_host = base.netloc
        else:
            scheme = "https"
            base_path = ""
            endpoint_host = f"s3.{self.config.region}.amazonaws.com"

        if self.config.addressing_style == "path":
            host = endpoint_host
            canonical_uri = f"{base_path}/{self.config.bucket}/{encoded_key}"
        else:
            host = f"{self.config.bucket}.{endpoint_host}"
            canonical_uri = f"{base_path}/{encoded_key}"

        canonical_uri = "/" + canonical_uri.strip("/")
        url = f"{scheme}://{host}{canonical_uri}"
        return url, host, canonical_uri

    def _signed_headers(
        self,
        method: str,
        host: str,
        canonical_uri: str,
        canonical_querystring: str,
        payload_hash: str,
        extra_headers: dict[str, str],
    ) -> dict[str, str]:
        now = datetime.now(timezone.utc)
        amz_date = now.strftime("%Y%m%dT%H%M%SZ")
        date_stamp = now.strftime("%Y%m%d")
        effective_payload_hash = payload_hash or hashlib.sha256(b"").hexdigest()

        headers = {
            "host": host,
            "x-amz-content-sha256": effective_payload_hash,
            "x-amz-date": amz_date,
            **{key.lower(): value for key, value in extra_headers.items()},
        }
        if self.config.session_token:
            headers["x-amz-security-token"] = self.config.session_token

        signed_header_names = sorted(headers.keys())
        canonical_headers = "".join(f"{name}:{headers[name].strip()}\n" for name in signed_header_names)
        signed_headers = ";".join(signed_header_names)
        canonical_request = "\n".join(
            [
                method,
                canonical_uri,
                canonical_querystring,
                canonical_headers,
                signed_headers,
                effective_payload_hash,
            ]
        )

        credential_scope = f"{date_stamp}/{self.config.region}/{SERVICE}/aws4_request"
        string_to_sign = "\n".join(
            [
                "AWS4-HMAC-SHA256",
                amz_date,
                credential_scope,
                hashlib.sha256(canonical_request.encode("utf-8")).hexdigest(),
            ]
        )

        signing_key = build_signature_key(self.config.secret_access_key, date_stamp, self.config.region, SERVICE)
        signature = hmac.new(signing_key, string_to_sign.encode("utf-8"), hashlib.sha256).hexdigest()
        authorization = (
            "AWS4-HMAC-SHA256 "
            f"Credential={self.config.access_key_id}/{credential_scope}, "
            f"SignedHeaders={signed_headers}, Signature={signature}"
        )

        return {
            "Authorization": authorization,
            "Host": host,
            "x-amz-content-sha256": effective_payload_hash,
            "x-amz-date": amz_date,
            **({"x-amz-security-token": self.config.session_token} if self.config.session_token else {}),
            **extra_headers,
        }

    def _map_http_error(self, exc: urllib.error.HTTPError) -> ToolError:
        body = exc.read().decode("utf-8", errors="replace")
        details = {"status": exc.code}
        if body:
            details["body"] = body[:500]
        if exc.code in {401, 403}:
            return ToolError("bad_api_credentials", "The configured S3 credentials were rejected.", details=details)
        if exc.code == 404:
            return ToolError("provider_request_failed", "The configured S3 resource was not found.", details=details)
        return ToolError("upload_failure", "The S3 request failed.", details=details)


def read_message() -> dict[str, Any] | None:
    headers: dict[str, str] = {}
    while True:
        line = sys.stdin.buffer.readline()
        if not line:
            return None
        if line in {b"\r\n", b"\n"}:
            break
        key, _, value = line.decode("utf-8").partition(":")
        headers[key.strip().lower()] = value.strip()

    length = int(headers.get("content-length", "0"))
    if length <= 0:
        return None

    body = sys.stdin.buffer.read(length)
    if not body:
        return None
    return json.loads(body.decode("utf-8"))


def send_message(payload: dict[str, Any]) -> None:
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    header = f"Content-Length: {len(body)}\r\n\r\n".encode("utf-8")
    sys.stdout.buffer.write(header)
    sys.stdout.buffer.write(body)
    sys.stdout.buffer.flush()


def send_response(message_id: Any, result: dict[str, Any]) -> None:
    send_message({"jsonrpc": "2.0", "id": message_id, "result": result})


def load_config() -> UploaderConfig:
    if not CONFIG_PATH.exists():
        raise ToolError(
            "missing_config",
            "Missing S3 upload config. Create .secrets/blog-image-s3.json before using this server.",
            details={"path": str(CONFIG_PATH)},
        )

    try:
        raw = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ToolError(
            "invalid_config",
            "The S3 upload config file is not valid JSON.",
            details={"path": str(CONFIG_PATH), "reason": str(exc)},
        ) from exc

    if not isinstance(raw, dict):
        raise ToolError("invalid_config", "The S3 upload config must be a JSON object.", details={"path": str(CONFIG_PATH)})

    required_fields = ["bucket", "region", "access_key_id", "secret_access_key"]
    missing = [field for field in required_fields if not isinstance(raw.get(field), str) or not str(raw.get(field)).strip()]
    if missing:
        raise ToolError(
            "invalid_config",
            "The S3 upload config is missing required string fields.",
            details={"missing_fields": missing, "path": str(CONFIG_PATH)},
        )

    addressing_style = str(raw.get("addressing_style", "virtual")).strip() or "virtual"
    if addressing_style not in {"virtual", "path"}:
        raise ToolError(
            "invalid_config",
            "addressing_style must be either 'virtual' or 'path'.",
            details={"path": str(CONFIG_PATH)},
        )

    timeout_raw = raw.get("timeout_seconds", 30)
    if not isinstance(timeout_raw, int) or timeout_raw <= 0:
        raise ToolError(
            "invalid_config",
            "timeout_seconds must be a positive integer when provided.",
            details={"path": str(CONFIG_PATH)},
        )

    endpoint_url = raw.get("endpoint_url")
    if endpoint_url is not None and (not isinstance(endpoint_url, str) or not endpoint_url.strip()):
        raise ToolError("invalid_config", "endpoint_url must be a non-empty string when provided.", details={"path": str(CONFIG_PATH)})

    public_base_url = raw.get("public_base_url")
    if public_base_url is not None and (not isinstance(public_base_url, str) or not public_base_url.strip()):
        raise ToolError("invalid_config", "public_base_url must be a non-empty string when provided.", details={"path": str(CONFIG_PATH)})

    key_prefix = str(raw.get("key_prefix", "")).strip().strip("/")
    history_path_raw = raw.get("history_path")
    if history_path_raw is None:
        history_path = REPO_ROOT / ".secrets" / "blog-image-upload-history.json"
    elif isinstance(history_path_raw, str) and history_path_raw.strip():
        history_path = resolve_repo_path(history_path_raw)
    else:
        raise ToolError("invalid_config", "history_path must be a non-empty string when provided.", details={"path": str(CONFIG_PATH)})

    return UploaderConfig(
        bucket=str(raw["bucket"]).strip(),
        region=str(raw["region"]).strip(),
        access_key_id=str(raw["access_key_id"]).strip(),
        secret_access_key=str(raw["secret_access_key"]).strip(),
        session_token=(str(raw.get("session_token", "")).strip() or None),
        endpoint_url=(str(endpoint_url).strip() if isinstance(endpoint_url, str) else None),
        public_base_url=(str(public_base_url).strip().rstrip("/") if isinstance(public_base_url, str) else None),
        key_prefix=key_prefix,
        history_path=history_path,
        addressing_style=addressing_style,
        timeout_seconds=timeout_raw,
    )


def resolve_repo_path(raw_path: str) -> Path:
    path = Path(raw_path).expanduser()
    if path.is_absolute():
        return path
    return (REPO_ROOT / path).resolve()


def encode_key(key: str) -> str:
    return "/".join(urllib.parse.quote(part, safe="-_.~") for part in key.split("/"))


def build_signature_key(secret_key: str, date_stamp: str, region: str, service: str) -> bytes:
    k_date = hmac.new(("AWS4" + secret_key).encode("utf-8"), date_stamp.encode("utf-8"), hashlib.sha256).digest()
    k_region = hmac.new(k_date, region.encode("utf-8"), hashlib.sha256).digest()
    k_service = hmac.new(k_region, service.encode("utf-8"), hashlib.sha256).digest()
    return hmac.new(k_service, b"aws4_request", hashlib.sha256).digest()


def normalize_content_type(local_path: Path, provided: Any) -> str:
    if provided is not None:
        if not isinstance(provided, str) or not provided.strip():
            raise ToolError("invalid_input", "content_type must be a non-empty string when provided.")
        content_type = provided.strip()
    else:
        guessed, _ = mimetypes.guess_type(str(local_path))
        content_type = guessed or "application/octet-stream"

    if not content_type.startswith("image/"):
        raise ToolError("invalid_input", f"Only image uploads are supported. Detected content type: {content_type}")
    return content_type


def resolve_local_path(raw_path: str) -> Path:
    path = Path(raw_path).expanduser()
    if path.is_absolute():
        return path
    return (REPO_ROOT / path).resolve()


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "image"


def sanitize_object_key(raw_key: str) -> str:
    cleaned = raw_key.replace("\\", "/").strip("/")
    if not cleaned:
        raise ToolError("invalid_input", "object_key must not be empty.")

    parts: list[str] = []
    for part in PurePosixPath(cleaned).parts:
        if part in {"", "."}:
            continue
        if part == "..":
            raise ToolError("invalid_input", "object_key must not contain parent directory segments.")
        stem, suffix = split_suffix(part)
        parts.append(f"{slugify(stem)}{suffix.lower()}")

    normalized = "/".join(parts)
    if not normalized:
        raise ToolError("invalid_input", "object_key must contain at least one valid path segment.")
    return normalized


def split_suffix(filename: str) -> tuple[str, str]:
    path = Path(filename)
    suffix = path.suffix if path.suffix else ""
    stem = path.stem if suffix else filename
    return stem, suffix


def build_object_key(config: UploaderConfig, local_path: Path, arguments: dict[str, Any]) -> str:
    if "object_key" in arguments and arguments["object_key"] is not None:
        key = sanitize_object_key(str(arguments["object_key"]))
    else:
        stem = slugify(local_path.stem)
        suffix = local_path.suffix.lower() or ".jpg"
        filename = f"{stem}{suffix}"
        extra_prefix = ""
        if "prefix" in arguments and arguments["prefix"] is not None:
            extra_prefix = sanitize_object_key(str(arguments["prefix"])).strip("/")
        segments = [segment for segment in [config.key_prefix, extra_prefix, filename] if segment]
        key = "/".join(segments)

    return sanitize_object_key(key)


def call_tool(name: str, arguments: dict[str, Any]) -> dict[str, Any]:
    if name != "upload_image":
        raise ToolError("provider_request_failed", f"Unknown tool: {name}")

    config = load_config()
    client = S3Client(config)
    history = UploadHistory(config.history_path)

    local_path_raw = str(arguments.get("local_path", "")).strip()
    if not local_path_raw:
        raise ToolError("invalid_input", "upload_image requires a non-empty local_path.")

    local_path = resolve_local_path(local_path_raw)
    if not local_path.exists():
        raise ToolError("file_not_found", f"Local file not found: {local_path}")
    if not local_path.is_file():
        raise ToolError("invalid_input", f"Local path is not a file: {local_path}")

    content_type = normalize_content_type(local_path, arguments.get("content_type"))
    object_key = build_object_key(config, local_path, arguments)
    overwrite_raw = arguments.get("overwrite", False)
    if not isinstance(overwrite_raw, bool):
        raise ToolError("invalid_input", "overwrite must be a boolean when provided.")
    overwrite = overwrite_raw

    if not overwrite and client.object_exists(object_key):
        raise ToolError(
            "object_exists",
            f"The target object already exists: {object_key}",
            details={"bucket": config.bucket, "object_key": object_key},
        )

    payload = local_path.read_bytes()
    upload_result = client.upload_object(object_key, payload, content_type)
    public_url = client.public_url(object_key)
    record = {
        "local_path": str(local_path),
        "object_key": object_key,
        "bucket": config.bucket,
        "public_url": public_url,
        "content_type": content_type,
        "bytes_uploaded": len(payload),
        "uploaded_at": datetime.now(timezone.utc).isoformat(),
        "etag": upload_result.get("etag", ""),
    }
    history.add(object_key, record)

    return {
        "success": True,
        "local_path": str(local_path),
        "bucket": config.bucket,
        "object_key": object_key,
        "public_url": public_url,
        "etag": upload_result.get("etag", ""),
        "content_type": content_type,
        "bytes_uploaded": len(payload),
    }


def tool_result_payload(result: dict[str, Any], *, is_error: bool) -> dict[str, Any]:
    return {
        "content": [{"type": "text", "text": json.dumps(result, indent=2, ensure_ascii=False)}],
        "isError": is_error,
    }


def main() -> int:
    while True:
        message = read_message()
        if message is None:
            return 0

        message_id = message.get("id")
        method = message.get("method")

        try:
            if method == "initialize":
                send_response(
                    message_id,
                    {
                        "protocolVersion": PROTOCOL_VERSION,
                        "capabilities": {"tools": {}},
                        "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
                    },
                )
            elif method == "notifications/initialized":
                continue
            elif method == "ping":
                send_response(message_id, {})
            elif method == "tools/list":
                send_response(message_id, {"tools": TOOLS})
            elif method == "tools/call":
                params = message.get("params", {})
                name = str(params.get("name"))
                arguments = dict(params.get("arguments", {}))
                result = call_tool(name, arguments)
                send_response(message_id, tool_result_payload(result, is_error=False))
            else:
                send_response(
                    message_id,
                    tool_result_payload(
                        {
                            "ok": False,
                            "error": {
                                "type": "provider_request_failed",
                                "message": f"Method not found: {method}",
                            },
                        },
                        is_error=True,
                    ),
                )
        except ToolError as exc:
            send_response(
                message_id,
                tool_result_payload(
                    {
                        "ok": False,
                        "error": {
                            "type": exc.error_type,
                            "message": str(exc),
                            "details": exc.details,
                        },
                    },
                    is_error=True,
                ),
            )
        except Exception as exc:  # pragma: no cover
            send_response(
                message_id,
                tool_result_payload(
                    {
                        "ok": False,
                        "error": {
                            "type": "internal_error",
                            "message": "Unexpected server failure.",
                            "details": {
                                "error": "".join(traceback.format_exception_only(type(exc), exc)).strip(),
                            },
                        },
                    },
                    is_error=True,
                ),
            )


if __name__ == "__main__":
    sys.exit(main())
