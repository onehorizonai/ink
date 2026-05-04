---
name: copywriting
description: Write, rewrite, or improve final marketing copy for website pages such as homepages, landing pages, pricing pages, feature pages, about pages, product pages, and solution pages. Use when Codex needs finished page copy, section copy, headline options, subheadline options, or CTA copy for a website page, including requests like "write copy for this landing page", "rewrite this feature page", "improve this page copy", "headline help", or "CTA copy". Do not use it for strategic page briefs or page-strategy work; use page-brief-builder for that.
---

# Copywriting

## Overview

Write final website-page copy that is clear, specific, and conversion-focused.

Use this skill after the page strategy is clear enough to draft real copy. If the user still needs the page direction, positioning, or brief, route to `../page-brief-builder/SKILL.md` first.

## Quick Start

1. Read `../page-brief-copy-playbook/references/copy-rules.md` for the shared local copy and CTA rules.
2. Read `../page-brief-builder/references/clarification-loop.md` when the strategy or locked copy atoms are still unresolved.
3. Read `references/page-copy-patterns.md` when you need section mix, page flow, or page-type guidance.
4. Read `references/headlines-and-ctas.md` when you need headline, subheadline, or CTA options.
5. If a page brief already exists, treat it as the source of truth.
6. If no brief exists, gather the minimum context below before drafting.
7. If the page must match existing site patterns, inspect the current site pages or use `../website-pattern-analyzer/SKILL.md`.
8. Draft the copy, then run the quality check before finalizing.

When called from `../page-brief-builder/SKILL.md`, do not draft the full page. Return locked copy atoms for the brief: exact H1, hero subheading, title tag, meta description, CTA labels, section headings, and supporting-content modules. Do not return options unless the user explicitly needs to choose before the brief can continue. If those atoms are still soft, ask 1-3 targeted verification questions instead of inventing them.

## Gather Before Writing

Confirm or request:

- page type
- page goal
- primary CTA
- secondary CTA, if any
- audience
- problem the audience is trying to solve
- what they have already tried or currently use
- likely objections or hesitations
- offer or product being sold
- differentiators
- proof points already available
- traffic source or awareness stage when known
- messaging or promise the visitor has already seen before this page
- hard constraints such as legal review, claim limits, word count, or required sections

If website context, page goal, audience, or offer are still thin enough that the copy would require guesswork, stop and route to `../page-brief-builder/SKILL.md` instead of inventing strategy.
If no brief exists and 4 or more core inputs are still missing, stop and route to `../page-brief-builder/SKILL.md`.
If the copy is mostly locked but 1-3 critical facts still determine the headline, CTA, or proof language, ask those verification questions before drafting.

## Workflow

1. Lock the one-page goal and the one dominant CTA.
2. Define the main promise the page needs to land.
3. Choose the section order using `references/page-copy-patterns.md`.
4. Draft the hero first: headline, subheadline, primary CTA, and supporting proof cue.
5. Draft the middle sections in a persuasive order: problem, solution, benefits, proof, objections, and any how-it-works or comparison sections.
6. Draft the close so it restates the value clearly and moves the reader toward the primary action.
7. Use `references/headlines-and-ctas.md` to generate 2-3 headline and CTA options only when the user asks for options or when the hero is still unresolved.
8. Add meta title and meta description only when the user asks for them or when organic discovery is part of the page goal.
9. Run the quality check.

## Rules

- Reuse an existing page brief whenever one exists.
- Reuse the local copy and CTA rules in `../page-brief-copy-playbook/references/copy-rules.md` instead of rewriting them from scratch.
- Favor clarity over cleverness.
- Connect features to customer outcomes.
- Use customer language instead of internal jargon.
- Keep one dominant idea per section.
- Keep one primary CTA unless the page genuinely serves two different readiness levels.
- Match CTA intensity to page type, traffic source, and funnel stage.
- Keep the copy specific where proof exists and conservative where proof does not.
- Never invent testimonials, metrics, customer outcomes, competitor claims, or product details.
- Flag any claim that still needs proof or fact-checking.
- Ask targeted verification questions when a missing promise, proof point, or CTA detail would materially change the copy.
- Do not backfill missing strategy with copy formulas.
- Do not output code, UI components, or design comps.

## Routing

- If the user needs strategy, positioning, or a structured brief, use `../page-brief-builder/SKILL.md`.
- If the user needs strategic copy guidance inside a brief rather than final copy, use `../page-brief-copy-playbook/SKILL.md`.
- If `../page-brief-builder/SKILL.md` calls this skill for brief assembly, provide exact copy atoms only. Do not provide alternatives, directions, or final full-page copy.
- If `../page-brief-builder/SKILL.md` calls this skill and the exact atoms are still unresolved, ask the next copy verification questions instead of drafting around the gap.
- If same-site structure, tone, or section rhythm needs analysis first, use `../website-pattern-analyzer/SKILL.md`.
- If claims, stats, dates, names, or product facts need validation, use `../fact-check/SKILL.md`.

## Quality Check

Before finalizing, check:

- the headline says what the page is and why it matters
- the subheadline adds specificity instead of repeating the headline
- the page reads like an argument, not a random feature list
- benefits are concrete and outcome-linked
- proof supports the strongest claims
- objections are answered directly
- CTA text says what the visitor gets or does next
- filler, buzzwords, passive voice, and vague superlatives are removed
- no fabricated specifics slipped in

## Output Shape

Unless the user asks for only one piece, return these exact headings:

- `Context used`
- `Page copy`
- `Headline and CTA alternatives`
- `Notes and gaps`

Under `Page copy`, label the parts clearly. Use the labels that fit the request, such as:

- `Headline`
- `Subheadline`
- `Primary CTA`
- `[Section name]`
- `Secondary CTA`
- `Meta title`
- `Meta description`

Use `Notes and gaps` to flag missing proof, weak assumptions, or anything the user should confirm before publishing.

## Files

- Read `../page-brief-copy-playbook/references/copy-rules.md` for the shared local copy rules.
- Read `references/page-copy-patterns.md` for section mix, page flow, and page-type guidance.
- Read `references/headlines-and-ctas.md` for formulas, CTA guidance, and option generation.
