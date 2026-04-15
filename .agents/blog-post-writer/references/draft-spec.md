# Draft Spec

## Purpose

Use `content/blog/drafts/` for unpublished article drafts only.

Do not place unpublished drafts in the published corpus.

## Layout

Store drafts under:

- `content/blog/drafts/`

## File Naming

Use:

```text
YYYY-MM-DD-NN--draft--blog--short-slug.mdx
```

`NN` is the follow-up number for that date.

## Working Shape

Keep drafts close to the publishable article format.

Prefer:

1. imports only when needed
2. `export const metadata = { ... }` with working values
3. the article body

In the article body:

- separate major sections with `---`
- default to paragraphs instead of bullet points or numbered lists unless the brief clearly requires a list

Image URL contract:

- keep `metadata.coverImage` as a plain `posts/...` path such as `posts/my-image-name.jpg`
- use `getImageUrl('posts/my-image-name.jpg')` for inline blog image URLs
- do not replace inline image URLs with raw CDN URLs
- do not inspect or explain the implementation of `getImageUrl()` unless the user explicitly asks

Do not include:

- JSX comments such as `{/* ... */}`
- HTML comments
- placeholder asset manifests
- TODO or editor-note blocks inside the article file

## Recommended Metadata Fields

- `title`
- `date`
- `author`
- `excerpt`
- `coverImage`
- `tags`
- `readingTime`

## Image Rules

- treat `coverImage` as required for every working draft
- include at least one inline image beyond the cover image
- follow `workflow.md` for inline-image count and placement on longer articles
- keep source URLs and attribution notes with the draft handoff when the image came from an external provider
- keep asset notes in the handoff, not inside the `.mdx` draft

## Template

Use `../assets/templates/blog-article.mdx`.
