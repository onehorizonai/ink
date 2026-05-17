# Channel Workspace

Generic channel work should stay profile-local by default. Resolve the active Ink profile before reading or writing private channel material.

Use this reference for channels and production surfaces that do not yet have a dedicated Ink workspace such as `content/linkedin`, `content/reddit`, or `content/blog`.

## Private Workspace

Private selected-profile channel work belongs under:

```text
.local/content/<profile-id>/channels/
```

Profiles may also define:

```json
{
  "contentRoots": {
    "channels": ".local/content/<profile-id>/channels"
  }
}
```

Use this root for private drafts, examples, corpora, assets, performance notes, and manual handoff bundles.

## Supported Model

Ink can help with any marketing channel or production surface by using:

- dedicated channel skills when they exist
- `channel-content-writer` for generic channel-native drafts and handoffs
- Content Program packs for repeatable formats and campaigns
- manual handoff bundles for external tools Ink cannot operate directly

Examples include Instagram, TikTok, Facebook, YouTube, X, newsletters, email sequences, Discord, forums, podcasts, webinars, ads, SMS, push notifications, in-app messages, app-store listings, marketplace listings, events, sales decks, one-pagers, and case studies.

## Local Layout Suggestion

```text
.local/content/<profile-id>/channels/
├── drafts/
├── published/
├── examples/
├── assets/
└── performance/
```

Use whichever subfolders match the selected profile's workflow. Do not commit private channel material unless it is intentionally made generic.

## Why This Is Not Under content/

The tracked `content/` folder currently holds legacy/default workspaces for channels with dedicated corpus formats. A tracked generic `content/channels/` folder would look like another writable corpus root, but generic channel work is too broad and usually private.

Keep public channel conventions in this reference and keep real channel work in the selected profile's local root.
