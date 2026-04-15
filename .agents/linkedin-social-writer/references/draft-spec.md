# Draft Spec

## Purpose

Use `content/linkedin/drafts/` for unpublished drafts only.

Do not place unpublished drafts in the published corpus.

## Layout

Store drafts under:

- `content/linkedin/drafts/posts/`
- `content/linkedin/drafts/comment-replies/`
- `content/linkedin/drafts/dms/`
- `content/linkedin/drafts/dm-replies/`
- `content/linkedin/drafts/reposts/`

## File Naming

Use:

```text
YYYY-MM-DD-NN--draft--format--short-slug.md
```

`NN` is the follow-up number for that date inside the format folder.

## Required Frontmatter

- `channel`
- `format`
- `status`
- `created_at`
- `title`

## Recommended Frontmatter

- `goal`
- `audience`
- `format_template`
- `asset_type`
- `source_brief`
- `based_on_examples`

## Template

Use `templates/storage/draft.md`.
