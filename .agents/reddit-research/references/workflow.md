# Workflow

## 1. Build the research brief

Capture:

- audience
- topic, product, or discussion area
- goal of the Reddit presence
- hard boundaries such as no links, no product mention, or no self-promo
- whether the next step is drafting or just research

## 2. Ask only if the research would be misleading

Ask only when the audience, topic, or promotional boundary is missing and cannot be recovered from One Horizon context docs or the prompt.

High-value questions:

- Who is this Reddit content meant to reach?
- What can or cannot be mentioned?
- Are we looking for broad community fit or one post angle right now?

## 3. Load the minimum user context

Resolve the author and load only the relevant author-scoped One Horizon context docs. Use `../../one-horizon-context-setup/references/context-doc-templates.md` for the naming and missing-doc contract:

- `Profile` for identity basics
- `Current Work` for almost every business topic
- `Market Context` when audience fit or positioning matters
- `Work History` only when founder credibility or experience changes the angle

If a required author-scoped context doc is missing or unusable, use `../../one-horizon-context-setup/SKILL.md` to create the missing doc through its confirmation flow before researching.
If a required One Horizon tool call is missing or fails, follow `../../one-horizon-context-setup/references/mcp-readiness.md`.

## 4. Generate seed queries

- Translate the topic into 3-5 audience or problem-space queries.
- Prefer terms real Reddit users would search for, not marketing taglines.
- Use adjacent problem statements as well as direct solution terms.

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

- Read the rules, posting guidance, submission type, and any obvious anti-promo language.
- Drop communities that clearly punish the intended style of post.

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

## 8. Produce the handoff

Return:

- ranked subreddit recommendations
- why each subreddit fits or does not fit
- rule and tone constraints
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
