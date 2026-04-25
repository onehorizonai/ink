---
name: reddit-research
description: Research Reddit communities and winning discussion patterns using public Reddit data, One Horizon context docs, and Ink's MCP tools. Use when Codex needs to find audience-relevant subreddits, inspect the best recent posts, understand subreddit rules and anti-promo norms, or hand a Reddit writing brief to another skill.
---

# Reddit Research

## Overview

Find the right subreddit before drafting. Shortlist communities, inspect their rules and top posts, then distill the hooks, tones, and discussion patterns that actually work there.

## Intent Split

- Use this skill for subreddit discovery, rule analysis, top-post analysis, and writing handoff briefs.
- Do not use this skill to draft the Reddit post itself. Use `../reddit-social-writer/SKILL.md`.
- Do not use this skill for storage-only requests. Use `../reddit-store-post/SKILL.md`.

## Quick Start

1. Read `references/workflow.md`.
2. Resolve the author and load only the relevant author-scoped One Horizon context docs. Use `../one-horizon-context-setup/references/context-doc-templates.md` for the naming contract.
3. Read `references/tool-contracts.md` for the exact Reddit tool argument shapes.
4. Read `../linkedin-social-writer/references/mcp-tools.md` before using Ink's local research tools.
5. Use the Reddit tools to shortlist subreddits, inspect rules, and analyze top posts from the past week.
6. Return a compact handoff brief for `../reddit-social-writer/SKILL.md` when the next step is drafting.

## Working Agreement

- Start from audience and topic fit, not from the biggest subreddit by subscriber count.
- Treat subreddit rules and posting guidance as hard constraints.
- Use public no-auth Reddit access for v1. If a Reddit endpoint fails, fall back to the other local research tools instead of inventing results.
- Use One Horizon context docs to understand the author and audience. Do not use tracked repo files for live context.
- If a One Horizon tool call is missing or fails, follow `../one-horizon-context-setup/references/mcp-readiness.md`. Do not search tracked repo files as a substitute for live context.
- Surface promotion risk explicitly. If a subreddit is likely to reject branded, link-heavy, or self-promotional posts, say so.
- Separate general subreddit fit from topic-specific post fit. A large subreddit can still be the wrong place for a given angle.
- Produce a drafting handoff, not just raw research notes.
- Use the exact tool schemas from `references/tool-contracts.md`. Do not improvise argument keys.
- If no subreddit looks like a credible fit, say that explicitly and stop instead of forcing a recommendation.

## Output Shape

Unless the user asks differently, return:

- `Recommended Subreddits`: 3 or fewer ranked by fit
- `Rules And Risks`: notable rules, anti-promo risks, and tone constraints
- `Winning Patterns`: the recent post patterns that matter
- `Angle Options`: 2 or 3 viable angles the author could post about
- `Writer Handoff`: one recommended brief for `reddit-social-writer` using the required handoff fields
- `Sources Used`: the One Horizon context docs and research tools used

## Files

- Read `references/workflow.md`.
- Read `references/tool-contracts.md` before calling the Reddit tools.
- If a One Horizon tool call fails, read `../one-horizon-context-setup/references/mcp-readiness.md` for recovery.
- Resolve the author with One Horizon MCP tools, then load relevant author-scoped context from One Horizon: `Profile`, `Current Work`, and `Market Context`.
- Read `../linkedin-social-writer/references/mcp-tools.md` before using Ink's local research tools.
- Hand off drafting work to `../reddit-social-writer/SKILL.md`.
