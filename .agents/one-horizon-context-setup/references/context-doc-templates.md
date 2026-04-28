# One Horizon Author Context Contract

Use this contract to resolve and shape Ink author context docs in One Horizon.

Rules:

- Resolve the author first with One Horizon MCP tools. If the user names an author, resolve that person with member/team lookup tools such as `find-team-member` when available. Otherwise use the authenticated/current One Horizon user from tools such as `list-my-teams` when available.
- If One Horizon cannot identify a single author, ask the user which author to use before loading or creating docs.
- Use author-scoped document names: `Ink Context - {Author Name} - {Doc Type}`.
- Use `find-documents` only to discover candidate document IDs, titles, statuses, types, and excerpts. Its `excerpt` is not the full document body.
- When a workflow needs the full content of an existing context doc, call `get-document` with the selected `documentId` before extracting fields or treating the doc as loaded.
- Keep task work separate: when a workflow needs full task context or content-document-backed task descriptions, use `get-task-details`.
- Do not use global author docs such as `Ink Context - Profile`.
- Create missing author docs from these templates only after explicit confirmation.
- Do not overwrite, patch, refresh, or otherwise change an existing author context doc. Existing author docs are read-only source material for writing workflows.
- Keep the headings and labels exactly as written.
- Replace `[replace-me]` only with confirmed values.
- Use `[unset]` for unknown required values.
- Do not write these templates to `.local/context/`.
- Use old `.local/context/*.md` files only as approved migration source material.

## Missing Required Docs

If a downstream Ink workflow requires an author-scoped context doc and that document is missing or unusable, run the `one-horizon-context-setup` skill to create the missing doc through its confirmation flow before continuing.

Do not substitute tracked repo files, README content, public web search, or local corpus examples for a required One Horizon context doc.

Optional docs are different: if a workflow says a doc is optional or only needed for a specific angle, skip that doc when it is missing unless the user asks to create it.

Doc types:

- `Profile`
- `Current Work`
- `Market Context`
- `Work History`
- `Personal Interests`
- `Personal Life`

Example for author `Jane Doe`:

- `Ink Context - Jane Doe - Profile`
- `Ink Context - Jane Doe - Current Work`
- `Ink Context - Jane Doe - Market Context`
- `Ink Context - Jane Doe - Work History`
- `Ink Context - Jane Doe - Personal Interests`
- `Ink Context - Jane Doe - Personal Life`

## Profile

```md
# Profile

- Name: [replace-me]
- Short excerpt: [one-paragraph public bio]
- Country: [replace-me]
- Timezone: [replace-me]
- Base location: [replace-me]
- Preferred public identifiers: [replace-me]
- Writing voice notes:
  - [tone cue]
  - [tone cue]
  - [tone cue]
```

## Current Work

```md
# Current Work

- Company or project: [replace-me]
- Role: [replace-me]
- What they are building now: [replace-me]
- Current positioning: [replace-me]
- Main audience: [replace-me]
- Key offers or products: [replace-me]
- Current themes worth posting about: [replace-me]
- Words or angles to avoid: [replace-me]
```

## Market Context

```md
# Market Context

Use this for product, positioning, competitive, integration, or partner-related writing.

## Competitors

- Main competitors to keep in mind: [replace-me]
- Positioning note: [replace-me]

## Integrations

- Source of truth for the current integration list: [replace-me or not used]
- Current ecosystem to keep in mind:
  - [replace-me]
- Writing guidance: [replace-me]

## Partners

- Current partners to keep in mind: [replace-me]
- Writing guidance: [replace-me]
```

## Work History

```md
# Work History

- Prior companies or projects:
  - [company or project]

- Notable career chapters:
  - [replace-me]

- Expertise areas: [replace-me]

- Credibility markers:
  - [replace-me]

- Past lessons or stories worth reusing:
  - [replace-me]

- Topics where historical context matters:
  - [replace-me]
```

## Personal Interests

```md
# Personal Interests

- Interests: [replace-me]
- Music: [replace-me]
- Sports: [replace-me]
- Books: [replace-me]
- Hobbies: [replace-me]
- Taste notes: [replace-me]
- Analogies or references that feel natural for this person: [replace-me]
```

## Personal Life

```md
# Personal Life

- Family notes: [replace-me]
- Pets: [replace-me]
- Home base details: [replace-me]
- Daily-life patterns: [replace-me]
- Personal themes they are comfortable posting about: [replace-me]
- Boundaries and things to avoid mentioning: [replace-me]
```
