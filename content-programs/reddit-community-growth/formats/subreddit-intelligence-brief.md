# Subreddit Intelligence Brief

Use this format before any Reddit post, comment campaign, or DM workflow.

## Required Inputs

- Product/business and audience.
- Campaign goal and acceptable ask.
- Seed topics, keywords, competitors, alternatives, pain points, and phrases.
- Sender identity and affiliation disclosure needs.
- Known posting-account status: account age, total karma, subreddit-specific karma, local comment karma, prior participation, recent removals, and posting-frequency limits when available.
- Hard exclusions and risk boundaries.

## Output Shape

- Ranked subreddit shortlist with fit, activity, audience, and recommended motion.
- Rule snapshot for each finalist: date checked, rules URL/source, account eligibility gates, link policy, self-promotion policy, required flair, megathread requirements, modmail recommendation, and removal risk.
- Recent winning patterns: title styles, body structures, comment behavior, debates, and topics to avoid.
- Keyword and thread opportunity map: phrases to search, thread types to monitor, and intent signals.
- Promotion ladder recommendation: no mention, principle mention, disclosed mention, allowed link, or approved promotional post.
- DM eligibility: excluded, permission-gated, or direct-invitation-only.
- Writer handoff using the `reddit-research` field labels when drafting comes next.

## Checks

- Do not recommend a subreddit only because it is large.
- Do not mark links as allowed unless rules or recent norms support it.
- Do not mark posting or exact repost/share as available when the current account fails a known account-age, karma, local-karma, local-comment-karma, or participation gate.
- Do not recommend DMs as a default motion.
- If no subreddit fits safely, say so and stop.
