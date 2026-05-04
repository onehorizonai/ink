---
name: blog-image-uploader
description: Upload local blog image files to the configured S3 bucket through a local MCP server and return the object metadata plus public URL. Use when Codex needs to publish a downloaded blog image, move a local JPG, PNG, or WebP asset into the blog-images bucket, verify the target object key before upload, or keep blog image credentials isolated in a local .secrets config.
---

# Blog Image Uploader

## Overview

Use this skill to publish a local blog image into the configured S3 bucket through `mcp/blog-image-s3/server.py`. The server signs requests locally, checks for collisions before upload unless the caller explicitly allows overwrite, and returns the object key plus the public URL.

## Workflow

1. Read `references/setup.md`.
2. Assume the repo-local MCP registration is already loaded and call `upload_image` directly when publication is needed. Do not run MCP verification as a preflight step.
3. Use this skill only after the final local file is ready for publication.
4. Call `upload_image` with the local file path and, when needed, an explicit `object_key` or `prefix`. In this repo, published blog-post assets should upload under `images/posts/...`.
5. Keep the returned `object_key` and `public_url` with the article or publishing notes.

## Rules

- Do not commit `.secrets/blog-image-s3.json` or any derived credentials.
- Do not upload non-image files through this skill.
- Let the server detect existing objects before upload unless the user explicitly wants overwrite behavior.
- Do not verify MCP setup before using the tool. Call the tool first and troubleshoot only after a concrete tool failure.
- Preserve attribution metadata separately when the source image came from Unsplash or another provider. This skill uploads bytes; it does not clear rights.
- Do not confuse article asset paths with storage object keys. Blog articles may reference `posts/...`, but uploaded storage objects should land under `images/posts/...`.
- Keep the skill narrow. Use it for bucket upload work, not image sourcing or article editing.

## Files

- Read `references/setup.md` for config shape, tool contract, and the MCP config snippet.
- Use `mcp/blog-image-s3/server.py` as the local MCP server entrypoint.
