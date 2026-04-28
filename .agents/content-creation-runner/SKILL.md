---
name: content-creation-runner
description: Turn approved One Horizon Ink content ideas into reviewable draft initiatives. Use when Codex is asked to process planned `[Ink Idea]` records, create `[Ink Draft]` child initiatives under `Ink - Blog`, `Ink - LinkedIn`, or `Ink - Reddit`, run the matching writer workflow, and leave draft content in One Horizon for human review. Do not use this skill for ideation, direct publishing, corpus storage, or automation setup.
---

# Content Creation Runner

One Horizon is the review source of truth. This workflow turns approved ideas into draft initiatives; it does not publish and does not create local LinkedIn or Reddit draft files.

Before mutating One Horizon records, read `../one-horizon-context-setup/references/ink-initiative-hierarchy.md`.
When an idea needs human input, read `references/planned-blocker-comment.md`, comment, and set the idea status to `In Review`.

## Workflow

1. Resolve workspace, author, and the `Ink - Blog`, `Ink - LinkedIn`, and `Ink - Reddit` parent initiatives.
2. Find `Planned` records titled `[Ink Idea] [Blog] ...`, `[Ink Idea] [LinkedIn] ...`, or `[Ink Idea] [Reddit] ...`; use `search_tasks`, then `get_task_details`.
3. If a source `[Ink Idea]` record is an initiative and its parent is missing or does not match the channel, move it with `update_initiative` before drafting. If it is not an initiative and the available mutation tool has no parent field, note that and continue.
4. Parse the Content Idea Brief. Required to draft: channel, angle, audience, and enough thesis direction to avoid inventing the core argument. Treat missing `Proof needed`, `Risks`, and `Next workflow` as draft assumptions.
5. If the idea still needs user input, comment with `references/planned-blocker-comment.md`, set the source idea to `In Review` with `update_feature_request` for reported ideas or `update_initiative` for initiative records, and stop. Do not post raw `missing fields` lists. Do not leave human-action items in `Planned`.
6. Run the channel writer:
   - Blog: `../blog-post-writer/SKILL.md`; do not write to `publish_output_dir`.
   - LinkedIn: `../linkedin-social-writer/SKILL.md`; do not use local draft scripts.
   - Reddit: `../reddit-research/SKILL.md` when needed, then `../reddit-social-writer/SKILL.md`; do not use local draft scripts.
7. Create one child initiative with `create_initiative`:
   - `parentInitiativeId`: matching `Ink - Channel` initiative task ID
   - title: `[Ink Draft] [Channel] <idea title without [Ink Idea]>`
   - status: `In Review`
   - description: draft content, source idea, review notes, assumptions, and `Ink automation checkpoint: content-creation-runner <ISO timestamp>`
8. Comment on the source idea with the draft initiative link, then mark the source idea `Completed`.

## Channel Gates

- Blog ideas must include or clearly imply `Blog type`; once the idea is approved, treat that type as confirmed. If wording is clear but not an exact playbook label, normalize it to the closest supported type and continue. Example: `practical explainer with opinion backbone` means primary type `explainer` with an opinion angle note.
- Reddit ideas must include a target subreddit or a `Reddit research need`.
- LinkedIn ideas need only the shared required fields.
- Do not fail older or thinner idea records only because `Proof needed`, `Risks`, or `Next workflow` is absent. Use the channel from the title or `Recommended channel`, route to the matching writer, and include `Proof needed: unspecified`, `Risks: default channel risk check`, or `Next workflow: inferred from channel` in the draft notes.

## Output

Return processed ideas, created draft initiatives, ideas moved to `In Review` for human input, and failures.
