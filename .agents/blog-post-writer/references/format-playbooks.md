# Format Playbooks

## Visual Rules

Apply these rules to every blog article:

- include one cover image in `metadata.coverImage`
- include at least one inline image beyond the cover image
- for longer articles, target inline images for roughly 30% of substantive sections, rounded up
- do not place inline images in every substantive section
- make every image earn its place by clarifying a workflow, supporting a claim, or giving the reader a visual reset
- keep the image choice aligned with the thesis, not just the nearest keyword
- use `search_images` then `download_image` from `blog-image-finder` for final external blog assets
- keep `metadata.coverImage` as a `posts/...` path and use `getImageUrl('posts/...')` for inline blog image URLs
- keep upload targets separate from article paths: upload stored assets under `images/posts/...`, while the article still references `posts/...`
- use `search_unsplash` only as fallback inspiration, not as the final blog-asset path
- do not insert placeholder asset manifests, JSX comments, or editorial notes into the article body

## Editorial Rules

Apply these rules to every blog article:

- keep the voice closer to a sharp tech-magazine feature or analysis than to a generic SaaS blog post
- keep the prose specific, contemporary, and a little edgy without copying any one publication's phrasing
- default to paragraphs and flowing prose
- avoid bullet points and numbered lists unless the brief or evidence genuinely requires them
- use `---` between major sections

## Opinion / Argument

Purpose:

- make a clear claim, explain why the current model fails, and offer a better one

Build with:

- a sharp opening thesis
- a concrete problem setup
- a structural explanation of why the problem persists
- a clear alternative
- a close that fits the archive's usual CTA intensity

Check:

- the argument stays coherent all the way through
- each section earns its place
- the image plan supports the argument instead of decorating it
- the article does not drift into generic thought leadership

Avoid:

- vague trend language
- repeating the same claim with different wording
- unsupported certainty
- turning the article into bullet-point talking points

## Explainer

Purpose:

- teach how a concept, workflow, or system works without sounding like documentation

Build with:

- a clear problem or misconception
- one logical walkthrough
- concrete examples
- a practical takeaway

Check:

- the article stays teachable without becoming dry
- examples make the abstract parts easier to follow
- the images make the walkthrough easier to follow
- the reader can explain the idea back after reading

Avoid:

- jargon without translation
- long setup before the main idea appears
- filler subheads
- numbered-step dumps when prose can carry the idea more naturally

## Comparison

Purpose:

- contrast two approaches, tools, or operating models and show what the difference changes in practice

Build with:

- a fair framing of both sides
- the real tradeoff
- examples of where the old model breaks
- a conclusion that makes the recommended path feel earned

Check:

- the comparison is specific
- the distinction matters in practice
- the visuals clarify the comparison or tradeoff
- the piece does not become a feature checklist

Avoid:

- strawman versions of the alternative
- overly broad claims
- turning the whole piece into a sales page
- turning the comparison into a checklist or scorecard

## Product / Deep Dive

Purpose:

- explain what the product changes, how it works, and why the old workflow is broken

Build with:

- a real workflow problem
- a concrete walkthrough
- one or two enabling product details
- proof through examples, not slogans

Check:

- the product stays in service of the argument
- the article does not read like release notes pasted into prose
- the visuals show the workflow or product detail the text is discussing
- the close fits the archive's normal level of directness

Avoid:

- feature dumping
- hiding the core claim behind too much setup
- aggressive CTA pressure that the archive would not support
- list-heavy walkthroughs that read like release notes in disguise
