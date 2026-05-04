---
name: fact-check
description: Verify unstable or external claims in drafts using local research tools or equivalent web access. Use when a draft contains dates, names, numbers, public-company facts, product claims, sourced statements, or references to recent events that should be checked before the draft is finalized.
---

# Fact Check

Verify the draft without turning it into a research memo.

## Read

- the active writer skill's workflow file
- the active writer skill's review-passes file
- the active writer skill's MCP or research-tools reference when available

## Workflow

1. List the unstable claims in the draft.
2. Use the local research tools first:
   - `web_search`
   - `fetch_page`
3. Narrow queries with `site:` when the likely source is known.
4. Remove or soften claims you cannot verify.

## Guardrails

- check facts, not style
- do not keep a punchy claim if the evidence is weak
- prefer primary sources when available
- if nothing unstable is present, say so briefly and stop

## Output

Return:

- the revised draft if any claims changed
- a short list of checked claims
- what still remains uncertain
