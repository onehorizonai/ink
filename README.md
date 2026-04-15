# Ink

![Ink banner](assets/readme/ink-banner-1280x640.png)

Turn your context, corpus, and research into publish-ready LinkedIn posts and blog drafts.

Ink is a [One Horizon](https://onehorizon.ai) project for running repeatable writing workflows in Claude Code, Cursor, or Codex using local context, saved content, and optional research and image tooling.

It works with Claude Code, Cursor, and Codex. Claude and Cursor are the simplest path. Codex works too, but needs one extra sync step so it can see the repo's local skills.

## What Ink does

- Finds content ideas from your current context, published content, and live research
- Drafts LinkedIn posts, comment replies, DMs, DM replies, and reposts
- Drafts long-form blog posts with research, review passes, and optional image support
- Reviews drafts for tone, structure, facts, URLs, and AI-sounding copy
- Stores approved LinkedIn posts back into a local corpus
- Keeps live context, secrets, and real content out of git

## Quick start

### 1. Clone the repo

```bash
git clone https://github.com/onehorizonai/ink ink
cd ink
```

### 2. Install `uv`

Ink uses `uv` to run local helpers and MCP servers.

On macOS:

```bash
brew install uv
```

On other platforms, use the [official uv installation guide](https://docs.astral.sh/uv/).

### 3. Open the cloned folder in your assistant

Open the repo root, not a subfolder. That lets the assistant pick up the repo files and the local [.mcp.json](.mcp.json) config.

- Claude Code: start Claude Code from the `ink/` folder
- Cursor: open `ink/` as the project or workspace
- Codex: add `ink/` as a project

### 4. If you use Codex, run the Codex sync step once

```bash
./scripts/sync_repo_skills.sh codex
```

This step is for Codex only.

Codex does not automatically load repo-local skills from `.agents/`. The sync script creates links from this repo's skill folders into your local Codex skills directory so Codex can discover and use them.

Run it:

- once after cloning
- again after pulling changes that update repo skills
- any time Codex is missing the repo skills

If the skills still do not appear in Codex, restart the Codex app or CLI and open the repo again.

### 5. Run the one-time setup

In your assistant, run:

```text
Setup ink
```

This is the normal setup path. You do not need to create `.local/` folders by hand first.

The setup flow will:

- ask for your website and LinkedIn profile
- pull in the public context it needs
- confirm anything that might overwrite existing local context
- create or update the local context files under `.local/context/`

### 6. Start writing

Good first prompts:

- `Find three content ideas I should write next`
- `Draft a LinkedIn post about...`
- `Outline a blog post about...`
- `Refresh my local context from my website and LinkedIn`

## Skills included

### Core workflows

- `local-context-setup`: one-time setup and refresh for `.local/context/`
- `content-idea-finder`: finds what to write next
- `linkedin-social-writer`: drafts LinkedIn posts, replies, DMs, and reposts
- `linkedin-finalize-post`: gives a LinkedIn draft its final pass and stores it when approved
- `linkedin-store-post`: stores LinkedIn posts that already exist
- `blog-post-writer`: writes full blog drafts from brief to article

### Review and quality passes

- `content-humanizer`: removes AI-sounding copy early in the editing flow
- `content-tone-review`: checks whether the draft sounds like the author
- `content-style-review`: tightens structure, readability, and persuasion
- `fact-check`: verifies unstable claims and external facts
- `source-url-check`: checks blog source URLs before publishing
- `blog-post-ramsay-review`: gives blog drafts a blunt publish-or-don't-publish review

### Optional image workflow

- `blog-image-finder`: searches Unsplash and downloads candidate blog images
- `blog-image-uploader`: uploads approved blog images to your configured S3 bucket

## What stays local

Ink is local-first. The workflow is tracked in git. Your real working data is not.

Keep these local and uncommitted:

- `.local/context/` for live identity, company, and writing context
- `.secrets/` for API keys and local config
- `content/linkedin/` for your real LinkedIn corpus
- `content/linkedin/drafts/` for unpublished LinkedIn drafts
- `content/blog/drafts/` for unpublished blog drafts
- any published blog source folder referenced by `.local/context/blog-publishing.local.md`

## Advanced setup

You only need this section if you want MCP-backed research or the blog image workflow.

### MCP capabilities

This repo ships a workspace-local [.mcp.json](.mcp.json) with three local MCP servers:

- `linkedin-social-research` for research during writing
- `blog-image-finder` for Unsplash-backed image search and download
- `blog-image-uploader` for S3-backed image upload

If your assistant supports workspace MCP config, opening the repo root is usually enough for discovery.

If you want to verify the MCP setup:

```bash
uv run .agents/mcp/verify_servers.py
```

If `uv` cache permissions get in the way:

```bash
UV_CACHE_DIR=/tmp/uv-cache uv run .agents/mcp/verify_servers.py
```

### Unsplash setup for `blog-image-finder`

You need an Unsplash developer app before image search will work.

1. Create or sign in to your Unsplash account.
2. Open [your Unsplash apps](https://unsplash.com/oauth/applications) and create a new application.
3. Copy the app's `Access Key`.
4. Save that key in `.secrets/image-provider.json` as `access_key`.

New Unsplash apps start in demo mode, which is enough to test the setup. If you plan to use this more heavily, apply for production access from the Unsplash dashboard after your integration is working.

Create `.secrets/image-provider.json`:

```json
{
  "provider": "unsplash",
  "access_key": "YOUR_UNSPLASH_ACCESS_KEY",
  "download_dir": "./.secrets/downloads/blog-images",
  "history_path": "./.secrets/image-download-history.json",
  "timeout_seconds": 30
}
```

Keep the key local. Do not commit it. If you plan to ship an Unsplash-backed workflow publicly, review the [Unsplash API documentation](https://unsplash.com/documentation) and the [API guidelines](https://help.unsplash.com/en/articles/2511245-unsplash-api-guidelines), especially around attribution and download tracking.

### S3 setup for `blog-image-uploader`

Create `.secrets/blog-image-s3.json`:

```json
{
  "bucket": "your-blog-images",
  "region": "your-region",
  "access_key_id": "YOUR_ACCESS_KEY_ID",
  "secret_access_key": "YOUR_SECRET_ACCESS_KEY",
  "session_token": "",
  "endpoint_url": "https://your-s3-endpoint.example.com",
  "public_base_url": "https://cdn.example.com/your-blog-images",
  "key_prefix": "images/posts",
  "history_path": "./.secrets/blog-image-upload-history.json",
  "addressing_style": "path",
  "timeout_seconds": 30
}
```

Use `addressing_style: "path"` for path-style S3 endpoints. Use `virtual` for bucket-subdomain hosts with matching TLS support.

### Manual local setup

You only need this if you do not want to use `Setup ink`.

Start with [.local/README.md](.local/README.md), then copy the templates into `.local/context/`:

```bash
mkdir -p .local/context

for src in .local/templates/*.template.md; do
  name="$(basename "$src" .template.md)"
  cp "$src" ".local/context/$name.md"
done
```

## Troubleshooting

- Codex does not show the repo skills:
  Run `./scripts/sync_repo_skills.sh codex`, then restart the Codex app or CLI and open the repo again.
- MCP tools are missing:
  Make sure you opened the repo root so the assistant can see `.mcp.json`.
- Writing feels generic:
  Run `Setup ink` again or ask Ink to refresh your local context.
- Unsplash image search does not work:
  Confirm you created an Unsplash app and saved the `Access Key` in `.secrets/image-provider.json`.

## Repo layout

- [.agents](.agents): the repo skills, references, templates, and MCP helpers
- [.local](.local/README.md): local setup contract, starter templates, and ignored runtime context
- [content/linkedin](content/linkedin/README.md): local LinkedIn corpus workspace
- [content/blog](content/blog/README.md): local blog workspace
- [scripts](scripts): repo helper scripts

## License

This repo is released under [Apache-2.0](LICENSE).
