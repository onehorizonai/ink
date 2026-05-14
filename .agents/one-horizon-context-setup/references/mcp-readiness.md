# One Horizon MCP Recovery

Use this when an Ink workflow depends on One Horizon context docs, workspace documents, task writes, feature-request reports, or parent initiatives.

Resolve the selected Ink profile first with `ink-profile-contract.md`. A working One Horizon default workspace is not enough for Ink work when multiple profiles exist.

## Operating Contract

Use the intended One Horizon tool directly. Do not run an upfront MCP readiness check, inspect server status, list resources, or check visible skills/plugins before the real tool call.

Examples:

- Resolve the selected Ink profile and use its `workspaceId` when a read or write requires `workspaceId`.
- Resolve the author inside the selected profile workspace before loading or creating author-scoped context docs.
- Use `find-documents` only to discover document IDs, titles, statuses, types, and excerpts; call `get-document` before reading or extracting a full document body.
- Read or create the needed One Horizon document directly.
- Report or update the selected work item directly.

Visible server status, skill lists, plugin lists, resource listings, or integration lists are not a substitute for the actual tool call. They can be stale, unavailable, or unrelated to callable tools in the current assistant session.

Missing required resources are not soft failures. If the required One Horizon tool call works but the required document, context doc, or parent initiative is missing, follow the owning setup or creation flow for that resource instead of continuing with guessed context.

## If The Tool Call Works

Continue into the calling workflow. Do not mention setup or recovery.

## If The Tool Is Missing Or Fails

Use the smallest recovery path that matches the failure:

- If One Horizon auth is missing, expired, or the tool is not callable, stop and give the recovery message below.
- If the tool is callable and exact-title lookup confirms a required author context doc is missing, run `../SKILL.md` to create only the missing docs through the confirmation flow.
- If the required author context doc exists but cannot be read, do not create a duplicate. Stop the dependent workflow and ask the user to fix One Horizon document lookup or access for the exact title.
- If the tool is callable but a workflow-owned workspace document is missing, follow that workflow's creation contract before continuing.
- If the tool is callable but required IDs, profile fields, or workspace fields are missing, resolve them with One Horizon tools or ask the smallest targeted question. Do not guess IDs.
- If an optional One Horizon write fails after the core work is done, report the skipped write and continue any non-One-Horizon handoff that does not depend on that write.

Recovery message:

```text
One Horizon auth is required. Authenticate the One Horizon MCP server, then start a fresh assistant session.
```

Do not search tracked repo files, old local context files, README files, or skill docs as a substitute for live One Horizon context. The only exception is approved profile bootstrap source material listed in `ink-profile-contract.md`, and that source material still requires confirmation before creating One Horizon docs.
