---
name: reddit-social-writer
description: Draft Reddit posts and follow-up comment replies using local context, subreddit research, the Reddit corpus, and Ink's staged review passes. Use when Codex needs to write or revise Reddit content that should fit subreddit norms instead of sounding like generic social copy.
---

# Reddit Social Writer

## Overview

Ground every Reddit draft in the subreddit first, then in the author's context and any saved Reddit corpus examples. Use the separate research skill to decide where and how to post before drafting.

## Intent Split

- Use this skill to draft or revise Reddit posts and comment replies.
- Use `../reddit-research/SKILL.md` for subreddit discovery, rules, and top-post analysis.
- Use `../reddit-store-post/SKILL.md` for storage-only requests.
- Use `../reddit-finalize-post/SKILL.md` when the draft is already close and needs the final review loop before optional storage.

## Quick Start

1. Read `references/workflow.md`.
2. Read `../../.local/README.md`, then load only the relevant files from `../../.local/context/`.
3. Read `../reddit-research/references/tool-contracts.md` if you need to call Reddit tools directly.
4. Run `../reddit-research/SKILL.md` unless the user already supplied a stable subreddit brief with rules and angle constraints.
5. Search `../../content/reddit/` for 3-5 relevant examples when the local Reddit corpus exists.
6. Draft against the matching playbook in `references/format-playbooks.md`.
7. Run the review passes described in `references/review-passes.md`.
8. Save unpublished drafts in `content/reddit/drafts/` if the user wants them persisted.
9. Use the dedicated finalize/store paths when the user wants approval or storage rather than fresh drafting.

## Working Agreement

- Prioritize subreddit fit over generic brand voice. Reddit punishes tone mismatch faster than LinkedIn does.
- Use the Reddit corpus as the source of truth for what this author has already posted, but if the corpus is thin, let subreddit norms drive the draft.
- Use local context files to make the writing authentic, but load only what is relevant to the task.
- Use `.local/context/*.md` for live runtime context. Do not use tracked repo files outside `.local/` for live context.
- Reuse patterns, not sentences. Do not lift title shapes or body phrasing from top Reddit posts.
- Treat subreddit rules and anti-promo norms as hard constraints, not suggestions.
- Default to text-first discussion posts. Do not assume links, screenshots, or product mentions are welcome.
- Do not draft until you have one target subreddit plus the rule and anti-promo constraints that apply there. If those are missing, run `../reddit-research/SKILL.md`.
- Ask only the smallest set of high-leverage questions. If the prompt, research, and local context are enough, do not ask.
- Keep unpublished drafts separate from the published Reddit corpus at all times.
- If the user asks to store, save, import, or log existing Reddit posts, route to `../reddit-store-post/SKILL.md`.
- If the user asks to finalize and then optionally store an approved Reddit draft, route to `../reddit-finalize-post/SKILL.md`.
- Use the exact Reddit tool schemas from `../reddit-research/references/tool-contracts.md` when you need thread context or subreddit refreshes.

## Workflow

Follow the shared workflow in `references/workflow.md`.

For posts:

- Run at least 3 iterations.
- Start with `../content-humanizer/SKILL.md`.
- Continue with `../content-tone-review/SKILL.md`.
- Continue with `../content-style-review/SKILL.md`.
- Add `../fact-check/SKILL.md` whenever the draft contains unstable or external claims.
- Add one extra tightening pass for longer, more opinionated, or higher-risk posts.

For comment replies:

- Keep the loop lighter, but still run the humanizer pass early and tone review before finalizing.

## Format Rules

- `post`: Deliver one polished Reddit post for a specific subreddit. Include a title and body when the subreddit uses titled text posts.
- `comment-reply`: Reply to the actual thread or comment first. Keep it conversational, useful, and non-promotional.

## Supporting Skills

Use the local thin skills first because they are tuned for this repo's workflow:

- `../reddit-research/SKILL.md`
- `../content-humanizer/SKILL.md`
- `../content-tone-review/SKILL.md`
- `../content-style-review/SKILL.md`
- `../fact-check/SKILL.md`
- `../reddit-store-post/SKILL.md`
- `../reddit-finalize-post/SKILL.md`

If the session also includes external writing skills, use them in support of this skill instead of replacing it.

- Use `../copywriting/SKILL.md` only after subreddit fit is already established.
- Use `$humanizer` as reference material for the local humanizer pass, not as a replacement for the repo workflow.

Keep the local Reddit corpus, subreddit research, and shared repo references as the source of truth when those skills pull in a different style.

## Output Shape

Unless the user asks differently, return:

- the final draft first
- the recommended subreddit and research inputs used
- the local context files and corpus examples used
- a short note on the rules, tone, and anti-promo constraints that shaped the draft
- any assumptions or missing facts that could change the draft
- the saved draft path if you persisted the draft to `content/reddit/drafts/`

For `post`, return this draft shape:

- `Title`
- `Body`

For `comment-reply`, return the reply only unless the user asks for alternatives.

## Files

- Read `references/corpus-spec.md` for the archive schema.
- Read `references/draft-spec.md` for unpublished draft storage.
- Read `references/workflow.md` for the orchestration flow.
- Read `references/review-passes.md` for pass order and responsibilities.
- Read `references/format-playbooks.md` for format-specific drafting rules.
- Read `../reddit-research/references/tool-contracts.md` if you need to call the Reddit tools directly.
- Read `../../.local/README.md` before loading any user context.
- Read `../../content/reddit/README.md` if the corpus location or naming is unclear.
- Read `../linkedin-social-writer/references/mcp-tools.md` before using the local research tools.
- Use `scripts/create_draft.py` when you need to persist an unpublished draft.
- Use `scripts/store_published.py` when you need to persist a shared or approved post in the corpus.
- Run `scripts/validate_corpus.py` after corpus updates or before larger drafting sessions.
