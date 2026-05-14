# Local Workspace

`.local/` holds machine-local runtime state that cannot live in One Horizon because it is specific to this machine and this installation.

Live author, company, and personal context now lives in author-scoped One Horizon context docs inside the selected Ink profile's One Horizon workspace. See `one-horizon-context-setup` to create missing docs for an author.

Use this folder only for:

- the machine-local Ink profile registry
- machine-local blog path state

## Layout

- `.local/context/`
  Runtime files. These stay ignored by git.

## Hard Rules

- Do not store live author or company context here. Use author-scoped One Horizon context docs in the selected profile workspace instead.
- Do not commit `.local/context/*`.
- Use the filenames in this document exactly. Do not rename them.

## Runtime Files

Runtime files:

- `ink-profiles.local.json`
- `blog-publishing.local.md`

## Ink Profile Contract

Keep machine-local profile routing in:

- `.local/context/ink-profiles.local.json`

Use `.local/templates/ink-profiles.local.template.json` as the starter. This file maps profile IDs such as `primary` and `secondary` to:

- `workspaceId`
- `authorName` and optional `authorUserId`
- `website`
- `sourceRepo`
- `contentRoots.linkedin`
- `contentRoots.reddit`
- `contentRoots.blogDrafts`
- `blogPublishingConfig`
- `imageProviderConfig`
- `imageUploadConfig`

Rules:

- Resolve an explicit prompt profile first, then `INK_PROFILE`, then this config.
- If this config contains more than one profile and no profile was named, ask which profile to use before continuing.
- Do not silently fall back to the One Horizon default workspace.
- Use each profile's local content roots for corpus and draft reads/writes.
- Use each profile's `blogPublishingConfig` for blog source and publish paths.
- Use each profile's image provider/upload configs for image downloads, download history, bucket credentials, public URLs, and upload history.

## Blog Path Contract

For the legacy/default One Horizon profile, keep the active published-blog source folder and publish output folder in:

- `.local/context/blog-publishing.local.md`

For any other profile, use that profile's `blogPublishingConfig` from `.local/context/ink-profiles.local.json`.

Required fields:

- `source_articles_dir`
- `publish_output_dir`
- `last_confirmed_on`

Optional post-publish fields:

- `post_publish_generate_command`
- `post_publish_build_command`

Rules:

- Resolve the selected Ink profile before reading blog path state.
- Read the selected profile's `blogPublishingConfig` before searching for existing blog articles or publishing a finished blog post.
- If the file is missing, create it after asking the user where to load existing blog articles from and where to publish finished blog posts.
- If either stored path is `[unset]`, ask the user for the missing folder and update the local file.
- If a stored path no longer exists on disk, ask the user for the new folder and update the local file before continuing.
- Do not assume `content/blog/posts/`.
- Use `source_articles_dir` for internal corpus research.
- Use `publish_output_dir` for published blog output.
- These folders may be the same.
- If `post_publish_generate_command` is set, run it from the publishing repo root after writing a published article.
- If `post_publish_build_command` is set, run it from the publishing repo root after the generate command and before reporting publication complete.
- Use the selected profile's `contentRoots.blogDrafts` for unpublished drafts. Legacy/default installs use `content/blog/drafts/`.

Minimal valid blog publishing file shape:

```md
# Blog Publishing Local Config

This file stores machine-local blog path values for this workspace.

## Active Paths

- `source_articles_dir`: `/absolute/path/to/published/articles`
- `publish_output_dir`: `/absolute/path/to/published/articles`
- `post_publish_generate_command`: `[unset]`
- `post_publish_build_command`: `[unset]`
- `last_confirmed_on`: `YYYY-MM-DD`
```

Invalid:

- missing any required field
- renaming the field keys
- storing relative paths when the workflow expects a concrete local folder
