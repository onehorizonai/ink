# Local Workspace

`.local/` holds machine-local runtime state that cannot live in One Horizon because it is specific to this machine and this installation.

Live author, company, and personal context now lives in author-scoped One Horizon context docs. See `one-horizon-context-setup` to create missing docs for an author.

Use this folder only for:

- machine-local blog path state

## Layout

- `.local/context/`
  Runtime files. These stay ignored by git.

## Hard Rules

- Do not store live author or company context here. Use author-scoped One Horizon context docs instead.
- Do not commit `.local/context/*`.
- Use the filenames in this document exactly. Do not rename them.

## Runtime Files

The only required runtime file is:

- `blog-publishing.local.md`

## Blog Path Contract

Keep the active published-blog source folder and publish output folder in:

- `.local/context/blog-publishing.local.md`

Required fields:

- `source_articles_dir`
- `publish_output_dir`
- `last_confirmed_on`

Rules:

- Read `.local/context/blog-publishing.local.md` before searching for existing blog articles or publishing a finished blog post.
- If the file is missing, create it after asking the user where to load existing blog articles from and where to publish finished blog posts.
- If either stored path is `[unset]`, ask the user for the missing folder and update the local file.
- If a stored path no longer exists on disk, ask the user for the new folder and update the local file before continuing.
- Do not assume `content/blog/posts/`.
- Use `source_articles_dir` for internal corpus research.
- Use `publish_output_dir` for published blog output.
- These folders may be the same.
- Use `content/blog/drafts/` for unpublished drafts.

Minimal valid file shape:

```md
# Blog Publishing Local Config

This file stores machine-local blog path values for this workspace.

## Active Paths

- `source_articles_dir`: `/absolute/path/to/published/articles`
- `publish_output_dir`: `/absolute/path/to/published/articles`
- `last_confirmed_on`: `YYYY-MM-DD`
```

Invalid:

- missing any required field
- renaming the field keys
- storing relative paths when the workflow expects a concrete local folder
