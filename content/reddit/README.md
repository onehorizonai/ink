# Reddit Corpus

This directory is the local Reddit corpus workspace.

## Rules

- Keep one Markdown file per published item.
- Store files in the matching format folder.
- Follow the schema in `.agents/reddit-social-writer/references/corpus-spec.md`.
- Start from the matching file in `.agents/reddit-social-writer/templates/storage/` when adding or normalizing items.

## Folders

- `posts/`
- `comment-replies/`

## Notes

- Keep real corpus files local. This repo only tracks keep files and workspace docs.
- Keep unpublished drafts out of this folder. Drafts belong in `content/reddit/drafts/`.
- Run `.agents/reddit-social-writer/scripts/validate_corpus.py` after adding or editing files.
