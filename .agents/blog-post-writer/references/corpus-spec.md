# Corpus Spec

## Path Resolution

Read `../../../.local/context/blog-publishing.local.md` for the active path values.

- Use `source_articles_dir` to load existing published articles for internal examples.
- Use `publish_output_dir` when writing a published blog post.
- Use the field names in `.local/context/blog-publishing.local.md` exactly as written.
- If the local file is missing, ask the user for the correct folders and create it before continuing.
- If either path is `[unset]` or missing on disk, ask the user for the correct folder and update the local file before continuing.
- Do not assume `content/blog/posts/`.

The read folder and write folder may be the same or different.

## Layout

Store one published article per file under the configured `publish_output_dir`.

Do not store unpublished drafts here. Store those in `content/blog/drafts/`.

## File Naming

Use:

```text
YYYY-MM-DD-NN--blog--short-slug.mdx
```

Example:

```text
2026-02-16-01--blog--product-roadmaps-vs-engineering-reality.mdx
```

`NN` is the follow-up number for that date.

## File Shape

Keep the published article in its native blog format.

Prefer this shape:

1. imports if needed
2. `export const metadata = { ... }`
3. article body in Markdown or MDX

## Required Metadata Fields

Keep these in every article's `metadata` export:

- `title`
- `date`
- `author`
- `excerpt`
- `coverImage`

## Recommended Metadata Fields

Add these whenever known:

- `tags`
- `readingTime`

## Body Conventions

- preserve the published article structure instead of normalizing it into a different archive format
- keep blockquote TL;DR sections when the article uses them
- keep the article prose-led by default; avoid bullet points and numbered lists unless the material truly requires them
- use `---` between major sections
- keep inline images, buttons, footnotes, and MDX components when they are part of the published piece
- include at least one inline image beyond the cover image
- follow `workflow.md` for inline-image count and placement on longer articles
- preserve links and citations that explain where claims came from
- keep `metadata.coverImage` as the stored `posts/...` asset path
- use and preserve `getImageUrl('posts/...')` for inline blog image URLs
- do not replace project image helpers with raw asset URLs unless the user explicitly asks
- do not store placeholder asset manifests, JSX comments, HTML comments, or editor-note blocks in published article files

## Notes

- store the actual article text, not a summary
- keep the corpus high-signal; fewer strong examples are better than many weak ones
- treat the corpus as the source of truth for tone and structure, not as a sentence bank or a reusable source bank
