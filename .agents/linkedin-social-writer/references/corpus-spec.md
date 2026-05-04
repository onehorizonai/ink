# Corpus Spec

## Layout

Store one Markdown file per published item under `content/linkedin/` at the repo root.

Do not store unpublished drafts here. Store those in `content/linkedin/drafts/`.

Use these folders:

- `posts/`
- `comment-replies/`
- `dms/`
- `dm-replies/`
- `reposts/`

## File Naming

Use:

```text
YYYY-MM-DD-NN--linkedin--format--short-slug.md
```

Example:

```text
2026-03-18-01--linkedin--post--ai-agents-need-clear-owners.md
```

`NN` is the follow-up number for that date inside the format folder.

## Required Frontmatter

Keep these fields in every file:

- `channel`: Always `linkedin` for this skill.
- `format`: One of `post`, `comment-reply`, `dm`, `dm-reply`, `repost`.
- `published_at`: ISO date or datetime.
- `context`: Why this was written, what it responded to, or what campaign or situation it belonged to.
- `asset_type`: One of `none`, `image`, `carousel`, `video`, `document`, `link`, `other`.

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

- `comment-reply`: Capture the original comment or enough thread context to explain the response.
- `dm`: Capture who the recipient was, why the outreach was relevant, and what next step was being sought.
- `dm-reply`: Capture the inbound question or objection that the reply addressed.
- `repost`: Capture what was being reposted and why it mattered to the author.

## Template

Use the matching file in `templates/storage/` as the starting point for new archive entries.
