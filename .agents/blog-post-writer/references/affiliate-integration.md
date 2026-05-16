# Affiliate Integration

Use this when a blog brief includes partner, referral, commerce, or affiliate links.

## Editorial Fit

- Plan affiliate links during the outline and source pass, not after the article is drafted.
- Include a partner only where the article is already discussing the reader's buying decision, access constraint, equipment constraint, or product tradeoff.
- Omit the link when the article has no natural buying-decision moment.
- Do not create a shopping paragraph just because an affiliate exists.
- Keep the article's argument independent of the commission relationship.

## Prose Pattern

Use a three-part placement:

1. Name the real constraint or decision.
2. Mention the partner as one possible route, comparison point, or source.
3. Put a plain disclosure immediately after the link paragraph.

For Markdown or MDX articles, prefer a short blockquote or note directly after the paragraph with the links:

`> **Disclosure:** The links above are paid affiliate/referral links. If readers buy through them, [publisher/site/project] may earn a commission at no extra cost to them.`

Replace `[publisher/site/project]` with the actual publishing brand or use `we` when the article voice already makes the publisher clear. Do not hardcode a product or publisher name in reusable guidance.

Add a short terms caveat when offers, regions, discounts, referral codes, or availability are mentioned:

`Check final terms on the partner page because offers and availability can change.`

## Claims

- Avoid `best`, guaranteed savings, guaranteed performance, medical, financial, or outcome claims unless the affiliate profile and source material support them.
- Do not mention discount values, referral rewards, codes, or eligibility unless verified from the current affiliate profile, source material, or product repo data.
- Treat affiliate profiles, project support-offer data, and verified partner pages as claim sources, not as copy to paste.
- If a partner URL is dead, soft-404s, redirects to an unrelated page, or requires a missing code to be useful, omit it until the link is fixed.

## Review Gate

- Run `affiliate-compliance-review` whenever a draft includes affiliate links and the skill is available in the session.
- The draft is not ready if the affiliate pass flags missing disclosure, unsupported offer claims, awkward insertion, or unclear commercial relationship.
- Style review, tone review, and Ramsay review must treat bolted-on affiliate paragraphs as blocking content issues, not harmless monetization notes.
