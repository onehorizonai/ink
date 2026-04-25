# Workflow

Use this sequence as the non-negotiable workflow for `page-brief-builder`.

Every step is mandatory. If a step cannot be completed, record:

- what could not be done
- why it could not be done
- what assumption was used instead
- what follow-up input would resolve it

## Cross-Stage Clarification Loop

Use `references/clarification-loop.md` as the shared questioning contract.

- Ask 2-4 tightly related verification questions when multiple adjacent inputs block the same decision.
- Ask a single question only when one blocking uncertainty remains.
- If the user gives a thin or ambiguous answer, verify the vague part before moving forward.
- At the end of each major stage, check whether the next stage can be completed without guesswork. If not, ask the next verification questions and stop.

## 1. Capture intake and required inputs

Use `../../website-brief-intake/SKILL.md`.

Do not continue until each required input is either:

- confirmed
- intentionally absent
- or asked back to the user in the next verification round

Do not use assumptions for missing user-answerable strategy inputs.
Ask 2-4 tightly related verification questions when the same decision is blocked by several missing inputs.
Ask one question only when one blocking uncertainty remains.

## 2. Confirm website and business context

- Resolve the author and load only the relevant author-scoped One Horizon context docs. Use `../../one-horizon-context-setup/references/context-doc-templates.md` for the naming contract.
- If a required One Horizon tool call is missing or fails, follow `../../one-horizon-context-setup/references/mcp-readiness.md`.
- Ask for additional business-specific context even when author-scoped One Horizon context docs already exist.
- Resolve conflicts between user input and context docs explicitly.

## 3. Confirm page type

- Record the page type explicitly.
- If multiple page types are plausible, show the short list and ask for confirmation.

## 4. Confirm audience, goals, and CTAs

- Capture the target audience.
- Capture the page goal.
- Capture the primary CTA.
- Capture the secondary CTA or mark it intentionally absent.
- Capture funnel stage or awareness stage.

## 5. Require additional business-specific context

- Ask for product, offer, differentiation, proof, or constraints that are specific to this business.
- Never finalize the brief from a generic topic prompt alone.
- If the business-specific context is still too thin to choose a page strategy credibly, ask the next targeted verification questions and stop.

## 6. Determine whether the page is new or existing

- Record `new` or `update`.
- If `update`, capture the current live public page URL and the reason it is changing.
- If `update`, also capture what is not working well, what must stay, and what success looks like after the update.
- If the user names a public page but does not provide its URL, resolve the live URL on the target site with web search.
- Do not search repo files to find a public page unless the user explicitly provides a local file path or asks for repo-level implementation analysis.

## 7. Inspect existing relevant site pages when possible

Use `../../website-pattern-analyzer/SKILL.md`.
Use `../../page-brief-page-playbook/SKILL.md` only when live same-site evidence is thin.

- Review the current live public page when this is an update.
- Use local files only when the user explicitly provides a local file path or asks for repo-level implementation analysis.
- Review relevant same-site pages to understand structure, rhythm, proof, CTA style, and conventions.

## 8. Research comparable competitor pages

Use `../../competitor-page-research/SKILL.md`.

- Use web search and live page inspection for this step. Do not rely on memory.
- Do not assume which competitors, analogs, or page patterns are relevant without checking live sources first.
- Review the closest competitor or comparable pages.
- Distill useful patterns, differentiation opportunities, and things to avoid.

## 9. Brainstorm up to 3 page directions

Use `../../page-positioning-strategist/SKILL.md`.

- Generate at most 3 materially different directions for the page.
- Make the directions meaningfully different in promise, narrative angle, audience emphasis, or proof strategy. Do not waste slots on cosmetic variants.
- For each direction, capture:
  - a short label
  - the core angle
  - why it could work
  - what proof it would need
  - the main risk
- Rank the directions and recommend one.

## 10. Choose a direction or ask the user

Use `../../page-positioning-strategist/SKILL.md`.

- If one direction is clearly strongest, lock it and say why.
- If 2 or more directions are still materially viable, ask the user to choose before continuing.
- If the direction is chosen but the page still lacks a clear promise, differentiator, proof base, or objection map, ask the next positioning verification questions before continuing.
- If the user needs to choose, stop the workflow there and return only:
  - the direction shortlist
  - the recommended direction
  - the decision still needed
- Do not proceed into SEO, messaging, or conversion planning with an unresolved direction.

## 11. Run SEO and search-intent planning

Use `../../page-seo-intent-planner/SKILL.md`.
Use `../../page-brief-seo-playbook/SKILL.md` to enforce the local SEO rules.

- Define primary intent.
- Define secondary intents only when they materially affect the page.
- Determine the keyword or topic cluster.
- Check overlap risk.
- If the organic role, internal-link targets, supporting-content module, or slug constraints are still soft, ask the next SEO verification questions and stop.
- Lock exact metadata, internal links, structured-data requirements, and supporting-content modules where relevant.

## 12. Run messaging and positioning planning

Use `../../page-positioning-strategist/SKILL.md`.
Use `../../page-brief-copy-playbook/SKILL.md` to enforce the local copy rules.

- Define value proposition, differentiators, proof, objections, tone, and claims needing support for the chosen direction.
- If any of those remain too soft to lock exact page instructions, ask the next positioning verification questions and stop.

## 13. Run conversion and CTA planning

Use `../../conversion-cta-planner/SKILL.md`.
Use `../../page-brief-copy-playbook/SKILL.md` when hero or CTA guidance needs the local copy rules.

- Define CTA logic, friction points, trust supports, and stage-appropriate conversion behavior.
- If CTA destinations, secondary CTA role, or reassurance needs are still unclear, ask the next conversion verification questions and stop.

## 14. Use copywriting to sharpen the copy guidance

Use `../../copywriting/SKILL.md` after the strategy is clear.

- Use it to lock exact H1, hero subheading, title tag, meta description, section headings, supporting-content modules, and CTA labels for the brief.
- Do not use it to draft the whole page as part of this workflow.
- Keep the output at the brief level: exact copy atoms and labels, not finished full-page copy.
- If exact copy atoms still depend on unresolved promise, proof, CTA, or terminology choices, ask the next copy verification questions and stop.

## 15. Run fact-checking and claim validation where needed

Use `../../fact-check/SKILL.md` when the brief includes:

- statistics
- market claims
- product claims
- comparisons
- sourced statements
- dates, names, numbers, or external facts

Separate:

- verified facts
- unsupported claims
- proposed messaging that still needs proof

## 16. Assemble the final brief

Use `../../page-brief-assembler/SKILL.md`.

- Follow the exact structure in `../../page-brief-assembler/references/final-brief-template.md`.
- Assemble a concise locked execution spec, not a research summary.
- Do not include a source ledger, workflow recap, research recap, or rationale section.
- For every proposed page section, specify exact placement, section heading, required content, required proof or link, CTA, and what not to include.
- Do not assemble the brief while blocking verification questions remain unanswered.
- Do not assemble the brief while user-answerable strategy inputs remain soft, implied, or bundled into assumptions.
- Do not assemble the brief if any section would require `TBD`, `TODO`, generic filler, or a vague recommendation.
- Do not assemble the brief if the next LLM agent would need to infer the required page changes from bullet-point observations.
- Do not assemble the brief if H1, title tag, meta description, CTA labels, section headings, supporting-content modules, links, or claims remain advisory instead of exact.

## 17. Run the final QA pass

Confirm before presenting the brief:

- the required final-brief template sections are present
- confirmed inputs are separated from assumptions
- site-pattern guidance is present or explicitly blocked
- competitor insights are present or explicitly blocked
- a chosen direction is present or the user explicitly selected one
- SEO contract matches the page goal
- positioning and CTA logic align with the audience and funnel stage
- no user-answerable strategy input remains soft, implied, or unresolved behind an assumption
- unsupported claims are flagged
- implementation notes explicitly say the brief does not include code
- no `TBD`, `TODO`, `TBA`, `TBC`, or placeholder language appears
- the current-page diagnosis says what to keep, rewrite, add, remove, and reposition when this is an update
- the section-by-section plan includes exact section headings, required content, required proof or links, CTA labels, and `do not include` guidance
- H1, title tag, meta description, primary CTA, secondary CTA, section headings, supporting-content modules, and required links are exact
- the brief does not include a source ledger, workflow recap, research recap, or rationale section
- section recommendations are concrete enough that the writer, designer, and implementation agent do not have to guess what is meant

If a step fails because the inputs are incomplete, stop and use `../../website-brief-intake/SKILL.md` instead of guessing.
