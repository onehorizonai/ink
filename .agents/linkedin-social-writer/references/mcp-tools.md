# Local MCP Tools

## Server

The local stdio MCP server lives at:

- `mcp/social-research/server.py`

## Tools

### `web_search`

Use for:

- finding sources to verify claims
- finding primary pages about public announcements
- narrowing a fact-check query with a `site:` filter

Inputs:

- `query`
- `max_results`
- `site` optional

### `fetch_page`

Use for:

- pulling readable text from a source page
- checking whether a source actually supports a claim

Inputs:

- `url`
- `max_chars`

### `search_unsplash`

Use for:

- finding quick candidate images for a post concept or asset brief
- gathering photographer and photo page links
- fallback inspiration when a dedicated image MCP server is unavailable

Inputs:

- `query`
- `per_page`
- `page`
- `orientation` optional

### `google_trends_trending_searches`

Use for:

- scanning daily Google Trends topics by geography
- finding timely hooks before reacting on LinkedIn
- spotting whether a current event is big enough to warrant a content angle

Inputs:

- `geo`
- `max_results`
- `query` optional

### `google_trends_keyword_insights`

Use for:

- testing whether a seed topic is rising or flattening
- finding related queries and adjacent phrasing around a theme
- checking which regions are showing stronger relative interest

Inputs:

- `keyword`
- `geo`
- `timeframe`
- `max_related`
- `max_points`

Note:

- This uses Google Trends web endpoints, not an official public API. It can rate-limit. If it fails, fall back to `web_search`.

### `reddit_find_subreddits`

Use for:

- finding subreddits that match an audience, niche, or problem space
- building a shortlist before inspecting rules and top posts
- comparing subscriber scale and activity across likely communities

Inputs:

- `query`
- `limit`
- `sort` optional

### `reddit_subreddit_details`

Use for:

- checking a subreddit's title, description, subscriber scale, and posting mode
- loading posting guidance and subreddit rules before drafting
- confirming whether a subreddit is a bad fit for promotional or link-heavy posts

Inputs:

- `subreddit`

### `reddit_top_posts`

Use for:

- pulling the top posts from a subreddit over the last day, week, month, or longer
- identifying recurring hooks, formats, and discussion triggers
- spotting whether the subreddit rewards text posts, link posts, stories, or debates

Inputs:

- `subreddit`
- `limit`
- `sort` optional
- `timeframe` optional

### `reddit_search_posts`

Use for:

- finding topic-specific posts inside a shortlisted subreddit
- checking whether a seed angle already appears often in that community
- collecting examples closer to the user's topic than the general top posts

Inputs:

- `subreddit`
- `query`
- `limit`
- `sort` optional
- `timeframe` optional

### `reddit_post_thread`

Use for:

- reading a post plus its top comments before drafting a reply
- checking what kind of follow-up discussion the community rewards
- validating whether a proposed angle or question would fit the thread energy

Inputs:

- `url`
- `comment_limit` optional
- `comment_sort` optional

## When to use the tools

- Use `web_search` and `fetch_page` from the fact-check pass.
- Use `search_unsplash` when the user wants quick visual inspiration or a fallback candidate image source.
- Do not use `search_unsplash` as the primary final-asset path for blog posts when the dedicated `blog-image-finder` MCP tools are available.
- Use `google_trends_keyword_insights` when testing content angles, phrasing, or adjacent topics before drafting.
- Use `google_trends_trending_searches` when looking for a timely hook in a specific geography.
- Use the Reddit tools from `reddit-research` and `reddit-social-writer` when the user wants subreddit discovery, weekly top-post analysis, topic-specific subreddit examples, or thread-aware Reddit replies.
- Do not use web search for stable personal context that should come from One Horizon context docs.
- Do not let mass-market or celebrity trends dictate B2B content unless the connection is real.
