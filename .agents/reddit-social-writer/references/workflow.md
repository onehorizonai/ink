# Workflow

## 1. Build the brief

Capture:

- format
- audience
- goal
- topic or source material
- target subreddit if already known
- what must not be said or linked
- desired close, such as a question or debatable statement
- hard constraints such as banned claims, brand mentions, or timing

## 2. Ask only necessary questions

Ask questions only when the draft would otherwise require invention or would likely break subreddit fit.

Ask at most 3 short questions in one turn.

High-value questions:

- Which subreddit is this for, if you already know it?
- What is the main outcome of this post?
- Are there any product mentions, links, or claims that must stay out?

Do not ask for information that can be recovered from the research skill, One Horizon context docs, or the supplied brief.

## 3. Load the minimum user context

Resolve the author and load only the relevant author-scoped One Horizon context docs. Use `../../one-horizon-context-setup/references/context-doc-templates.md` for the naming contract:

- `Profile` for identity basics
- `Current Work` for almost every business draft
- `Market Context` when audience or positioning matters
- `Work History` only when credibility or lived experience matters

Do not load unrelated personal docs just because they exist.
Do not use tracked repo files for live runtime context.
If a required One Horizon tool call is missing or fails, follow `../../one-horizon-context-setup/references/mcp-readiness.md`.

## 4. Run Reddit research

- Use `../../reddit-research/SKILL.md` unless the user already provided a stable subreddit brief.
- Treat the research output as the source of truth for:
  - candidate subreddits
  - winning recent post patterns
  - rule constraints
  - anti-promo guardrails
  - the recommended close style

Do not proceed with drafting until you have:

- one `target_subreddit`
- one `recommended_angle`
- the matching `rules_and_guardrails`

If the request is a comment reply and includes a Reddit URL, use `reddit_post_thread` with the exact argument shape from `../../reddit-research/references/tool-contracts.md` before drafting.

## 5. Retrieve examples

- Search the same format folder in `../../content/reddit/` first.
- Use 3-5 good examples before widening.
- If the local Reddit archive is thin, say so explicitly and continue.
- Favor examples from the same subreddit when available.

## 6. Draft fast

- Write a fresh draft from the brief, the research, the selected examples, and the One Horizon context.
- Stay close to the subreddit fit, not to any single source post.
- Keep one central idea per draft.
- Default to a useful, discussion-first close instead of a CTA.

For posts, structure the result as:

- `Title`
- `Body`

## 7. Run staged review passes

Read `references/review-passes.md`.

For every post:

- run the humanizer pass first
- run the tone review pass second
- run the style review pass third

Add:

- the fact-check pass when the draft includes unstable claims, dates, names, numbers, product claims, or references to external events
- one extra tightening pass for strong opinions, longer posts, or anything that risks sounding promotional

## 8. Save drafts separately

If the user wants the draft stored locally:

- use `scripts/create_draft.py`
- write to `content/reddit/drafts/`
- never place unpublished drafts inside `content/reddit/`

## 9. Store shared or approved posts

- Use `../reddit-store-post/SKILL.md` when the user says they already posted something and wants it logged in the corpus.
- Use `../reddit-finalize-post/SKILL.md` when the user wants a draft finalized and then stored only after approval is explicit.
- Use `scripts/store_published.py` for the actual write so naming and templates stay consistent.

Do not handwrite storage filenames or corpus frontmatter when the scripts can do it.

## 10. Final response

Return:

- the final draft
- what research, context, and examples were used
- the subreddit and rule constraints that shaped it
- what assumptions remain
- what was checked, if fact review happened
