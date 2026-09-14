---
name: blog-image-uploader
description: Upload local image files to the configured S3 bucket through a local MCP server and return object metadata plus the public URL. Use for blog posts (images/posts), docs screenshots (one-ui-docs), release-note changelog images (one-ui-website), or any Ink profile imageUploadConfig upload.
---

# Blog Image Uploader

## Overview

Use this skill to publish a local blog image into the selected Ink profile's configured S3 bucket through `mcp/blog-image-s3/server.py`. The server signs requests locally, checks for collisions before upload unless the caller explicitly allows overwrite, and returns the object key plus the public URL.

## Workflow

1. Read `references/setup.md`.
2. Resolve the active Ink profile. If multiple profiles exist and none is named, ask which profile to use before upload work.
3. Assume the repo-local MCP registration is already loaded and call `upload_image` directly when publication is needed. Pass `profile` when it is known. Do not run MCP verification as a preflight step.
4. Use this skill only after the final local file is ready for publication.
5. Call `upload_image` with the local file path and, when needed, an explicit `object_key` or `prefix`.
   - Blog posts: `images/posts/...` via the selected Ink profile's `imageUploadConfig`.
   - Docs screenshots: `images/screenshots/...` via the `docs-screenshots` profile (see documentation-page program).
   - Release notes: `images/changelog/...` via the `release-notes-images` profile (see release-notes program).
6. Keep the returned `object_key` and `public_url` with the article or publishing notes.

## Rules

- Do not commit `.secrets/blog-image-s3.json`, profile-specific `.secrets/*/blog-image-s3.json`, or any derived credentials.
- Do not share image upload configs across Ink profiles unless those profiles intentionally publish to the same bucket/CDN.
- Do not upload non-image files through this skill.
- Let the server detect existing objects before upload unless the user explicitly wants overwrite behavior.
- Do not verify MCP setup before using the tool. Call the tool first and troubleshoot only after a concrete tool failure.
- Preserve attribution metadata separately when the source image came from Unsplash or another provider. This skill uploads bytes; it does not clear rights.
- Do not confuse article asset paths with storage object keys. Blog articles may reference `posts/...`, but uploaded storage objects should land under `images/posts/...` in the selected profile's bucket.
- For changelog release notes, use profile `release-notes-images` and bucket `one-ui-website` with `images/changelog/...` object keys. Never reuse blog or docs upload configs for `packages/content/src/content/releases/` MDX.
- Keep the skill narrow. Use it for bucket upload work, not image sourcing or article editing.

## Files

- Read `references/setup.md` for config shape, tool contract, and the MCP config snippet.
- Use `mcp/blog-image-s3/server.py` as the local MCP server entrypoint.
