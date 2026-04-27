---
name: content-publishing-runner
description: Process reviewed One Horizon Ink draft initiatives into revised drafts or publish-ready output. Use when Codex is asked to handle `[Ink Draft]` initiatives under `Ink - Blog`, `Ink - LinkedIn`, or `Ink - Reddit` that are `Planned` or `In Progress`, apply human comments, prepare social posts for manual publishing, or create blog publishing branches and pull requests. Do not use this skill for ideation, first-draft creation from ideas, corpus storage, or automation setup.
---

# Content Publishing Runner

`In Review` means human review. `Planned` or `In Progress` means the runner may act. Social publishing stays manual. Blog publishing means opening a PR.

## Workflow

1. Find `Planned` or `In Progress` initiatives titled `[Ink Draft] [Blog] ...`, `[Ink Draft] [LinkedIn] ...`, or `[Ink Draft] [Reddit] ...`; use `search_tasks` or `list_initiatives`, then fetch details and comments.
2. Treat comments containing `Ink automation checkpoint` as automation comments. Treat later non-automation comments as human feedback.
3. If human feedback exists, revise the draft with the matching writer skill, update the `## Draft` section with `patch_document(taskId=...)`, comment with a short change summary, and set status to `In Review`.
4. If no human feedback exists, treat the status move as publish intent:
   - LinkedIn: comment with final copy and say it is ready for manual LinkedIn publishing; set `In Review`.
   - Reddit: comment with final title/body and target subreddit; set `In Review`.
   - Blog: run the Blog PR path below; set `In Review` after the PR comment.

Do not mark social draft initiatives `Completed` here. Completion happens after the user stores/logs the published item.

## Blog PR Path

1. Read `../../.local/context/blog-publishing.local.md` and resolve `publish_output_dir`.
2. Find the publishing repo with `git -C <publish_output_dir> rev-parse --show-toplevel`.
3. If the repo is dirty, comment the blocker and set the initiative `Blocked`.
4. Create branch `geeza/ink-blog-<taskId>-<slug>`; append `-2`, `-3`, etc. on collision.
5. Write `YYYY-MM-DD-short-slug.mdx` into `publish_output_dir`.
6. Commit only the article and required assets, push, and open a PR with `gh pr create --title "Ink blog: <draft title>"`.
7. Comment with the PR URL and `Ink automation checkpoint: content-publishing-runner <ISO timestamp>`.

If branch, commit, push, GitHub auth, or PR creation fails, comment the blocker and set `Blocked`.

## Output

Return processed drafts, revisions, social ready-to-publish items, blog PR URLs, and blockers.
