# Blog Image Uploader Setup

## Config

The local MCP server resolves the active Ink profile first. In multi-profile installs, it reads the selected profile's `imageUploadConfig` from `.local/context/ink-profiles.local.json`.

Legacy installs with no profile config read:

- `.secrets/blog-image-s3.json`

If the selected config file is missing or invalid, the server returns a structured config error.

Example:

```json
{
  "bucket": "example-blog-images",
  "region": "eu-west-1",
  "access_key_id": "AKIA...",
  "secret_access_key": "replace-me",
  "session_token": "",
  "endpoint_url": "https://s3.eu-west-1.amazonaws.com",
  "public_base_url": "https://cdn.example.com/blog-images",
  "key_prefix": "images/posts",
  "history_path": "./.secrets/<profile-id>/blog-image-upload-history.json",
  "addressing_style": "path",
  "timeout_seconds": 30
}
```

Notes:

- `endpoint_url` is optional. If omitted, the server targets AWS S3 for the configured region.
- `public_base_url` is optional. Set it when the bucket is served through CloudFront or another CDN.
- `key_prefix` is optional and is prepended to uploaded object keys.
- For this repo, the preferred published location for blog-post images is `images/posts/...`.
- `history_path` is optional. If omitted, legacy installs store upload history in `.secrets/blog-image-upload-history.json`, while selected profiles store it in `.secrets/<profile-id>/blog-image-upload-history.json`.
- `addressing_style` supports `virtual` and `path`. Use `path` for Supabase S3 endpoints like `...storage.supabase.co/storage/v1/s3`. Use `virtual` for bucket subdomain hosts that present a matching TLS certificate.
- In multi-profile installs, use separate `history_path`, bucket, and public URL values per profile unless multiple profiles intentionally publish to the same image host.

## Tool

### `upload_image`

Inputs:

- `local_path` required path to a local image file
- `object_key` optional explicit S3 object key
- `prefix` optional extra path prefix below the configured `key_prefix`
- `overwrite` optional boolean, default `false`
- `content_type` optional MIME type override
- `profile` optional Ink profile id. Defaults to `INK_PROFILE`; required in practice when multiple profiles are configured and no environment profile is set.
- `profile_config` optional path to the local Ink profile config. Defaults to `INK_PROFILE_CONFIG` or `.local/context/ink-profiles.local.json`.

Returns:

- `success`
- `local_path`
- `bucket`
- `object_key`
- `public_url`
- `etag`
- `content_type`
- `bytes_uploaded`

Behavior:

- Relative `local_path` values resolve from the repo root.
- The server rejects missing files and non-image content.
- If `overwrite` is false, the server checks whether the target object already exists before uploading.
- The server writes a selected-profile upload-history record after a successful upload.

## Error Types

Tool failures return a structured JSON error payload with one of these `type` values:

- `missing_config`
- `invalid_config`
- `bad_api_credentials`
- `file_not_found`
- `invalid_input`
- `object_exists`
- `upload_failure`
- `provider_request_failed`

## Local MCP Config

Treat the repo-root `.mcp.json` as the canonical registration for this server. Codex also mirrors this server in `.codex/config.toml`. The registration uses this command shape:

```json
{
  "mcpServers": {
    "blog-image-uploader": {
      "command": "uv",
      "args": [
        "run",
        "./.agents/blog-image-uploader/mcp/blog-image-s3/server.py"
      ]
    }
  }
}
```

## Usage Notes

- Prefer an explicit `object_key` when the published URL must match an existing naming convention.
- In this repo, use `images/posts/...` for explicit upload targets, not `posts/...`.
- If `key_prefix` is already `images/posts`, you can omit `object_key` and let the tool keep uploads under that prefix.
- Keep the distinction clear: the article may still reference `posts/...`, while the uploaded storage object lives under `images/posts/...`.
- Do not use another profile's bucket or CDN as a fallback. If the selected profile upload config is incomplete, stop and ask for that profile's hosting details.
- Use the MCP tool directly and assume the repo-local registration works. Do not run the verifier unless a real tool call fails.
- Troubleshooting: run `uv run .agents/mcp/verify_servers.py --profile <profile-id> blog-image-uploader` only after a concrete failure to check repo-local registration, stdio startup, and selected-profile local config status. If `uv` cannot initialize its cache, retry with `UV_CACHE_DIR=/tmp/uv-cache uv run .agents/mcp/verify_servers.py --profile <profile-id> blog-image-uploader`.
- Set `public_base_url` when the live site serves images through a CDN or vanity domain.
- Use this skill after `../blog-image-finder/SKILL.md` when the image started in the local Unsplash download flow.
