---
name: content-publishing-runner
description: Process reviewed One Horizon Ink draft initiatives into revised drafts or publish-ready output. Use when Codex is asked to handle `[Ink Draft]` initiatives under `Ink - Blog`, `Ink - LinkedIn`, or `Ink - Reddit` that are `Planned` or `In Progress`, apply human comments, prepare social posts for manual publishing, or rebuild blog drafts through the blog writer before creating publishing branches and pull requests. Do not use this skill for ideation, first-draft creation from ideas, corpus storage, or automation setup.
---

# Content Publishing Runner

`In Review` means human review. `Planned` or `In Progress` means the runner may act. Social publishing stays manual. Blog publishing means opening a PR.

Before mutating One Horizon records, read `../one-horizon-context-setup/references/ink-initiative-hierarchy.md`.

## Workflow

1. Find `Planned` or `In Progress` initiatives titled `[Ink Draft] [Blog] ...`, `[Ink Draft] [LinkedIn] ...`, or `[Ink Draft] [Reddit] ...`; use `search_tasks` or `list_initiatives`, then fetch details and comments.
2. For each draft initiative, verify its parent matches the channel in the title. If it is missing or under the wrong parent, call `update_initiative` with the matching `Ink - Channel` `parentInitiativeId` before applying feedback or publishing.
3. Treat comments containing `Ink automation checkpoint` as automation comments. Treat later non-automation comments as human feedback.
4. If human feedback exists, revise the draft with the matching writer skill, update the `## Draft` section with `patch_document(taskId=...)`, comment with a short change summary, and set status to `In Review`.
5. If no human feedback exists, treat the status move as publish intent:
   - LinkedIn: comment with final copy and say it is ready for manual LinkedIn publishing; set `In Review`.
   - Reddit: comment with final title/body and target subreddit; set `In Review`.
   - Blog: run the Blog Writer Publish Pass below, then run the Blog PR Path with that pass output; set `In Review` after the PR comment.

Do not mark social draft initiatives `Completed` here. Completion happens after the user stores/logs the published item.

## Blog Writer Publish Pass

Publishing a blog draft means sending the reviewed One Horizon draft back through `../blog-post-writer/SKILL.md`. This is mandatory even when the stored draft looks publish-ready, already has citations, or already has image notes. Do not write the stored `## Draft` section directly to the publishing repo.

Use this handoff shape when invoking the blog writer:

```text
Publish this reviewed Ink blog draft by rebuilding it through the full blog-post-writer workflow.

Inputs:
- One Horizon initiative: <taskId> <title>
- Current initiative description: <description>
- Stored draft body from ## Draft: <draft>
- Human review context: <later non-automation comments, or "none">
- Publish intent: create a publish-ready MDX article and required assets for a PR

Constraints:
- This is not a new idea. Preserve the approved thesis, audience, and core direction unless validation proves a change is needed.
- Run the full blog-post-writer workflow again before returning publish output.
- Rebuild sources, image plan, and prose instead of copying the stored draft directly.
- Return blockers instead of publish output if mandatory review or asset work cannot complete.
```

The blog writer pass must complete these checks before the PR path can start:

1. Resolve the confirmed blog post type from the draft or comments. If it is missing and cannot be safely inferred, comment the blocker and set the initiative `Blocked`.
2. Rerun internal corpus research, fresh external research, source validation, outline validation, image planning, image search, and image download.
3. Rerun both writing passes and the full review sequence: humanizer, style review, fact-check, source URL check, tone review, and Ramsay review.
4. Return the final MDX body, final metadata, required article filename or slug, selected/downloaded assets, optional uploaded asset paths, review ledger, and a short rebuild summary.
5. Treat unresolved Ramsay `Must Fix` items, failed source validation, missing required images, missing local publishing context, or incomplete review ledger as blockers. Comment the blocker and set the initiative `Blocked` instead of opening a PR.

## Blog PR Path

1. Read `../../.local/context/blog-publishing.local.md` and resolve `publish_output_dir`.
2. Find the publishing repo with `git -C <publish_output_dir> rev-parse --show-toplevel`.
3. If the repo is dirty, comment the blocker and set the initiative `Blocked`.
4. Create branch `geeza/ink-blog-<taskId>-<slug>`; append `-2`, `-3`, etc. on collision.
5. Write only the final MDX returned by the Blog Writer Publish Pass to `YYYY-MM-DD-short-slug.mdx` in `publish_output_dir`.
6. Commit only that article and the required assets returned by the Blog Writer Publish Pass, push, and open a PR with `gh pr create --title "Ink blog: <draft title>"`.
7. Comment with the PR URL, the rebuild summary, and `Ink automation checkpoint: content-publishing-runner <ISO timestamp>`.

If branch, commit, push, GitHub auth, or PR creation fails, comment the blocker and set `Blocked`.

## Output

Return processed drafts, revisions, social ready-to-publish items, blog PR URLs, and blockers.
