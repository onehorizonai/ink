#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# ///
from __future__ import annotations

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
from pathlib import Path
from typing import Any


SERVER_NAME = "blog-image-finder"
SERVER_VERSION = "0.1.0"
PROTOCOL_VERSION = "2024-11-05"

REPO_ROOT = Path(__file__).resolve().parents[4]
CONFIG_PATH = REPO_ROOT / ".secrets" / "image-provider.json"

TOOLS = [
    {
        "name": "search_images",
        "description": "Search Unsplash for fresh candidate blog images that have not been downloaded before.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {"type": "string"},
                "orientation": {
                    "type": "string",
                    "enum": ["landscape", "portrait", "squarish"],
                },
                "limit": {"type": "integer", "minimum": 1, "maximum": 20, "default": 6},
            },
            "required": ["query"],
            "additionalProperties": False,
        },
    },
    {
        "name": "download_image",
        "description": "Download a selected Unsplash image into the configured local staging folder.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "image_id": {"type": "string"},
            },
            "required": ["image_id"],
            "additionalProperties": False,
        },
    },
]

LICENSE_SUMMARY = (
    "Unsplash images are subject to the Unsplash License and API terms. Review current usage "
    "rights, restrictions, and attribution expectations before publication."
)
PROVIDER_USAGE_NOTES = (
    "Keep the provider name, source URL, and photographer credit with the asset. Use the "
    "provider download flow so the attribution metadata stays attached."
)


class ToolError(Exception):
    def __init__(self, error_type: str, message: str, *, details: dict[str, Any] | None = None) -> None:
        super().__init__(message)
        self.error_type = error_type
        self.details = details or {}


@dataclass(frozen=True)
class FinderConfig:
    provider: str
    access_key: str
    download_dir: Path
    history_path: Path
    timeout_seconds: int


class DownloadHistory:
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
                "The configured image history file is not valid JSON.",
                details={"path": str(self.path), "reason": str(exc)},
            ) from exc

        if not isinstance(data, dict) or not isinstance(data.get("items", {}), dict):
            raise ToolError(
                "invalid_config",
                "The configured image history file must contain an object with an items map.",
                details={"path": str(self.path)},
            )
        return data

    def downloaded_ids(self) -> set[str]:
        return set(self.load().get("items", {}).keys())

    def add(self, image_id: str, record: dict[str, Any]) -> None:
        payload = self.load()
        payload.setdefault("items", {})[image_id] = record
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


class UnsplashProvider:
    def __init__(self, config: FinderConfig) -> None:
        self.config = config

    def search_images(self, query: str, orientation: str | None, limit: int, downloaded_ids: set[str]) -> dict[str, Any]:
        collected: list[dict[str, Any]] = []
        page = 1
        seen_ids: set[str] = set()
        per_page = min(max(limit * 3, 10), 30)

        while len(collected) < limit and page <= 5:
            params = {
                "query": query,
                "page": str(page),
                "per_page": str(per_page),
            }
            if orientation:
                params["orientation"] = orientation

            response = self._request_json(
                "https://api.unsplash.com/search/photos?" + urllib.parse.urlencode(params),
            )

            results = response.get("results", [])
            if not isinstance(results, list) or not results:
                break

            for result in results:
                if not isinstance(result, dict):
                    continue
                image_id = str(result.get("id", "")).strip()
                if not image_id or image_id in downloaded_ids or image_id in seen_ids:
                    continue
                collected.append(self._format_result(result))
                seen_ids.add(image_id)
                if len(collected) >= limit:
                    break

            total_pages = int(response.get("total_pages") or 0)
            if total_pages and page >= total_pages:
                break
            page += 1

        return {
            "provider": "unsplash",
            "query": query,
            "results": collected,
        }

    def get_image(self, image_id: str) -> dict[str, Any]:
        try:
            image = self._request_json(f"https://api.unsplash.com/photos/{urllib.parse.quote(image_id, safe='')}")
        except ToolError as exc:
            if exc.error_type == "provider_request_failed" and exc.details.get("status") == 404:
                raise ToolError("image_not_found", f"Unsplash image '{image_id}' was not found.") from exc
            raise
        if not isinstance(image, dict):
            raise ToolError("image_not_found", f"Unsplash image '{image_id}' returned an invalid payload.")
        return image

    def resolve_download_url(self, image: dict[str, Any]) -> str:
        links = image.get("links", {})
        if not isinstance(links, dict) or not isinstance(links.get("download_location"), str):
            raise ToolError("download_failure", "Unsplash did not return a download location for the selected image.")
        payload = self._request_json(str(links["download_location"]))
        url = payload.get("url") if isinstance(payload, dict) else None
        if not isinstance(url, str) or not url:
            raise ToolError("download_failure", "Unsplash did not return a downloadable image URL.")
        return url

    def download_binary(self, url: str) -> tuple[bytes, str]:
        request = urllib.request.Request(url, headers={"User-Agent": SERVER_NAME})
        try:
            with urllib.request.urlopen(request, timeout=self.config.timeout_seconds) as response:
                return response.read(), response.headers.get("Content-Type", "application/octet-stream")
        except urllib.error.HTTPError as exc:
            raise ToolError(
                "download_failure",
                "The selected image could not be downloaded.",
                details={"status": exc.code},
            ) from exc
        except urllib.error.URLError as exc:
            raise ToolError(
                "download_failure",
                "The selected image download failed before completion.",
                details={"reason": str(exc.reason)},
            ) from exc

    def _request_json(self, url: str) -> dict[str, Any]:
        request = urllib.request.Request(
            url,
            headers={
                "Accept": "application/json",
                "Authorization": f"Client-ID {self.config.access_key}",
                "User-Agent": SERVER_NAME,
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=self.config.timeout_seconds) as response:
                raw = response.read()
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            raise self._map_http_error(exc.code, body) from exc
        except urllib.error.URLError as exc:
            raise ToolError(
                "provider_request_failed",
                "Unsplash could not be reached.",
                details={"reason": str(exc.reason)},
            ) from exc

        try:
            payload = json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError as exc:
            raise ToolError("provider_request_failed", "Unsplash returned invalid JSON.") from exc
        if not isinstance(payload, dict):
            raise ToolError("provider_request_failed", "Unsplash returned an unexpected JSON payload.")
        return payload

    def _map_http_error(self, status: int, body: str) -> ToolError:
        details = {"status": status}
        if body:
            details["body"] = body[:500]
        if status in {401, 403}:
            return ToolError("bad_api_credentials", "Unsplash rejected the configured API credentials.", details=details)
        if status == 404:
            return ToolError("provider_request_failed", "Unsplash did not find the requested resource.", details=details)
        if status == 429:
            return ToolError("rate_limited", "Unsplash rate-limited the request.", details=details)
        return ToolError("provider_request_failed", "Unsplash request failed.", details=details)

    def _format_result(self, raw: dict[str, Any]) -> dict[str, Any]:
        image_id = str(raw.get("id", "")).strip()
        title = str(raw.get("description") or raw.get("alt_description") or f"Unsplash photo {image_id}")
        photographer_name = self._extract_photographer_name(raw)
        preview_url = str(raw.get("urls", {}).get("small") or raw.get("urls", {}).get("thumb") or "")
        source_page_url = str(raw.get("links", {}).get("html") or "")
        return {
            "id": image_id,
            "title": title,
            "preview_url": preview_url,
            "source_page_url": source_page_url,
            "photographer_name": photographer_name,
            "attribution_text": format_attribution_text(photographer_name),
            "license_summary": LICENSE_SUMMARY,
            "provider_usage_notes": PROVIDER_USAGE_NOTES,
        }

    def extract_photographer_name(self, raw: dict[str, Any]) -> str:
        return self._extract_photographer_name(raw)

    def _extract_photographer_name(self, raw: dict[str, Any]) -> str:
        user = raw.get("user", {})
        if isinstance(user, dict) and isinstance(user.get("name"), str) and user["name"].strip():
            return user["name"].strip()
        return "Unknown photographer"


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


def load_config() -> FinderConfig:
    if not CONFIG_PATH.exists():
        raise ToolError(
            "missing_config",
            "Missing image provider config. Create .secrets/image-provider.json before using this server.",
            details={"path": str(CONFIG_PATH)},
        )

    try:
        raw = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ToolError(
            "invalid_config",
            "The image provider config file is not valid JSON.",
            details={"path": str(CONFIG_PATH), "reason": str(exc)},
        ) from exc

    if not isinstance(raw, dict):
        raise ToolError("invalid_config", "The image provider config must be a JSON object.", details={"path": str(CONFIG_PATH)})

    provider = str(raw.get("provider", "")).strip() or "unsplash"
    if provider != "unsplash":
        raise ToolError(
            "invalid_config",
            "Only the unsplash provider is supported by this server right now.",
            details={"provider": provider},
        )

    access_key = str(raw.get("access_key", "")).strip()
    if not access_key:
        access_key = str(raw.get("api_key", "")).strip()
    if not access_key:
        access_key = str(raw.get("client_id", "")).strip()
    if not access_key:
        raise ToolError(
            "invalid_config",
            "The image provider config must include a non-empty access_key. api_key and client_id are accepted as backward-compatible aliases.",
            details={"path": str(CONFIG_PATH)},
        )

    download_dir_raw = raw.get("download_dir")
    if not isinstance(download_dir_raw, str) or not download_dir_raw.strip():
        raise ToolError(
            "invalid_config",
            "The image provider config must include a non-empty download_dir string.",
            details={"path": str(CONFIG_PATH)},
        )

    timeout_raw = raw.get("timeout_seconds", 30)
    if not isinstance(timeout_raw, int) or timeout_raw <= 0:
        raise ToolError(
            "invalid_config",
            "timeout_seconds must be a positive integer when provided.",
            details={"path": str(CONFIG_PATH)},
        )

    download_dir = resolve_repo_path(download_dir_raw)
    download_dir.mkdir(parents=True, exist_ok=True)

    history_path_raw = raw.get("history_path")
    if history_path_raw is None:
        history_path = download_dir / ".image-download-history.json"
    elif isinstance(history_path_raw, str) and history_path_raw.strip():
        history_path = resolve_repo_path(history_path_raw)
    else:
        raise ToolError(
            "invalid_config",
            "history_path must be a non-empty string when provided.",
            details={"path": str(CONFIG_PATH)},
        )

    return FinderConfig(
        provider=provider,
        access_key=access_key,
        download_dir=download_dir,
        history_path=history_path,
        timeout_seconds=timeout_raw,
    )


def resolve_repo_path(raw_path: str) -> Path:
    path = Path(raw_path).expanduser()
    if path.is_absolute():
        return path
    return (REPO_ROOT / path).resolve()


def format_attribution_text(photographer_name: str) -> str:
    return f"Photo by {photographer_name} on Unsplash"


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "image"


def extension_from_content_type(content_type: str) -> str:
    mime_type = content_type.split(";", 1)[0].strip().lower()
    extension = mimetypes.guess_extension(mime_type) or ""
    if extension == ".jpe":
        return ".jpg"
    return extension or ".jpg"


def filename_for_image(image: dict[str, Any], content_type: str) -> str:
    image_id = str(image.get("id", "")).strip() or "unknown"
    title = str(image.get("description") or image.get("alt_description") or f"unsplash-{image_id}")
    extension = extension_from_content_type(content_type)
    prefix = datetime.now(timezone.utc).strftime("%Y%m%d")
    title_slug = slugify(title)[:80].rstrip("-")
    return f"{prefix}-{title_slug}-{image_id}{extension}"


def call_tool(name: str, arguments: dict[str, Any]) -> dict[str, Any]:
    config = load_config()
    history = DownloadHistory(config.history_path)
    provider = UnsplashProvider(config)

    if name == "search_images":
        query = str(arguments.get("query", "")).strip()
        if not query:
            raise ToolError("invalid_input", "search_images requires a non-empty query.")
        orientation = arguments.get("orientation")
        if orientation is not None and not isinstance(orientation, str):
            raise ToolError("invalid_input", "orientation must be a string when provided.")
        if isinstance(orientation, str) and orientation not in {"landscape", "portrait", "squarish"}:
            raise ToolError("invalid_input", "orientation must be one of landscape, portrait, or squarish.")

        limit_raw = arguments.get("limit", 6)
        if isinstance(limit_raw, bool) or not isinstance(limit_raw, int):
            raise ToolError("invalid_input", "limit must be an integer when provided.")
        if limit_raw < 1 or limit_raw > 20:
            raise ToolError("invalid_input", "limit must be between 1 and 20.")
        limit = limit_raw
        return provider.search_images(query, orientation, limit, history.downloaded_ids())

    if name == "download_image":
        image_id = str(arguments.get("image_id", "")).strip()
        if not image_id:
            raise ToolError("invalid_input", "download_image requires a non-empty image_id.")
        if image_id in history.downloaded_ids():
            raise ToolError(
                "image_already_downloaded",
                f"Image '{image_id}' is already recorded in the local download history.",
            )
        image = provider.get_image(image_id)
        download_url = provider.resolve_download_url(image)
        binary, content_type = provider.download_binary(download_url)
        filename = filename_for_image(image, content_type)
        local_path = config.download_dir / filename
        local_path.write_bytes(binary)

        photographer_name = provider.extract_photographer_name(image)
        source_page_url = str(image.get("links", {}).get("html") or "")
        record = {
            "provider": "unsplash",
            "filename": filename,
            "local_path": str(local_path),
            "source_page_url": source_page_url,
            "photographer_name": photographer_name,
            "attribution_text": format_attribution_text(photographer_name),
            "license_summary": LICENSE_SUMMARY,
            "downloaded_at": datetime.now(timezone.utc).isoformat(),
        }
        history.add(image_id, record)

        return {
            "success": True,
            "local_path": str(local_path),
            "filename": filename,
            "source_page_url": source_page_url,
            "photographer_name": photographer_name,
            "attribution_text": format_attribution_text(photographer_name),
            "license_summary": LICENSE_SUMMARY,
            "provider": "unsplash",
        }

    raise ToolError("provider_request_failed", f"Unknown tool: {name}")


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
