---
name: blog-image-finder
description: Search and download candidate blog images through a local Unsplash-backed MCP server while filtering out previously used assets and preserving attribution metadata. Use when Codex needs to source a fresh image for a blog post, compare candidate photos for an article concept, download a selected image into the configured local staging folder, or check the local image-provider setup before image work.
---

# Blog Image Finder

## Overview

Use this skill to source blog images through the local MCP server at `mcp/image-provider/server.py`. It searches Unsplash, skips images already recorded in the local history file, downloads the selected image into the configured staging folder, and returns the attribution data needed for later publishing.

## Workflow

1. Read `references/setup.md`.
2. Assume the repo-local MCP registration is already loaded and call `search_images` directly. Do not run MCP verification as a preflight step.
3. Treat the returned list as candidate inputs, not final approval.
4. Form `search_images.query` as a short visual concept, usually 1-4 words, not as a sentence or article summary.
5. Search for what can actually be photographed: a place, object, mood, or simple scene. Use metaphor or adjacent imagery when the article idea is abstract.
6. Start broad, then narrow only if the first results miss the brief.
7. Good queries: `empty office`, `quiet workspace`, `single desk`, `small team meeting`, `warehouse shelf`.
8. Bad query: `a lean technology team overseeing a dense stack of dashboards, agents, and workflows, not a crowded open office`.
9. Pick one image that fits the article and call `download_image` with its `image_id`.
10. Keep the returned provider, source URL, photographer credit, and attribution text with the asset record.
11. Hand the downloaded file to `../blog-image-uploader/SKILL.md` when the user wants the asset uploaded to the blog image bucket.

## Rules

- Do not claim an image is rights-free. Preserve the provider and attribution metadata exactly as returned.
- Do not bypass the provider download flow with a raw image URL.
- Do not save downloaded files outside the configured `download_dir`.
- Do not pass long descriptive prompts to `search_images`. Use short, searchable visual concepts instead.
- Do not verify MCP setup before using the tool. Call the tool first and troubleshoot only after a concrete tool failure.
- Treat the download history as the dedupe source of truth. If the same image was already downloaded, choose another one unless the user explicitly wants the duplicate.
- Return the config error as-is when `.secrets/image-provider.json` is missing or invalid.
- Keep the skill narrow. Use it for image sourcing and download, not for article writing or upload work.

## Files

- Read `references/setup.md` for config shape, tool contracts, and the MCP config snippet.
- Use `mcp/image-provider/server.py` as the local MCP server entrypoint.
