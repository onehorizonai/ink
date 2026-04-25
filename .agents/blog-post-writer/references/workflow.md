# Workflow

Use this workflow in order. Every step is mandatory. Do not skip, collapse, reorder, or silently defer steps. Do not merge steps 2-13 into one drafting pass. If a step has little or no substantive output, state that outcome explicitly instead of omitting the step. Silent completion does not count; the step outcome must be visible in working notes or the final response.

## 1. Build the brief

Capture:

- article thesis
- confirmed general blog post type
- audience
- goal or desired next step
- source material, links, transcripts, or notes
- required claims, examples, or products
- visuals, screenshots, charts, or code that should appear
- the required cover image plus likely inline-image opportunities
- hard constraints such as target length, SEO terms, internal links, legal sensitivity, or launch timing

## 2. Ask and verify the blog post type

- Ask the user what general type of blog post this should be before researching or outlining.
- If the brief already implies a type, state the inferred type and ask the user to confirm or correct it instead of silently assuming.
- Use the playbooks in `references/format-playbooks.md` as the allowed shapes. Common choices include `opinion / argument`, `explainer`, `comparison`, `product / deep dive`, `personal essay / rant`, `journal / dispatch`, `reflective / inspirational`, and `review`.
- If the user answers with a broad label such as `article`, `story`, or `essay`, map it to the nearest playbook and verify the mapped type back to the user before continuing.
- Use one short, explicit confirmation move. Good shapes:
  - `Before I draft this, what general blog post type should it be? Pick one primary type: opinion / argument, explainer, comparison, product / deep dive, personal essay / rant, journal / dispatch, reflective / inspirational, or review.`
  - `I read this as a comparison post. Confirm or correct that before I research or outline.`
- Do not treat `article`, `blog post`, `story`, or `essay` as a confirmed final type by themselves.
- Record the confirmed type in the brief and keep it visible in the working notes or final response. Do not proceed to the outline until the type is verified.
- Do not start internal research, external research, or outline work before the type is verified.

## 3. Resolve blog paths

- Read `../../../.local/context/blog-publishing.local.md` for the active path values.
- If the local file is missing, ask the user where to load existing blog articles from and where to publish finished blog posts, then create the local file.
- If `source_articles_dir` is `[unset]`, ask the user where to load existing blog articles from.
- If `publish_output_dir` is `[unset]`, ask the user where to publish finished blog posts.
- If either stored folder no longer exists on disk, ask the user for the new folder and update the local file before continuing.
- Keep the total question budget for this workflow to 4 short questions. The mandatory type-confirmation step above uses one slot. When paths are unresolved, use the remaining question budget on the path questions first.
- Do not assume `../../content/blog/posts/`.
- Use One Horizon context docs for live runtime context. Do not use tracked repo files for live context. The exception is `.local/context/blog-publishing.local.md` for machine-local blog path state.

## 4. Research internally first

- Search `source_articles_dir` from `../../../.local/context/blog-publishing.local.md` for related published articles before looking outward.
- Pull up to 3-5 solid internal examples that match the topic, confirmed article type, argument shape, product angle, or proof density.
- Prefer recent examples when the voice may have shifted.
- Note recurring section patterns, CTA pressure, and how directly the archive makes similar claims.
- Use internal examples for angle, pacing, and voice, not as a reusable source bank.
- Do not copy an older article's links, citations, or source notes into the new draft.
- If an older article points to something worth checking, treat it as a lead and re-open the underlying source directly before deciding whether it belongs in the new article.
- If no useful internal examples exist, say so explicitly and continue without internal examples.

## 5. Research externally

- Run a lightweight web research pass after the internal corpus scan.
- Use the local MCP tools in `../../linkedin-social-writer/references/mcp-tools.md`.
- Collect 2-5 solid sources that help with current terminology, proof points, counterpoints, and source discovery.
- Build a fresh source set for the current article. Do not reuse an older article's source bundle or citations as-is.
- Prefer primary sources, original company docs, canonical essays, and credible reporting over derivative SEO summaries.
- Note the claims that still need verification during the fact-check pass.
- Do not skip this step. If the article is intentionally personal, reflective, or journal-like and web research adds no signal, run a minimal external scan and state that no outside source materially shaped the draft.

## 6. Ask only necessary questions

The mandatory blog-type confirmation in step 2 always happens. Ask additional questions only when the article would otherwise require invention or lead to the wrong angle.

Ask at most 4 short questions total across this workflow, including the type-confirmation question and any path-resolution questions from step 3.

High-value questions:

- What is the main claim or takeaway of this article?
- Who is it for?
- Which source, example, or proof point must be included?

Do not ask for information that can be recovered from the corpus, One Horizon context docs, or the supplied brief.

## 7. Load the minimum user context

Resolve the author and load only the relevant author-scoped One Horizon context docs. Use `../../one-horizon-context-setup/references/context-doc-templates.md` for the naming contract:

- `Profile` for identity basics
- `Current Work` for almost every company or product article
- `Work History` only when credibility, experience, or story matters
- `Personal Interests` only when it helps the angle feel lived-in
- `Personal Life` only when the article is intentionally personal

Use the confirmed article type to decide whether personal context is appropriate. `personal essay / rant`, `journal / dispatch`, and `reflective / inspirational` pieces may justify personal docs. `explainer`, `comparison`, `review`, and most `product / deep dive` drafts usually should not.
Do not load personal docs just because they exist.
If a required One Horizon tool call is missing or fails, follow `../../one-horizon-context-setup/references/mcp-readiness.md`.

## 8. Draft the outline

- Build a section-by-section outline from the brief, the confirmed article type, the internal examples, the external research, and the selected user context.
- Lock the central claim, the opening move, the major proof points, and the close before writing full prose.
- Keep one central argument per article.
- Include only the sections needed to move the argument forward.
- Bias the structure toward a sharper tech-magazine flow: a live thesis, clear stakes, concrete proof, and momentum from section to section.
- Let the confirmed article type set the opening move, proof model, and close. Do not outline an `explainer` like a `rant`, or a `journal / dispatch` like a `comparison`.
- Decide which sections should carry visuals while the outline is still cheap to change.

## 9. Plan the images

- Require one cover image for `metadata.coverImage`.
- Require at least one inline image beyond the cover image.
- For longer articles, target inline images for roughly 30% of substantive sections, rounded up, but do not place an image in every substantive section.
- Use this rule of thumb when the count is unclear:
  - 1-3 substantive sections: 1 inline image
  - 4-6 substantive sections: 2 inline images
  - 7-9 substantive sections: 3 inline images
- Treat substantive sections as the body sections that carry the argument. Do not count the TL;DR block, footnotes, or the final CTA block.
- Use the dedicated image MCP flow for final image sourcing:
  - `search_images` with arguments shaped like `{"query":"...", "orientation":"landscape", "limit":6}`
  - `download_image` with arguments shaped like `{"image_id":"..."}`
- Keep `metadata.coverImage` as a plain `posts/...` path.
- For inline blog images, use `getImageUrl('posts/...')` directly in the MDX.
- Keep article paths separate from storage upload targets. The article contract stays `posts/...`, while uploaded image objects should land under `images/posts/...`.
- Do not chase the implementation of `getImageUrl()`. Treat it as the project-standard helper and just use it.
- Form `search_images.query` as a short broad visual concept, usually 1-4 words.
- Search for what a photographer could plausibly capture, not the full argument of the article.
- For abstract ideas, use a visual metaphor or adjacent scene first. Example: use `empty office` for an article about lean AI-enabled teams.
- Do not use long descriptive prompts such as `a lean technology team overseeing a dense stack of dashboards, agents, and workflows, not a crowded open office`.
- Assume the repo-local MCP tools are already available and working. Do not run verification as a preflight step. Only troubleshoot MCP after a concrete tool failure.
- Use `../../blog-image-finder/references/setup.md` for the tool contract.
- Do not use `search_unsplash`, generic web search, or raw image URLs as the final blog-asset path when `blog-image-finder` is available.
- Use `search_unsplash` from `../../linkedin-social-writer/references/mcp-tools.md` only as fallback inspiration or when the dedicated image finder tools are unavailable.
- Use `upload_image` from `../../blog-image-uploader/references/setup.md` only when the user wants the assets uploaded to the blog image bucket, with arguments shaped like `{"local_path":"...", "object_key":"images/posts/..."}`
- Keep `local_path`, `source_page_url`, `photographer_name`, and `attribution_text` with the asset notes.
- Keep asset planning notes out of the article file itself. Never insert JSX comments, HTML comments, placeholder asset lists, or TODO blocks into the MDX.

## 10. Validate the outline against the rules

- Check the outline against the relevant article-type playbook in `references/format-playbooks.md`.
- Confirm the outline and image plan fit the brief constraints such as SEO targets, required links, visuals, and CTA intensity.
- Cut sections that repeat instead of advancing the argument.
- Convert list-shaped sections back into prose unless the brief truly demands a list.
- Plan `---` between major sections before full drafting starts.
- Verify that the draft shape still matches the confirmed blog post type before full drafting starts.
- Fix structural problems here before full drafting.
- Do not start full prose until this step is satisfied.

## 11. Write pass one

- Write the opening, section spine, conclusion, and image placements first.
- Use this pass to lock the argument shape, pacing, and destination.
- Insert `---` between major sections as you lock the structure.
- Default to paragraphs rather than bullet points or numbered steps.
- Keep weak or thin sections brief rather than padding them.
- Do not try to finish the article here.

## 12. Write pass two

- Expand the body with proof, examples, transitions, practical detail, and the final inline images.
- Strengthen thin sections and remove repetition introduced in pass one.
- Stay close to the voice profile, not to any single source article.
- Keep the tone closer to sharp tech-magazine analysis than to generic SaaS content. Vary the rhythm and keep some edge without copying any one publication.
- Finish the full article here.

## 13. Run staged review passes

Read `references/review-passes.md`.

For every article:

- run the humanizer pass first
- run the style review pass second
- run the fact-check pass third
- run the source-url-check pass fourth for every article; if the draft, notes, or handoff include no URLs, state `No URLs present to validate` instead of skipping the pass
- run the tone review fifth and use it as the last content-adjustment pass before Ramsay review
- run `../../blog-post-ramsay-review/SKILL.md` sixth for every article after tone review
- if `../../blog-post-ramsay-review/SKILL.md` returns any `Must Fix` items, revise the draft to address every one of them before calling the article final unless the user explicitly waives an item
- after revising, check the updated draft against the Ramsay `Must Fix` list instead of assuming the problems are gone
- record a `Review Ledger` with one line per pass in the exact order above; if a pass made no material changes, state that explicitly
- on the `Ramsay review` line, include the verdict, the `X/15` score, and whether `Must Fix` is `none`, `addressed`, or `waived by user`

Add:

- one extra tightening pass for long articles, nuanced argument pieces, or drafts with multiple moving parts

## 14. Save drafts separately

If the user wants the draft stored locally:

- write to `content/blog/drafts/`
- use `../assets/templates/blog-article.mdx` as the starting point
- never place unpublished drafts inside `publish_output_dir` from `../../../.local/context/blog-publishing.local.md`
- save only the actual article content and working MDX structure; do not save editorial comments or placeholder asset manifests inside the file

## 14a. One Horizon: Record the Article

After saving a draft or writing a published article, use the One Horizon MCP to create a child initiative under `Ink - Blog`.

Fields:

- **Title**: the article title
- **Description**: confirmed blog post type, review ledger summary (Ramsay verdict + score), and the local file path (draft path or `publish_output_dir` path)
- **Status**: `in-progress` when saving a draft to `content/blog/drafts/`; `published` when writing to `publish_output_dir`

Rules:

- Create the One Horizon record after the local file write succeeds.
- If the user only wants the draft in memory and does not save it locally, skip this step.
- If the One Horizon MCP is unavailable, log the local path in the final response and continue.
- If `Ink - Blog` does not exist, note that in the output and skip the One Horizon step.

## 15. Final response

Return:

- the final draft
- the confirmed blog post type and any normalized playbook mapping used
- the resolved blog source folder and publish output folder when they affected the work
- the internal corpus examples and external research sources that informed it
- the selected cover image plus the inline-image plan or inserted image locations
- if no relevant internal examples existed, say so explicitly
- what context, outline decisions, and examples were used
- what assumptions remain
- what was checked, if fact review or source URL review happened
- a `Review Ledger` section listing `Humanizer`, `Style review`, `Fact check`, `Source URL check`, `Tone review`, and `Ramsay review` in that order
- on the `Ramsay review` line, include the verdict, the `X/15` score, and whether blocking items are `none`, `addressed`, or `waived by user`
- a short workflow-completion note covering all mandatory steps and the full review ledger
- which Ramsay blocking issues were addressed or explicitly waived
- use `Working draft` instead of `Final draft` if the review ledger is incomplete or the Ramsay blocking issues are still open
