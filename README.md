# Ink

![Ink banner](assets/readme/ink-banner-1280x640.png)

A local writing system for LinkedIn posts and blog articles.

Ink is a [One Horizon](https://onehorizon.ai/?utm_source=github&utm_medium=ink&utm_content=readme) project for Claude Code, Cursor, and Codex. It pulls in your local context, checks your saved content, runs a structured writing flow, and keeps the working files on your machine.

Claude Code and Cursor are the easy path. Codex works too, but needs one extra sync step so it can see the repo's local skills.

## What Ink does

- Finds content ideas from your context, published content, and live research
- Drafts LinkedIn posts, comment replies, DMs, DM replies, and reposts
- Writes blog posts with research, review passes, and optional image support
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

Open the repo root, not a subfolder. That gives the assistant access to the repo files and the local [.mcp.json](.mcp.json) config.

- Claude Code: start Claude Code from the `ink/` folder
- Cursor: open `ink/` as the project or workspace
- Codex: add `ink/` as a project

#### Codex only: run the sync step once

```bash
./scripts/sync_repo_skills.sh codex
```

This step is for Codex only.

Codex does not automatically pick up repo-local skills from `.agents/`. This script links the repo's skill folders into your local Codex skills directory so Codex can see them.

Run it:

- once after cloning
- again after pulling changes that update repo skills
- any time Codex is missing the repo skills

If the skills still do not appear in Codex, restart the Codex app or CLI and open the repo again.

### 4. Run setup once

In your assistant, run:

```text
Setup ink
```

This is the normal way to do it. You do not need to create `.local/` folders by hand first.

It will:

- ask for your website and LinkedIn profile
- pull in the public context it needs
- confirm anything that might overwrite existing local context
- create or update the local context files under `.local/context/`

### 5. Start writing

Good first prompts:

- `Find three content ideas I should write next`
- `Draft a LinkedIn post about...`
- `Outline a blog post about...`
- `Refresh my local context from my website and LinkedIn`

# Usage guides

## Set up Ink once

Run `local-context-setup` once after cloning, then again any time your local context changes.

Guided example:

```md
User:
Set up Ink

Agent:
I can do that. What is the primary company site?

User:
https://piedpiper.com

Agent:
What is the LinkedIn profile URL?

User:
https://www.linkedin.com/in/richard-hendricks

Agent:
I’ll use the standard setup and skip personal-life for now. If I find existing local context, I’ll stop and ask before changing it.

...
```

What happens:

- reads the local setup contract
- asks for the minimum missing facts
- checks whether anything can be overwritten
- creates or updates `.local/context/`

## Find what to write next

Use `content-idea-finder` if you want ideas before you commit to a post or an article.

Example prompt:

```text
Find five content ideas for me.
Give me three LinkedIn ideas and two blog ideas based on my current context, recent themes, and gaps in my existing content.
```

## Write a LinkedIn post

Use `linkedin-social-writer` to draft the post itself.

Example prompt:

```text
Draft a LinkedIn post about why most AI workflow demos fall apart in production.
```

LinkedIn workflow:

```mermaid
flowchart TD
    A["Build the brief"] --> B["Ask only the missing questions"]
    B --> C["Load the minimum local context"]
    C --> D["Pull 3 to 5 relevant LinkedIn examples"]
    D --> E["Draft the post"]
    E --> F["Run humanizer pass"]
    F --> G["Run tone review"]
    G --> H["Run style review"]
    H --> I{"Needs fact check?"}
    I -- "Yes" --> J["Run fact check"]
    I -- "No" --> K["Finalize draft"]
    J --> K
    K --> L{"Save unpublished draft?"}
    L -- "Yes" --> M["Write to content/linkedin/drafts/"]
    L -- "No" --> N["Ready for manual publishing"]
    M --> N
    N --> O["Publish manually on LinkedIn"]
    O --> P["Store final shared version in the corpus if needed"]
```

How LinkedIn publishing works:

- Ink does not post to LinkedIn for you.
- Ink writes drafts and corpus entries locally.
- You review the final copy, then publish it yourself on LinkedIn.
- Use `linkedin-finalize-post` if the draft still needs a final pass before you save it.
- Use `linkedin-store-post` if you already published it and just want the exact text logged.

## Write a blog post

Use `blog-post-writer` for a full article draft.

Example prompt:

```text
Write a blog post about why agent workflows break between demo and deployment.
```

Blog workflow:

```mermaid
flowchart TD
    A["Build the article brief"] --> B["Check .local/context/blog-publishing.local.md"]
    B --> C{"File exists and paths work?"}
    C -- "No" --> D["Ask for source and publish folders"]
    D --> E["Update blog-publishing.local.md"]
    E --> F["Research the published blog archive first"]
    C -- "Yes" --> F
    F --> G["Run a lightweight external research pass"]
    G --> H["Load the minimum local context"]
    H --> I["Draft the outline"]
    I --> J["Plan the cover image and inline images"]
    J --> K["Validate the outline"]
    K --> L["Write pass one"]
    L --> M["Write pass two"]
    M --> N["Run humanizer pass"]
    N --> O["Run style review"]
    O --> P["Run fact check"]
    P --> Q["Run source URL check"]
    Q --> R["Run tone review"]
    R --> S["Run Ramsay review"]
    S --> T{"Working draft or final draft?"}
    T --> U["Save unpublished draft to content/blog/drafts/ if needed"]
    T --> V["Write published article to publish_output_dir when requested"]
```

How blog publishing works:

- Ink reads `.local/context/blog-publishing.local.md` to find `source_articles_dir` and `publish_output_dir`.
- If that file is missing, unset, or points to a folder that no longer exists, Ink asks for the correct folders first.
- It uses `source_articles_dir` to read your published archive.
- It uses `publish_output_dir` to write finished articles.
- Unpublished working drafts still belong in `content/blog/drafts/`.
- If you use blog images, `blog-image-finder` handles search and download, and `blog-image-uploader` handles S3 upload.

## Review a draft without starting over

Use the review skills when you already have a draft and only want one kind of pass.

- `content-humanizer`: remove AI tells early
- `content-tone-review`: check voice, stance, and personal-detail level
- `content-style-review`: tighten flow, readability, and persuasion
- `fact-check`: verify dates, names, numbers, product facts, and other unstable claims
- `source-url-check`: verify URLs in blog articles
- `blog-post-ramsay-review`: get a blunt late-stage review of a blog draft

## Store published content in the corpus

Use these two skills when the writing already exists and you want it logged in the corpus.

- `linkedin-finalize-post`: final pass, then optional storage when approval is explicit
- `linkedin-store-post`: store content that was already shared or published

## Skill guide

### Core workflows

| Skill | Use it for |
| --- | --- |
| `local-context-setup` | Set up or refresh `.local/context/` |
| `content-idea-finder` | Decide what to write next |
| `linkedin-social-writer` | Draft LinkedIn posts, replies, DMs, and reposts |
| `linkedin-finalize-post` | Final-pass a LinkedIn draft and store it when approved |
| `linkedin-store-post` | Store LinkedIn posts that already exist |
| `blog-post-writer` | Write full blog drafts from brief to article |

### Review and quality passes

| Skill | Use it for |
| --- | --- |
| `content-humanizer` | Remove AI-sounding copy early |
| `content-tone-review` | Check whether the draft sounds like the author |
| `content-style-review` | Tighten structure, readability, and persuasion |
| `fact-check` | Verify unstable or external claims |
| `source-url-check` | Check blog source URLs before publishing |
| `blog-post-ramsay-review` | Pressure-test a blog draft late in the process |

### Optional image workflow

| Skill | Use it for |
| --- | --- |
| `blog-image-finder` | Search Unsplash and download candidate blog images |
| `blog-image-uploader` | Upload approved blog images to your configured S3 bucket |

## What stays local

The repo keeps the process. Your actual context, drafts, and secrets stay on your machine.

Keep these local and uncommitted:

- `.local/context/` for live identity, company, and writing context
- `.secrets/` for API keys and local config
- `content/linkedin/` for your real LinkedIn corpus
- `content/linkedin/drafts/` for unpublished LinkedIn drafts
- `content/blog/drafts/` for unpublished blog drafts
- any published blog source folder referenced by `.local/context/blog-publishing.local.md`

## Advanced setup

Skip this section unless you want MCP research or the blog image flow.

### MCP setup

The repo includes a workspace-local [.mcp.json](.mcp.json) with three local MCP servers:

- `linkedin-social-research` for research during writing
- `blog-image-finder` for Unsplash-backed image search and download
- `blog-image-uploader` for S3-backed image upload

If your assistant supports workspace MCP config, opening the repo root is usually enough.

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

New Unsplash apps start in demo mode, which is enough for setup and testing. If you want to use this more seriously, apply for production access from the Unsplash dashboard after the integration works.

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

Keep the key local. Do not commit it. If you plan to ship an Unsplash-backed workflow publicly, read the [Unsplash API documentation](https://unsplash.com/documentation) and the [API guidelines](https://help.unsplash.com/en/articles/2511245-unsplash-api-guidelines), especially the parts about attribution and download tracking.

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

## Contributing

Contributions are welcome, especially for setup fixes, doc fixes, new skills, and integration support.

If you want to contribute:

1. Open an issue first for larger changes, new workflows, or new integrations.
2. Keep each pull request focused on one clear change.
3. Explain the user-facing impact, not just the implementation details.
4. Update the README or skill docs when setup or behavior changes.
5. Never commit `.local/`, `.secrets/`, private corpora, or other local-only content.

This repo includes:

- a pull request template for describing the change, review path, and checks
- a bug report template for setup, workflow, MCP, and skill issues
- a feature request template for new workflows and improvements
