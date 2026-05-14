# Ink Initiative Hierarchy

Use this contract whenever an Ink skill creates, updates, or processes One Horizon initiatives for content work.

Resolve the active Ink profile first with `ink-profile-contract.md`. All initiative lookup, creation, updates, and hierarchy repair happen inside the selected profile's `workspaceId`. Do not use the One Horizon MCP default workspace silently.

## Parents

- `Ink` is the root initiative inside the selected profile workspace.
- `Ink - Blog` is the parent for Blog ideas, drafts, published articles, and blog publishing work.
- `Ink - LinkedIn` is the parent for LinkedIn ideas, drafts, and published posts.
- `Ink - Reddit` is the parent for Reddit ideas, drafts, and published posts.
- `Ink - Website Briefs` is the parent for website brief work.

## Required Behavior

- Resolve the selected profile workspace and required `Ink - ...` parent initiative before mutating channel work.
- When creating an initiative, pass the matching channel parent as `parentInitiativeId` and the selected profile's `workspaceId`.
- When processing an existing initiative, inspect its current parent. If it is missing or does not match the channel implied by the title or brief, move it before continuing.
- Use `update_initiative` for initiative hierarchy repair. Do not use comments, status updates, or description edits as a substitute for setting the parent.
- Set work to `In Review` whenever a human needs to look at it, confirm it, or answer a blocker. `Planned` and `In Progress` are automation-actionable states, not human waiting states.
- Do not attempt hierarchy repair for non-initiative records when the available One Horizon mutation tool does not expose parent metadata. Note the limitation and continue with the workflow-specific contract.

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
