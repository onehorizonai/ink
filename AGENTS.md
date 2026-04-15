# Agent Notes

Start with [README.md](README.md).

## Repo rules

- Treat [linkedin-social-writer](.agents/linkedin-social-writer/SKILL.md) as the LinkedIn orchestrator.
- Treat [blog-post-writer](.agents/blog-post-writer/SKILL.md) as the blog orchestrator.
- Treat the shared references under `.agents/linkedin-social-writer/references/` as the source of truth for LinkedIn writing rules.
- Treat the shared references under `.agents/blog-post-writer/references/` as the source of truth for blog writing rules.
- Treat `.local/README.md` as the source of truth for local-context setup and runtime file conventions.
- Treat `.local/context/` as the gitignored source of truth for live user identity, background, personal context, and blog-path state shared across agents.
- Treat `.local/context/blog-publishing.local.md` as the gitignored source of truth for the active blog corpus source folder and published blog output folder.
- Do not create or read live runtime context from tracked repo files outside `.local/`.
- If a repo skill is missing from the current Codex session, run `./scripts/sync_repo_skills.sh` from the repo root to sync repo skills into every configured app skill directory, then restart the session if needed.
- Keep unpublished drafts in `content/linkedin/drafts/`.
- Keep unpublished blog drafts in `content/blog/drafts/`.
- Do not duplicate workflow or context rules across files unless there is a clear need.
