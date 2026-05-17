# Run Contract

## Run Identity

Use stable ids:

```text
<program-id>-YYYY-MM-DD
<program-id>-YYYY-MM-DD-02
```

When batching many runs, use the planned publish date when known. If dates are not known, use the creation date and a short theme slug.

## Run Folder

Use local run folders for private or unpublished artifacts:

```text
runs/YYYY-MM-DD--short-run-id/
```

Recommended files:

- `brief.md`
- `outputs.md`
- `asset-brief.md`
- `review-notes.md`
- `handoff.md`

Tracked starter packs should usually keep `runs/` empty except `.gitkeep`.

## Output Metadata

When a run creates or updates a channel draft, generic channel handoff, or specialized channel record, include optional metadata:

```yaml
program_id: daily-recap-card
format_id: caption
run_id: daily-recap-card-2026-01-05
campaign_id: launch-window
```

Omit `campaign_id` when there is no campaign.

## Calendar Updates

Append or update `calendar.csv` only when the user asks to persist scheduling or planning state.

Allowed statuses:

- `idea`
- `planned`
- `in_progress`
- `in_review`
- `scheduled`
- `published`
- `blocked`
- `example`

## Performance Updates

Only write metrics the user provides or that are fetched from an explicit accessible source. Leave unknown metric cells blank. Do not estimate metrics.

## Manual Handoff

For external tools, include:

- tool name
- prompt or input text
- settings or style guidance
- asset requirements
- rights or compliance notes
- expected output files
- next Ink step after the manual step

## Generic Channel Outputs

For channels without a dedicated writer skill, use `channel-content-writer` and include:

- channel slug
- format id
- destination constraints
- draft, script, outline, or asset brief
- manual external-tool steps
- review and compliance notes
