# Workflow

## 1. Build the brief

Capture:

- format
- audience
- goal
- topic or source material
- CTA or desired next step
- asset type and asset summary
- hard constraints such as length, banned claims, mentions, links, or timing

## 2. Ask only necessary questions

Ask questions only when the draft would otherwise require invention or lead to the wrong angle.

Ask at most 3 short questions in one turn.

High-value questions:

- What is the main outcome of this post or message?
- Who is it for?
- Is there an asset, source, or specific claim that must be included?

Do not ask for information that can be recovered from the corpus, the local context files, or the supplied brief.

## 3. Load the minimum user context

Start with `../../context/index.md`.

Load:

- `.local/context/profile.md` for identity basics
- `.local/context/current-work.md` for almost every business draft
- `.local/context/work-history.md` only when credibility, story, or background matters
- `.local/context/personal-interests.md` only when it helps the angle feel lived-in
- `.local/context/personal-life.md` only when the post is explicitly personal or reflective

Do not load personal files just because they exist.

## 4. Retrieve examples

- Search the same format folder first.
- Use 3-5 good examples before widening.
- Expand to adjacent formats only when the exact bucket is thin.
- Favor recent examples when the voice may have shifted.

If the user names a reusable format template, read it from `templates/formats/`.

## 5. Draft fast

- Write a fresh draft from the brief, the context, and the selected examples.
- Stay close to the voice profile, not to any single source post.
- Keep one central idea per draft.

## 6. Run staged review passes

Read `references/review-passes.md`.

For every post:

- run the humanizer pass first
- run the tone review pass second
- run the style review pass third

Add:

- the fact-check pass when the draft includes unstable claims, dates, names, numbers, product claims, or references to external events
- one extra tightening pass for long posts, nuanced founder posts, or posts with multiple moving parts

## 7. Save drafts separately

If the user wants the draft stored locally:

- use `scripts/create_draft.py`
- write to `content/linkedin/drafts/`
- never place unpublished drafts inside `content/linkedin/`

## 8. Store shared or approved posts

- Use `../linkedin-store-post/SKILL.md` when the user says they already shared something and wants it logged in the corpus.
- Use `../linkedin-store-post/SKILL.md` when the user says things like `Store this post`, `Store these posts`, `Store the following posts`, or provides multiple posts separated by `|`.
- Use `../linkedin-finalize-post/SKILL.md` when the user wants a post finalized and then stored only after approval is explicit.
- Use `scripts/store_published.py` for the actual write so naming and templates stay consistent.

## 9. Final response

Return:

- the final draft
- what context and examples were used
- what assumptions remain
- what was checked, if fact review happened
