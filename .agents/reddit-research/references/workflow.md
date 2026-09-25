# Workflow

## 1. Build the research brief

Capture:

- audience
- topic, product, or discussion area
- goal of the Reddit presence
- hard boundaries such as no links, no product mention, or no self-promo
- intended motion: subreddit post, comment engagement, DM follow-up, or mixed
- campaign ask, such as feedback, Product Hunt visit/comment, honest review, download, website visit, or support
- known posting-account status, such as account age, total karma, subreddit-specific karma, local comment karma, prior participation, recent removals, and posting-frequency limits
- whether the next step is drafting or just research

## 2. Ask only if the research would be misleading

Ask only when the audience, topic, or promotional boundary is missing and cannot be recovered from One Horizon context docs or the prompt.

High-value questions:

- Who is this Reddit content meant to reach?
- What can or cannot be mentioned?
- Are we looking for broad community fit or one post angle right now?

## 3. Load the minimum user context

Resolve the active Ink profile with `../../one-horizon-context-setup/references/ink-profile-contract.md`, then resolve the author and load only the relevant author-scoped One Horizon context docs from the selected workspace. Use `../../one-horizon-context-setup/references/context-doc-templates.md` for the naming and missing-doc contract:

- `Profile` for identity basics
- `Current Work` for almost every business topic
- `Market Context` when audience fit or positioning matters
- `Work History` only when founder credibility or experience changes the angle

Use `find-documents` only to locate candidate context docs by ID, title, status, type, or excerpt. Call `get-document` for the selected `documentId` before extracting fields or treating a context doc as loaded.
If a required author-scoped context doc is missing or unusable, use `../../one-horizon-context-setup/SKILL.md` to create the missing doc through its confirmation flow before researching.
If a required One Horizon tool call is missing or fails, follow `../../one-horizon-context-setup/references/mcp-readiness.md`.

## 4. Generate seed queries

- Translate the topic into 3-5 audience or problem-space queries.
- Prefer terms real Reddit users would search for, not marketing taglines.
- Use adjacent problem statements as well as direct solution terms.
- For comment engagement, also generate phrases people would use when asking for help, comparing alternatives, complaining about existing options, or requesting recommendations.

## 5. Shortlist candidate subreddits

- Use `reddit_find_subreddits` for each high-signal seed.
- Use the exact argument shape from `tool-contracts.md`, for example:

```json
{
  "query": "b2b saas founders",
  "limit": 5,
  "sort": "relevance"
}
```

- Build a shortlist of roughly 3-6 communities.
- Prefer communities with clear relevance, visible activity, and discussion behavior that matches the goal.

## 6. Inspect rules and posting norms

- Use `reddit_subreddit_details` on each shortlisted subreddit.
- Use the exact argument shape:

```json
{
  "subreddit": "startups"
}
```

- Read the rules, posting guidance, submission type, account eligibility gates, and any obvious anti-promo language.
- Capture a rule snapshot with date, account age/karma/local karma/local comment karma requirements when known, link policy, flair or megathread requirements, self-promotion policy, modmail advice, and whether product links are allowed.
- Drop communities that clearly punish the intended style of post.
- Mark communities as warm-up-required when posting is otherwise relevant but the current account does not meet a known eligibility gate.

## 7. Analyze recent winners

- Use `reddit_top_posts` with `timeframe=week` for each finalist subreddit.
- If the topic is narrow, also use `reddit_search_posts` inside the subreddit.
- Use exact argument shapes such as:

```json
{
  "subreddit": "startups",
  "limit": 5,
  "sort": "top",
  "timeframe": "week"
}
```

```json
{
  "subreddit": "startups",
  "query": "AI outreach",
  "limit": 5,
  "sort": "relevance",
  "timeframe": "month"
}
```

- Note:
  - common hook styles
  - common post structures
  - whether posts are story-led, question-led, or opinion-led
  - what comments or debates the strongest posts tend to trigger
  - what looks overused or unwelcome

## 8. Map comment and DM opportunities

When the goal includes comment engagement, use `reddit_search_posts` for high-intent phrases inside finalist subreddits.

Classify opportunities as:

- answer-only: reply publicly with no product mention
- disclosed mention: product can be named without a link if directly relevant
- allowed link: link appears permitted and useful
- mod-approved or weekly thread only: wait for the right thread or ask moderators
- skip: promotion risk is too high

For DM eligibility, default to no DM. Mark private follow-up as permission-gated only when a public reply can ask whether DM is welcome, or allowed only after direct invitation when the user explicitly requests private details.

## 9. Produce the handoff

Return:

- ranked subreddit recommendations
- why each subreddit fits or does not fit
- rule and tone constraints
- account eligibility gates and any warm-up required before posting
- keyword and thread opportunities when relevant
- link and CTA decision
- DM eligibility decision
- post-angle opportunities
- one recommended subreddit plus a compact writing brief

If no subreddit is a credible fit, say so explicitly and stop. Do not manufacture a weak recommendation just to complete the flow.

The brief should include:

- target subreddit
- intended audience inside that subreddit
- one recommended angle
- title or opener direction
- anti-promo guardrails
- the kind of question or statement that should close the draft
- 2 or 3 example posts by URL or title

Use these field labels literally when handing off to `reddit-social-writer`:

- `target_subreddit`
- `audience`
- `recommended_angle`
- `title_or_opener_direction`
- `rules_and_guardrails`
- `close_style`
- `example_posts`
