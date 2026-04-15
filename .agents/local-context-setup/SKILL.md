---
name: local-context-setup
description: Set up or refresh this repo's `.local/context/` files from confirmed user answers, relevant public URLs, and a LinkedIn profile URL. Use when the user asks to set up Ink, configure local context, onboard a new author or team context, populate `.local/context/*.md`, refresh local context from public sources, or fix missing local context before using the writing workflows.
---

# Local Context Setup

Set up `.local/context/` without guessing.

This skill owns local context setup for Ink. Read the local contract, inspect any existing local files, ask for the right public URLs, gather the remaining missing facts in one grouped pass, show a confirmation summary, and write only after explicit approval.

## Read First

- `../../.local/README.md`
- `../../.local/templates/README.md`
- the matching files in `../../.local/context/` when they already exist
- the matching files in `../../.local/templates/` when a target file does not exist yet

Do not treat `.agents/context/`, `README.md`, `AGENTS.md`, `CLAUDE.md`, or other tracked repo files as live runtime context.

## Scope

This skill is for local context setup only.

Write only these files:

- `../../.local/context/profile.md`
- `../../.local/context/current-work.md`
- `../../.local/context/market-context.md`
- `../../.local/context/work-history.md`
- `../../.local/context/personal-interests.md`
- `../../.local/context/personal-life.md`

Do not create or update `../../.local/context/blog-publishing.local.md` here unless the user explicitly asks for that file.

## Hard Rules

- Ask for at least one relevant public URL.
- Prefer the company website as the primary public source when the user has one.
- Always ask for the exact LinkedIn profile URL.
- If the user gives more than one public URL, ask which one is primary.
- Ask whether existing local files may be overwritten before changing confirmed values.
- Do not overwrite existing values without explicit approval.
- Ask only for facts that are still missing, unclear, or conflicting.
- Keep questions short and concrete.
- Gather missing inputs in one grouped pass when possible.
- Never make assumptions.
- Do not infer facts from a domain name, logo, slogan, or generic marketing copy.
- Do not infer personal-life details unless the user explicitly confirms them.
- If the user wants a file created now but some fields are still unknown, leave those fields as `[unset]`.
- If an optional file has no confirmed content yet, skip creating it instead of inventing content.
- Do not write files until the user explicitly approves the confirmation summary.

## File Contract

Preserve the existing headings and bullet labels for each target file.

If a target file is missing, copy the matching template from `../../.local/templates/` into `../../.local/context/` and then replace placeholders with confirmed values.

Use these template labels as the default field list:

- `profile.md`
  `Name`, `Short excerpt`, `Country`, `Timezone`, `Base location`, `Preferred public identifiers`, `Writing voice notes`
- `current-work.md`
  `Company or project`, `Role`, `What they are building now`, `Current positioning`, `Main audience`, `Key offers or products`, `Current themes worth posting about`, `Words or angles to avoid`
- `market-context.md`
  `Main competitors to keep in mind`, `Positioning note`, `Source of truth for the current integration list`, `Current ecosystem to keep in mind`, `Writing guidance`, `Current partners to keep in mind`
- `work-history.md`
  `Prior companies or projects`, `Notable career chapters`, `Expertise areas`, `Credibility markers`, `Past lessons or stories worth reusing`, `Topics where historical context matters`
- `personal-interests.md`
  `Interests`, `Music`, `Sports`, `Books`, `Hobbies`, `Taste notes`, `Analogies or references that feel natural for this person`
- `personal-life.md`
  `Family notes`, `Pets`, `Home base details`, `Daily-life patterns`, `Personal themes they are comfortable posting about`, `Boundaries and things to avoid mentioning`

## Question Flow

Ask for missing inputs in this order.

### 1. Source and overwrite inputs

Always ask:

- the relevant public URLs to use
- which URL is primary if the user gives more than one
- the exact LinkedIn profile URL
- whether existing `.local/context/*.md` files may be overwritten if they already contain values

Prefer the company website as primary when one exists, but confirm that with the user.

If public access is blocked or the page content is not available, ask the user to paste the relevant public bio, about, company, or product text instead of inferring from memory.

### 2. File-selection inputs

Ask which local context files the user wants to set up now.

Default suggestion:

- `profile.md`
- `current-work.md`
- `market-context.md`
- `work-history.md`

Ask whether `personal-interests.md` and `personal-life.md` should also be created now or skipped.

### 3. Missing fact inputs

After reading the approved public sources plus any existing local files, ask only for the missing facts needed to complete the selected files.

Ask by file and by template label so the user can answer directly.

## Source Priority

Use this order:

1. explicit user answer
2. existing `.local/context/*.md` value
3. exact statement from the approved primary website
4. exact statement from the approved LinkedIn profile
5. exact statement from another approved public URL
6. `[unset]`

If sources disagree, ask the user which version is correct.

## Confirmation Flow

Before writing, present a structured confirmation summary grouped by target file.

For each proposed value, show:

- target file
- field label
- proposed value
- source: `user`, `existing local file`, `primary website`, `linkedin`, `other public URL`, or `unset`
- action: `create`, `keep`, `update`, or `skip`

Then ask for explicit approval.

Use direct wording such as:

- `I need your confirmation before I write these files.`
- `If any line is wrong, correct it now.`

Do not use soft wording such as `I can go ahead if this looks right`.

## Write Rules

After approval:

- write only the files covered by the confirmation summary
- preserve approved existing values the user did not change
- update existing values only when overwrite permission was given
- skip optional files the user chose not to create
- leave only still-unknown fields as `[unset]`
- keep the template headings and labels intact

## Output Shape

Unless the user asks differently, return:

- the missing inputs you still need, if any
- the grouped confirmation summary before writing
- after approval, the list of files created or updated
- any files that were skipped
- any fields left as `[unset]`
- any conflicts that required user correction

## Typical Triggers

- `Set up Ink`
- `Setup ink`
- `Configure local context for Ink`
- `Populate .local/context for this repo`
- `Refresh my local context from my website and LinkedIn`
