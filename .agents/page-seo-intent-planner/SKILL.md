---
name: page-seo-intent-planner
description: Plan the search-intent and SEO contract for a website page brief by defining primary intent, secondary intents, keyword or topic cluster, exact title tag, exact meta description, internal links, structured-data decisions, supporting-content modules, and overlap risk. Use when Codex needs search-aware guidance for a new or updated product page, landing page, help page, comparison page, solution page, or evergreen page. Do not use it for sitewide SEO strategy, standalone keyword research, or final page copy.
---

# Page SEO Intent Planner

## Overview

Make the brief search-aware without turning it into an SEO-only artifact.

This skill defines intent, topic focus, and exact on-page search requirements that support the page strategy.

## Workflow

1. Read `../page-brief-seo-playbook/SKILL.md` and `../page-brief-seo-playbook/references/seo-rules.md`.
2. Confirm whether the page is expected to attract organic traffic.
3. If organic traffic is not a goal, say so clearly and keep SEO guidance light.
4. Define the primary search intent.
5. Define secondary intents when they materially affect the page.
6. Identify the primary keyword or topic cluster.
7. Identify secondary terms, entities, and supporting concepts.
8. Check for overlap or cannibalization risk against existing pages.
9. Recommend:
   - exact title tag
   - exact meta description
   - exact URL slug
   - exact internal links
   - exact structured-data requirement only when the page naturally supports it
   - exact supporting-content module when the page needs one
10. State the required page structure, metadata, internal links, structured-data requirement, and supporting-content module.

## Rules

- Read `../page-brief-builder/references/clarification-loop.md` before deciding the SEO inputs are locked enough to finalize.
- Use `../page-brief-page-playbook/SKILL.md` when the page type changes the SEO pattern materially, especially for help, comparison, integration, and evergreen resource pages.
- Strategy comes before keyword mechanics.
- Do not invent search-volume numbers or false keyword data.
- If hard SEO data is unavailable, provide the exact strategic keyword and intent contract. Label it as unmeasured, not evidence.
- Keep the SEO requirements concrete. Name the intent, topic cluster, exact metadata, and internal-link targets.
- Do not output `direction`, `option`, `could`, or `should` language.
- Translate SEO decisions into implementation requirements. Do not return keyword notes without saying exactly what the page must do.
- Do not force FAQ sections. Use FAQ only when existing page patterns, search intent, or explicit user input justifies Q&A.
- If a different support module is better, specify it exactly, such as docs CTA, comparison table, setup steps, related integration links, proof block, or `none`.
- Use existing site pages to check overlap risk before recommending a new angle.
- If the page is not meant to rank organically, state that explicitly instead of forcing an SEO narrative.
- If the organic role, slug constraints, internal-link targets, or support module are still ambiguous, ask 1-3 targeted verification questions instead of inventing exact SEO fields.
- Do not output code or schema markup.

## Stop Conditions

- If page type, page goal, or target website are unclear, stop and use `../website-brief-intake/SKILL.md` to ask targeted verification questions.
- If the chosen direction is unresolved, stop and use `../page-positioning-strategist/SKILL.md` before continuing.
- If same-site overlap cannot be checked because the site is inaccessible, record the gap and keep the cannibalization notes provisional.
- If exact SEO fields still depend on unresolved user-answerable inputs, stop and ask the next SEO verification questions before continuing.

## Output Shape

Return these exact headings:

- `Organic role`
- `Primary intent`
- `Secondary intents`
- `Keyword or topic cluster`
- `Supporting terms and entities`
- `Exact metadata`
- `Required internal links`
- `Structured-data requirement`
- `Supporting-content module`
- `Overlap or cannibalization notes`
- `Implementation requirements`
- `Missing data and low-confidence assumptions`

If the workflow is blocked on missing SEO inputs, return only `Known SEO inputs`, `Open SEO gaps`, `Next verification questions`, and `Why these are next`.
