# Agent Notes

Start with [README.md](README.md).

## Repo rules

- Treat [linkedin-social-writer](.agents/linkedin-social-writer/SKILL.md) as the LinkedIn orchestrator.
- Treat [blog-post-writer](.agents/blog-post-writer/SKILL.md) as the blog orchestrator.
- Treat the shared references under `.agents/linkedin-social-writer/references/` as the source of truth for LinkedIn writing rules.
- Treat the shared references under `.agents/blog-post-writer/references/` as the source of truth for blog writing rules.
- Treat `.agents/context/` as the source of truth for public context contracts and starter templates.
- Treat `.local/context/` as the gitignored source of truth for live user identity, background, and personal context shared across agents.
- Treat `.agents/context/blog-publishing.md` as the source of truth for the blog path-resolution contract.
- Treat `.local/context/blog-publishing.local.md` as the gitignored source of truth for the active blog corpus source folder and published blog output folder.
- If a repo skill is missing from the current Codex session, run `./scripts/sync_repo_skills.sh` from the repo root to sync repo skills into every configured app skill directory, then restart the session if needed.
- Keep unpublished drafts in `content/linkedin/drafts/`.
- Keep unpublished blog drafts in `content/blog/drafts/`.
- Do not duplicate workflow or context rules across files unless there is a clear need.
