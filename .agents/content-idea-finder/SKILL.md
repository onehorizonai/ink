---
name: content-idea-finder
description: Decide what blog article or LinkedIn post to write next by combining current company context, published-content gaps, a workspace-shared One Horizon trend-source URL doc, recent web research, and local MCP trend tools. Use when Codex needs to map a goal to concrete topic ideas, choose between blog and LinkedIn, manage trend or inspiration source URLs for content ideation, or turn a current trend into a credible content angle that fits this repo's saved context and positioning. Do not use this skill to draft the final article or post once the topic is chosen; hand off to the matching writer skill instead.
---

# Content Idea Finder

## Overview

Start with the goal, not the format.

Run a three-role workflow: the orchestrator loads context and manages handoff, the journalist finds up to 3 timely story suggestions, and the editor chooses the strongest topic against company fit, archive uniqueness, and follow-up potential.

## Quick Start

1. Read `references/workflow.md`.
2. Orchestrator: clarify the content job, resolve the author and workspace, run the setup path for missing required context, and load the required One Horizon author context before any local corpus scan.
3. Orchestrator: load or set up `Ink Context - Trend Sources`. If the document is missing or has no usable `Active URLs`, ask the user for trend or inspiration websites and wait for the answer unless the user explicitly says to skip trend-source research for this run. After the user confirms the proposed body, create or update the One Horizon document before journalist research.
4. Journalist: use the trend-source doc or user-provided run sources, `../linkedin-social-writer/references/mcp-tools.md`, trend tools, `web_search`, and `fetch_page` to produce at most 3 timely story suggestions. Do not return journalist suggestions from local corpus search alone.
5. Editor: compare those suggestions against One Horizon company context, `../../content/linkedin/posts/`, and the configured blog source folder, then choose one recommended topic.
6. Editor: report the chosen idea in One Horizon with `report-feature-request`.
7. Orchestrator: return the final recommendation, One Horizon idea record, rationale, source URLs, and a handoff brief for `../blog-post-writer/SKILL.md` or `../linkedin-social-writer/SKILL.md`.

## Working Agreement

- Start from the desired outcome: awareness, product education, launch support, trust or credibility, SEO, demand capture, recruiting, or event follow-up.
- Ask at most 3 short questions only when goal, audience, or timing are genuinely unclear.
- When blog coverage matters, use `../../.local/context/blog-publishing.local.md` for the active blog archive location. Do not assume `content/blog/posts/`.
- Treat the author's `Current Work` One Horizon doc as the boundary for what the team can credibly talk about.
- Use One Horizon context docs for live runtime context. Do not use tracked repo files for live context. The exception is `.local/context/blog-publishing.local.md` for machine-local blog path state.
- If required One Horizon context or workspace resolution is missing, run the setup path in `references/workflow.md` before research. If a required One Horizon tool call is missing or fails, follow the recovery path there. Do not silently continue with guessed company context or substitute local posts for One Horizon context.
- Treat `Ink Context - Trend Sources` as the workspace-shared source of truth for trend and inspiration websites. Do not store this URL list in tracked repo files.
- If `Ink Context - Trend Sources` is missing, empty, or unavailable, ask for the websites to use or get explicit permission to skip trend-source research. When the user provides URLs, create or update the document after explicit confirmation. Do not continue in the same turn as if no source list exists.
- The journalist may bring back at most 3 suggestions. Do not pad the list when fewer stories are worth considering.
- The editor checks the archive after the journalist proposes stories, so uniqueness and follow-up potential are evaluated against actual candidates.
- The local LinkedIn and blog corpora are archive checks, not the primary discovery source. Use them after external story suggestions exist.
- Use trend-source URLs and trend tools as signal, not as the thesis. Translate a signal into a point of view the team can credibly own.
- When trend-source URLs exist, the journalist must search or fetch relevant pages from them before returning suggestions. Each suggestion needs at least one source URL from a fetched page, targeted search result, trend result, primary announcement, credible report, or canonical essay.
- Prefer ideas with proof, examples, product context, or lived experience. Avoid generic "AI is changing everything" angles.
- Do not recommend a format just because the signal is fresh. Timely sharp takes usually fit LinkedIn. Durable explainers, comparisons, and search-intent topics usually fit the blog.
- Allow follow-up stories when a fresh development, stronger proof point, or sharper company angle makes the revisit useful.
- When recommending a blog idea, include the suggested blog post type so `blog-post-writer` can verify it with the user before drafting.
- Treat the suggested blog post type as advisory only. The writing workflow must still ask the user to confirm or correct it before research or drafting starts.
- When no useful trend signal exists, say so and propose evergreen ideas that still fit the goal.
- Reporting the selected content idea to One Horizon is mandatory once the editor chooses a topic. Use `report-feature-request` before the final handoff. Do not end with only local recommendations unless the One Horizon report tool is missing or fails.

## Workflow

Follow `references/workflow.md`.

Use `references/channel-fit.md` when the best format is unclear.

## One Horizon: Report Editor-Selected Idea

When the editor chooses one topic, create the idea in One Horizon before handing off.

Rules:

- Use the MCP report tool `report-feature-request`.
- Do not use `create-todo` or `create-initiative` for the editor-selected content idea.
- This is a real One Horizon MCP tool call, not a sentence in the final response. Do not claim the idea was reported unless the tool call succeeded.
- Title: the working title of the selected idea, prefixed with the channel in brackets, e.g. `[Blog] Why agent workflows break in production`.
- Description: include the one-sentence angle, why now, source URLs, editor rationale, net-new or follow-up status, proof points still needed, recommended channel, and suggested blog post type when the channel is the blog.

If the One Horizon report tool is missing or fails at reporting time, skip this step and say the idea record was not created. A failure means an actual tool call failed or the tool is not callable in the current session. Do not block the handoff brief or the writer routing on One Horizon availability.

## Output Shape

Unless the user asks differently, return:

- the recommended channel first
- up to 3 journalist suggestions with source URLs, short story summary, why now, likely content angle, and confidence or evidence note
- the editor's chosen topic, rejected alternatives, company-fit and archive rationale, whether it is net-new or a follow-up, and why it belongs on LinkedIn or the blog
- a ready-to-use handoff brief for `blog-post-writer` or `linkedin-social-writer`, including the suggested blog post type for blog handoffs
- the One Horizon feature request URL or title when the editor-selected idea was successfully reported
- the context docs, trend-source doc status, corpus examples, and external sources that shaped the recommendation

## Files

- Read `references/workflow.md` for the orchestration flow.
- Read `references/channel-fit.md` when selecting blog vs LinkedIn.
- If a One Horizon context or write tool call fails, read `../one-horizon-context-setup/references/mcp-readiness.md` for recovery.
- Orchestrator resolves the author with One Horizon MCP, runs setup for missing required context, then loads relevant author-scoped context from One Horizon: `Profile`, `Current Work`, and `Work History`.
- Orchestrator loads or sets up the workspace-shared One Horizon doc `Ink Context - Trend Sources` before the journalist researches trend and inspiration signals.
- Editor reads `../../.local/context/blog-publishing.local.md` for the active blog source folder when blog is a possible channel.
- Read `../linkedin-social-writer/references/mcp-tools.md` before using the local research tools.
- Editor searches `../../content/linkedin/posts/` and the configured blog source folder before choosing the topic.
- Hand off selected ideas to `../linkedin-social-writer/SKILL.md` or `../blog-post-writer/SKILL.md`.
