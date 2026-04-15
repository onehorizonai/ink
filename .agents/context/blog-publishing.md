# Blog Publishing Contract

This file defines the contract for blog path resolution.

Do not store runtime directory values in this file.

## Runtime State File

Store the active published-blog source folder and publish output folder in the gitignored local file:

- `.local/context/blog-publishing.local.md`

## Required Fields In The Local File

- `source_articles_dir`
- `publish_output_dir`
- `last_confirmed_on`

## Rules

- Read `.local/context/blog-publishing.local.md` before searching for existing blog articles or publishing a finished blog post.
- If the local file is missing, create it after asking the user:
  - `Where should I load existing blog articles from?`
  - `Where should I publish finished blog posts?`
- If either stored path is `[unset]`, ask the user for the missing folder and update the local file.
- If a stored path no longer exists on disk, ask the user for the new folder and update the local file before continuing.
- Do not assume `content/blog/posts/`.
- Use `source_articles_dir` for internal corpus research.
- Use `publish_output_dir` for published blog output.
- These folders may be the same.
- Use `content/blog/drafts/` for unpublished drafts.
- Do not treat the draft folder as configurable in either file.
