# Workflow

Run this as a three-role workflow: orchestrator, journalist, then editor. These are procedural roles inside this skill, not separate skills.

The endpoint is a One Horizon approval record that can be approved, rejected, or prioritized later inside One Horizon. Blog ideas follow the Blog Lifecycle Contract in `../../one-horizon-context-setup/references/ink-initiative-hierarchy.md`. Generic non-specialized channel ideas can use `Ink - Channel Content`. Do not ask the user to approve the idea in chat, and do not draft the content in this workflow.

## 1. Orchestrator: Clarify and Load Context

Capture:

- goal
- audience
- timing window
- channel constraint if any, including dedicated Ink channels, broad generic channels, Content Program fit, or no preference
- product area or theme
- required source, launch, event, or claim if any

If the goal, audience, or timing is unclear, ask at most 3 short questions total for this workflow.

Resolve the active Ink profile with `../../one-horizon-context-setup/references/ink-profile-contract.md`, then resolve the author and workspace with One Horizon MCP inside the selected profile workspace. Load only the relevant author-scoped One Horizon context docs. Use `../../one-horizon-context-setup/references/context-doc-templates.md` for the naming and missing-doc contract:

- `Profile` for voice and identity basics
- `Current Work` for the active company, positioning, audience, and safe themes
- `Work History` only when founder background or credibility is part of the angle

Do not load personal files just because they exist.
Do not use tracked repo files for live runtime context.

### Context loading

Before journalist research, load the minimum One Horizon context:

- A single Ink profile and workspace are resolved.
- A single author is resolved.
- `Ink Context - {Author Name} - Current Work` exists and is usable.
- `Ink Context - {Author Name} - Profile` exists when voice or identity matters.
- `Ink Context - {Author Name} - Work History` exists when founder background or credibility is part of the angle.

This is a hard gate. Do not start local corpus searches, trend searches, or journalist ideation until the required profile, workspace, author, and `Current Work` context have been resolved and loaded.

A context doc is loaded only when its document content has been read and the workflow has extracted the relevant fields for this run. For `Current Work`, extract the company or project, role, current positioning, main audience, key offers or products, themes worth posting about, and words or angles to avoid. Finding a document by title is not enough.
Use `find-documents` only to locate candidate context docs by ID, title, status, type, or excerpt. Call `get-document` for the selected `documentId` before reading fields or treating the context doc as loaded.

If a required One Horizon tool call is missing or fails while loading required context, follow `../../one-horizon-context-setup/references/mcp-readiness.md`. Do not run web research from guessed company context.

If any required author-scoped context doc is missing, use `../../one-horizon-context-setup/SKILL.md` before continuing. That setup skill owns creating missing author context docs and required Ink parent initiatives. Follow its confirmation flow, then return to this workflow after setup completes.

If a required doc exists but key fields needed for idea selection are `[unset]` or too thin, ask the user for only the missing business facts needed for this run. Do not overwrite the existing doc from this workflow.

Keep using the local blog path setup rules in the editor stage when blog coverage is possible. Reddit and LinkedIn published archive checks use the selected profile corpus paths. Generic channel checks use `contentRoots.channels`, `.local/content/<profile-id>/channels/`, and relevant Content Program examples when available. Do not use local draft folders for content-idea dedupe.

## 2. Orchestrator: Load or Maintain Trend Sources

Use the selected workspace's One Horizon document `Ink Context - Trend Sources` as the source of truth for websites used as trend and inspiration sources.

Resolve this document before journalist research. If the document is missing, empty, unavailable, or has no usable URLs under `## Active URLs`, ask the user for the websites they want to use for trend and inspiration research. Wait for the user's answer unless they already explicitly said to skip trend-source research.

If the One Horizon tool call for this document is missing or fails, ask whether the user wants to provide run-specific source URLs or skip trend-source research for this run. Continue without the document only after the required author/company context has loaded successfully and the user explicitly chooses to skip or provides no URLs after being asked. Say trend-source context was skipped. Do not create a local fallback file.

### Existing document

If `Ink Context - Trend Sources` exists:

- Read it with `get-document` before the journalist builds seed topics or web research queries.
- Use `Active URLs` to identify sites worth searching directly or checking for recent posts, announcements, essays, changelogs, or market signals.
- Use `Research Guidance` to include preferred themes and avoid excluded topics.
- Do not treat a source URL as proof by itself. Fetch or search the actual relevant page before using it as evidence.
- If `Active URLs` is empty, `[unset]`, or only contains unusable placeholders, treat the document as incomplete for this run and ask for websites. After confirmation, update the existing document instead of creating a duplicate.

### Missing document

If `Ink Context - Trend Sources` does not exist:

- Ask the user for the websites they want to use for trend and inspiration research.
- Accept URLs with optional notes, such as theme, audience, or why the source matters.
- Show the proposed document body and ask for explicit confirmation before creating it.
- Do not continue in the same assistant turn after asking for URLs. Wait for the user's answer.
- If the user explicitly says they have no URLs or wants to skip this setup, continue without the document and note that trend-source context was skipped.
- If the user provides URLs and confirms the proposed body, create `Ink Context - Trend Sources` in One Horizon before journalist research. Do not keep confirmed URLs only in the chat transcript.

Create the document with this shape:

```md
# Trend Sources

## Active URLs

- https://example.com - Optional note or theme.

## Research Guidance

- Preferred themes: [unset]
- Excluded topics: [unset]
- Notes: [unset]
```

If the document does not exist, create it with the One Horizon document creation tool using this shape:

```json
create_document({
  "title": "Ink Context - Trend Sources",
  "type": "Requirement",
  "status": "Completed",
  "content": "# Trend Sources\n\n## Active URLs\n\n- https://example.com - Optional note or theme.\n\n## Research Guidance\n\n- Preferred themes: [unset]\n- Excluded topics: [unset]\n- Notes: [unset]",
  "workspaceId": "<selected profile workspaceId>"
})
```

If the document exists but has no usable `Active URLs`, update the existing document with the confirmed body:

```json
update_document({
  "documentId": "<documentId>",
  "workspaceId": "<selected profile workspaceId>",
  "status": "Completed",
  "content": "# Trend Sources\n\n## Active URLs\n\n- https://example.com - Optional note or theme.\n\n## Research Guidance\n\n- Preferred themes: [unset]\n- Excluded topics: [unset]\n- Notes: [unset]"
})
```

### Updating the document

If the user gives new trend-source URLs:

- Read the current `Ink Context - Trend Sources` document first.
- Normalize URLs enough to spot obvious duplicates, such as trailing slashes or `www.` differences, without rewriting the user's preferred display text.
- Append only new URLs to `## Active URLs`.
- Preserve existing notes and guidance unless the user explicitly changes them.
- Show the URLs that will be added and ask for confirmation before updating.

If the user asks to remove, replace, or change URLs or guidance:

- Read the current document first.
- Show a concise before/after summary of the affected lines.
- Ask for explicit confirmation before updating.
- Preserve unaffected URLs, notes, headings, and guidance.

## 3. Orchestrator: Build One Horizon Exclude List

Before journalist research, search One Horizon for existing Ink content work. This is the primary dedupe list for planned, in-review, and already-filed ideas or drafts.

Use `search_tasks` with this shape when categories are supported:

```json
search_tasks({
  "query": "[Ink]",
  "categories": ["initiative", "ongoing", "bug", "triage-bug", "triage-item", "triage-initiative", "review-bug", "review-item", "review-initiative", "day-task"],
  "limit": 50,
  "workspaceId": "<selected profile workspaceId>"
})
```

Filter to titles starting `[Ink Idea]` or `[Ink Draft]`. Keep title, channel, status, type, parent, and short excerpt. Use these as exclusion signals, not source material.

Reject overlapping ideas unless the new signal, proof, audience, channel, or angle is materially different. If search fails, say so and continue with published archive checks; do not scan local drafts.

## 4. Journalist: Find Story Suggestions

The journalist finds up to 3 timely stories worth considering. Do not return more than 3 suggestions, and do not pad weak stories to reach 3.

Before using tools, read `../../linkedin-social-writer/references/mcp-tools.md`.

Build the reporting set from:

- the user's goal, theme, timing, and channel constraint
- the author's `Current Work` doc
- the selected profile's `Ink Context - Trend Sources` or user-provided run-specific source URLs
- the One Horizon `[Ink]` exclude list
- current events, product announcements, vendor releases, canonical essays, or credible reporting

Do not build journalist suggestions from local LinkedIn, Reddit, or blog corpus search alone. The archive is checked in the editor stage after current external candidates exist.

Research current signals:

- Derive 5-10 seed phrases from the goal, current-work themes, trend-source doc, and any current event already in play.
- Use `google_trends_keyword_insights` on the best 2-5 seeds.
- Use `google_trends_trending_searches` only to discover timely hooks within the target geography.
- Search or fetch relevant pages from `Ink Context - Trend Sources` or run-specific URLs when they match the goal, audience, product area, or seed list.
- Use `web_search` and `fetch_page` to verify what the signal actually refers to.
- Prefer primary docs, vendor announcements, canonical essays, and credible reporting over generic summaries.

When source URLs are available, use at least one targeted source search or page fetch before returning journalist suggestions. Valid tool shapes:

```json
web_search({"query":"agent workflow reliability site:example.com","max_results":5})
fetch_page({"url":"https://example.com/post","max_chars":6000})
```

If no source URLs are available because the user explicitly skipped them, still run a lightweight web search and trend pass from the goal and `Current Work` themes before returning ideas. If the research tools are unavailable, say that timely external research could not run and only offer evergreen ideas when the user still wants to continue.

For each journalist suggestion, include:

- working title
- source URLs
- short story summary
- why now
- likely content angle
- plausible channels, including Reddit when the idea is discussion-first or community-specific
- confidence or evidence note

Discard stories that depend on hype, weak evidence, or a point of view the repo does not own.

## 5. Editor: Check Archive and Choose Topic

The editor evaluates the journalist's suggestions against company fit, archive uniqueness, and follow-up potential.

If blog is a possible channel:

- Read the selected profile's `blogPublishingConfig`.
- If the local file is missing, ask the user for the existing blog articles folder and create the local file before scanning blog coverage.
- If `source_articles_dir` is `[unset]` or missing on disk, ask the user for the existing blog articles folder and update the selected profile's blog publishing config before scanning blog coverage.
- If the user does not know the blog folder yet, skip blog archive scanning, say blog path setup is incomplete, and prefer LinkedIn unless the prompt requires a blog recommendation.

Check the published archive after the journalist proposes stories:

- Search the LinkedIn corpus under the selected profile's `contentRoots.linkedin`.
- Search the Reddit corpus under the selected profile's `contentRoots.reddit`.
- Search the configured blog source folder when blog is possible.
- Do not search local draft folders for content-idea dedupe.
- Compare each suggestion against same keywords, adjacent concepts, launches, and recent dates.
- Pull 3-6 relevant examples total across LinkedIn, Reddit, and blog.
- Note repeated angles, under-covered areas, and any very recent post that should not be cannibalized.
- Prefer recent examples when the voice or positioning may have shifted.

Choose one topic by scoring:

- company and audience fit
- freshness
- uniqueness versus the One Horizon exclude list and published archive
- follow-up value when the topic is not net-new
- proof availability
- channel fit

Allow follow-up stories when a fresh development, stronger proof point, sharper company angle, or clearer audience need makes the revisit useful. Reject follow-ups that only restate a recent post.

For the editor decision, include:

- chosen topic
- rejected alternatives
- One Horizon exclude-list, published archive, and company-fit rationale
- whether the chosen topic is net-new or a follow-up
- recommended channel
- suggested blog post type when the channel is the blog
- Reddit research need, likely audience, and any subreddit assumptions when the channel is Reddit

Use `channel-fit.md` when the best format is unclear. Timely sharp takes usually fit LinkedIn. Discussion-first, community-specific, or "learn in public" prompts may fit Reddit. Durable explainers, comparisons, and search-intent topics usually fit the blog.

## 6. Editor: Report Selected Idea in One Horizon

After choosing the topic, create a new idea record in One Horizon. This record starts the One Horizon approval workflow and stores the handoff brief for later writing work.

For Blog, use `create_initiative` and the Blog Lifecycle Contract.
For LinkedIn and Reddit, use `report-feature-request` unless that channel workflow changes.
Do not use `create-todo`.

This step is mandatory after the editor chooses a topic. It requires a real One Horizon MCP tool call before the final handoff. Do not treat writing the idea in the response as reporting it.

Use `idea-brief-template.md` as the description format. The brief is the handoff artifact, so fill it with the decision context a later workflow needs after approval.

For Blog, resolve the `Ink - Blog` parent initiative, then call `create_initiative` with this shape:

```json
create_initiative({
  "title": "[Ink Idea] [Blog] Why agent workflows break in production",
  "description": "<filled Content Idea Brief from references/idea-brief-template.md>",
  "status": "In Review",
  "parentInitiativeId": "<Ink - Blog initiative taskId>",
  "workspaceId": "<selected profile workspaceId>",
  "teamIds": ["<teamId>"],
  "assigneeIds": ["<userId>"]
})
```

For LinkedIn and Reddit, call the report tool with this shape:

```json
report_feature_request({
  "title": "[Ink Idea] [LinkedIn] Why agent workflows break in production",
  "description": "<filled Content Idea Brief from references/idea-brief-template.md>",
  "workspaceId": "<selected profile workspaceId>",
  "teamIds": ["<teamId>"],
  "assigneeIds": ["<userId>"]
})
```

Title rules:

- Prefix the title with `[Ink Idea]` and the recommended channel in brackets: `[Ink Idea] [Blog]`, `[Ink Idea] [LinkedIn]`, or `[Ink Idea] [Reddit]`.
- Use the editor's chosen working title after the prefix.
- Do not create new content idea records with only `[Ink]`, `[Blog]`, `[LinkedIn]`, or `[Reddit]`.

Description rules:

- Follow `idea-brief-template.md`.
- Do not include drafted content.
- Include a clear next workflow, but do not start that workflow in this skill.

Use the selected profile workspace resolved during context loading as `workspaceId`; it is required for the One Horizon write tool. If no workspace can be resolved, resolve the Ink profile and One Horizon workspace before reporting. If team or assignee IDs are not available from the active One Horizon context, omit only `teamIds` or `assigneeIds` rather than guessing.

If the One Horizon create/report tool is missing or fails at reporting time, skip this step and say the idea record was not created. A failure means an actual tool call failed or the tool is not callable in the current session. Do not retry or block the recommendation on One Horizon availability.

## 7. Orchestrator: Handoff

Return the recommended channel first.

Include:

- up to 3 journalist suggestions with source URLs, story summaries, why-now notes, likely angles, and confidence or evidence notes
- the editor's chosen topic and rationale
- rejected alternatives
- whether the chosen topic is net-new or a follow-up
- the One Horizon record URL or title when the editor-selected idea was successfully reported
- a short summary of the filed Content Idea Brief
- the context docs, trend-source doc status, One Horizon exclude-list status, published corpus examples, and external sources used

When the format is the blog, make it explicit that the suggested type is part of the approval brief. If the idea is later moved to `Planned` unchanged, `content-creation-runner` treats that type as confirmed for automation.

Name the later workflow after the One Horizon report attempt, but do not invoke it. Use `../../content-creation-runner/SKILL.md` after the idea is approved and moved to `Planned`; that runner routes to `blog-post-writer`, `linkedin-social-writer`, or `reddit-research` plus `reddit-social-writer`. If the create/report tool was missing or failed, include the skipped-report note and still provide the recommendation summary.
