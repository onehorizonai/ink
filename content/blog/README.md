# Blog Workspace

The blog path contract lives in `.agents/context/blog-publishing.md`.

The active published-blog source folder and publish output folder are stored in the gitignored local file `.local/context/blog-publishing.local.md`.

## Rules

- Follow the schema in `.agents/blog-post-writer/references/corpus-spec.md`.
- Keep the article in its native Markdown or MDX format.
- Keep unpublished drafts out of the configured published folder. Drafts belong in `content/blog/drafts/`.

## Folders

- `drafts/` for `content/blog/drafts/`

## Notes

- Published blog content may live outside this repo.
- Keep real published content and working drafts local. This repo only tracks workspace docs and keep files.
- Treat the configured published articles as the source of truth for blog voice, section shape, and CTA intensity.
