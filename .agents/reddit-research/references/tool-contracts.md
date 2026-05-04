# Reddit Tool Contracts

Use the exact tool names and argument shapes below. Do not invent fields, rename fields, or pass pseudo-JSON.

## `reddit_find_subreddits`

Use for audience or topic-based subreddit discovery.

Minimal example:

```json
{
  "query": "b2b saas founders",
  "limit": 5,
  "sort": "relevance"
}
```

Rules:

- `query` is required.
- `limit` must be an integer from 1 to 10.
- `sort` must be `relevance` or `activity`.

## `reddit_subreddit_details`

Use for rules, posting guidance, subscriber scale, and submission constraints.

Minimal example:

```json
{
  "subreddit": "startups"
}
```

Rules:

- Pass the subreddit name only. Do not pass `/r/startups`.
- Use this before recommending a subreddit as the final target.

## `reddit_top_posts`

Use for the strongest recent posts in a subreddit.

Minimal example:

```json
{
  "subreddit": "startups",
  "limit": 5,
  "sort": "top",
  "timeframe": "week"
}
```

Rules:

- `subreddit` is required.
- `limit` must be an integer from 1 to 10.
- `sort` must be one of `top`, `hot`, `new`, `rising`, `controversial`.
- `timeframe` must be one of `hour`, `day`, `week`, `month`, `year`, `all`.

## `reddit_search_posts`

Use for topic-specific post search inside one subreddit.

Minimal example:

```json
{
  "subreddit": "startups",
  "query": "AI outreach",
  "limit": 5,
  "sort": "relevance",
  "timeframe": "month"
}
```

Rules:

- `subreddit` and `query` are required.
- `sort` must be one of `relevance`, `top`, `new`, `comments`.
- `timeframe` must be one of `hour`, `day`, `week`, `month`, `year`, `all`.

## `reddit_post_thread`

Use for reading one post plus its comments before drafting a reply.

Minimal example:

```json
{
  "url": "https://old.reddit.com/r/startups/comments/1spr3p8/the_10_things_i_wish_i_knew_when_starting_my_1st/",
  "comment_limit": 6,
  "comment_sort": "best"
}
```

Rules:

- `url` is required and can be a full Reddit URL or permalink.
- `comment_limit` must be an integer from 1 to 20.
- `comment_sort` must be one of `best`, `top`, `new`, `controversial`, `old`, `qa`.

## Handoff Requirement

When `reddit-research` hands work to `reddit-social-writer`, the handoff must include these fields explicitly:

- `target_subreddit`
- `audience`
- `recommended_angle`
- `title_or_opener_direction`
- `rules_and_guardrails`
- `close_style`
- `example_posts`

Do not hand off a vague paragraph when these fields can be stated directly.
