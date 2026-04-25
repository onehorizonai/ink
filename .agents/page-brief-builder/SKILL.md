---
name: page-brief-builder
description: Create or update strategic implementation briefs for website pages by coordinating intake, site-pattern analysis, competitor research, brief-direction ideation, SEO intent planning, positioning, conversion planning, copy guidance, claim validation, and final brief assembly. Use when Codex needs a website page brief, web page brief, landing page brief, product page brief, comparison page brief, help page update brief, "alternative to X" page brief, or requests such as "create a brief for a new product page", "write a landing page brief", "update our alternative to Linear page", "update the brief for this help page", or "plan a web page brief for this site". Do not use it to write the full page, implementation tickets, HTML, CSS, JS, React, or components.
---

# Page Brief Builder

## Overview

Own the full page-brief workflow from intake through QA.

Use this skill as the entry point for strategic website page briefs.
It must not output production code, HTML, CSS, JS, React, component code, or final implementation.

## Quick Start

1. Read `references/workflow.md`.
2. Read `references/clarification-loop.md`.
3. Read `references/reuse-map.md`.
4. Resolve the author and load only the relevant author-scoped One Horizon context docs. Use `../one-horizon-context-setup/references/context-doc-templates.md` for the naming contract.
5. If the relevant author-scoped One Horizon context docs are missing, ask for business-specific context directly. Use `../one-horizon-context-setup/SKILL.md` only if the user wants missing author context docs created.
7. If intake is incomplete, stop and resolve the intake gaps before analysis.
8. Run every mandatory step in `references/workflow.md`.
9. Use `../page-brief-assembler/SKILL.md` only after every upstream step is complete or explicitly blocked.
10. Run the final QA gate before presenting the brief.

## Working Agreement

- Treat `references/workflow.md` as the authoritative sequence. Every step is mandatory.
- Treat `references/clarification-loop.md` as the shared questioning contract for every page-brief stage.
- If a step is impossible, do not skip it silently. State what could not be done, why, what assumption was used instead, and what follow-up input would resolve it.
- Always confirm the target website or web property.
- Always ask for additional business-specific context even when author-scoped One Horizon context docs already provide partial context.
- If a One Horizon tool call is missing or fails, follow `../one-horizon-context-setup/references/mcp-readiness.md`. Do not search tracked repo files as a substitute for live context.
- Always distinguish confirmed inputs, assumptions, strategic recommendations, and validated facts.
- Run a guided clarification loop across the workflow, not just at the intake step.
- Do not turn missing user-answerable strategy inputs into assumptions.
- Ask 2-4 tightly related verification questions per turn when several inputs block the same decision. Ask one question only when one blocking uncertainty remains.
- For updates to existing pages, do not stop after asking why the page needs to change. Also verify what is not working, what must stay, and what success looks like before analysis begins.
- Before moving into a later stage with soft inputs, bounce back into clarification instead of drafting around the ambiguity.
- Before final assembly, verify any still-soft implementation decisions instead of inferring them.
- Use assumptions only for minor research gaps or external unknowns after the user-answerable strategy inputs are resolved.
- If a final recommendation would be vague, generic, or placeholder-like, stop and ask the user instead of softening it into the brief.
- For updates to public website pages, inspect the live public URL on the target site. Do not search repo files to find the page unless the user explicitly provides a local file path or asks for repo-level implementation analysis.
- Inspect relevant pages on the target site when the site is reachable.
- Use the repo-local sub-skills below. Do not bypass them with ad hoc prompt logic when a matching local skill already exists.
- Use browsing or local MCP research tools for external page analysis. In Ink's local MCP setup, read `../linkedin-social-writer/references/mcp-tools.md` before using those tools.
- After competitor research, brainstorm at most 3 materially different page directions.
- If the direction is still unresolved after ranking, stop and ask the user to choose before continuing into SEO, messaging, conversion, or brief assembly.
- Never invent product details, proof, metrics, customer quotes, or competitor specifics.
- Never let SEO distort the core page goal.
- Never present the result as code or finished production copy. This skill produces an execution-ready brief only.
- The final brief must be actionable by another LLM agent or human without rereading the research notes.
- The final brief must state required page changes, exact copy atoms, required links, and CTA labels section by section.
- Keep the final brief in the exact structure required by `../page-brief-assembler/references/final-brief-template.md`.

## Routing Contract

Use this routing split exactly:

- missing or unclear inputs -> `../website-brief-intake/SKILL.md`
- same-site structure, tone, CTA, and keep-vs-improve analysis -> `../website-pattern-analyzer/SKILL.md`
- competitor or comparable-page research -> `../competitor-page-research/SKILL.md`
- page-family defaults when live evidence is thin -> `../page-brief-page-playbook/SKILL.md`
- brainstorm up to 3 viable page directions and choose one -> `../page-positioning-strategist/SKILL.md`
- search intent and locked SEO fields -> `../page-seo-intent-planner/SKILL.md` plus `../page-brief-seo-playbook/SKILL.md`
- messaging, value proposition, proof, and claims ledger -> `../page-positioning-strategist/SKILL.md` plus `../page-brief-copy-playbook/SKILL.md`
- conversion logic and CTA behavior -> `../conversion-cta-planner/SKILL.md` plus `../page-brief-copy-playbook/SKILL.md`
- exact H1, hero subheading, metadata, section headings, supporting-content modules, and CTA labels for the brief -> `../copywriting/SKILL.md`
- claim validation -> `../fact-check/SKILL.md`
- final brief formatting -> `../page-brief-assembler/SKILL.md`

Do not merge these jobs into one free-form response when the matching sub-skill exists.

## Composition

Use the local sub-skills for the core workflow:

- `../website-brief-intake/SKILL.md`
- `../website-pattern-analyzer/SKILL.md`
- `../competitor-page-research/SKILL.md`
- `../page-brief-page-playbook/SKILL.md`
- `../page-positioning-strategist/SKILL.md` to brainstorm up to 3 page directions and choose one before later planning
- `../page-seo-intent-planner/SKILL.md`
- `../page-brief-seo-playbook/SKILL.md`
- `../page-positioning-strategist/SKILL.md`
- `../conversion-cta-planner/SKILL.md`
- `../page-brief-copy-playbook/SKILL.md`
- `../copywriting/SKILL.md` only to lock brief-level H1, hero subheading, metadata, section headings, supporting-content modules, and CTA labels after strategy is clear
- `../page-brief-assembler/SKILL.md`
- `../fact-check/SKILL.md` for claim validation

## Output Shape

Unless the user asks differently, return:

- the final page brief only

Put validation requirements inside the brief itself.
Do not append a separate workflow note unless the user explicitly asks for it.
Do not append a final checklist or done checklist.

If the workflow is blocked on intake gaps or later strategy-verification gaps, do not draft the brief. Ask the next small set of related verification questions in plain language and stop.
Ask 1-4 questions per verification turn. Ask one question only when one blocker remains.
If the workflow stops at the direction-selection gate, do not fake the rest of the brief. Return the shortlisted directions, the recommendation, and the decision still needed instead.
Keep the final brief concise and implementable. Use exact instructions, not advisory language.
Do not reduce the brief to a collection of short research bullets.
Do not include a source ledger, workflow recap, research recap, or rationale section.
Do not write advisory title, headline, or CTA language in the final brief.
Lock exact H1, title tag, meta description, CTA labels, section headings, supporting-content modules, links, and claims.
Do not output `TBD`, `TODO`, `TBA`, `TBC`, `placeholder`, `etc.`, or vague filler in the final brief.

## Files

- Read `references/workflow.md` for the mandatory sequence and failure handling.
- Read `references/clarification-loop.md` for the shared questioning contract.
- Read `references/reuse-map.md` for sub-skill routing and tool guidance.
- If a One Horizon tool call fails, read `../one-horizon-context-setup/references/mcp-readiness.md` for recovery.
- Resolve the author with One Horizon MCP tools, then load relevant author-scoped context from One Horizon: `Profile`, `Current Work`, and `Market Context`.
- Read `../linkedin-social-writer/references/mcp-tools.md` before using Ink's local research tools.
- Use `../page-brief-assembler/references/final-brief-template.md` as the output contract.
