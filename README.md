# Ink

Writing agents for LinkedIn posts and blog articles, with local context, local draft workspaces, and repo-local MCP helpers.

Built by [One Horizon](https://onehorizon.ai).

## Quick Start

### 1. Clone the repo

```bash
git clone <your-github-url> ink
cd ink
```

### 2. Install `uv`

On macOS:

```bash
brew install uv
```

See the [uv docs](https://docs.astral.sh/uv/) for other platforms.

### 3. Sync the repo skills into Codex

```bash
./scripts/sync_repo_skills.sh codex
```

Start a fresh Codex session after syncing so the skill list refreshes.

### 4. Create your local context directory

```bash
mkdir -p .local/context
```

Copy the starter templates into `.local/context/`:

```bash
for src in .agents/context/templates/*.template.md; do
  name="$(basename "$src" .template.md)"
  cp "$src" ".local/context/$name.md"
done
```

Update the copied files with your own local identity, company, and blog path data.

### 5. Create your local secrets directory

```bash
mkdir -p .secrets
```

### 6. Open the repo in Codex

This repo ships a workspace-local [.mcp.json](.mcp.json). Open the repo as the workspace root so Codex can load those MCP registrations directly.

## What This Repo Includes

- LinkedIn writing orchestration in [.agents/linkedin-social-writer](.agents/linkedin-social-writer/SKILL.md)
- Blog writing orchestration in [.agents/blog-post-writer](.agents/blog-post-writer/SKILL.md)
- Review passes for humanizing, tone, style, fact checking, and URL validation
- Local draft workspaces under [content/linkedin/drafts](content/linkedin/drafts/README.md) and [content/blog/drafts](content/blog/drafts/README.md)
- Repo-local MCP helpers for research and optional image workflows

## What Stays Local

Keep these out of version control:

- `.local/context/` for live user, company, and blog-path context
- `.secrets/` for API keys, local config JSON, and download history
- real LinkedIn corpus files under `content/linkedin/`
- real unpublished drafts under `content/linkedin/drafts/` and `content/blog/drafts/`

Tracked files in this repo are the public workflow, templates, scripts, and keep files. Your actual writing corpus and runtime context stay local.

## Local Context Contract

Public context contracts live in [.agents/context](.agents/context/index.md).

Live runtime context belongs in `.local/context/`. The main files are:

- `.local/context/profile.md`
- `.local/context/current-work.md`
- `.local/context/market-context.md`
- `.local/context/work-history.md`
- `.local/context/personal-interests.md`
- `.local/context/personal-life.md`
- `.local/context/blog-publishing.local.md`

Starter templates live in [.agents/context/templates](.agents/context/templates/README.md).

## Optional Local MCP Services

The repo-local `.mcp.json` registers:

- `linkedin-social-research`
- `blog-image-finder`
- `blog-image-uploader`

The research server is useful for writing workflows. The image servers are only needed if you want image sourcing and upload support for blog work.

To verify the local MCP wiring:

```bash
uv run .agents/mcp/verify_servers.py
```

If `uv` cache permissions get in the way, use a writable cache directory:

```bash
UV_CACHE_DIR=/tmp/uv-cache uv run .agents/mcp/verify_servers.py
```

## Optional Secret Config Files

### Unsplash image search

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

### S3-compatible blog image uploads

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

## Workspace Layout

- [.agents](.agents): skills, references, templates, and MCP helpers
- [.agents/context](.agents/context/index.md): public context contracts and starter templates
- [content/linkedin](content/linkedin/README.md): local LinkedIn corpus workspace
- [content/blog](content/blog/README.md): local blog workspace
- [scripts](scripts): repo helpers such as skill syncing

## Common Commands

Sync skills:

```bash
./scripts/sync_repo_skills.sh
```

Validate MCP registrations:

```bash
uv run .agents/mcp/verify_servers.py
```

Create a LinkedIn draft:

```bash
uv run .agents/linkedin-social-writer/scripts/create_draft.py \
  --format post \
  --title "Replace with title" \
  --body "Replace with draft text"
```

Store a published LinkedIn post locally:

```bash
uv run .agents/linkedin-social-writer/scripts/store_published.py \
  --format post \
  --body "Replace with published text"
```

Validate the local LinkedIn corpus:

```bash
uv run .agents/linkedin-social-writer/scripts/validate_corpus.py
```

## Working Rules

- Start with [AGENTS.md](AGENTS.md) for repo-specific agent rules.
- Use [.agents/linkedin-social-writer](.agents/linkedin-social-writer/SKILL.md) as the LinkedIn orchestrator.
- Use [.agents/blog-post-writer](.agents/blog-post-writer/SKILL.md) as the blog orchestrator.
- Keep live context in `.local/context/`, not in tracked repo files.
- Keep real drafts and corpora local.
- Reuse the shared references instead of duplicating workflow rules.

## License

This repo is released under [Apache-2.0](LICENSE).
