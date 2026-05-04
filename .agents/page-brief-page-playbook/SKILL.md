---
name: page-brief-page-playbook
description: Apply repo-local page-type, site-role, and structural rules to website page briefs. Use when Codex needs page-specific guidance for product pages, feature pages, landing pages, solution pages, comparison pages, help or FAQ pages, integration pages, or evergreen resource pages while preparing a new or updated website page brief. Do not use it as a substitute for live same-site analysis when relevant site pages are available.
---

# Page Brief Page Playbook

## Overview

Provide local page-type rules that support the briefing workflow.

Use this skill when same-site examples and competitor research need a page-type baseline, not as a replacement for live site analysis.

## Quick Start

1. Read `references/page-types.md`.
2. Confirm the page type and whether the page is new or an update.
3. Choose the nearest page family.
4. Apply only the rules that fit the business, audience, and site context.

## Rules

- Use same-site evidence first. Use generic defaults only to fill structural gaps.
- Use the playbook to fill structural gaps, not to override strong evidence from the target site.
- Keep one clear page job. If the page tries to educate, compare, capture leads, and close a sale all at once, narrow the scope.
- Keep internal-link expectations and CTA behavior aligned with the page's role in the site.
- Distinguish page families that look similar but serve different jobs, especially:
  - feature vs solution
  - landing vs evergreen resource
  - help center page vs in-page FAQ section
  - integrations index vs single integration page
- Do not output code, wireframes, or final copy.

## Decision Rule

- If the page job is clear, choose the matching page family.
- If the page job is mixed, choose the dominant job and record the conflict as a risk.
- If the site already has a strong pattern for this page type, use the site pattern first and the playbook second.

## Output Shape

Return these exact headings:

- `Selected page family`
- `Page role in the site`
- `Section-pattern guidance`
- `CTA and proof expectations`
- `Internal-link expectations`
- `Page-type-specific risks`

## Files

- Read `references/page-types.md` for the page-family rules.
