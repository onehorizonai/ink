# Corpus Spec

## Layout

Store one Markdown file per published item under `content/reddit/` at the repo root.

Do not store unpublished drafts here. Store those in `content/reddit/drafts/`.

Use these folders:

- `posts/`
- `comment-replies/`

## File Naming

Use:

```text
YYYY-MM-DD-NN--reddit--format--short-slug.md
```

Example:

```text
2026-04-23-01--reddit--post--what-founders-get-wrong-about-distribution.md
```

`NN` is the follow-up number for that date inside the format folder.

## Required Frontmatter

Keep these fields in every file:

- `channel`: Always `reddit` for this skill.
- `format`: One of `post`, `comment-reply`.
- `published_at`: ISO date or datetime.
- `subreddit`: The target subreddit without the `/r/` prefix.
- `context`: Why this was written, what thread it answered, or what situation it belonged to.
- `asset_type`: One of `none`, `image`, `video`, `link`, `poll`, `other`.

## Recommended Frontmatter

Add these whenever known:

- `title`
- `format_template`
- `audience`
- `goal`
- `topic_tags`
- `author`
- `source_url`
- `thread_summary`
- `outcome_notes`
- `based_on_research`
- `discussion_prompt`

## Conditional Frontmatter

- Add `asset_summary` whenever `asset_type` is not `none`.

## Body Sections

Use these sections in this order:

1. `## Published Copy`
2. `## Context Notes`
3. `## Asset Notes`
4. `## Outcome Notes`

Only `Published Copy` is mandatory. Keep the other sections if you have useful context.

## Notes By Format

- `post`: Capture the subreddit and the research angle that shaped the post.
- `comment-reply`: Capture enough thread context to explain the response and the claim it answered.

## Template

Use the matching file in `templates/storage/` as the starting point for new archive entries.
