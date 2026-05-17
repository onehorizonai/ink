# Program Pack Contract

## Terms

- **Program**: strategic container with goal, audience, channels, routes, cadence, assets, workflow, and measurement.
- **Format**: repeatable creative unit inside a program.
- **Run**: one execution of a format on a date or batch.
- **Campaign**: optional time-boxed program or phase.
- **Channel**: where the content goes.
- **Route**: which Ink skill, handoff, or manual step creates it.

## Roots

Tracked generic packs:

```text
content-programs/<program-id>/
```

Private selected-profile packs:

```text
.local/content-programs/<profile-id>/<program-id>/
```

If a selected profile defines `contentProgramRoots`, use those roots instead. Tracked roots must remain safe for open-source users.

## Required Layout

```text
program-id/
├── README.md
├── program.yaml
├── workflow.md
├── formats/
├── prompts/
├── assets/
├── examples/
├── calendar.csv
├── performance.csv
└── runs/
```

## README.md

Include:

- program purpose
- goal and audience
- channels
- routes and automation boundary
- format summary
- workflow diagram when useful
- links to relevant repo skills or references
- notes about what is automated versus manual

Use Mermaid for workflows when it improves clarity.

## program.yaml

Required top-level fields:

```yaml
id: program-id
name: Program Name
status: starter
visibility: tracked
summary: One sentence summary.
goals:
  - brand awareness
channels:
  - newsletter
cadence:
  type: recurring
  recommendation: weekly
  batch_size: 1
formats:
  - id: format-id
    output: social-caption
    route: generic-channel-draft
routes:
  - id: generic-channel-draft
    uses: channel-content-writer
    when: draft channel-native content or handoff assets
kpis:
  - reach
```

Recommended fields:

```yaml
audiences:
  - software teams
campaigns:
  - id: launch-window
    starts: 2026-01-01
    ends: 2026-01-31
required_context:
  - Ink Context - <Author Name> - Current Work
one_horizon:
  parent: Ink - Programs
  program_title: "[Ink Program] Program Name"
  run_title: "[Ink Program Run] Program Name - <date>"
```

Channels should use canonical slugs from `channel-taxonomy.md` when possible.

Route `uses` values:

- `content-idea-finder`
- `content-creation-runner`
- `channel-content-writer`
- `linkedin-social-writer`
- `reddit-research`
- `reddit-social-writer`
- `blog-post-writer`
- `page-brief-builder`
- `copywriting`
- `blog-image-finder`
- `blog-image-uploader`
- `content-program-runner`
- `manual-asset`
- `manual-external-tool`
- `review-only`

`channels` describe the destination. `routes` describe the production path. `formats[].route` should reference a route id, not a channel name.

## calendar.csv

Required columns:

```csv
planned_date,run_id,format_id,channel,status,campaign_id,theme,asset_brief,copy_brief,one_horizon_url,publish_url,notes
```

Use `status` values such as `idea`, `planned`, `in_progress`, `in_review`, `scheduled`, `published`, `blocked`, or `example`.

## performance.csv

Required columns:

```csv
published_date,run_id,format_id,channel,publish_url,impressions,reach,engagements,likes,comments,shares,saves,clicks,followers_delta,notes
```

Leave metric cells blank when unknown. Do not invent performance.

## runs/

Use `runs/YYYY-MM-DD--short-run-id/` for run artifacts when a program execution produces local files.

Recommended files:

- `brief.md`
- `outputs.md`
- `asset-brief.md`
- `review-notes.md`
- `handoff.md`

Keep unpublished or private run artifacts local unless the user explicitly wants a public-safe example.

## Optional Metadata For Channel Work

Existing channel records may include these optional fields:

- `program_id`
- `format_id`
- `run_id`
- `campaign_id`

Workflows must remain valid when these fields are missing.
