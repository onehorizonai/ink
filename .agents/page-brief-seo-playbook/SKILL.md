---
name: page-brief-seo-playbook
description: Apply repo-local SEO, search-intent, internal-linking, structured-data, supporting-content, and on-page structure rules to website page briefs. Use when Codex needs search-aware guidance for a new or updated landing page, product page, feature page, help page, comparison page, solution page, integration page, or evergreen resource page brief. Do not use it as a full sitewide SEO strategy or standalone keyword-research workflow.
---

# Page Brief SEO Playbook

## Overview

Provide local SEO rules for page briefs without turning the work into a generic SEO exercise.

Use this skill to support the SEO step in the page-brief workflow.

## Quick Start

1. Read `references/seo-rules.md`.
2. Decide whether organic search matters for this page.
3. Map one primary intent before adding secondary intents.
4. Use the rules to lock exact SEO fields for the brief, not to force a search-first page that does the wrong job.

## Rules

- Keep the page's business goal and user need ahead of keyword mechanics.
- Use one primary intent per page unless the user explicitly accepts a mixed-intent tradeoff.
- Check existing pages before recommending a new target keyword or topic.
- Treat keyword placement, headings, support blocks, lists, and tables as support tools, not ends in themselves.
- Never invent search-volume data, ranking difficulty, or SERP features.
- Use real user phrasing for help, support, and objection-handling sections when possible.
- Provide exact title tag, meta description, slug, internal links, and supporting-content module when enough context exists.
- Do not force FAQ sections. Use FAQ only when existing page patterns, search intent, or explicit user input justifies Q&A.
- Valid supporting-content modules include FAQ, docs CTA, comparison table, setup steps, related integration links, proof block, pricing note, security note, or `none`.
- Do not output metadata `direction`, `options`, `could`, or `should` language for final brief inputs.
- Do not output schema markup or code.

## Decision Rule

- If the page is not meant to rank, say so and keep SEO guidance minimal.
- If the page has one obvious intent, protect that intent and avoid stacking extra intents onto it.
- If overlap risk is credible, recommend updating or differentiating before recommending a new page.

## Output Shape

Return these exact headings:

- `Primary and secondary intent`
- `Keyword or topic cluster`
- `Exact metadata and slug`
- `Internal-link logic`
- `Supporting-content and structured-data requirement`
- `Overlap or cannibalization risks`
- `Page-specific SEO cautions`

## Files

- Read `references/seo-rules.md` for the local SEO rules.
