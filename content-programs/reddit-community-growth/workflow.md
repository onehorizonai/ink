# Workflow

## Inputs

- Product, business, software project, community, launch, or offer.
- Audience and relevant problem spaces.
- Campaign goal: feedback, Product Hunt visit/comment, honest review, download, website visit, support, awareness, or qualified conversation.
- Hard boundaries: no links, no product mention, no DMs, only mod-approved posts, no competitor claims, no medical/financial claims, or no review asks.
- Sender identity: founder, employee, brand account, personal account, community member, or support owner.
- Known account status: account age, total karma, subreddit-specific karma, local comment karma, prior participation, recent removals, and posting-frequency limits when available.

## Steps

1. Resolve the active Ink profile and load relevant context.
2. Run `reddit-research` to generate seed queries, discover subreddits, inspect rules, capture account eligibility gates and link policy, analyze recent top posts, and map keyword/thread opportunities.
3. Classify each subreddit by allowed motion: post, comment-only, warm-up required, weekly thread, mod-approved only, app/showcase thread, permission-gated DM, or skip.
4. For standalone posts, draft one subreddit-specific title/body with `reddit-social-writer`, then add an exact repost/share target map that lists only subreddits where the same post can be shared unchanged through Reddit's repost/share feature.
5. For comment engagement, create if/then opportunity patterns and draft replies only after a real thread, post, or comment context is supplied.
6. For DMs, draft a public permission reply first. Draft one manual DM only after explicit opt-in or direct invitation.
7. Run safety review before any promotional link, review ask, Product Hunt ask, download CTA, website CTA, or DM.
8. Publish, comment, send modmail, or send opted-in DMs manually.
9. Track only real outcomes in `performance.csv` when provided.

## Guardrails

- Do not ask for Product Hunt upvotes. Ask for visits, comments, tries, or feedback.
- Do not ask for positive reviews. Ask actual users for honest reviews only.
- Do not include product links where rules are unclear.
- Do not reuse the same post or comment across multiple subreddits.
- Do not post, repost, or share into a subreddit when the posting account does not meet known account-age, karma, local-karma, local-comment-karma, or prior-participation gates.
- Do not label a target "simple repost/share" if it requires edits, removed links, a different thread format, mod approval, more local karma, or a different account posture.
- Keep simple repost/share low-volume so it does not become repeated mass posting.
- Do not pretend to be unaffiliated.
- Do not automate Reddit posts, comments, voting, scraping, chat requests, private messages, or follow-ups.
- Do not DM unless the user opted in or directly invited private follow-up.
- Do not follow up on a DM if ignored.
- If moderators do not answer modmail, treat that as no approval.

## Output Bundle

Each run should include:

- `brief.md`: product, audience, goals, constraints, seed keywords, and target communities.
- `outputs.md`: research tables, post drafts, exact repost/share targets, comment playbooks, permission replies, DM drafts, and modmail copy.
- `review-notes.md`: rules checked, link/CTA decision, disclosure notes, Product Hunt/review safety, DM opt-in evidence, and skip reasons.
- `handoff.md`: manual posting/sending steps, owners, timing, and performance fields to capture.
