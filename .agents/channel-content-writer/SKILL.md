---
name: channel-content-writer
description: Draft or prepare channel-native marketing outputs for Ink channels that do not yet have a dedicated writer skill, including Instagram, TikTok, YouTube, X/Twitter, Facebook, newsletters, email sequences, Discord, forums, communities, podcasts, webinars, ads, SMS, push, in-app messages, app-store listings, marketplace listings, events, sales collateral, and program-run handoffs. Route to specialized Ink skills when available.
---

# Channel Content Writer

## Overview

Create channel-native marketing outputs for any channel or surface that is not covered by a dedicated Ink writer skill.

Use this for one-off channel content and Content Program runs. It can produce drafts, captions, scripts, outlines, asset briefs, prompts for external tools, review notes, and manual publishing handoffs.

## Quick Start

1. Resolve the active Ink profile with `../one-horizon-context-setup/references/ink-profile-contract.md`.
2. Read `../content-program-builder/references/channel-taxonomy.md`.
3. If the requested channel has a dedicated skill, route there:
   - LinkedIn: `../linkedin-social-writer/SKILL.md`
   - Reddit: `../reddit-research/SKILL.md` then `../reddit-social-writer/SKILL.md`
   - Blog: `../blog-post-writer/SKILL.md`
   - Website/page briefs: `../page-brief-builder/SKILL.md`
   - Final page copy: `../copywriting/SKILL.md`
4. Read `references/channel-format-index.md` and resolve the request through `references/channel-format-registry.csv`.
5. For broad channels, load only the relevant One Horizon context and any selected Content Program pack.
6. Produce a channel-native output or handoff bundle. Do not publish, schedule, send email, generate video/music, or upload externally unless a real tool is available and explicitly used.
7. Store private drafts or examples only when requested, under the selected profile's channel workspace.

## Channel Defaults

- Social: load `references/channels/social.md`, then the registry's channel and format guides.
- Video and audio: load `references/channels/video-audio.md`, then the registry's channel and format guides.
- Owned and email: load `references/channels/owned-email.md`, then the registry's channel and format guides.
- Communities: load `references/channels/communities.md`, then the registry's channel and format guides.
- Paid and partner: load `references/channels/paid-partner.md`, then the registry's channel and format guides.
- Direct and product: load `references/channels/direct-product.md`, then the registry's channel and format guides.
- Events and sales: load `references/channels/events-sales.md`, then the registry's channel and format guides.
- Dedicated adapters: route to the dedicated skill and its playbooks from the registry.

## Guardrails

- Be channel-native, not a generic social rewrite.
- Keep production notes out of audience-facing copy. Do not leak labels such as `<brand> angle:`, `CTA:`, `hook:`, `note:`, `audience:`, or `internal:` into captions, descriptions, scripts, comments, or post bodies unless the platform-native artifact explicitly calls for that visible label.
- Put strategy, rationale, assumptions, and review notes in separate handoff sections instead of inside the final copy block.
- Respect platform norms and likely moderation, compliance, or deliverability risk.
- Keep claims, metrics, prices, and customer examples out unless provided or verified.
- Separate generation from manual execution for tools such as Buffer, Metricool, email service providers, design tools, music generators, and video editors.
- Use existing review skills for longer narrative drafts or risky claims.
- When a channel output is sent to One Horizon for someone else to review, the One Horizon record must include the actual draft or handoff bundle in a structure that fits the requested content type. Include only the relevant sections for that output, such as copy, scripts, outlines, variants, captions, hashtags, replies, asset notes, source notes, claims, compliance risks, manual steps, or review questions. Do not ask reviewers to inspect local files on the user's machine.

## Output Shape

Return:

- target channel and format
- draft or handoff bundle
- asset requirements
- manual steps that remain outside Ink
- optional Content Program metadata
- review or fact-check needs

## Files

- `../content-program-builder/references/channel-taxonomy.md`
- `../content-program-runner/references/run-contract.md`
- `references/channel-format-index.md`
- `references/channel-format-registry.csv`
- `references/channel-workspace.md`
- `references/channels/`
- `references/formats/`
- selected profile local channel workspace, usually `.local/content/<profile-id>/channels/`
