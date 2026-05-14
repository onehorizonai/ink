# Local Templates

Copy `ink-profiles.local.template.json` into `.local/context/` and rename it to `ink-profiles.local.json`.

Use:

```bash
mkdir -p .local/context
cp .local/templates/ink-profiles.local.template.json .local/context/ink-profiles.local.json
```

Replace every placeholder value with machine-local profile values.

Copy `blog-publishing.local.template.md` into `.local/context/` and rename it to `blog-publishing.local.md` for the legacy/default One Horizon profile.

Replace every placeholder value with machine-local blog path values.

Use:

```bash
mkdir -p .local/context
cp .local/templates/blog-publishing.local.template.md .local/context/blog-publishing.local.md
```

For other profiles, create the blog publishing file at the path set by that profile's `blogPublishingConfig`.

Create image provider and upload config files at each profile's `imageProviderConfig` and `imageUploadConfig` paths. Keep those files in ignored local locations such as `.secrets/<profile-id>/`.

Do not edit templates in place for live work. Copy them into `.local/context/` first.

Live author, company, and personal context belongs in author-scoped One Horizon context docs created by `one-horizon-context-setup` inside the selected profile workspace.
