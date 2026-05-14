# Reuse Map

Prefer composition over duplicate logic.

## Core Local Sub-Skills

Use these repo-local skills as the default workflow components:

- `../../website-brief-intake/SKILL.md`
- `../../website-pattern-analyzer/SKILL.md`
- `../../competitor-page-research/SKILL.md`
- `../../page-brief-page-playbook/SKILL.md`
- `../../page-seo-intent-planner/SKILL.md`
- `../../page-brief-seo-playbook/SKILL.md`
- `../../page-positioning-strategist/SKILL.md`
- `../../conversion-cta-planner/SKILL.md`
- `../../page-brief-copy-playbook/SKILL.md`
- `../../page-brief-assembler/SKILL.md`
- `../../fact-check/SKILL.md`
- `../../copywriting/SKILL.md`

## Contract Rule

Use the repo-local skills above when their job matches the task. Do not replace them with free-form prompt logic inside the orchestrator.

## Local Supporting Playbooks

These replace the earlier dependency on globally installed page, SEO, and copy skills.

- `../../page-brief-page-playbook/SKILL.md`
  Use for page-type-specific structure, site-role, and internal-link expectations.
- `../../page-brief-seo-playbook/SKILL.md`
  Use for search intent, exact metadata, structured-data decisions, supporting-content modules, on-page structure, and cannibalization rules.
- `../../page-brief-copy-playbook/SKILL.md`
  Use for message hierarchy, hero logic, proof handling, objections, and CTA rules.
- `../../copywriting/SKILL.md`
  Use after the strategy is defined to lock exact H1, hero subheading, title tag, meta description, section headings, supporting-content modules, and CTA labels inside the brief. Do not use it to replace the brief or write the full page during this workflow.

## Local Context Rules

- Resolve the active Ink profile first, then use author-scoped One Horizon context docs from the selected workspace for live runtime context. Do not use tracked repo files for live context.
- If author context docs are missing and the user wants them created, hand off to `../../one-horizon-context-setup/SKILL.md`.

## Tool Guidance

- Use the best available browsing, page-fetching, and search tools in the current environment.
- In Ink's local MCP setup, read `../../linkedin-social-writer/references/mcp-tools.md` before using the local research tools.
- For updates to public website pages, use web search and page-fetch tools to resolve and inspect the live page URL.
- Do not search repo files to locate a public page unless the user explicitly provides a local file path or asks for repo-level implementation analysis.
- Prefer:
  - target site pages
  - official product and help pages
  - live competitor pages
  - first-party documentation
- Use search operators such as `site:` when site search is weak.

## What Not to Build

Keep these responsibilities out of new standalone skills:

- claim validation, because `../../fact-check/SKILL.md` already covers it
- a dedicated brief-direction ideation skill, because direction ideation is tightly coupled to positioning and is already owned by `../../page-positioning-strategist/SKILL.md`
- page-type-specific brief generators for every page type, because the local playbooks already cover the needed guidance without exploding the skill count
- a dedicated QA skill, because QA is a final orchestration gate rather than a reusable independent workflow
- scripts, unless a repeated deterministic operation appears later and cannot be handled reliably through instructions alone
