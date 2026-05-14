# Blog Image Finder Setup

## Config

The local MCP server resolves the active Ink profile first. In multi-profile installs, it reads the selected profile's `imageProviderConfig` from `.local/context/ink-profiles.local.json`.

Legacy installs with no profile config read:

- `.secrets/image-provider.json`

If the selected config file is missing or invalid, the server returns a structured config error and does not use fallback secrets.

Example:

```json
{
  "provider": "unsplash",
  "access_key": "YOUR_UNSPLASH_ACCESS_KEY",
  "download_dir": "./.secrets/<profile-id>/downloads/blog-images",
  "history_path": "./.secrets/<profile-id>/image-download-history.json",
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
- In multi-profile installs, use separate `download_dir` and `history_path` values per profile so image staging and dedupe history do not mix.

## Tools

### `search_images`

Inputs:

- `query` required text
- `orientation` optional enum: `landscape`, `portrait`, `squarish`
- `limit` optional integer, default `6`, max `20`
- `profile` optional Ink profile id. Defaults to `INK_PROFILE`; required in practice when multiple profiles are configured and no environment profile is set.
- `profile_config` optional path to the local Ink profile config. Defaults to `INK_PROFILE_CONFIG` or `.local/context/ink-profiles.local.json`.

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
- The server filters out image IDs already present in the selected profile's local history file.
- If enough fresh results are not available on the first page, it fetches more pages until it reaches the requested limit or exhausts the provider results.

### `download_image`

Inputs:

- `image_id` required text
- `profile` optional Ink profile id. Use the same profile as `search_images`.
- `profile_config` optional path to the local Ink profile config.

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
- The server records the download in the selected profile's local history file so later searches can skip it.

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

Treat the repo-root `.mcp.json` as the canonical registration for this server. Codex also mirrors this server in `.codex/config.toml`. The registration uses this command shape:

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
- If a real tool call fails with a provider/network-style error such as `provider_request_failed`, retry the same call once before escalating to MCP verification or broader workflow blocking.
- Troubleshooting: run `uv run .agents/mcp/verify_servers.py --profile <profile-id> blog-image-finder` only after a concrete failure to check repo-local registration, stdio startup, and selected-profile local config status. If `uv` cannot initialize its cache, retry with `UV_CACHE_DIR=/tmp/uv-cache uv run .agents/mcp/verify_servers.py --profile <profile-id> blog-image-finder`.
- Review the provider terms before publication. The server returns a usage summary, not legal clearance.
- Pair this skill with `../blog-image-uploader/SKILL.md` when the selected asset should be published to the blog image bucket.
