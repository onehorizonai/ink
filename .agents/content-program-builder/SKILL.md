---
name: content-program-builder
description: Create or update Ink Content Program packs for recurring marketing series, campaigns, repeatable formats, asset workflows, calendars, and performance trackers across any marketing channel or production surface, including social, video, audio, email, communities, owned web, paid/partner, direct/product, events, and sales assets.
---

# Content Program Builder

## Overview

Build Content Programs, not one-off drafts. A program is the strategic container for repeatable marketing work: goal, audience, channels, routes, cadence, formats, workflow, assets, calendar, and measurement.

Use this skill when the user wants a recurring series, campaign, repeatable format, semi-manual creative process, or structured program pack for any channel or surface.

## Quick Start

1. Resolve the active Ink profile with `../one-horizon-context-setup/references/ink-profile-contract.md`.
2. Read `references/program-pack-contract.md`.
3. Read `references/channel-taxonomy.md`.
4. Clarify only the missing high-impact details with `references/program-interview.md`.
5. For new programs, ask the required storage question before writing files: should this be `local/private`, or `public/tracked` as part of the open-source repo? Do not infer the answer from defaults.
6. Decide storage from the user's answer:
   - use `.local/content-programs/<profile-id>/<program-id>/` for `local/private` programs
   - use tracked `content-programs/<program-id>/` only for `public/tracked` programs that are generic and safe for open-source users
   - for updates to existing packs, preserve the current storage visibility unless the user asks to move it
7. Audit relevant existing corpus and program examples:
   - selected profile LinkedIn corpus
   - selected profile Reddit corpus
   - selected profile blog source folder when relevant
   - tracked `content-programs/`
   - selected profile local program root
8. Create or update the program pack using the required layout, with `channels` for destinations and `routes` for production paths.
9. Run `python3 scripts/validate_program.py <program-dir>` when the pack is created or changed.
10. If One Horizon tools are available and the user wants tracking, create or update `[Ink Program] <name>` under `Ink - Programs`.

## Working Agreement

- Do not replace existing one-off workflows. Programs are optional.
- Always ask whether a new Content Program is `local/private` or `public/tracked` before creating the pack. This is a hard gate even when the program appears obviously private.
- Do not store private brand assets, live customer facts, or real performance data in tracked starter packs.
- Do not silently use the One Horizon default workspace. Use the selected Ink profile workspace.
- Do not make one Codex skill per program. Program packs are loaded by this builder and by `../content-program-runner/SKILL.md`.
- Keep program docs concise and operational. Link to existing specialized skills when available and use `../channel-content-writer/SKILL.md` as the broad fallback route.
- For semi-manual workflows, document what Ink can automate and what remains manual.
- If a program uses external tools such as design apps, schedulers, music generators, or video editors, produce prompts and handoff steps without claiming Ink performed those external actions.
- If the program creates One Horizon review or triage records, design those records as self-contained review packages whose sections come from the program's formats and routes. A reviewer should be able to approve, request changes, or block production from the One Horizon description alone, without access to `.local/` files or the user's machine. Do not assume every program has scripts, captions, hashtags, comments, footage, or source notes; include the artifacts that matter for that content type.

## Output Shape

Return:

- program name and id
- created or updated pack path
- confirmed storage choice and why it is tracked or local
- formats included
- calendar and performance tracking fields
- linked One Horizon record when created or updated
- validation result

## Files

- `references/program-pack-contract.md`: required program pack layout and field contract.
- `references/channel-taxonomy.md`: canonical channel groups and slugs.
- `references/program-interview.md`: questions and defaults for designing a new program.
- `../content-program-runner/SKILL.md`: use after a program exists and the user wants to create runs.
- `../channel-content-writer/SKILL.md`: generic channel-native drafting and handoffs.
- `../one-horizon-context-setup/references/ink-profile-contract.md`: profile and local root resolution.
- `../one-horizon-context-setup/references/ink-initiative-hierarchy.md`: One Horizon parent model.
- `../../content-programs/`: tracked generic starter packs.
- `../../scripts/validate_program.py`: pack validator.
