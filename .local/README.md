# Local Workspace

`.local/` is the home for repo-specific runtime context.

Use this as the only tracked contract for live context.

Use it for:

- live author or team context
- company or project positioning
- personal context used by the writing agents
- machine-local blog path state

## Layout

- `.local/context/`
  Runtime files. These stay ignored by git.
- `.local/templates/`
  Starter files you can copy into `.local/context/`.

## Hard Rules

- Use `.local/context/*.md` for live runtime context.
- Do not store live runtime context in `README.md`, `AGENTS.md`, `CLAUDE.md`, `.agents/`, `content/`, or any other tracked repo path.
- Do not commit `.local/context/*`.
- Use the filenames in this document exactly. Do not rename them.

## Runtime Files

Create the files you need under `.local/context/`:

- `profile.md`
- `current-work.md`
- `market-context.md`
- `work-history.md`
- `personal-interests.md`
- `personal-life.md`
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

## Starter Templates

Copy the templates from `.local/templates/` into `.local/context/` and rename them without the `.template` suffix.

Example:

- `.local/templates/profile.template.md` -> `.local/context/profile.md`
- `.local/templates/blog-publishing.local.template.md` -> `.local/context/blog-publishing.local.md`

Keep the copied runtime files local and untracked.
