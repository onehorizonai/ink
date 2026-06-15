# Content Programs

Content Programs are the repeatable marketing layer above individual channel workflows. They can target any marketing channel, format, or production surface, including social platforms, video, audio, email, communities, owned web, paid and partner channels, direct messages, product surfaces, events, and sales collateral.

Use a program when the work is more than a one-off post:

- a recurring series
- a time-boxed campaign
- a reusable visual format
- a cross-channel content motion
- a semi-manual workflow where Ink can standardize prompts, scripts, review, or tracking

One-off content can still use a dedicated channel skill or `channel-content-writer`. Do not force every draft into a program.

Reusable channel and format guidance lives under `.agents/channel-content-writer/references/`, with full slug coverage in `.agents/channel-content-writer/references/channel-format-registry.csv`. Content Programs should inherit that guidance, then add the repeatable campaign shape: audience, cadence, assets, approval flow, examples, calendar, and performance tracking. Do not create a program just to store shared channel rules such as cold outreach, Instagram Reels, deliverability, compliance, or platform-native copy guidance.

Resolve the active Ink profile before creating, updating, or running private programs so local packs, generic channel work, and One Horizon records stay scoped to the right workspace.

## Terms

- **Program**: strategic container with goal, audience, channels, cadence, assets, workflow, and measurement.
- **Format**: repeatable creative unit inside a program.
- **Run**: one execution of a format on a date or batch.
- **Campaign**: optional time-boxed program or phase.
- **Channel**: where the content goes.
- **Route**: which Ink skill, handoff, or manual step creates it.

## Tracked And Local Programs

Tracked starter packs live here and should be generic enough for open-source users.

Private user or company-specific packs belong under:

```text
.local/content-programs/<profile-id>/
```

Do not commit private brand assets, performance data, customer details, or live campaign context.

Before creating a new Content Program, ask the user whether it should be `local/private` or `public/tracked` as part of the open-source repo. Do not decide from defaults. Existing packs keep their current visibility unless the user asks to move them.

## Pack Layout

Every program pack uses this shape:

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

See `.agents/content-program-builder/references/program-pack-contract.md` for the full contract.

## Starter Packs

- `daily-recap-card`: recurring branded recap card plus caption and engagement comment.
- `meme-carousel`: recurring carousel made from multiple related meme slides.
- `channel-starter-formats`: generic starter formats for short video, newsletters, community posts, and YouTube outlines.
- `event-marketing-operating-system`: repeatable event marketing program for hosting, attending, promoting, following up, and measuring events.
- `hook-list-reel`: Instagram Reel with hook overlay video, keyword-rich list description, and exactly 5 bottom hashtags.

## Channels And Routes

Channels describe where content goes. Routes describe how Ink helps create it.

- Use `.agents/content-program-builder/references/channel-taxonomy.md` for canonical channel slugs.
- Use `.agents/channel-content-writer/references/channel-format-index.md` for reusable broad-channel and format guidance.
- Use `.agents/channel-content-writer/references/channel-format-registry.csv` to confirm the exact family guides, channel overrides, format playbooks, adapters, and manual boundary for a slug.
- Use dedicated skills when they exist, such as LinkedIn, Reddit, Blog, page brief, copywriting, image, and review skills.
- Use `channel-content-writer` for broad channels such as Instagram, TikTok, YouTube, X, Facebook, newsletters, email sequences, Discord, forums, podcasts, webinars, ads, SMS, push, in-app messages, listings, events, and sales assets.
- Use `manual-asset` or `manual-external-tool` routes when Ink can prepare prompts or handoff notes but cannot perform the external step.

## Validation

Run the pack validator after adding or changing a program:

```bash
python3 scripts/validate_program.py
```

Run the channel registry validator after adding or changing channel taxonomy, channel/format guidance, registry rows, or program channel slugs:

```bash
python3 scripts/validate_channel_registry.py
```

To validate one local pack:

```bash
python3 scripts/validate_program.py .local/content-programs/<profile-id>/<program-id>
```
