# Blog Image Finder Setup

## Config

The local MCP server reads this file on startup:

- `.secrets/image-provider.json`

If the file is missing or invalid, the server returns a structured config error and does not use fallback secrets.

Example:

```json
{
  "provider": "unsplash",
  "access_key": "YOUR_UNSPLASH_ACCESS_KEY",
  "download_dir": "./.secrets/downloads/blog-images",
  "history_path": "./.secrets/image-download-history.json",
  "timeout_seconds": 30
}
```

Notes:

- `provider` currently supports only `unsplash`.
- `access_key` should be the Unsplash access key used for API requests.
- Unsplash `Access Key` maps to `access_key`.
- Unsplash `Secret key` is not used by this server.
- Unsplash `Application ID` is not used by this server.
- `api_key` and `client_id` are still accepted as backward-compatible aliases, but prefer `access_key`.
- `download_dir` may be absolute or relative to the repo root.
- `history_path` is optional. If omitted, the server stores history in `download_dir/.image-download-history.json`.
- `timeout_seconds` is optional.

## Tools

### `search_images`

Inputs:

- `query` required text
- `orientation` optional enum: `landscape`, `portrait`, `squarish`
- `limit` optional integer, default `6`, max `20`

Returns:

- `provider`
- `query`
- `results`

Each result includes:

- `id`
- `title`
- `preview_url`
- `source_page_url`
- `photographer_name`
- `attribution_text`
- `license_summary`
- `provider_usage_notes`

Behavior:

- Keep `query` broad and visual. Prefer short searchable concepts such as `empty office`, `quiet workspace`, or `single desk`.
- Do not use sentence-length descriptions or article summaries as the search query.
- For abstract article ideas, search for an adjacent visual metaphor or simple scene instead of the full thesis.
- The server filters out image IDs already present in the local history file.
- If enough fresh results are not available on the first page, it fetches more pages until it reaches the requested limit or exhausts the provider results.

### `download_image`

Inputs:

- `image_id` required text

Returns:

- `success`
- `local_path`
- `filename`
- `source_page_url`
- `photographer_name`
- `attribution_text`
- `license_summary`
- `provider`

Behavior:

- The server resolves the provider download location first, then downloads the binary asset.
- The downloaded file is written only into the configured `download_dir`.
- The server records the download in the local history file so later searches can skip it.

## Error Types

Tool failures return a structured JSON error payload with one of these `type` values:

- `missing_config`
- `invalid_config`
- `invalid_input`
- `bad_api_credentials`
- `rate_limited`
- `image_not_found`
- `download_failure`
- `image_already_downloaded`
- `provider_request_failed`

## Local MCP Config

Treat the repo-root `.mcp.json` as the canonical registration for this server. If you need to mirror that config elsewhere, use:

```json
{
  "mcpServers": {
    "blog-image-finder": {
      "command": "uv",
      "args": [
        "run",
        "./.agents/blog-image-finder/mcp/image-provider/server.py"
      ]
    }
  }
}
```

## Usage Notes

- Keep the returned attribution metadata with the article asset notes or image manifest.
- Use the MCP tool directly and assume the repo-local registration works. Do not run the verifier unless a real tool call fails.
- Troubleshooting: run `uv run .agents/mcp/verify_servers.py blog-image-finder` only after a concrete failure to check repo-local registration, stdio startup, and local config status. If `uv` cannot initialize its cache, retry with `UV_CACHE_DIR=/tmp/uv-cache uv run .agents/mcp/verify_servers.py blog-image-finder`.
- Review the provider terms before publication. The server returns a usage summary, not legal clearance.
- Pair this skill with `../blog-image-uploader/SKILL.md` when the selected asset should be published to the blog image bucket.
