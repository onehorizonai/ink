---
name: linkedin-finalize-post
description: Finalize a LinkedIn post with the repo review workflow and store it in the published corpus only when approval is explicit. Use when the user asks to finalize a post, approve the final version, or save the approved post, and the result should go through the humanizer, tone, style, and optional fact-check passes before optionally being written into `content/linkedin/` with the repo storage template. Do not use this skill for simple corpus logging of already-written posts that do not need final editing.
---

# LinkedIn Finalize Post

Use this when the draft is close and needs a final pass before approval or storage.

## Read

- `../linkedin-social-writer/references/workflow.md`
- `../linkedin-social-writer/references/review-passes.md`
- `../linkedin-social-writer/references/corpus-spec.md`
- `../linkedin-social-writer/templates/README.md`

## Workflow

1. Run the normal post loop:
   - `../linkedin-humanizer/SKILL.md`
   - `../linkedin-tone-review/SKILL.md`
   - `../linkedin-style-review/SKILL.md`
   - `../linkedin-fact-check/SKILL.md` when needed
2. Produce the final candidate.
3. Store it only when approval is explicit.

## Approval rule

- If the user says to finalize but does not clearly approve storage, return the final draft and stop.
- If the user clearly approves or says to save/store the post, use the storage script.
- If the user is only asking to store existing posts, use `../linkedin-store-post/SKILL.md` instead.

## Write path

Use:

- `../linkedin-social-writer/scripts/store_published.py`

Carry forward:

- the final body
- the title
- the date if known
- the format template if one was used
- any metadata that belongs in the corpus entry

## One Horizon: Record Published Post

After local corpus storage succeeds, use the One Horizon MCP to create a child initiative under `Ink - LinkedIn`.

Before mutating One Horizon, read `../one-horizon-context-setup/references/ink-initiative-hierarchy.md`.

Fields:

- **Title**: the post title or the first 60 characters of the opening line
- **Description**: format, published date, and the local corpus path
- **Status**: `Completed`
- **Parent**: `Ink - LinkedIn` via `parentInitiativeId`

Rules:

- Only create the One Horizon record when local storage actually happened — not just when the draft is finalized without storage.
- If a matching LinkedIn initiative already exists and is missing the `Ink - LinkedIn` parent or is under a different parent, move it with `update_initiative` before updating or reporting it.
- If the One Horizon MCP is unavailable, log the corpus path in the response and continue. Do not block storage on One Horizon availability.
- If the `Ink - LinkedIn` parent initiative does not exist, note that in the output and skip the One Horizon step.

## Output

Return:

- the final draft
- the saved corpus path when storage happened
- the One Horizon initiative title and URL when the record was created
- any assumptions used during storage
