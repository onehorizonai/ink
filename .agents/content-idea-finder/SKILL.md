---
name: content-idea-finder
description: Decide what blog article or LinkedIn post to write next by combining current company context, published-content gaps, recent web research, and local MCP trend tools. Use when Codex needs to map a goal to concrete topic ideas, choose between blog and LinkedIn, or turn a current trend into a credible content angle that fits this repo's saved context and positioning. Do not use this skill to draft the final article or post once the topic is chosen; hand off to the matching writer skill instead.
---

# Content Idea Finder

## Overview

Start with the goal, not the format.

Find what matters now, check whether the repo already covered it, then turn the signal into a channel-specific angle the business can credibly own.

## Quick Start

1. Read `references/workflow.md`.
2. Read `../../.local/README.md`, then load only the relevant files from `../../.local/context/`.
3. If blog is in scope, read `../../.local/context/blog-publishing.local.md`, then resolve `source_articles_dir` from the local file before scanning blog coverage.
4. Search `../../content/linkedin/posts/` and the configured blog source folder for overlaps, repeats, and gaps.
5. Read `../linkedin-social-writer/references/mcp-tools.md`.
6. Use `google_trends_keyword_insights` on 2-5 seed topics pulled from the goal, current work, or the current event.
7. Use `web_search` and `fetch_page` to confirm what a rising query actually refers to and whether it fits the product context.
8. Recommend the best channel, then return 3-5 concrete ideas plus one recommended next move.
9. If the user picks an idea, hand off to `../blog-post-writer/SKILL.md` or `../linkedin-social-writer/SKILL.md`.

## Working Agreement

- Start from the desired outcome: awareness, product education, launch support, trust or credibility, SEO, demand capture, recruiting, or event follow-up.
- Ask at most 3 short questions only when goal, audience, or timing are genuinely unclear.
- When blog coverage matters, use `../../.local/context/blog-publishing.local.md` for the active blog archive location. Do not assume `content/blog/posts/`.
- Treat `../../.local/context/current-work.md` as the boundary for what the team can credibly talk about.
- Use `.local/context/*.md` for live runtime context. Do not use tracked repo files outside `.local/` for live context.
- Check the corpus before the web so new ideas do not repeat recent posts or articles.
- Use trend tools as signal, not as the thesis. Translate a signal into a point of view the team can credibly own.
- Prefer ideas with proof, examples, product context, or lived experience. Avoid generic "AI is changing everything" angles.
- Do not recommend a format just because the signal is fresh. Timely sharp takes usually fit LinkedIn. Durable explainers, comparisons, and search-intent topics usually fit the blog.
- When no useful trend signal exists, say so and propose evergreen ideas that still fit the goal.

## Workflow

Follow `references/workflow.md`.

Use `references/channel-fit.md` when the best format is unclear.

## Output Shape

Unless the user asks differently, return:

- the recommended channel first
- 3-5 ranked ideas
- for each idea: working title, core angle, why now, why it fits the goal, proof or sources to gather, and why it belongs on LinkedIn or the blog
- one recommended idea to write now
- a ready-to-use handoff brief for `blog-post-writer` or `linkedin-social-writer`
- the context files, corpus examples, and external sources that shaped the recommendation

## Files

- Read `references/workflow.md` for the orchestration flow.
- Read `references/channel-fit.md` when selecting blog vs LinkedIn.
- Read `../../.local/README.md` before loading any user context.
- Read `../../.local/context/blog-publishing.local.md` for the active blog source folder.
- Read `../linkedin-social-writer/references/mcp-tools.md` before using the local research tools.
- Search `../../content/linkedin/posts/` and the configured blog source folder before recommending a topic.
- Hand off selected ideas to `../linkedin-social-writer/SKILL.md` or `../blog-post-writer/SKILL.md`.
