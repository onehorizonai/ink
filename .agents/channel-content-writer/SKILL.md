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
4. For all other channels, load only the relevant One Horizon context and any selected Content Program pack.
5. Produce a channel-native output or handoff bundle. Do not publish, schedule, send email, generate video/music, or upload externally unless a real tool is available and explicitly used.
6. Store private drafts or examples only when requested, under the selected profile's channel workspace.

## Channel Defaults

- Short social: hook, body/caption, visual brief, alt text when relevant, hashtags only if native.
- Short video: hook, beat script, shot list, on-screen text, caption, asset notes.
- Long video or podcast: title options, premise, outline, segment beats, intro/outro, thumbnail or cover brief.
- Newsletter or email: subject options, preview text, body, CTA, segmentation notes.
- Community or forum: native title/opening, body, discussion prompt, rule/risk notes.
- Paid or partner: angle, creative brief, copy variants, claim/compliance notes, landing-page dependency.
- Direct or product messaging: trigger, audience segment, message, CTA, frequency/risk notes.
- Events or sales: talk/deck outline, key message, proof needs, follow-up assets.

## Guardrails

- Be channel-native, not a generic social rewrite.
- Respect platform norms and likely moderation or deliverability risk.
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
- `references/channel-workspace.md`
- selected profile local channel workspace, usually `.local/content/<profile-id>/channels/`
