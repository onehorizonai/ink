---
name: content-tone-review
description: Review a draft against the saved corpus and One Horizon context docs to catch tone drift, stance drift, and the wrong level of personal detail. Use when Codex needs to compare a content draft such as a LinkedIn post or blog article to the author's actual voice near the end of the editing loop or wherever the active writer workflow places tone review before finalization.
---

# Content Tone Review

Review whether the draft sounds like the author, not just like good generic copy. Follow the active writer workflow for the exact place of this pass in the sequence.

## Read

- the active writer skill's workflow file
- the active writer skill's review-passes file
- the active writer skill's style-capture file if one exists
- `../social-common/references/repetition-guard.md`

Then resolve the author with One Horizon MCP and load only the relevant author-scoped One Horizon context docs plus 3-5 matching corpus examples. Use `../one-horizon-context-setup/references/context-doc-templates.md` for the naming contract.
Use `find-documents` only to locate candidate context docs by ID, title, status, type, or excerpt. Call `get-document` for the selected `documentId` before extracting fields or treating a context doc as loaded.

Use One Horizon context docs for live runtime context.
Do not infer live context from tracked repo files.

## Check

- opening energy
- sentence rhythm
- level of specificity
- section density
- CTA pressure
- amount of personal detail
- whether the draft sounds too polished, too safe, or too salesy
- for blog articles, whether the draft feels sharp and reportorial enough
- whether list-heavy formatting flattens the voice or makes the piece feel like a deck
- whether the draft overfits one corpus example or repeats recent author phrasing too closely

## Guardrails

- prefer the corpus over generic best practices
- do not inject personal details that were not loaded on purpose
- when the active writer is the blog workflow, bias toward a Verge-adjacent editorial edge without copying any outlet's phrasing
- do not turn a sharp draft into neutral corporate copy
- do not overcorrect into blandness
- do not treat repeated phrasing as voice when the corpus shows it is just a recent habit

## Output

Return:

- the revised draft or precise tone notes
- the main tone mismatches you fixed
- any corpus mimicry or repeated voice pattern you corrected
