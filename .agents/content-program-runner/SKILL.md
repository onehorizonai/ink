---
name: content-program-runner
description: Execute or prepare runs from an existing Ink Content Program pack for any marketing channel or production surface. Use when the user wants to batch recurring content, create program run artifacts, route a format into dedicated Ink skills, use the generic channel-content-writer fallback, or produce handoff prompts for semi-manual marketing steps.
---

# Content Program Runner

## Overview

Run an existing Content Program. A run may create channel-ready content, One Horizon records, local handoff files, asset briefs, scripts, prompts for external tools, or review notes.

Use this skill only after a program pack exists. Use `../content-program-builder/SKILL.md` first when the program needs to be designed or scaffolded.

## Quick Start

1. Resolve the active Ink profile with `../one-horizon-context-setup/references/ink-profile-contract.md`.
2. Discover matching program packs in:
   - selected profile `contentProgramRoots` when configured
   - `.local/content-programs/<profile-id>/`
   - tracked `content-programs/`
3. If tracked and local packs have the same `program.yaml` id, prefer the selected profile's local pack and say so.
4. Read the selected pack's `program.yaml`, `README.md`, `workflow.md`, relevant `formats/*.md`, and relevant `prompts/*.md`.
5. For broad channels, read `../channel-content-writer/references/channel-format-index.md`, resolve the slug in `../channel-content-writer/references/channel-format-registry.csv`, and load the matching channel and format guides before applying program-specific constraints.
6. Confirm only missing run facts: count, theme, date window, channels, and output type.
7. Create run output:
   - route to specialized skills when the route uses one
   - route broad channels to `../channel-content-writer/SKILL.md`
   - create a manual handoff bundle when external tools or design work are required
8. Update `calendar.csv` only when the user asked to persist the plan.
9. Update `performance.csv` only from provided published metrics.
10. Validate the pack with `python3 scripts/validate_program.py <program-dir>` after persistent edits.

## Routing

Use existing repo skills instead of duplicating channel logic. Specialized skills are adapters, not the boundary of what Ink supports:

- LinkedIn posts, replies, DMs, reposts: `../linkedin-social-writer/SKILL.md`
- Reddit research and posts: `../reddit-research/SKILL.md`, then `../reddit-social-writer/SKILL.md`
- Blog articles: `../blog-post-writer/SKILL.md`
- Website page briefs: `../page-brief-builder/SKILL.md`
- Final page copy: `../copywriting/SKILL.md`
- Blog/image sourcing: `../blog-image-finder/SKILL.md`, `../blog-image-uploader/SKILL.md`
- Review passes: local review skills such as `../content-humanizer/SKILL.md`, `../content-tone-review/SKILL.md`, `../content-style-review/SKILL.md`, and `../fact-check/SKILL.md`
- Broad channels and unsupported surfaces: `../channel-content-writer/SKILL.md`

For broad channels, shared channel and format guidance is loaded before program pack rules. Content Programs add consistency, cadence, campaign, asset, and KPI constraints; they do not replace reusable channel guidance.

For `manual-asset` or `manual-external-tool`, return prompts, asset briefs, and step-by-step handoff notes. Do not claim external publishing, scheduling, email sending, music generation, video editing, upload, or design rendering happened unless the tool actually did it.

## One Horizon

- Program definitions use `[Ink Program] <name>` under `Ink - Programs`.
- Manual or semi-manual runs may use `[Ink Program Run] <program> - <date/title>` under `Ink - Programs`.
- Specialized channel outputs stay under their existing parents. Generic channel outputs may use `Ink - Channel Content`. All may include optional `program_id`, `format_id`, `run_id`, and `campaign_id` metadata.
- Set work to `In Review` whenever a human must approve, publish, schedule, provide assets, or answer a blocker.
- One Horizon review records must be self-contained. Put the actual reviewable bundle in the One Horizon description or linked One Horizon document, using sections that match the specific program format and content type. Examples might include copy, scripts, outlines, captions, creative variants, asset briefs, footage notes, source notes, claims, compliance risks, publish handoffs, or QA steps, but do not force irrelevant sections. Local file paths may be included only as supplemental archive pointers, never as the primary review artifact.
- When creating triage/review items with a reporter and reviewer, include the final title, full description, team, and assignee/reviewer in the initial create/report call whenever possible. Avoid follow-up metadata-only updates that replace contributors unless the tool explicitly preserves reporter contributors; if an update is unavoidable, verify the reporter is still present afterward.
- Unknown-scope triage items may support only `Idea`, `Open`, or `Cancelled`; do not force `In Review` if the platform rejects it. Use the supported active review state and make the review decision clear in the description.

## Output Shape

Return:

- program and pack path
- run ids and planned dates
- generated outputs or handoff file paths
- routed skills used
- One Horizon records created or updated
- calendar or performance updates
- blockers and manual next steps

## Files

- `../content-program-builder/references/program-pack-contract.md`
- `../content-program-builder/references/channel-taxonomy.md`
- `references/run-contract.md`
- `../channel-content-writer/SKILL.md`
- `../channel-content-writer/references/channel-format-index.md`
- `../channel-content-writer/references/channel-format-registry.csv`
- `../one-horizon-context-setup/references/ink-profile-contract.md`
- `../one-horizon-context-setup/references/ink-initiative-hierarchy.md`
- `../../content-programs/`
- `../../scripts/validate_program.py`
