# Draft Spec

## Purpose

Use the selected Ink profile's Reddit draft root (`<contentRoots.reddit>/drafts/`) for unpublished drafts only.

Do not place unpublished drafts in the published corpus.

## Layout

Store drafts under:

- `<contentRoots.reddit>/drafts/posts/`
- `<contentRoots.reddit>/drafts/comment-replies/`

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
- `subreddit`

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
- `research_snapshot`

Content Program fields are optional. Existing one-off drafts remain valid without them.

## Template

Use `templates/storage/draft.md`.
