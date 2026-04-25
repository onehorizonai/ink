---
name: website-brief-intake
description: Capture and normalize the required inputs for a website page brief, identify missing context, and separate confirmed facts from assumptions before strategy work starts. Use when Codex needs to gather the minimum inputs for a new or updated product page, landing page, help page, feature page, solution page, comparison page, or evergreen page brief. Do not use it for site analysis, competitor research, SEO planning, or final brief assembly.
---

# Website Brief Intake

## Overview

Own the intake stage only.

This skill gathers and verifies the required inputs for a page brief, normalizes what the user asked for, and exposes what is still missing.
Run a guided clarification loop instead of treating the first user prompt as enough context.
When critical strategy inputs are missing, ask the next small pack of related verification questions, then wait for the answer before asking the next pack.

## Read First

- `../page-brief-builder/references/clarification-loop.md`
- only the relevant author-scoped One Horizon context docs. Resolve the author with One Horizon tools and use `../one-horizon-context-setup/references/context-doc-templates.md` for the naming contract.

## Required Inputs

Capture or explicitly mark open:

- topic, subject, or area of interest
- target website or web property
- additional business-specific context
- page status: new page or update to an existing page
- page type
- audience
- page goal
- primary CTA
- secondary CTA
- funnel stage or audience awareness stage
- region or language when relevant
- hard constraints, if any

If the request is an update, also capture:

- current public page URL
- why the page needs to change
- what is not working well on the current page
- any known constraints on what must stay
- what success looks like after the update
- explicit local file path only if the user wants repo-file analysis instead of live-page analysis

## Rules

- Always confirm the target website or web property.
- Always ask for additional business-specific context even when author-scoped One Horizon context docs already provide partial context.
- Never continue straight to final briefing from a generic topic alone.
- Ask 2-4 tightly related verification questions when the same decision is blocked by several missing inputs.
- Ask one question only when one blocking uncertainty remains.
- Ask the highest-priority unresolved question pack first, then stop for the answer.
- Do not return a long questionnaire or a final paragraph full of loose follow-ups.
- Do not stop after the first update-diagnosis question if the rest of that diagnosis pack is still unanswered.
- Separate confirmed inputs from assumptions.
- Do not use assumptions for missing user-answerable strategy inputs.
- If the page type is unclear, offer likely options but ask the user to confirm the choice.
- If the CTA is unknown, state that it is unresolved rather than inventing one.
- Do not treat tracked repo files outside `.local/` as live runtime context.
- If a One Horizon tool call is missing or fails, read `../one-horizon-context-setup/references/mcp-readiness.md` for recovery. Do not search tracked repo files as a substitute for live context.
- Do not analyze same-site patterns, competitors, SEO, or messaging strategy here.
- For updates to public pages, capture the live public URL. If the user names a page but does not give a URL, resolve it on the target site with web search. Do not search repo files unless the user explicitly provides a local file path or asks for repo-file analysis.
- Do not produce code, wireframes, or final page copy.

## Question Packs

Ask unresolved questions in this order. Ask only the first unresolved pack, then wait for the answer.

1. Page identification pack
   - target website or web property
   - page status: new or update
   - live public page URL when this is an update
   - page type when it is already guessable enough to verify now
2. Update diagnosis pack when this is an update
   - why the page needs to change
   - what is not working well on the current page
   - what must stay
   - what success looks like after the update
3. Audience and conversion pack
   - target audience
   - page goal
   - primary CTA
   - secondary CTA or intentional absence
4. Business-specific strategy pack
   - offer or product context
   - differentiators
   - proof already available
   - hard constraints
5. Supporting detail pack
   - funnel stage or awareness stage
   - region or language
   - any remaining delivery constraints

If the user answers several questions at once, update the confirmed inputs and then ask only the next unresolved pack.

## Stop Conditions

- If the target website is unknown, stop and ask for it.
- If this is an update to a public page and the live URL cannot be determined, stop and ask for the page URL.
- If the page type is unclear, stop and ask for confirmation.
- If audience, page goal, or primary CTA are missing, ask the audience and conversion pack instead of guessing.
- If this is an update and the update diagnosis is incomplete, ask the missing update diagnosis questions together and stop.
- If any blocking strategic input is unresolved, ask the next verification question pack and stop before handing off.

## Output Shape

If intake is complete, return these exact headings:

- `Normalized request`
- `Confirmed inputs`
- `Assumptions`
- `Risks`

If intake is blocked, do not return the full output shape above.
Return only:

- `Normalized request`
- `Confirmed inputs`
- `Open gaps`
- `Next verification questions`
- `Why these are next`

Under `Next verification questions`, ask 1-4 direct questions in plain language and stop.
When intake is blocked, do not include `Assumptions` or `Risks`.
