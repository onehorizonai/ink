---
name: page-brief-assembler
description: Assemble a concise locked website page brief from collected planning inputs, turning intake, research, SEO, positioning, conversion, copy guidance, and claims validation into exact instructions another LLM agent or human can execute without interpreting options. Use when Codex has the research inputs and needs to produce the final implementation brief for a new or updated web page. Do not use it to fill research gaps by guesswork, write the full page itself, or produce code.
---

# Page Brief Assembler

## Overview

Assemble the final implementation brief as a locked execution spec.

This skill formats the final artifact. It does not replace intake, research, or claims validation.
The output must tell the next agent exactly what to change, what text atoms to use, what links and proof to include, and what to omit.

## Quick Start

1. Read `references/final-brief-template.md`.
2. Confirm that upstream inputs exist for intake, site patterns, competitor research, SEO, positioning, conversion, copy guidance, and claims validation.
3. Read `../page-brief-builder/references/clarification-loop.md`.
4. If any upstream input is missing, stop and surface the next verification questions instead of inventing content.
5. Build the final brief in the exact section order from the template.

## Rules

- Use the exact section order and headings from `references/final-brief-template.md`.
- Return the final brief only unless the caller explicitly asks for supplementary notes.
- Produce a locked execution spec, not a research digest.
- Keep the brief concise.
- Use exact decisions, not directions.
- Use tables only when they shorten the brief.
- Do not include a final checklist or done checklist.
- Do not collapse the output into short bullet summaries.
- Do not include a source ledger, workflow note, research recap, rationale section, or explanation of the process.
- Do not create a generic section named `FAQ And Related Pages`.
- Do not write advisory title, headline, or CTA language.
- Write exact fields such as `H1: "..."`, `Title tag: "..."`, `Primary CTA: "..."`.
- Do not hide uncertainty by writing confident filler.
- Do not infer missing strategic decisions from adjacent sections.
- Do not turn unanswered clarification questions into assumptions.
- If several adjacent blockers exist, ask a short verification pack instead of stopping after only one question.
- Do not use `TBD`, `TODO`, `TBA`, `TBC`, `placeholder`, `etc.`, or generic filler anywhere in the brief.
- Do not write vague recommendations such as `add proof`, `tighten headline`, or `improve CTA` without saying exactly what needs to be added or changed.
- Do not use weak requirement language such as `should`, `consider`, `could`, `maybe`, or `nice to have` for required page work.
- If a section cannot be made specific without user input, stop and surface the missing question instead of drafting around it.
- If claim validation was not completed, omit unvalidated claims or put exact forbidden wording under `Claims to avoid`.
- Keep the implementation notes strategic. Do not output HTML, CSS, JS, React, component code, or finished build instructions.
- The developer or implementation-agent notes may describe structural intent, assets needed, constraints, and dependencies, but must explicitly state that the brief does not include code.
- Keep the brief clear and implementable. Remove anything that does not directly instruct implementation.

## Preflight

Before assembling:

- confirm that intake exists
- confirm that site-pattern guidance exists or is explicitly blocked
- confirm that competitor research exists or is explicitly blocked
- confirm that a chosen direction exists or that the user explicitly selected one
- confirm that SEO, positioning, and conversion inputs exist
- confirm that claim validation status is known
- confirm that no blocking verification questions remain unanswered
- confirm that no user-answerable strategy input remains soft, implied, or unresolved behind an assumption
- confirm that every section can be stated concretely without placeholder language
- confirm that H1, title tag, meta description, CTA labels, section headings, supporting-content modules, links, and claims are locked as exact instructions
- confirm that the section-by-section plan includes exact placement, section heading, required content, required proof or link, CTA, and `do not include` guidance

If any of these are missing, stop and surface the gap instead of drafting around it.

## Output Shape

Return the final brief markdown only. Do not prepend commentary or summaries.

If the workflow is blocked on missing upstream inputs, return only `Open gaps`, `Next verification questions`, and `Why these are next`.

## Files

- Read `references/final-brief-template.md` for the required structure and section-level requirements.
