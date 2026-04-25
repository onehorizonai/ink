# Agent Notes

Start with [README.md](README.md).

## Repo rules

- Treat [linkedin-social-writer](.agents/linkedin-social-writer/SKILL.md) as the LinkedIn orchestrator.
- Treat [reddit-social-writer](.agents/reddit-social-writer/SKILL.md) as the Reddit drafting orchestrator.
- Use [reddit-research](.agents/reddit-research/SKILL.md) as the entry point for Reddit subreddit discovery, weekly top-post analysis, and writing handoff briefs.
- Treat [blog-post-writer](.agents/blog-post-writer/SKILL.md) as the blog orchestrator.
- Use [page-brief-builder](.agents/page-brief-builder/SKILL.md) as the entry point for website page briefs.
- Treat the shared references under `.agents/linkedin-social-writer/references/` as the source of truth for LinkedIn writing rules.
- Treat the shared references under `.agents/blog-post-writer/references/` as the source of truth for blog writing rules.
- Treat the shared references under `.agents/reddit-social-writer/references/` as the source of truth for Reddit writing and storage rules.
- Use [page-types.md](.agents/page-brief-page-playbook/references/page-types.md) for website page-type briefing rules.
- Use [seo-rules.md](.agents/page-brief-seo-playbook/references/seo-rules.md) for website page SEO briefing rules.
- Use [copy-rules.md](.agents/page-brief-copy-playbook/references/copy-rules.md) for website page copy and CTA briefing rules.
- Treat One Horizon author-scoped context docs as the source of truth for live user identity, background, and personal context shared across agents. Resolve the author through One Horizon MCP first, then use doc names shaped as `Ink Context - {Author Name} - {Doc Type}`.
- Treat `.local/context/blog-publishing.local.md` as the gitignored source of truth for the active blog corpus source folder and published blog output folder. This is the only local context file writer skills should read at runtime.
- Use `one-horizon-context-setup` to create missing One Horizon author context docs. Do not overwrite or refresh existing author context docs.
- Do not create or read live runtime context from tracked repo files.
- If a repo skill is missing from the current Codex session, run `./scripts/sync_repo_skills.sh` from the repo root, then start a new Codex thread or restart Codex. Current sessions do not reliably reload the skill list after syncing.
- Keep unpublished drafts in `content/linkedin/drafts/`.
- Keep unpublished Reddit drafts in `content/reddit/drafts/`.
- Keep unpublished blog drafts in `content/blog/drafts/`.
- For blog files, do not use the `NN--blog--` filename prefix; use date + slug only for published files.
- Do not duplicate workflow or context rules across files unless there is a clear need.
- Stay inside the website page-brief suite when the user asks for a strategic brief. Do not jump straight to final page copy.
- Website page briefs must be concise locked specs with exact page changes, exact H1/title/meta/CTA labels, and required links. Do not return a loose research summary or append a final checklist.
- After competitor research, brainstorm up to 3 viable page directions, then choose one or ask the user to choose before later brief steps continue.
- Use [page-brief-copy-playbook](.agents/page-brief-copy-playbook/SKILL.md) for exact copy atoms inside the brief.
- Use [copywriting](.agents/copywriting/SKILL.md) only when the user explicitly wants final page copy drafted, rewritten, or improved.
