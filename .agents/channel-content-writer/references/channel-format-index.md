# Channel And Format Index

Use this index whenever `channel-content-writer`, `content-idea-finder`, or a Content Program runner touches a broad marketing surface.

The machine-readable registry is `channel-format-registry.csv`. It must contain every canonical slug from `.agents/content-program-builder/references/channel-taxonomy.md`.

## Inheritance Contract

Load guidance in this order:

1. Global writer rules from `.agents/channel-content-writer/SKILL.md`.
2. Canonical slug from `.agents/content-program-builder/references/channel-taxonomy.md`.
3. Registry row from `.agents/channel-content-writer/references/channel-format-registry.csv`.
4. Family guide or guides from `.agents/channel-content-writer/references/channels/`.
5. Specific channel guide when the registry row has one.
6. Format playbook or dedicated adapter playbook.
7. Optional Content Program constraints.

Content Programs consume this stack. They should add audience, cadence, campaign, assets, approval flow, examples, calendar, and KPIs. They should not become the source of truth for reusable channel behavior, compliance, deliverability, social SEO, platform norms, or copy psychology.

## Registry Fields

- `slug`: canonical destination from `channel-taxonomy.md`.
- `route`: `dedicated-skill`, `generic-channel-writer`, or `manual-handoff`.
- `family_guides`: shared channel-family references.
- `channel_guides`: optional destination-specific overrides.
- `format_guides`: reusable format playbooks or dedicated adapter playbooks.
- `adapter_paths`: dedicated Ink skills when the slug is handled outside the generic writer.
- `manual_boundary`: what Ink prepares versus what remains manual.

Run `python3 scripts/validate_channel_registry.py` after changing taxonomy, registry rows, channel guides, format guides, or Content Program channels.

## Coverage Summary

Dedicated adapters:

- `linkedin` -> `linkedin-social-writer`
- `reddit` -> `reddit-research` and `reddit-social-writer`
- `blog` -> `blog-post-writer`
- `website`, `landing-page` -> `page-brief-builder` and `copywriting`

Generic social:

- `instagram`, `facebook`, `x`, `threads`, `bluesky`, `mastodon`, `pinterest`
- family guide: `channels/social.md`
- common formats: `social-post.md`, `carousel.md`

Generic video and audio:

- `youtube-long`, `youtube-shorts`, `instagram-reels`, `tiktok-video`, `tiktok`, `podcast`, `webinar`, `livestream`
- family guide: `channels/video-audio.md`
- common formats: `short-video.md`, `long-video-outline.md`, `podcast-episode.md`, `livestream-webinar.md`
- channel overrides: `youtube.md`, `tiktok.md`, `instagram.md`

Owned and email:

- `newsletter`, `email-sequence`, `lifecycle-email`, `docs`, `changelog`, `help-center`
- family guide: `channels/owned-email.md`
- common formats: `newsletter-issue.md`, `email-sequence.md`, `email-cold-outreach.md`, `lifecycle-email.md`, `docs-changelog-help-center.md`
- channel override: `email.md`

Communities:

- `discord`, `slack-community`, `forum`, `hacker-news`, `product-hunt`, `quora`
- family guide: `channels/communities.md`
- common formats: `community-post.md`, `forum-qa-post.md`
- channel override: `product-hunt.md`

Paid and partner:

- `paid-social`, `paid-search`, `influencer`, `affiliate`, `partner-marketing`, `sponsorship`
- family guide: `channels/paid-partner.md`
- common formats: `paid-ad.md`, `partner-influencer-brief.md`

Direct and product:

- `sms`, `whatsapp`, `push-notification`, `in-app-message`, `app-store-listing`, `marketplace-listing`
- family guide: `channels/direct-product.md`
- common formats: `sms-whatsapp.md`, `push-notification.md`, `in-app-message.md`, `app-store-marketplace-listing.md`
- channel override: `app-store-marketplace.md`

Events and sales:

- `conference-talk`, `conference-booth`, `field-event`, `hackathon`, `meetup`, `roundtable`, `sponsored-event`, `workshop`
- `sales-deck`, `one-pager`, `case-study`
- family guide: `channels/events-sales.md`
- common event formats: `event-hosting.md`, `event-attendance.md`, `event-promotion-follow-up.md`, `event-talk-workshop.md`, `conference-booth.md`, `hackathon.md`, `meetup-roundtable.md`, `livestream-webinar.md`
- common sales formats: `sales-deck.md`, `one-pager.md`, `case-study.md`

## Intent Aliases

Use these mappings when the user describes a format instead of naming a slug:

- Cold email, cold outreach, outbound sales email, or partner outreach -> `email-sequence` plus `formats/email-cold-outreach.md`.
- Newsletter, digest, or editorial send -> `newsletter` plus `formats/newsletter-issue.md`.
- Onboarding, activation, retention, winback, or product-triggered email -> `lifecycle-email` plus `formats/lifecycle-email.md`.
- Reel, TikTok, Shorts, vertical video, or hook video -> the matching video slug plus `formats/short-video.md`; for Reels also load `formats/instagram-reels.md`.
- Community launch, discussion prompt, or Discord/Slack post -> community slug plus `formats/community-post.md`.
- Q&A answer, forum answer, Hacker News post, or Quora answer -> community slug plus `formats/forum-qa-post.md`.
- Ad creative, paid search, or paid social -> paid slug plus `formats/paid-ad.md`.
- Influencer, affiliate, partner, or sponsorship brief -> partner slug plus `formats/partner-influencer-brief.md`.
- SMS or WhatsApp -> direct slug plus `formats/sms-whatsapp.md`.
- Push or in-app -> direct/product slug plus the matching product-message format.
- App store, marketplace, integration listing, or plugin listing -> listing slug plus `formats/app-store-marketplace-listing.md`.
- Hosting a meetup, community event, user group, field event, customer event, breakfast, dinner, drinks, roundtable, or local partner event -> matching event slug plus `formats/event-hosting.md`, `formats/event-promotion-follow-up.md`, and any specific event-type format.
- Attending, sponsoring, exhibiting, tabling, speaking at, or networking around an external event -> `conference-booth`, `conference-talk`, or `sponsored-event` plus `formats/event-attendance.md` and the matching format guide.
- Webinar, livestream, virtual demo, office hours, or online event -> `webinar` or `livestream` plus `formats/livestream-webinar.md` and event promotion/follow-up guidance.
- Hackathon -> `hackathon` plus `formats/hackathon.md`.
- Talk, workshop, deck, one-pager, or case study -> event/sales slug plus the matching enablement format.

## Extension Rules

When adding a new channel or format:

- Add the canonical slug to `channel-taxonomy.md` only if no existing slug fits.
- Add or update a registry row in `channel-format-registry.csv`.
- Reuse a family guide and format guide before creating a new specific guide.
- Create a new channel guide only when platform behavior materially changes the output.
- Create a new format guide when the output shape is reusable across programs.
- Run `python3 scripts/validate_channel_registry.py`.
