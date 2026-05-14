---
name: one-horizon-context-setup
description: Set up Ink's author-scoped context docs in One Horizon. Use when the user asks to set up Ink, configure context, onboard a new author, populate missing One Horizon author context docs, or fix missing context before using the writing workflows. Requires a connected One Horizon MCP server. Does not overwrite or refresh existing author context docs.
---

# One Horizon Context Setup

Set up Ink's author-scoped context docs and parent initiatives in One Horizon without guessing.

This skill owns context setup for Ink. Resolve the Ink profile first, then use One Horizon tools to resolve the selected profile workspace and author, inspect existing author context docs and initiatives, offer to use old `.local/context/` files as migration source after confirmation, gather missing facts in one grouped pass, show a confirmation summary, and create missing docs only after explicit approval.

## Read First

- `../../.local/README.md` — for the profile registry and blog-publishing path contracts
- `references/mcp-readiness.md` — for One Horizon tool-call recovery when a required MCP call is missing or fails
- `references/ink-profile-contract.md` — for selecting the active Ink profile, workspace, author, local corpus roots, and bootstrap source safety
- `references/context-doc-templates.md` — for author resolution, document naming, and the canonical body shape of each One Horizon context doc
- `references/ink-initiative-hierarchy.md` — for the required Ink parent initiative tree and child-placement contract
- Check whether the author's One Horizon context docs already exist before gathering new inputs

Do not treat `.agents/context/`, `README.md`, `AGENTS.md`, `CLAUDE.md`, or other tracked repo files as live runtime context.

## Scope

This skill creates missing author-scoped One Horizon context docs in the selected Ink profile workspace. It does not update existing author context docs.

Doc name pattern:

- `Ink Context - {Author Name} - Profile`
- `Ink Context - {Author Name} - Current Work`
- `Ink Context - {Author Name} - Market Context`
- `Ink Context - {Author Name} - Work History`
- `Ink Context - {Author Name} - Personal Interests`
- `Ink Context - {Author Name} - Personal Life`

And the following parent initiatives if they are missing:

- `Ink` (root)
  - `Ink - LinkedIn`
  - `Ink - Reddit`
  - `Ink - Blog`
  - `Ink - Website Briefs`

This skill does not create or update profile blog publishing path files unless the user explicitly asks.

## Hard Rules

- Use the intended One Horizon tool directly. Use `references/mcp-readiness.md` only when a required One Horizon tool is missing or a call fails.
- Ask for at least one relevant public URL.
- Prefer the company website as the primary public source when the user has one.
- Always ask for the exact LinkedIn profile URL.
- If the user gives more than one public URL, ask which one is primary.
- Resolve the author with One Horizon MCP tools before choosing doc names.
- Do not overwrite, patch, refresh, or otherwise change existing author context docs.
- If an author context doc already exists, treat it as read-only and skip it.
- Ask only for facts that are still missing, unclear, or conflicting.
- Keep questions short and concrete.
- Gather missing inputs in one grouped pass when possible.
- Never make assumptions.
- Do not infer facts from a domain name, logo, slogan, or generic marketing copy.
- Do not infer personal-life details unless the user explicitly confirms them.
- If the user wants a doc created now but some fields are still unknown, leave those fields as `[unset]`.
- If an optional doc has no confirmed content yet, skip creating it instead of inventing content.
- Do not write docs or initiatives until the user explicitly approves the confirmation summary.

## MCP Use and Recovery

Before doing anything else:

1. Read `references/mcp-readiness.md`.
2. Resolve the active Ink profile using `references/ink-profile-contract.md`. If multiple profiles are configured and none is named in the prompt or `INK_PROFILE`, ask which profile to use before continuing.
3. Use the selected profile's `workspaceId`. Do not silently use the One Horizon MCP default workspace.
4. Resolve the author inside the selected profile workspace:
   - If the user named an author, use One Horizon member/team tools to find that person.
   - If the selected profile has `authorUserId`, use that identity after confirming it exists in the workspace.
   - Otherwise use `authorName` from the selected profile when available.
   - Otherwise use the authenticated/current One Horizon person when the MCP exposes it.
   - If the current person cannot be determined, ask which author these context docs are for before continuing.
5. If a required One Horizon tool is missing or a tool call fails, follow `references/mcp-readiness.md`.
6. Derive doc names with `Ink Context - {Author Name} - {Doc Type}` inside the selected workspace. Do not use unscoped global doc names or docs from another workspace.

## Migration from Old Local Files

If `.local/context/profile.md`, `.local/context/current-work.md`, or other context files exist locally, offer to use them as source material for creating missing docs for the resolved author.

Rules:
- Ask for explicit permission before reading any old local file.
- Treat old local files as a source, not as authoritative values. Show the user what was found and ask for confirmation.
- Do not delete or modify old local files. That is outside this skill's scope.
- Do not use old local files to change existing author docs.

## Doc Content Contract

Use `references/context-doc-templates.md` as the canonical content template for each context doc. Keep headings and labels intact so downstream writer skills can scan predictable sections.

Field groups:

- `Ink Context - {Author Name} - Profile`
  `Name`, `Short excerpt`, `Country`, `Timezone`, `Base location`, `Preferred public identifiers`, `Writing voice notes`

- `Ink Context - {Author Name} - Current Work`
  `Company or project`, `Role`, `What they are building now`, `Current positioning`, `Main audience`, `Key offers or products`, `Current themes worth posting about`, `Words or angles to avoid`

- `Ink Context - {Author Name} - Market Context`
  `Main competitors to keep in mind`, `Positioning note`, `Source of truth for the current integration list`, `Current ecosystem to keep in mind`, `Writing guidance`, `Current partners to keep in mind`

- `Ink Context - {Author Name} - Work History`
  `Prior companies or projects`, `Notable career chapters`, `Expertise areas`, `Credibility markers`, `Past lessons or stories worth reusing`, `Topics where historical context matters`

- `Ink Context - {Author Name} - Personal Interests`
  `Interests`, `Music`, `Sports`, `Books`, `Hobbies`, `Taste notes`, `Analogies or references that feel natural for this person`

- `Ink Context - {Author Name} - Personal Life`
  `Family notes`, `Pets`, `Home base details`, `Daily-life patterns`, `Personal themes they are comfortable posting about`, `Boundaries and things to avoid mentioning`

## Question Flow

Ask for missing inputs in this order.

### 1. Source and overwrite inputs

Always ask:

- the relevant public URLs to use
- which URL is primary if the user gives more than one
- the exact LinkedIn profile URL
- the author if the One Horizon MCP cannot determine the current person

Prefer the selected profile's `website` as primary when it exists, but confirm that with the user.

For profile setup from a source repo, use only the safe source paths listed in `references/ink-profile-contract.md` from the selected profile's `sourceRepo` after the user confirms the setup summary. Do not read `.env*`, secrets, dependency folders, build output, or private runtime state.

If public access is blocked or the page content is not available, ask the user to paste the relevant public bio, about, company, or product text instead of inferring from memory.

### 2. Doc selection

Ask which missing context docs the user wants to create now.

Default suggestion:

- `Ink Context - {Author Name} - Profile`
- `Ink Context - {Author Name} - Current Work`
- `Ink Context - {Author Name} - Market Context`
- `Ink Context - {Author Name} - Work History`

Ask whether `Ink Context - {Author Name} - Personal Interests` and `Ink Context - {Author Name} - Personal Life` should also be created now or skipped.

### 3. Missing fact inputs

After reading the approved public sources plus any approved old local files, ask only for the missing facts needed to create the selected missing docs. Existing author docs are not edited.

Ask by doc name and by field label so the user can answer directly.

## Source Priority

Use this order:

1. explicit user answer
2. approved old `.local/context/` value
3. exact statement from the approved primary website
4. exact statement from the approved LinkedIn profile
5. exact statement from another approved public URL
6. `[unset]`

If sources disagree, ask the user which version is correct.

## Confirmation Flow

Before writing, present a structured confirmation summary grouped by target doc.

For each proposed value, show:

- target doc name
- field label
- proposed value
- source: `user`, `old local file`, `primary website`, `linkedin`, `other public URL`, or `unset`
- action: `create` or `skip`

Then ask for explicit approval.

Use direct wording such as:

- `I need your confirmation before I write these docs.`
- `If any line is wrong, correct it now.`

Do not use soft wording such as `I can go ahead if this looks right`.

## Initiative Check

After context docs are confirmed, check whether the required parent initiatives exist in the selected profile workspace:

- `Ink`
- `Ink - LinkedIn`
- `Ink - Reddit`
- `Ink - Blog`
- `Ink - Website Briefs`

If any are missing, show a list and ask for confirmation before creating them.

Create `Ink` first as the root, then create child initiatives under it.

Use `references/ink-initiative-hierarchy.md` as the source of truth for the parent tree. If an existing `Ink - ...` parent initiative is not under the root `Ink` initiative, move it with `update_initiative` after the user approves initiative setup.

## Write Rules

After approval:

- create only the missing docs covered by the confirmation summary
- skip existing author docs without editing them
- skip optional docs the user chose not to create
- leave only still-unknown fields as `[unset]`
- keep the template headings, field groups, and labels intact

For each approved missing author context doc, use the One Horizon document creation tool with this shape:

```json
create_document({
  "title": "Ink Context - {Author Name} - Current Work",
  "type": "Requirement",
  "status": "Completed",
  "content": "# Current Work\n\n- Company or project: ...",
  "workspaceId": "<workspaceId>"
})
```

Do not use document patch or update tools to create missing context docs. Existing author context docs are read-only in this skill.

For initiatives: create missing ones only after the user explicitly approves.

## Output Shape

Unless the user asks differently, return:

- the missing inputs you still need, if any
- the grouped confirmation summary before writing
- after approval, the list of docs created
- any docs that were skipped
- any fields left as `[unset]`
- any existing docs that were left unchanged
- any conflicts that required user correction
- the initiative status: which exist and which were created

## Typical Triggers

- `Set up Ink`
- `Setup ink`
- `Configure context for Ink`
- `Create missing context docs from my website and LinkedIn`
- `Set up my One Horizon context`
- `Populate the Ink context docs`
