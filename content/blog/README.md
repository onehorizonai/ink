# Blog Workspace

The local blog path contract lives in `.local/README.md`.

The active published-blog source folder and publish output folder are stored in the selected Ink profile's gitignored `blogPublishingConfig`. The legacy/default One Horizon profile uses `.local/context/blog-publishing.local.md`.

## Rules

- Follow the schema in `.agents/blog-post-writer/references/corpus-spec.md`.
- Keep the article in its native Markdown or MDX format.
- Keep unpublished drafts out of the configured published folder. Drafts belong in the selected profile's `contentRoots.blogDrafts`.

## Folders

- `drafts/` for the legacy/default `content/blog/drafts/`

## Notes

- Published blog content may live outside this repo.
- Use the selected profile's `blogPublishingConfig` for live path state. Do not store that state anywhere else in the repo.
- Keep real published content and working drafts local. This repo only tracks workspace docs and keep files.
- Treat the configured published articles as the source of truth for blog voice, section shape, and CTA intensity.
