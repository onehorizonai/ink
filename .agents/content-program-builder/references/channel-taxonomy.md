# Channel Taxonomy

Use this taxonomy when a Content Program targets a marketing surface that does not already have a dedicated Ink writer skill.

Channels describe where the content is intended to go. Routes describe which Ink skill, handoff, or manual step creates it.

## Social

- `instagram`
- `tiktok`
- `facebook`
- `x`
- `threads`
- `bluesky`
- `mastodon`
- `pinterest`
- `linkedin`

## Video And Audio

- `youtube-long`
- `youtube-shorts`
- `instagram-reels`
- `tiktok-video`
- `podcast`
- `webinar`
- `livestream`

## Owned

- `blog`
- `website`
- `landing-page`
- `newsletter`
- `email-sequence`
- `lifecycle-email`
- `docs`
- `changelog`
- `help-center`

For email work, use `newsletter`, `email-sequence`, or `lifecycle-email` as the destination slug, then load the shared email channel and format guidance from `../../channel-content-writer/references/channel-format-index.md` and `../../channel-content-writer/references/channel-format-registry.csv`. Treat cold outreach as `Email -> Cold Outreach`, not as a standalone Content Program.

## Communities

- `reddit`
- `discord`
- `slack-community`
- `forum`
- `hacker-news`
- `product-hunt`
- `quora`

## Paid And Partner

- `paid-social`
- `paid-search`
- `influencer`
- `affiliate`
- `partner-marketing`
- `sponsorship`

## Direct And Product

- `sms`
- `whatsapp`
- `push-notification`
- `in-app-message`
- `app-store-listing`
- `marketplace-listing`

## Events

- `conference-talk`
- `conference-booth`
- `field-event`
- `hackathon`
- `meetup`
- `roundtable`
- `sponsored-event`
- `workshop`

## Sales

- `sales-deck`
- `one-pager`
- `case-study`

## Route Defaults

Use specialized Ink skills when the repo has one:

- `linkedin` -> `linkedin-social-writer`
- `reddit` -> `reddit-research` and `reddit-social-writer`
- `blog` -> `blog-post-writer`
- `website` or `landing-page` -> `page-brief-builder` or `copywriting`

Use `channel-content-writer` for channel-native drafting or handoff work on all other channels unless the program format requires only `manual-asset`, `manual-external-tool`, or `review-only`.

## Naming Rules

- Use lowercase slugs.
- Prefer a canonical slug from this file.
- If a new surface is needed, add the slug here before using it in `program.yaml`.
- Do not create a new skill just because a new platform appears. Use `channel-content-writer` unless the channel earns a dedicated workflow.
- Do not create a new Content Program just to hold reusable channel or format guidance. Put shared rules in `channel-content-writer` references, then let programs inherit them.
- Every slug in this file must have one row in `../../channel-content-writer/references/channel-format-registry.csv`.
