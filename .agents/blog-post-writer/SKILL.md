---
name: blog-post-writer
description: Orchestrate blog writing from brief to final draft using the repo blog corpus, lightweight web research, One Horizon context docs, image planning, two writing passes, and the required review sequence. Use when Codex needs to draft or revise an original long-form blog article for this repo. Do not use this skill for LinkedIn posts, social-first writing, or storage-only tasks.
---

# Blog Post Writer

## Overview

Ground every article in the published blog corpus resolved from `../../.local/context/blog-publishing.local.md`. First confirm what general type of blog post the user wants, then find related internal articles for angle, structure, and voice, not for reusable sourcing. Build a fresh external source set, validate an outline, and write long-form copy in two passes that fits the thesis, the confirmed article type, the audience, and the desired next step.

Use the workflow in `references/workflow.md` as the authoritative sequence for this skill. Every workflow step is mandatory. Do not skip, collapse, reorder, or silently defer any step. If a step has no substantive output, record that outcome explicitly instead of omitting the step.
Before presenting anything as final, complete and report a visible review ledger. Silent completion does not count. If the Ramsay line is missing, or its `Must Fix` items are still open, the article is still a working draft.

## Quick Start

1. Read `references/workflow.md`.
2. Load the minimum author-scoped One Horizon context docs (resolved in step 9 below; read here only if the blog post type requires personal context before the archive search).
3. Read `../../.local/context/blog-publishing.local.md`.
4. Ask the user to confirm the general blog post type before drafting. If the brief already implies one, state the inferred type and ask the user to confirm or correct it. If the user says something broad like `article`, map it to the nearest playbook in `references/format-playbooks.md` and verify the mapped type back to the user. Do not start internal research, external research, or outline work until the type is confirmed.
5. If the local file is missing, or if either stored folder is `[unset]` or missing on disk, ask the user for the existing blog articles folder and the published blog output folder, then update `../../.local/context/blog-publishing.local.md` before continuing.
6. Search `source_articles_dir` from `../../.local/context/blog-publishing.local.md` for up to 3-7 relevant internal examples. Prefer the same theme, argument shape, or confirmed article type first. Use them for voice and structure only. Do not inherit their source lists or citations. If none are relevant, say so explicitly and continue.
7. Read `../linkedin-social-writer/references/mcp-tools.md`.
8. Do a lightweight external research pass on the topic. Build a fresh source set for the article with the local MCP research tools.
9. Resolve the author and load only the relevant author-scoped One Horizon context docs. Use `../one-horizon-context-setup/references/context-doc-templates.md` for the naming contract.
10. Distill voice markers with `references/style-capture.md`.
11. Draft an outline and image plan and validate both against `references/format-playbooks.md` and the brief constraints.
12. Use `search_images` then `download_image` from `../blog-image-finder/SKILL.md` for final external blog assets.
13. Write pass one by locking the opening, section spine, `---` section breaks, cover image, and inline image placements.
14. Write pass two by adding proof, examples, transitions, detail, and the final inline images while keeping the article prose-led rather than list-led.
15. Run every mandatory review pass described in `references/review-passes.md`, including `../blog-post-ramsay-review/SKILL.md` after tone review, then report the review ledger with Ramsay verdict, score, and `Must Fix` disposition.
16. Save unpublished drafts in `content/blog/drafts/` if the user wants them persisted.

## Working Agreement

- Use the blog corpus as the source of truth for tone, pacing, argument style, section shape, CTA intensity, and how directly to sell.
- Read `../../.local/context/blog-publishing.local.md` for the active path values.
- Use One Horizon context docs for live runtime context. Do not use tracked repo files for live context. The exception is `.local/context/blog-publishing.local.md` for machine-local blog path state.
- If a One Horizon tool call is missing or fails, follow `../one-horizon-context-setup/references/mcp-readiness.md`. Do not search tracked repo files as a substitute for live context.
- Always ask the user to confirm the general blog post type before outlining. If the type is implied, reflect the inferred type and ask for confirmation or correction instead of silently assuming.
- Normalize broad labels such as `article`, `story`, or `essay` to the closest playbook in `references/format-playbooks.md`, then verify the mapped type with the user before continuing.
- Use the exact confirmation and verification wording from `references/format-playbooks.md` when the type is missing or only implied.
- If the local file is missing, create it after asking the user for the required folders.
- If a stored folder no longer exists, ask the user for the new folder and update `../../.local/context/blog-publishing.local.md` before continuing.
- Do not assume `content/blog/posts/`.
- Research internally first so the archive shapes the angle before outside sources do, but do not treat earlier articles as a reusable source bank.
- Do not reuse or carry forward source lists, citations, or outbound links from other articles. If an older piece points to something useful, treat it as a lead and re-open the original source directly before deciding whether it belongs in the new draft.
- Follow with a brief web research pass to sharpen the angle, gather current terminology, and surface claims that need verification later.
- Use One Horizon context docs to make the writing authentic, but load only what is relevant to the article.
- Reuse patterns, not sentences. Do not remix published copy line by line.
- Prefer a narrow, evidence-based voice profile over generic SEO-blog language.
- For blog articles, aim for a sharper, more reportorial tech-magazine voice, closer to Verge-style analysis than to a generic SaaS post. Borrow the energy, clarity, and sense of stakes, not any outlet's phrasing.
- Prefer primary sources, company docs, and strong secondary reporting over generic SEO summaries when researching.
- Always draft an outline before prose and validate it against the active format playbook and the brief.
- Use the confirmed article type to pick internal examples, the relevant One Horizon context docs, and the matching format playbook.
- Every workflow step is mandatory. Execute the step even when the result is `no relevant internal examples`, `no external sources materially changed the draft`, or `no URLs were present to validate`.
- Make skipped-looking work explicit. If a mandatory step or pass ran but made no material change, record that outcome explicitly instead of omitting the step from the response.
- Always produce one cover image for `metadata.coverImage`.
- Always plan at least one inline image beyond the cover image.
- Follow the section-coverage rule in `references/workflow.md` for inline image count and placement.
- Use `search_images` then `download_image` from `blog-image-finder` for final external blog assets. Do not use `search_unsplash`, generic web search, or raw image URLs as the final asset path.
- Keep `metadata.coverImage` as a plain `posts/...` asset path such as `posts/my-image-name.jpg`.
- For inline blog images, use `getImageUrl('posts/my-image-name.jpg')` as the final URL in the article.
- Keep article image paths separate from storage upload targets. The article contract stays `posts/...`, while uploaded objects should land under `images/posts/...`.
- Treat `getImageUrl()` as the fixed project contract for blog image URLs. Do not inspect, explain, or reverse-engineer how it works unless the user explicitly asks.
- Form `search_images.query` as a short visual concept, not a literal description of the article thesis. Search for simple scenes like `empty office` or `quiet workspace`, then narrow only if needed.
- Assume the image MCP tools work. Do not run verifier or setup checks before using them. Only troubleshoot MCP after a concrete tool failure.
- Never include placeholder asset manifests, JSX comments, HTML comments, TODO notes, or editorial notes inside the article file. Do not add blocks like `{/* Placeholder assets expected ... */}`.
- If asset work is still pending, keep that note in the response or handoff summary, not in the `.mdx` body.
- Use `upload_image` from `blog-image-uploader` only when the user wants the selected assets uploaded to the blog image bucket or the publish workflow requires it. When uploading, target `images/posts/...`, not `posts/...`.
- Treat pass one as structure work and pass two as expansion work. Do not try to fully solve the whole article in one run.
- Use the exact workflow order. Do not skip or merge mandatory steps, and do not start full prose before the outline is validated.
- Do not skip internal research when relevant published blog examples exist.
- Default to paragraphs. Avoid bullet points and numbered lists in the article body unless the brief or the material truly leaves no good prose alternative.
- Separate major sections with `---`.
- Use `Final draft`, `ready to publish`, or equivalent only when the review ledger is complete and the Ramsay `Must Fix` status is `none`, `addressed`, or `waived by user`. Otherwise label the result as a working draft.
- Treat visuals, code samples, screenshots, charts, and citations as part of the brief. Make the text and the asset work together.
- Ask only the smallest set of high-leverage questions. The blog-type confirmation is mandatory; beyond that, if the brief, corpus, and One Horizon context are sufficient, do not ask.
- Keep unpublished drafts separate from the published corpus at all times.

## Workflow

Follow the shared blog workflow in `references/workflow.md`.

For articles:

- Confirm the blog post type with the user before internal research and outline work.
- Use the matching article-type playbook in `references/format-playbooks.md`, normalizing broad labels to the nearest playbook and verifying the mapping when needed.
- Do not treat a handoff suggestion or an inferred label as confirmed until the user explicitly confirms or corrects it.
- Research the published archive before the web.
- Build a fresh source set for each article instead of carrying over citations from older posts.
- Draft and validate an outline plus image plan before writing full prose.
- Require one `coverImage` in metadata and at least one inline image in the article body.
- Follow the inline-image coverage rule in `references/workflow.md` for longer articles.
- Use at least 2 writing passes before the review loop.
- Keep blog articles prose-led, not list-led, unless the brief explicitly demands a list.
- Use `---` between major sections in the article body.
- Start with `../content-humanizer/SKILL.md`.
- Continue with `../content-style-review/SKILL.md`.
- Continue with `../fact-check/SKILL.md`.
- Continue with `../source-url-check/SKILL.md` for every article. If there are no URLs to validate, say so explicitly instead of skipping the pass.
- Continue with `../content-tone-review/SKILL.md` as the last content-adjustment pass before Ramsay review.
- Continue with `../blog-post-ramsay-review/SKILL.md` for every article after tone review. If that pass returns any `Must Fix` items, address all of them before calling the draft final unless the user explicitly waives one, then verify the fixes against the Ramsay findings instead of assuming they are resolved.
- Finish with a `Review Ledger` section that lists all six passes in order. For `Ramsay review`, include the verdict, the score, and whether `Must Fix` is `none`, `addressed`, or `waived by user`.
- Add one extra self-edit for longer articles, argument-heavy articles, or drafts with multiple claims.
- Do not present a draft as final until every mandatory step and pass above has been completed, reported in the review ledger, and accounted for.

## Format Rules

- `article`: Deliver one polished article in the repo's blog voice. Offer multiple title options only if asked or if the brief is weak.
- Confirm one primary blog post type before drafting. Supported playbooks are `opinion / argument`, `explainer`, `comparison`, `product / deep dive`, `personal essay / rant`, `journal / dispatch`, `reflective / inspirational`, and `review`.
- Preserve the core thesis all the way through the piece.
- Use section headings that move the argument forward, not generic SEO filler.
- Keep the article in paragraphs by default. Avoid bullet points and numbered lists unless the brief clearly requires them.
- Use `---` between major sections.
- Keep the voice closer to a sharp tech-magazine feature or analysis than to a generic SaaS explainer.
- Include `metadata.coverImage` in every draft and published article.
- Include inline images in at least one substantive section, and follow `references/workflow.md` for coverage on longer posts.
- Use a CTA only when it fits the archive's usual intensity.

## Supporting Skills

Use the local shared review skills first because they are tuned for this repo's workflow:

- `../content-humanizer/SKILL.md`
- `../content-tone-review/SKILL.md`
- `../content-style-review/SKILL.md`
- `../fact-check/SKILL.md`
- `../source-url-check/SKILL.md`
- `../blog-post-ramsay-review/SKILL.md` for blunt late-stage pressure testing
- `../blog-image-finder/SKILL.md`
- `../blog-image-uploader/SKILL.md` when publishing image assets

If the session also includes external writing skills, use them in support of this skill instead of replacing it.

- Use `../copywriting/SKILL.md` to sharpen structure or CTA options after the corpus voice is established.
- Use `$prompt-engineering-patterns` principles to keep the workflow strict, progressive, and low-noise.

Keep the published corpus and shared repo references as the source of truth when those skills pull in a different style.

## Output Shape

Unless the user asks differently, return:

- the final draft first
- the confirmed blog post type and any normalized playbook mapping
- a short note on the internal and external research that shaped the angle, including when no relevant internal examples existed
- the resolved blog source folder and publish output folder when they affected the work
- the key context files, corpus examples, and external sources used
- the selected cover image and inline image plan, plus any downloaded or uploaded asset paths when image work happened
- a short note on the outline or structural decisions that shaped the article
- a short note listing the voice cues you matched
- a `Review Ledger` section with these lines in this order: `Humanizer`, `Style review`, `Fact check`, `Source URL check`, `Tone review`, `Ramsay review`
- on the `Ramsay review` line, include the verdict, the `X/15` score, and whether `Must Fix` is `none`, `addressed`, or `waived by user`
- a short workflow-completion note confirming that internal research, external research, outline validation, both writing passes, and the full review ledger all ran
- any assumptions or missing facts that could change the draft
- the saved draft path if you persisted the draft to `content/blog/drafts/`
- the One Horizon initiative title when a One Horizon record was created under `Ink - Blog`

## Files

- Read `references/corpus-spec.md` for the blog archive schema.
- Read `references/draft-spec.md` for unpublished draft storage.
- Read `references/workflow.md` for the orchestration flow.
- Read `references/review-passes.md` for pass order and responsibilities.
- Read `references/style-capture.md` when extracting voice markers.
- Read `references/format-playbooks.md` for article-shape rules.
- Read `../../.local/context/blog-publishing.local.md` for the active blog source and publish folders.
- If a One Horizon tool call fails, read `../one-horizon-context-setup/references/mcp-readiness.md` for recovery.
- Resolve the author with One Horizon MCP tools, then load relevant author-scoped context from One Horizon using the contract in `../one-horizon-context-setup/references/context-doc-templates.md`.
- Read `../../content/blog/README.md` only if `../../.local/context/blog-publishing.local.md` points into this repo and the local naming is unclear.
- Read `../linkedin-social-writer/references/mcp-tools.md` before using local research tools.
- Read `../blog-image-finder/references/setup.md` before sourcing external blog images.
- Read `../blog-image-uploader/references/setup.md` only when blog images should be uploaded to the blog image bucket.
- Use `assets/templates/blog-article.mdx` when you need to persist an unpublished draft manually.
