---
name: reddit-store-post
description: Store one or more already written, shared, or published Reddit posts or comment replies in the local Reddit corpus with deterministic filenames and repo templates. Use when the primary user intent is storage, logging, saving, or importing existing Reddit content rather than drafting new copy.
---

# Reddit Store Post

Use this to log Reddit content that was already posted or fully written.

## Intent Split

- Use this skill when the primary user intent is storage, logging, saving, or importing existing Reddit content.
- Do not use this skill to draft new Reddit copy.
- Do not use this skill when the user wants a final review loop before storage. Use `../reddit-finalize-post/SKILL.md`.

## Defaults

- default `format` to `post` unless the user says otherwise
- default `published_at` to today if the user gives no date
- default `format_template` to `discussion-post` for posts unless another template is named
- derive the title from the opening line if the user does not provide one

## Intent Contract

- Use this skill when the primary user intent is storage, logging, saving, importing, or adding existing Reddit content to the corpus.
- Do not switch to the drafting workflow just because the stored content is pasted inline.
- Do not use `reddit-finalize-post` unless the user also wants a final review pass before storage.
- Valid `format` values are `post` and `comment-reply`.

Examples that should route here:

- `Store this Reddit post:`
- `Store this Reddit comment reply`
- `Add these Reddit posts to the corpus`
- `Log this post I shared in r/startups`

## Ask only if needed

Ask only when the storage would be misleading without the answer.

High-value questions:

- Was this a post or a comment reply?
- Which subreddit was it posted in?
- Was this shared today, or on another date?

If the user gives no subreddit, ask. Do not invent it.
If the user gives no format, store it as `post`.

## Read

- `../reddit-social-writer/references/corpus-spec.md`

## Write path

**Single item:**

```bash
python3 .agents/reddit-social-writer/scripts/store_published.py --subreddit startups --body "..."
```

**Multiple items (batch):**

Write all posts to a temporary file separated by `|` (or `---` for multi-line posts), then call:

```bash
python3 .agents/reddit-social-writer/scripts/store_published_batch.py \
  --posts-file /tmp/posts.txt \
  --subreddit startups \
  [--separator "|"] \
  [--format post] \
  [--published-at YYYY-MM-DD]
```

Do not handcraft filenames or file bodies manually when the scripts can do it.
Do not handwrite YAML frontmatter for normal storage flows when the scripts can do it.

## One Horizon: Record Published Post

After each local corpus write succeeds, use the One Horizon MCP to create a child initiative under `Ink - Reddit`.

Fields:

- **Title**: the post title or the first 60 characters of the opening line, with the subreddit in parentheses — e.g. `Why manual outreach beats automation early (r/startups)`
- **Description**: subreddit, format, published date, and the local corpus path
- **Status**: published (or the equivalent completed/done status available in the workspace)

Rules:

- Create one One Horizon record per stored item, not one record for the whole batch.
- If the One Horizon MCP is unavailable, log the corpus path in the response and continue. Do not block storage on One Horizon availability.
- If `Ink - Reddit` does not exist, note that and skip the One Horizon step for that item.

## Output

Return:

- the saved corpus path for each stored item
- the One Horizon initiative title for each item where the record was created
- the assumptions used for date, format, or template
