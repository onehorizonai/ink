---
name: content-creation-runner
description: Turn approved One Horizon Ink content ideas into reviewable drafts. Use when Codex is asked to process planned `[Ink Idea]` records, run the matching writer workflow, update Blog initiatives in place from `[Ink Idea] [Blog]` to `[Ink Draft] [Blog]`, and leave draft content in One Horizon for human review. Do not use this skill for ideation, direct publishing, corpus storage, or automation setup.
---

# Content Creation Runner

One Horizon is the review source of truth. For Blog, follow the Blog Lifecycle Contract in `../one-horizon-context-setup/references/ink-initiative-hierarchy.md`. This workflow does not publish or create local LinkedIn or Reddit draft files.

Resolve the active Ink profile before any One Horizon search or writer invocation. If more than one profile is configured and none is named in the prompt or `INK_PROFILE`, ask which profile to use. If One Horizon auth or tools are unavailable, stop. Do not draft, guess context, use the One Horizon default workspace silently, or use local fallback context.
Before mutating One Horizon records, read `../one-horizon-context-setup/references/ink-initiative-hierarchy.md`.
When an idea needs human input, read `references/planned-blocker-comment.md`, comment, and set the idea status to `In Review`.

## Workflow

1. Resolve the selected Ink profile with `../one-horizon-context-setup/references/ink-profile-contract.md`, then resolve workspace, author, and the `Ink - Blog`, `Ink - LinkedIn`, and `Ink - Reddit` parent initiatives inside that workspace.
2. Find `Planned` records titled `[Ink Idea] [Blog] ...`, `[Ink Idea] [LinkedIn] ...`, or `[Ink Idea] [Reddit] ...`; use `search_tasks`, then `get_task_details`.
3. If a source `[Ink Idea]` record is an initiative and its parent is missing or does not match the channel, move it with `update_initiative` before drafting. If a Blog idea is not an initiative, move it to `In Review` with a blocker comment asking for conversion to a single Blog initiative. If a non-Blog idea is not an initiative and the available mutation tool has no parent field, note that and continue.
4. Parse the Content Idea Brief. Required to draft: channel, angle, audience, and enough thesis direction to avoid inventing the core argument. Treat missing `Proof needed`, `Risks`, and `Next workflow` as draft assumptions.
5. Resolve required author context by exact One Horizon document title inside the selected profile workspace before invoking the writer. Follow `../one-horizon-context-setup/references/context-doc-templates.md` for missing or unreadable docs.
6. If the idea still needs user input, comment with `references/planned-blocker-comment.md`, set the source idea to `In Review` with `update_feature_request` for reported ideas or `update_initiative` for initiative records, and stop. Do not post raw `missing fields` lists. Do not leave human-action items in `Planned`.
7. Run the channel writer:
   - Blog: `../blog-post-writer/SKILL.md`; do not write to `publish_output_dir`.
   - LinkedIn: `../linkedin-social-writer/SKILL.md`; do not use local draft scripts.
   - Reddit: `../reddit-research/SKILL.md` when needed, then `../reddit-social-writer/SKILL.md`; do not use local draft scripts.
8. Store the draft:
   - Blog: update the same initiative title/status and linked content document according to the Blog Lifecycle Contract. Use `update_initiative` for metadata and `patch_document(taskId=...)` or `update_document` for the document.
   - LinkedIn and Reddit: create one child initiative with `create_initiative`, using the matching `Ink - Channel` parent, title `[Ink Draft] [Channel] <idea title without [Ink Idea]>`, status `In Review`, and a description containing draft content, source idea, review notes, assumptions, and `Ink automation checkpoint: content-creation-runner <ISO timestamp>`.
9. For Blog, comment on the same initiative with a short draft summary and `Ink automation checkpoint: content-creation-runner <ISO timestamp>`. Do not mark the initiative `Completed`; it is now the review draft. For LinkedIn and Reddit, comment on the source idea with the draft initiative link, then mark the source idea `Completed`.

## Channel Gates

- Blog ideas must be initiatives under `Ink - Blog` and must include or clearly imply `Blog type`; once approved, treat that type as confirmed. If wording is clear but not exact, normalize it to the closest supported type and continue.
- If a legacy Blog idea is not an initiative, do not create a separate draft initiative. Move it to `In Review` with a blocker comment asking for conversion to a single Blog initiative.
- Reddit ideas must include a target subreddit or a `Reddit research need`.
- LinkedIn ideas need only the shared required fields.
- Do not fail older or thinner idea records only because `Proof needed`, `Risks`, or `Next workflow` is absent. Use the channel from the title or `Recommended channel`, route to the matching writer, and include `Proof needed: unspecified`, `Risks: default channel risk check`, or `Next workflow: inferred from channel` in the draft notes.

## Output

Return processed ideas, updated Blog initiatives, created social draft initiatives, ideas moved to `In Review` for human input, and failures.
