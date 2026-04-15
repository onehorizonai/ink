---
name: linkedin-store-post
description: Store one or more already written, shared, or published LinkedIn items in the corpus with deterministic filenames and the repo storage templates. Use when the user says things like "I shared this", "store this post", "store these posts", "store the following posts", "save this to the corpus", "add these to the corpus", "log this LinkedIn post", "import these posts", or provides multiple posts separated by `|`, especially when the content already exists and should be written into `content/linkedin/` with the correct format, date, follow-up number, and optional format-template metadata. Do not use this skill for drafting new copy or for final review before approval.
---

# LinkedIn Store Post

Use this to log content that was already shared.

## Defaults

- default `format` to `post` unless the user says otherwise
- default `published_at` to today if the user gives no date
- default `format_template` to `default-post` for posts unless another template is named
- derive the title from the opening line if the user does not provide one

## Intent Contract

- Use this skill when the primary user intent is storage, logging, saving, importing, or adding existing LinkedIn content to the corpus.
- Do not switch to the drafting workflow just because the stored content is pasted inline.
- Do not use `linkedin-finalize-post` unless the user also wants a final review pass before storage.

Examples that should route here:

- `Store this post:`
- `Store the following posts:`
- `Store the following posts (separated by |):`
- `Add these LinkedIn posts to the corpus`
- `Log these posts from this week`

## Ask only if needed

Ask only when the storage would be misleading without the answer.

High-value questions:

- Was this a post, comment reply, DM, DM reply, or repost?
- Was this shared today, or on another date?
- Which format template did this follow, if any?

If the user only says "I shared this:" and gives text, store it as a post for today.

## Batch Input

- If the user provides multiple posts separated by `|`, split on `|`, trim whitespace, and ignore empty items.
- Store each post as a separate corpus entry in input order.
- Apply shared defaults for `format`, `published_at`, and `format_template` unless the user gives per-item metadata.
- Do not merge multiple posts into one file.

## Read

- `../linkedin-social-writer/references/corpus-spec.md`
- `../linkedin-social-writer/templates/README.md`
- `../linkedin-social-writer/templates/formats/README.md`

## Write path

**Single post:**

```bash
python3 .agents/linkedin-social-writer/scripts/store_published.py --body "..."
```

**Multiple posts (batch):**

Write all posts to a temporary file separated by `|` (or `---` for multi-line posts), then call:

```bash
python3 .agents/linkedin-social-writer/scripts/store_published_batch.py \
  --posts-file /tmp/posts.txt \
  [--separator "|"] \
  [--format post] \
  [--published-at YYYY-MM-DD]
```

The batch script accepts the same metadata flags as `store_published.py` and applies them to every post in the file. It prints one stored path per post and a summary line at the end.

Do not handcraft filenames or file bodies manually when the scripts can do it.

## Output

Return:

- the saved path for each stored item
- the assumptions used for date, format, or template
