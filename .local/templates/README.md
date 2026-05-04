# Local Blog Path Template

Copy `blog-publishing.local.template.md` into `.local/context/` and rename it to `blog-publishing.local.md`.

Replace every placeholder value with machine-local blog path values.

Use:

```bash
mkdir -p .local/context
cp .local/templates/blog-publishing.local.template.md .local/context/blog-publishing.local.md
```

Do not edit the template in place for live work. Copy it into `.local/context/` first.

Live author, company, and personal context belongs in author-scoped One Horizon context docs created by `one-horizon-context-setup`.
