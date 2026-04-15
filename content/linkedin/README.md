# LinkedIn Corpus

This directory is the local LinkedIn corpus workspace.

## Rules

- Keep one Markdown file per published item.
- Store files in the matching format folder.
- Follow the schema in `.agents/linkedin-social-writer/references/corpus-spec.md`.
- Start from the matching file in `.agents/linkedin-social-writer/templates/storage/` when adding or normalizing items.

## Folders

- `posts/`
- `comment-replies/`
- `dms/`
- `dm-replies/`
- `reposts/`

## Notes

- Copy or symlink an existing archive into this directory if the source lives elsewhere.
- Keep image and asset descriptions factual. Describe what the asset showed, not how well it performed.
- Prefer fewer high-quality examples with good context over a large archive with thin metadata.
- Keep real corpus files local. This repo only tracks keep files and workspace docs.
- Keep unpublished drafts out of this folder. Drafts belong in `content/linkedin/drafts/`.
- Run `.agents/linkedin-social-writer/scripts/validate_corpus.py` after adding or editing files.
