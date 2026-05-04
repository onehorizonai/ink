# Draft Spec

## Purpose

Use `content/reddit/drafts/` for unpublished drafts only.

Do not place unpublished drafts in the published corpus.

## Layout

Store drafts under:

- `content/reddit/drafts/posts/`
- `content/reddit/drafts/comment-replies/`

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
- `asset_type`
- `source_brief`
- `based_on_examples`
- `research_snapshot`

## Template

Use `templates/storage/draft.md`.
