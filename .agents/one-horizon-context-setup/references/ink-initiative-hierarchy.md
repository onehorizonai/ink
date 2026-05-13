# Ink Initiative Hierarchy

Use this contract whenever an Ink skill creates, updates, or processes One Horizon initiatives for content work.

## Parents

- `Ink` is the root initiative.
- `Ink - Blog` is the parent for Blog post initiatives throughout idea, draft, review, and publishing work.
- `Ink - LinkedIn` is the parent for LinkedIn ideas, drafts, and published posts.
- `Ink - Reddit` is the parent for Reddit ideas, drafts, and published posts.
- `Ink - Website Briefs` is the parent for website brief work.

## Required Behavior

- Resolve the workspace and required `Ink - ...` parent initiative before mutating channel work.
- When creating an initiative, pass the matching channel parent as `parentInitiativeId`.
- When processing an existing initiative, inspect its current parent. If it is missing or does not match the channel implied by the title or brief, move it before continuing.
- Use `update_initiative` for initiative hierarchy repair. Do not use comments, status updates, or description edits as a substitute for setting the parent.
- Follow the Blog Lifecycle Contract below for Blog work.
- Set work to `In Review` whenever a human needs to look at it, confirm it, or answer a blocker. `Planned` and `In Progress` are automation-actionable states, not human waiting states.
- Do not attempt hierarchy repair for non-initiative records when the available One Horizon mutation tool does not expose parent metadata. Note the limitation and continue with the workflow-specific contract.

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
