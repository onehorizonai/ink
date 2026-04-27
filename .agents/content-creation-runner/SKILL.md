---
name: content-creation-runner
description: Turn approved One Horizon Ink content ideas into reviewable draft initiatives. Use when Codex is asked to process planned `[Ink Idea]` records, create `[Ink Draft]` child initiatives under `Ink - Blog`, `Ink - LinkedIn`, or `Ink - Reddit`, run the matching writer workflow, and leave draft content in One Horizon for human review. Do not use this skill for ideation, direct publishing, corpus storage, or automation setup.
---

# Content Creation Runner

One Horizon is the review source of truth. This workflow turns approved ideas into draft initiatives; it does not publish and does not create local LinkedIn or Reddit draft files.

## Workflow

1. Resolve workspace, author, and the `Ink - Blog`, `Ink - LinkedIn`, and `Ink - Reddit` parent initiatives.
2. Find `Planned` records titled `[Ink Idea] [Blog] ...`, `[Ink Idea] [LinkedIn] ...`, or `[Ink Idea] [Reddit] ...`; use `search_tasks`, then `get_task_details`.
3. Parse the Content Idea Brief. Required: `Recommended channel`, `Angle`, `Audience`, `Thesis`, `Proof needed`, `Risks`, and `Next workflow`.
4. If required brief data is missing, or a writer workflow would need user input, comment with the missing fields/questions and leave the idea `Planned`.
5. Run the channel writer:
   - Blog: `../blog-post-writer/SKILL.md`; do not write to `publish_output_dir`.
   - LinkedIn: `../linkedin-social-writer/SKILL.md`; do not use local draft scripts.
   - Reddit: `../reddit-research/SKILL.md` when needed, then `../reddit-social-writer/SKILL.md`; do not use local draft scripts.
6. Create one child initiative with `create_initiative`:
   - parent: matching `Ink - Channel`
   - title: `[Ink Draft] [Channel] <idea title without [Ink Idea]>`
   - status: `In Review`
   - description: draft content, source idea, review notes, assumptions, and `Ink automation checkpoint: content-creation-runner <ISO timestamp>`
7. Comment on the source idea with the draft initiative link, then mark the source idea `Completed`.

## Channel Gates

- Blog ideas must include `Blog type`; once the idea is approved, treat that type as confirmed.
- Reddit ideas must include a target subreddit or a `Reddit research need`.
- LinkedIn ideas need only the shared required fields.

## Output

Return processed ideas, created draft initiatives, planned ideas needing input, and failures.
