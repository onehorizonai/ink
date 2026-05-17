# Draft Spec

## Purpose

Use the selected Ink profile's LinkedIn draft root (`<contentRoots.linkedin>/drafts/`) for unpublished drafts only.

Do not place unpublished drafts in the published corpus.

## Layout

Store drafts under:

- `<contentRoots.linkedin>/drafts/posts/`
- `<contentRoots.linkedin>/drafts/comment-replies/`
- `<contentRoots.linkedin>/drafts/dms/`
- `<contentRoots.linkedin>/drafts/dm-replies/`
- `<contentRoots.linkedin>/drafts/reposts/`

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
- `program_id`
- `format_id`
- `run_id`
- `campaign_id`
- `asset_type`
- `source_brief`
- `based_on_examples`

Content Program fields are optional. Existing one-off drafts remain valid without them.

## Template

Use `templates/storage/draft.md`.
