# Claude Context

This repo contains LinkedIn and blog writing agent setups.

Read in this order:

1. [README.md](README.md)
2. [AGENTS.md](AGENTS.md)
3. [linkedin-social-writer/SKILL.md](.agents/linkedin-social-writer/SKILL.md) for LinkedIn work
4. [blog-post-writer/SKILL.md](.agents/blog-post-writer/SKILL.md) for blog work

Use the shared references instead of inventing duplicate local rules.
Use `.local/README.md` as the local setup contract.
Use author-scoped One Horizon context docs for live user and company context.
Use `.local/context/blog-publishing.local.md` only for machine-local blog path state.
Do not use tracked repo files for live runtime context.
