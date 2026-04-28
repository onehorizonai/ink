# Planned Blocker Comment

Use only when `content-creation-runner` cannot draft without one or more user decisions. After posting this comment, set the source idea status to `In Review`.

Do not say `missing fields`. Say `pickup decisions`.

## Draft Handoff

Use this when the idea needs a human decision before drafting:

```md
Moving this to `In Review`: I need the draft handoff confirmed before writing.

**Confirm**

- **Thesis**: <proposed thesis, or `needs your wording`>
  The thesis is the claim the piece should make, not just the topic.
- **<Channel decision>**: <recommended option or short option list>

**Assuming unless you object**

- **Risks**: default check for weak proof, overclaiming, sensitive details, and promo framing.
- **Next workflow**: `<workflow inferred from channel>`

Reply with the confirmed pickup decisions, or edit the idea brief.
```

## Context Lookup

```md
Moving this to `In Review`: required One Horizon author context cannot be read.

**Fix lookup**

- `<exact doc title>`

Do not create a duplicate. Fix One Horizon lookup/access, then move this back to `Planned`.
```

## Channel Decisions

- Blog: use `Blog type`. Options: `opinion / argument`, `explainer`, `comparison`, `product / deep dive`, `personal essay / rant`, `journal / dispatch`, `reflective / inspirational`, `review`.
- Reddit: use `Subreddit or research need`. Options: `confirm a subreddit` or `run reddit-research first`.
- LinkedIn: omit this unless format or audience is genuinely unclear.

## Rules

- Include only blockers in `Confirm`.
- Human-action items belong in `In Review`, not `Planned`; use `update_feature_request` for reported ideas or `update_initiative` for initiative records.
- Do not invoke a writer until required author context is readable.
- `Risks` and `Next workflow` do not block; infer them when absent.
- If blog type is clear but not exact, normalize it. Example: `practical explainer with opinion backbone` becomes `explainer`; carry `opinion backbone` as an angle note.
- If the angle clearly implies a thesis, propose it and continue. Block only when the core argument would be invented.
