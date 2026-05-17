# Ink Initiative Hierarchy

Use this contract whenever an Ink skill creates, updates, or processes One Horizon initiatives for content work.

Resolve the active Ink profile first with `ink-profile-contract.md`. All initiative lookup, creation, updates, and hierarchy repair happen inside the selected profile's `workspaceId`. Do not use the One Horizon MCP default workspace silently.

## Parents

- `Ink` is the root initiative inside the selected profile workspace.
- `Ink - Blog` is the parent for Blog post initiatives throughout idea, draft, review, publishing, and published article tracking.
- `Ink - LinkedIn` is the parent for LinkedIn ideas, drafts, and published posts.
- `Ink - Reddit` is the parent for Reddit ideas, drafts, and published posts.
- `Ink - Website Briefs` is the parent for website brief work.
- `Ink - Programs` is the optional parent for Content Program definitions and manual or semi-manual program runs.
- `Ink - Channel Content` is the optional parent for generic channel drafts, handoffs, and published records when a channel does not have a dedicated Ink parent yet.

## Required Behavior

- Resolve the selected profile workspace and required `Ink - ...` parent initiative before mutating channel work.
- When creating an initiative, pass the matching channel parent as `parentInitiativeId` and the selected profile's `workspaceId`.
- When processing an existing initiative, inspect its current parent. If it is missing or does not match the channel implied by the title or brief, move it before continuing.
- Use `update_initiative` for initiative hierarchy repair. Do not use comments, status updates, or description edits as a substitute for setting the parent.
- Follow the Blog Lifecycle Contract below for Blog work.
- Set work to `In Review` whenever a human needs to look at it, confirm it, or answer a blocker. `Planned` and `In Progress` are automation-actionable states, not human waiting states.
- Do not attempt hierarchy repair for non-initiative records when the available One Horizon mutation tool does not expose parent metadata. Note the limitation and continue with the workflow-specific contract.

## Content Program Contract

Content Programs are optional. They organize repeatable marketing series, campaigns, formats, calendars, and performance tracking across any marketing channel, format, or production surface without changing the existing dedicated channel parents.

- Store program definitions as `[Ink Program] <name>` initiatives under `Ink - Programs`.
- Store manual or semi-manual run work as `[Ink Program Run] <program> - <date/title>` initiatives under `Ink - Programs`.
- Keep dedicated channel outputs under `Ink - Blog`, `Ink - LinkedIn`, `Ink - Reddit`, or `Ink - Website Briefs`.
- Keep generic non-specialized outputs under `Ink - Channel Content` when One Horizon tracking is needed and no dedicated parent exists.
- Link channel outputs back to the program through optional metadata: `program_id`, `format_id`, `run_id`, and `campaign_id`.
- If `Ink - Programs` or `Ink - Channel Content` does not exist, program or generic channel skills may ask before creating it. Existing dedicated channel workflows do not require either optional parent.

## Blog Lifecycle Contract

Blog posts use one mutable initiative under `Ink - Blog` from idea through PR review.

- Create a Blog idea with `create_initiative`, title `[Ink Idea] [Blog] <title>`, status `In Review`, and `parentInitiativeId` set to `Ink - Blog`.
- When approved for drafting, a human moves the initiative to `Planned`.
- When drafted, update the same initiative to title `[Ink Draft] [Blog] <title>` and status `In Review`; do not create a draft child initiative.
- During publish prep, keep the same `[Ink Draft] [Blog]` initiative, rebuild the article, comment with the PR or blocker, and leave it `In Review` or `Blocked`.
- Mark the Blog initiative `Completed` only after the user explicitly confirms the article is published.

Keep the linked content document parseable with these sections:

```md
## Source Idea
<original Content Idea Brief, preserved>

## Draft
<current draft or publish-ready body>

## Review Notes
<confirmed type, review ledger, image/source notes, PR notes, and assumptions>

## Automation
Ink automation checkpoint: <runner> <ISO timestamp>
```

Use `## Draft` as the canonical boundary for revision and publishing handoffs.

## Tool Shapes

Create new channel work as a child initiative:

```json
create_initiative({
  "title": "[Ink Draft] [LinkedIn] Example title",
  "description": "<draft or record body>",
  "status": "In Review",
  "parentInitiativeId": "<Ink - LinkedIn initiative taskId>",
  "workspaceId": "<workspaceId>"
})
```

Move an existing initiative to the correct parent:

```json
update_initiative({
  "initiativeId": "<existing initiative taskId>",
  "parentInitiativeId": "<matching Ink - Channel initiative taskId>",
  "workspaceId": "<workspaceId>"
})
```

## Channel Mapping

- Titles starting `[Ink Idea] [Blog]`, `[Ink Draft] [Blog]`, or blog article records go under `Ink - Blog`.
- Titles starting `[Ink Idea] [LinkedIn]`, `[Ink Draft] [LinkedIn]`, or LinkedIn published-post records go under `Ink - LinkedIn`.
- Titles starting `[Ink Idea] [Reddit]`, `[Ink Draft] [Reddit]`, or Reddit published-post records go under `Ink - Reddit`.
- Website page brief records go under `Ink - Website Briefs`.
- Titles starting `[Ink Program]` or `[Ink Program Run]` go under `Ink - Programs`.
- Generic channel titles such as `[Ink Idea] [Instagram]`, `[Ink Draft] [TikTok]`, `[Ink Draft] [Newsletter]`, `[Ink Draft] [YouTube Shorts]`, `[Ink Published] [X]`, or `[Ink Channel] ...` go under `Ink - Channel Content` unless a dedicated parent exists.
- Do not create one parent initiative per platform by default. Add a dedicated parent only when the repo gains a dedicated workflow that needs its own lifecycle contract.
