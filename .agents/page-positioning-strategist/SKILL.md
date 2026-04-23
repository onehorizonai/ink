---
name: page-positioning-strategist
description: Define the messaging and positioning layer for a website page brief by brainstorming up to 3 viable page directions, choosing one direction or asking the user to choose, and then clarifying audience pains and motivations, value proposition, differentiators, proof points, objections, trust signals, tone guidance, and claims that require substantiation. Use when Codex needs strategic messaging guidance for a new or updated web page. Do not use it to draft the finished page or to replace claim validation.
---

# Page Positioning Strategist

## Overview

Turn business context into page-specific messaging strategy.

This skill defines what the page should say and how it should say it, without turning the output into finished copy.
It also owns the step where the workflow brainstorms up to 3 possible directions and locks one direction before deeper planning continues.
Use it first to narrow the direction, then again to deepen messaging for the chosen direction.

## Workflow

1. Confirm the audience, page goal, and offer.
2. Review the subject, same-site patterns, competitor findings, and page type.
3. Brainstorm at most 3 viable page directions.
4. For each direction, capture:
   - a short label
   - the core angle
   - why it could work
   - what proof it would need
   - the main risk
5. Rank the directions and recommend one.
6. If one direction is clearly strongest, choose it and explain why.
7. If 2 or more directions are still materially viable, ask the user to choose before continuing.
8. Only after a direction is chosen, extract or request the core value proposition.
9. Identify pains, motivations, and likely alternatives.
10. Identify differentiators that matter for this audience, page type, and chosen direction.
11. Identify proof points and trust signals the page should lean on.
12. Identify objections the page must answer.
13. Define tone and voice guidance.
14. Identify words, themes, or claim styles to use and avoid.
15. Convert the positioning into a page strategy contract:
   - main promise
   - narrative arc
   - required tradeoffs or honest-fit guidance
   - messages that must appear before the CTA
16. Build a claims ledger:
   - already supported
   - proposed but unverified
   - needs source support

## Rules

- Read `../page-brief-builder/references/clarification-loop.md` before deciding that the context is complete enough to proceed.
- Read `../page-brief-copy-playbook/SKILL.md` and `../page-brief-copy-playbook/references/copy-rules.md` before finalizing guidance.
- Keep the direction options materially distinct. Vary the angle, promise, emphasis, or proof strategy rather than restating the same idea three ways.
- Cap direction ideation at 3 options even when more are possible.
- Keep the output strategic. Do not write the full page.
- State messaging decisions concretely. Do not return abstract themes that the next step would have to interpret.
- State which messages must appear in the hero, comparison body, proof sections, and FAQ when those sections exist.
- Lock the chosen direction as a decision before final brief assembly. Do not carry multiple positioning options into the final brief.
- Do not use `could`, `should`, or `consider` language after the chosen direction is locked.
- If the chosen direction is clear but the promise, differentiator, proof base, or objection map is still soft, ask 1-3 targeted verification questions instead of drafting around the gap.
- Never invent proof, metrics, customer outcomes, or testimonials.
- Distinguish validated facts from proposed messaging.
- Flag every claim that appears to need evidence or later fact-checking.
- Keep the language audience-aware rather than company-jargon-heavy.
- Do not output code.

## Stop Conditions

- If the audience, offer, or page goal are still unclear, stop and use `../website-brief-intake/SKILL.md` to ask targeted verification questions.
- If the core value proposition is still missing after available evidence is reviewed, stop and use `../website-brief-intake/SKILL.md` to ask targeted verification questions.
- If 2 or more directions are still materially viable after ranking, stop and ask the user to choose before continuing.
- If the user still needs to choose a direction, do not continue into audience, value proposition, differentiators, objections, or claims detail.
- If the chosen direction is locked but exact positioning still depends on unresolved differentiator, proof, or objection details, stop and ask the next positioning verification questions before continuing.

## Output Shape

Return these exact headings:

- `Direction options`
- `Recommended direction`
- `Decision needed`
- `Chosen direction`
- `Page strategy contract`
- `Audience summary`
- `Pains and motivations`
- `Value proposition`
- `Differentiators`
- `Objections`
- `Trust signals and proof needs`
- `Tone and voice guidance`
- `Terminology to use and avoid`
- `Claims ledger`

If the workflow is blocked on direction selection, return only `Direction options`, `Recommended direction`, `Decision needed`, and `Chosen direction`, with `Chosen direction` marked unresolved.
If the workflow is blocked on missing positioning inputs after the direction is chosen, return only `Chosen direction`, `Open strategy gaps`, `Next verification questions`, and `Why these are next`.
