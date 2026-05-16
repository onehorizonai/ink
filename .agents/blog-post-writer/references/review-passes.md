# Review Passes

## Order

For articles, use this mandatory order:

1. humanizer
2. style review
3. fact check
4. source URL check
5. affiliate compliance review, only when the draft includes affiliate links and `affiliate-compliance-review` is available
6. tone review
7. Ramsay review

The standard six passes are mandatory. The affiliate compliance review is conditionally mandatory for drafts with affiliate links when the skill is available. Do not omit Ramsay review. Do not omit source URL check; if there are no URLs to inspect, run the pass and state that explicitly.
A pass does not count unless it is recorded in a visible `Review Ledger` with a one-line outcome.
If Ramsay review returns any `Must Fix` items, treat them as blocking. Revise the article to address them before treating the draft as final, unless the user explicitly waives one.
For blog articles in this workflow, list-heavy formatting is suspect by default. If bullet points or numbered lists appear without a clear reason, treat that as a style and tone problem, not as harmless formatting.

## Review Ledger Contract

Use exactly these labels and this order when closing the workflow:

- `Humanizer: ...`
- `Style review: ...`
- `Fact check: ...`
- `Source URL check: ...`
- `Affiliate compliance review: ...` when applicable
- `Tone review: ...`
- `Ramsay review: verdict=... | score=X/15 | Must Fix=none/addressed/waived by user | ...`

If a pass ran but made no material changes, say so explicitly instead of omitting the line.

## Humanizer

Goal:

- remove AI tells early so later passes review real writing instead of machine noise

Look for:

- em dashes
- canned transitions
- buzzword filler
- mechanical symmetry
- generic hype
- overclean paragraph rhythm
- outline-shaped bullet dumps hiding inside the draft

## Tone review

Goal:

- compare the final working draft against the saved voice, stance, and intensity in the blog corpus

Look for:

- wrong sentence rhythm
- wrong level of specificity
- wrong balance between story and argument
- wrong CTA pressure
- wrong level of founder certainty or restraint
- irrelevant One Horizon context details
- a draft that sounds too safe, too corporate, or not reportorial enough for the desired blog voice
- list-heavy formatting that kills momentum or flattens the voice

## Ramsay review

Goal:

- judge the article like an impatient target reader and call out what actually needs fixing before publish

Run on every article after tone review.
It is especially useful when:

- the user asks for a blunt or brutal review
- the article feels repetitive, safe, or too polished after the normal passes
- the article is high-stakes and needs a harder publish gate

Look for:

- dull opening
- sections that say the same thing twice
- fake depth or AI slop
- weak proof
- listicle scaffolding where prose should carry the argument
- boring pacing
- a close that does not earn the read

If this pass produces `Must Fix` items:

- treat them as required changes, not optional notes
- revise the draft to address them
- do not present the article as final until they are handled or explicitly waived by the user
- if there are no blocking items, state `Must Fix=none` explicitly in the review ledger

## Style review

Goal:

- improve clarity, flow, structure, and long-form readability before the final tone pass

Look for:

- weak opening thesis
- sections that repeat instead of advance the argument
- paragraph bloat
- weak proof
- abrupt transitions
- repeated opening moves, section rhythms, transitions, metaphors, sentence shapes, or claims from recent corpus examples; use `../../social-common/references/repetition-guard.md`
- soft close or overly aggressive close
- affiliate links inserted as a detached monetization paragraph instead of inside a real buying-decision moment
- disclosures that are too far from the affiliate links or too vague for a normal reader
- bullet points or numbered steps where prose should do the work
- missing `---` section breaks in a draft that needs clearer pacing

## Affiliate compliance review

Goal:

- verify affiliate claims, restrictions, links, and disclosures before the final tone pass

Run when:

- the draft includes partner, referral, commerce, or affiliate links
- `affiliate-compliance-review` is available in the session

Look for:

- missing or distant disclosure
- unsupported discount, availability, performance, medical, or `best` claims
- dead or misleading partner URLs
- links added without a natural editorial reason
- unclear separation between the article's advice and the commercial relationship

If this pass produces required edits:

- revise before tone review and Ramsay review
- do not present the article as final until the affiliate issues are resolved or explicitly waived by the user

## Fact check

Goal:

- verify unstable or external claims before finalizing

Run this pass on every article.

Verify any claims involving:

- dates
- numbers
- company or product facts
- sourced claims
- public events
- legal, financial, medical, or regulatory references

If the draft contains no unstable or external claims, say so explicitly.
If a claim or citation first surfaced in another article, re-open and validate the underlying source directly. Do not accept second-hand sourcing from the archive.

Use the local MCP research tools described in `../../linkedin-social-writer/references/mcp-tools.md`.

## Source URL check

Goal:

- verify that cited or linked URLs resolve and actually match the expected page before finalizing

Run this pass on articles that include:

- inline source links
- recommended outbound links
- citation URLs kept in notes for publication handoff

Look for:

- 404 pages
- soft 404s or generic error pages
- homepage or category redirects when a specific page is expected
- login walls or dead documentation paths
- a different article, product, or domain than the draft implies
- copied legacy links from earlier articles that were never re-checked for the current draft

Use the local MCP research tools described in `../../linkedin-social-writer/references/mcp-tools.md`.

## Extra pass threshold

Add one more pass after the normal loop when:

- the article is longer than roughly 900 words
- the article mixes story and claims
- the article uses a strong opinion that could overstate facts
- the user says the article is important or high-stakes
