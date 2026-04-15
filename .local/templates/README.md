# Local Context Templates

Copy the templates in this directory into `.local/context/` and rename them without the `.template` suffix.

Replace every placeholder value with your own local context.

Use:

```bash
mkdir -p .local/context

for src in .local/templates/*.template.md; do
  name="$(basename "$src" .template.md)"
  cp "$src" ".local/context/$name.md"
done
```

Do not edit the templates in place for live work. Copy them into `.local/context/` first.
