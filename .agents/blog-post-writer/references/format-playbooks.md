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

## Type Selection

- Ask the user to confirm the general blog post type before drafting.
- If the user gives a broad label such as `article`, `story`, or `essay`, map it to the nearest playbook below and verify that mapping back to the user.
- Use one primary playbook per article. Secondary elements are fine, but the opening move, proof model, and close should still follow one main type.
- Supported primary playbooks: `opinion / argument`, `explainer`, `comparison`, `product / deep dive`, `personal essay / rant`, `journal / dispatch`, `reflective / inspirational`, and `review`.
- Use an exact confirmation prompt when the type is missing: `Before I draft this, what general blog post type should it be? Pick one primary type: opinion / argument, explainer, comparison, product / deep dive, personal essay / rant, journal / dispatch, reflective / inspirational, or review.`
- Use an exact verification prompt when the brief already implies the type: `I read this as a <mapped type>. Confirm or correct that before I research or outline.`
- Do not accept `article`, `blog post`, `story`, or `essay` as the final stored type unless they are normalized to one playbook and confirmed back to the user.

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

## Personal Essay / Rant

Purpose:

- turn a lived frustration, observation, or hard-earned lesson into a specific argument without losing the rawness that makes it worth reading

Build with:

- a concrete trigger, scene, or moment
- first-person stakes
- specific failures, surprises, or reversals
- a takeaway grounded in experience instead of generic advice

Check:

- the voice stays personal and specific
- the frustration points somewhere useful instead of drifting into vague venting
- the article still lands on a clear takeaway
- the close feels earned rather than abruptly therapeutic

Avoid:

- abstract complaining
- fake swagger
- sanding the piece down until it loses all friction
- turning the rant into a list of tips

## Journal / Dispatch

Purpose:

- document what changed, what was learned, and what now looks different from a real checkpoint in time

Build with:

- a clear time window or moment
- what changed since the last state
- notable decisions, misses, or surprises
- the implication or next move

Check:

- it reads like a real dispatch, not a vague progress update
- time markers and decisions are concrete
- uncertainty is admitted when it is real
- visuals or screenshots anchor the update when they exist

Avoid:

- generic milestone language
- retroactive certainty
- turning the piece into release notes or standup bullets
- faking closure when the work is still open

## Reflective / Inspirational

Purpose:

- extract a grounded perspective shift or lesson from experience without drifting into generic motivation copy

Build with:

- one real observation or tension
- a concrete example or lived moment
- what changed in how the writer sees the work
- a restrained close

Check:

- the uplift feels earned
- specifics keep the piece out of cliche
- the tone stays honest and unsentimental
- any CTA stays light

Avoid:

- poster-copy inspiration
- vague life lessons
- manipulative emotional beats
- pretending the lesson applies universally

## Review

Purpose:

- judge a product, tool, book, process, or operating model based on direct use or credible hands-on evidence

Build with:

- the subject and context of use
- what held up
- what broke or disappointed
- a bottom line with caveats

Check:

- judgments are supported by concrete experience or evidence
- the tradeoffs matter more than the feature list
- the reader can tell who the review is for
- the verdict stays fair and specific

Avoid:

- affiliate-style puffery
- unsupported verdicts
- exhaustive feature tours
- hiding conflicts, caveats, or limitations
