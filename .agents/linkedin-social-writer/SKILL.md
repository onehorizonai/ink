---
name: linkedin-social-writer
description: Orchestrate LinkedIn social writing from brief to final draft using a published-post corpus, One Horizon context docs, staged review passes, and optional local MCP research tools. Use when Codex needs to draft or revise original LinkedIn posts, comment replies, DMs, DM replies, or reposts while matching the saved voice, loading only the relevant One Horizon context, asking only necessary questions, and iterating through humanizer, tone, style, and fact-check passes. Do not use this skill for storage-only requests such as logging, saving, importing, or batch-storing already-written posts in the corpus.
---

# LinkedIn Social Writer

## Overview

Ground every draft in the published corpus. Extract the voice from a small set of relevant examples, then write fresh copy that fits the brief, the format, and the relationship stage.

## Quick Start

1. Read `references/workflow.md`.
2. Resolve the author and load only the relevant author-scoped One Horizon context docs. Use `../one-horizon-context-setup/references/context-doc-templates.md` for the naming and missing-doc contract.
3. Search `../../content/linkedin/` for 3-7 relevant examples. Prefer the same format first, then widen only if the archive is thin.
4. Distill voice markers with `references/style-capture.md`.
5. Draft against the matching playbook in `references/format-playbooks.md`.
6. Run the review passes described in `references/review-passes.md`.
7. Save unpublished drafts in `content/linkedin/drafts/` if the user wants them persisted.
8. Store shared or approved posts with the dedicated store/finalize path when appropriate.
9. Run `scripts/validate_corpus.py` after corpus updates or before larger drafting sessions.

## Working Agreement

- Use the corpus as the source of truth for tone, pacing, formatting, CTA style, and how directly to sell.
- Use One Horizon context docs to make the writing authentic, but load only what is relevant to the task.
- Use One Horizon context docs for live runtime context. Do not use tracked repo files for live context.
- If a required author-scoped context doc is missing or unusable, use `../one-horizon-context-setup/SKILL.md` to create the missing doc through its confirmation flow before drafting.
- If a One Horizon tool call is missing or fails, follow `../one-horizon-context-setup/references/mcp-readiness.md`. Do not search tracked repo files as a substitute for live context.
- Reuse patterns, not sentences. Do not remix published copy line by line.
- Prefer a narrow, evidence-based voice profile over generic LinkedIn language.
- Treat asset descriptions as part of the brief. If an image or carousel exists, make the text and visual work together.
- Ask only the smallest set of high-leverage questions. If the brief, corpus, and One Horizon context are sufficient, do not ask.
- Keep unpublished drafts separate from the published corpus at all times.
- If the user asks to store, save, import, or log existing posts, route to `../linkedin-store-post/SKILL.md` instead of drafting.
- If the user asks to finalize and then store an approved post, route to `../linkedin-finalize-post/SKILL.md`.

## Workflow

Follow the shared workflow in `references/workflow.md`.

For posts:

- Run at least 3 iterations.
- Start with `../content-humanizer/SKILL.md`.
- Continue with `../content-tone-review/SKILL.md`.
- Continue with `../content-style-review/SKILL.md`.
- Add `../fact-check/SKILL.md` whenever the draft contains unstable or external claims.
- Add one extra self-edit for longer posts, story-led posts, or drafts with multiple claims.

For replies, DMs, and reposts:

- Keep the loop lighter, but still run the humanizer pass early and tone review before finalizing.

## Format Rules

- `post`: Deliver one polished post. Offer 2 hook alternatives only if asked or if the brief is weak.
- `comment-reply`: Reply to the actual comment first. Keep it conversational. Do not force a CTA.
- `dm`: Make it personal and low-friction. Earn the next step instead of demanding it.
- `dm-reply`: Answer the inbound message directly, then move the thread forward with one clear next action.
- `repost`: Add a real point of view or interpretation. Do not post a vague wrapper around someone else's post.

## Supporting Skills

Use the local thin skills first because they are tuned for this repo's workflow:

- `../content-humanizer/SKILL.md`
- `../content-tone-review/SKILL.md`
- `../content-style-review/SKILL.md`
- `../fact-check/SKILL.md`
- `../linkedin-store-post/SKILL.md`
- `../linkedin-finalize-post/SKILL.md`
- `../social-common/references/repetition-guard.md`

If the session also includes external writing skills, use them in support of this skill instead of replacing it.

- Use `../copywriting/SKILL.md` to sharpen structure or CTA options after the corpus voice is established.
- Use `$humanizer` as reference material for the local humanizer pass, not as a replacement for the repo workflow.
- Use `$prompt-engineering-patterns` principles to keep the workflow strict, progressive, and low-noise.

Keep the published corpus and shared repo references as the source of truth when those skills pull in a different style.

## Output Shape

Unless the user asks differently, return:

- the final draft first
- the key One Horizon context docs and corpus examples used
- a short note listing the voice cues you matched
- any assumptions or missing facts that could change the draft
- the saved draft path if you persisted the draft to `content/linkedin/drafts/`

## Files

- Read `references/corpus-spec.md` for the archive schema.
- Read `references/draft-spec.md` for unpublished draft storage.
- Read `references/workflow.md` for the orchestration flow.
- If a One Horizon tool call fails, read `../one-horizon-context-setup/references/mcp-readiness.md` for recovery.
- Read `references/review-passes.md` for pass order and responsibilities.
- Read `references/style-capture.md` when extracting voice markers.
- Read `references/format-playbooks.md` for format-specific drafting rules.
- Read `../social-common/references/repetition-guard.md` when comparing a draft against recent corpus patterns.
- Resolve the author with One Horizon MCP tools, then load relevant author-scoped context from One Horizon using the naming and missing-doc contract in `../one-horizon-context-setup/references/context-doc-templates.md`.
- Read `../../content/linkedin/README.md` if the corpus location or naming is unclear.
- Read `references/mcp-tools.md` before using local research tools.
- Read `templates/README.md` when the request involves reusable format templates.
- Use `scripts/create_draft.py` when you need to persist an unpublished draft.
- Use `scripts/store_published.py` when you need to persist a shared or approved post in the corpus.
- Run `scripts/validate_corpus.py` after corpus updates or before large drafting sessions.
