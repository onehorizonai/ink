---
name: reddit-finalize-post
description: Finalize a Reddit post or comment reply with the repo review workflow and store it in the local Reddit corpus only when approval is explicit. Use when the draft is close and needs the last review loop before optional storage.
---

# Reddit Finalize Post

Use this when the draft is close and needs a final pass before approval or storage.

## Intent Split

- Use this skill for final-pass review plus optional storage.
- Do not use this skill for storage-only requests. Use `../reddit-store-post/SKILL.md`.
- Do not use this skill for fresh subreddit discovery. Use `../reddit-research/SKILL.md`.

## Read

- `../reddit-social-writer/references/workflow.md`
- `../reddit-social-writer/references/review-passes.md`
- `../reddit-social-writer/references/corpus-spec.md`

## Workflow

1. Run the normal Reddit loop:
   - `../content-humanizer/SKILL.md`
   - `../content-tone-review/SKILL.md`
   - `../content-style-review/SKILL.md`
   - `../fact-check/SKILL.md` when needed
2. Produce the final candidate.
3. Store it only when approval is explicit.

Keep the subreddit, format, and any rule-sensitive wording stable unless the review loop finds a real fit problem.

## Approval rule

- If the user says to finalize but does not clearly approve storage, return the final draft and stop.
- If the user clearly approves or says to save/store the post, use the storage script.
- If the user is only asking to store existing posts, use `../reddit-store-post/SKILL.md` instead.
- If the subreddit is missing, ask before storage. Do not invent it because `store_published.py` requires `--subreddit`.

## Write path

Use:

- `../reddit-social-writer/scripts/store_published.py`

Carry forward:

- the final body
- the title
- the subreddit
- the date if known
- the format template if one was used
- any metadata that belongs in the corpus entry

## One Horizon: Record Published Post

After local corpus storage succeeds, use the One Horizon MCP to create a child initiative under `Ink - Reddit`.

Fields:

- **Title**: the post title or the first 60 characters of the opening line, with the subreddit appended in parentheses — e.g. `Why manual outreach beats automation early (r/startups)`
- **Description**: subreddit, format, published date, and the local corpus path
- **Status**: published (or the equivalent completed/done status available in the workspace)

Rules:

- Only create the One Horizon record when local storage actually happened — not just when the draft is finalized without storage.
- If the One Horizon MCP is unavailable, log the corpus path in the response and continue. Do not block storage on One Horizon availability.
- If the `Ink - Reddit` parent initiative does not exist, note that in the output and skip the One Horizon step.

## Output

Return:

- the final draft
- the saved corpus path when storage happened
- the One Horizon initiative title when the record was created
- any assumptions used during storage
