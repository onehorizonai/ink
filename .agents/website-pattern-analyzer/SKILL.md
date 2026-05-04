---
name: website-pattern-analyzer
description: Inspect the target website and comparable same-site pages to extract recurring structure, voice, CTA patterns, proof patterns, and keep-versus-improve guidance for a new or updated page brief. Use when Codex needs to align a new page with an existing site system or audit an existing page before rewriting its brief. Do not use it for competitor research or final brief assembly.
---

# Website Pattern Analyzer

## Overview

Analyze how the target site already communicates and structures similar pages.

This skill is about site alignment, not competitor research and not final brief assembly.

## Workflow

1. Confirm the target page and the page type.
2. If the request is an update to a public page, locate and review the live public URL first.
3. If the user explicitly provides a local file path or asks for repo-level implementation analysis, inspect that local file after the live page, not instead of it.
4. Find 2-5 relevant same-site comparison pages when they exist.
5. Capture repeated patterns in:
   - section order
   - headline and subhead rhythm
   - proof style
   - CTA style and placement
   - internal-link style
   - tone, pacing, and level of specificity
6. Identify what should be preserved because it reflects the site's current system.
7. Identify what should improve because it weakens clarity, differentiation, trust, or conversion.
8. If the request is an update, classify current-page elements as:
   - keep
   - remove
   - rewrite
   - add
   - reposition
9. For each update classification, state the exact page element and the required treatment.

## Page Selection Order

Review pages in this order:

1. the current live public page URL, if this is an update
2. same-purpose pages on the same site
3. same-funnel pages on the same site
4. nearest structural analogs on the same site
5. explicit local page files only when the user provides a local file path or asks for repo-level implementation analysis
6. page-family defaults from `../page-brief-page-playbook/SKILL.md` only when live evidence is thin

## Rules

- Analyze relevant pages on the same site whenever possible.
- Use `../page-brief-page-playbook/SKILL.md` when same-site evidence is thin and a page-type baseline is still needed.
- Use browsing or page-fetch tools instead of guessing. In Ink's local MCP setup, read `../linkedin-social-writer/references/mcp-tools.md` first.
- For public website updates, use web search or direct page fetch to resolve and inspect the live page URL.
- Do not search local repo files to find a public page. Use local files only when the user explicitly provides a file path or asks for repo-level implementation analysis.
- Prefer same-purpose pages first, then same-funnel pages, then nearest structural analogs.
- If live same-site evidence is unavailable, use `../page-brief-page-playbook/SKILL.md` only as provisional fallback guidance and label it provisional.
- Do not copy a page pattern blindly just because it already exists.
- Capture conventions and opportunities, not pixel-level design prescriptions.
- Translate observations into concrete brief inputs. Name which existing sections to keep, rewrite, add, remove, or reposition.
- Do not stop at describing patterns. State the implementation implication for the brief.
- If the site is inaccessible, say so explicitly and note the assumption being used instead.
- Do not turn this into competitor research.
- Do not output code or final page copy.

## Output Shape

Return these exact headings:

- `Pages reviewed`
- `Patterns to preserve`
- `Patterns to improve`
- `Structural and tone observations`
- `CTA and proof observations`
- `Current-page change map`
- `Implementation implications`
- `Gaps and assumptions`
