# Corpus Spec

## Path Resolution

Resolve the active Ink profile, then read the selected profile's `blogPublishingConfig` for the active path values.

- Use `source_articles_dir` to load existing published articles for internal examples.
- Use `publish_output_dir` when writing a published blog post.
- Use the field names in the selected profile's blog publishing config exactly as written.
- If the local file is missing, ask the user for the correct folders and create it before continuing.
- If either path is `[unset]` or missing on disk, ask the user for the correct folder and update the local file before continuing.
- Do not assume `content/blog/posts/`.

The read folder and write folder may be the same or different.

## Layout

Store one published article per file under the configured `publish_output_dir`.

Do not store unpublished drafts here. Store those in the selected profile's `contentRoots.blogDrafts`.

## File Naming

Use:

```text
YYYY-MM-DD-short-slug.mdx
```

Example:

```text
2026-02-16-product-roadmaps-vs-engineering-reality.mdx
```

Do not add `NN--blog--` to published blog filenames.

Published blog dates must be unique inside the selected Ink profile's `publish_output_dir`. Before writing a published file, scan existing `.mdx` files for filename dates and `metadata.date` values, choose an unused date, and make the filename date match `metadata.date`.

Do not append `-2`, `-3`, etc. to work around published blog date collisions. Pick a different unused date instead, unless the user explicitly asks to move an existing post date.

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
