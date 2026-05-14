# Reddit Corpus

This directory is the local Reddit corpus workspace.

In multi-profile installs, use the selected Ink profile's `contentRoots.reddit` instead. This legacy repo path is the default One Horizon profile root only when no profile config exists or the profile points here.

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
- Keep unpublished drafts out of published format folders. Drafts belong under `<contentRoots.reddit>/drafts/`.
- Run `.agents/reddit-social-writer/scripts/validate_corpus.py --profile <profileId>` after adding or editing files when profiles are configured.
