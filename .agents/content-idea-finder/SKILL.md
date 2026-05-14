---
name: content-idea-finder
description: Create a reusable Content Idea Brief for One Horizon approval across LinkedIn, Reddit, or the blog by combining current company context, trend signals, archive gaps, and channel fit. Use when Codex needs to map a goal to one concrete content idea, choose a channel, manage trend-source URLs, or turn a current signal into an approved-later brief that a writer workflow can pick up. Blog ideas follow the Blog Lifecycle Contract. Do not draft content in this skill.
---

# Content Idea Finder

## Overview

Start with the goal, not the format. The end state is a proposed Content Idea Brief filed into One Horizon, not a draft and not an approval request in chat.

Run a three-role workflow: orchestrator loads context, journalist finds up to 3 timely options, editor selects one and reports it as a reusable brief.

## Quick Start

1. Read `references/workflow.md`.
2. Orchestrator: clarify the content job, resolve the Ink profile, author, and workspace, run the setup path for missing required context, and load the required One Horizon author context before any local corpus scan.
3. Orchestrator: load or set up `Ink Context - Trend Sources`. If the document is missing or has no usable `Active URLs`, ask the user for trend or inspiration websites and wait for the answer unless the user explicitly says to skip trend-source research for this run. After the user confirms the proposed body, create or update the One Horizon document before journalist research.
4. Orchestrator: search One Horizon for existing work with titles starting `[Ink]` and treat those records as the primary exclude list before ideation.
5. Journalist: use the trend-source doc or user-provided run sources, `../linkedin-social-writer/references/mcp-tools.md`, trend tools, `web_search`, and `fetch_page` to produce at most 3 timely story suggestions. Do not return journalist suggestions from local corpus search alone.
6. Editor: check relevant published LinkedIn, Reddit, and blog archives, then choose one topic.
7. Editor: report the chosen idea in One Horizon, using `references/idea-brief-template.md` as the description format. Use `create_initiative` for Blog ideas; use the report tool for other channels.
8. Orchestrator: return the recommendation, the One Horizon record, and a short note on the later workflow to run after approval.

## Working Agreement

- Start from outcome and audience, then choose LinkedIn, Reddit, or blog with `references/channel-fit.md`.
- Resolve the active Ink profile before One Horizon lookups or local corpus scans. If multiple profiles exist and none is named, ask which profile to use.
- Load live context from the selected profile's One Horizon workspace. Do not infer company positioning from local corpus files.
- Use One Horizon `[Ink Idea]` and `[Ink Draft]` records as the primary planned-content exclude list.
- Use trend sources and web/trend tools for discovery; use published local corpora only to check overlap and gaps.
- Do not use local draft folders for content-idea dedupe.
- Return at most 3 journalist options, then choose one. Do not pad weak ideas.
- Report the selected idea to One Horizon using `references/idea-brief-template.md`. Blog ideas use `create_initiative`; LinkedIn and Reddit use the report tool.
- Do not draft content. Approval happens in One Horizon, and later writer workflows pick up the approved brief.

## Workflow

Follow `references/workflow.md`.

Use `references/channel-fit.md` when the best format is unclear.

## One Horizon: Report Editor-Selected Idea

When the editor chooses one topic, create the idea in One Horizon before returning the recommendation. This is a Content Idea Brief, not a draft.

Rules:

- For Blog, use `create_initiative` and the Blog Lifecycle Contract in `../one-horizon-context-setup/references/ink-initiative-hierarchy.md`.
- For LinkedIn and Reddit, use the MCP report tool `report-feature-request` unless their channel workflow says otherwise.
- Do not use `create-todo`. Do not use `create-initiative` for LinkedIn or Reddit ideas unless their channel workflow changes.
- This is a real One Horizon MCP tool call, not a sentence in the final response. Do not claim the idea was reported unless the tool call succeeded.
- Title: the working title of the selected idea, prefixed with `[Ink Idea]` and the channel in brackets, e.g. `[Ink Idea] [Blog] Why agent workflows break in production`.
- Description: use `references/idea-brief-template.md`. Fill every relevant field and omit only channel-specific fields that do not apply.

If the One Horizon create/report tool is missing or fails at reporting time, skip this step and say the idea record was not created. A failure means an actual tool call failed or the tool is not callable in the current session. Do not block the recommendation summary on One Horizon availability.

## Output Shape

Unless the user asks differently, return:

- the recommended channel first
- up to 3 journalist suggestions with source URLs, short story summary, why now, likely content angle, and confidence or evidence note
- the editor's chosen topic, rejected alternatives, company-fit and archive rationale, whether it is net-new or a follow-up, and why it belongs on LinkedIn, Reddit, or the blog
- the brief summary and the relevant future workflow after One Horizon approval
- the One Horizon record URL or title when the editor-selected idea was successfully reported for approval
- the context docs, trend-source doc status, One Horizon exclude-list status, published corpus examples, and external sources that shaped the recommendation

## Files

- Read `references/workflow.md` for the orchestration flow.
- Read `references/channel-fit.md` when selecting LinkedIn, Reddit, or blog.
- Use `references/idea-brief-template.md` as the single source of truth for the One Horizon description.
- If a One Horizon context or write tool call fails, read `../one-horizon-context-setup/references/mcp-readiness.md` for recovery.
- Orchestrator resolves the selected Ink profile with `../one-horizon-context-setup/references/ink-profile-contract.md`, resolves the author with One Horizon MCP inside that workspace, runs setup for missing required context, then loads relevant author-scoped context from One Horizon: `Profile`, `Current Work`, and `Work History`.
- Orchestrator loads or sets up the selected workspace's One Horizon doc `Ink Context - Trend Sources` before the journalist researches trend and inspiration signals.
- Editor reads the selected profile's `blogPublishingConfig` for the active blog source folder when blog is a possible channel.
- Read `../linkedin-social-writer/references/mcp-tools.md` before using the local research tools.
- Orchestrator searches One Horizon for `[Ink]` records before journalist ideation, then filters for `[Ink Idea]` and `[Ink Draft]` title prefixes.
- Editor searches published corpus paths from the selected profile only: LinkedIn `contentRoots.linkedin`, Reddit `contentRoots.reddit`, and the configured blog source folder before choosing the topic.
- After approval, use `../content-creation-runner/SKILL.md` to turn planned `[Ink Idea]` records into reviewable `[Ink Draft]` work, updating Blog in place and creating social draft initiatives as that runner specifies.
