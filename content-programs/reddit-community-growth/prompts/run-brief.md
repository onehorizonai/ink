# Run Brief Prompt

```text
Create a <format_id> for Reddit community growth.

Inputs:
- product/business:
- audience:
- campaign goal:
- safe ask:
- target subreddits if known:
- seed keywords/topics:
- thread URL or pasted thread context if this is a comment or DM run:
- sender identity:
- known account status:
- hard constraints:

Return:
- run_id
- format_id
- target subreddit(s)
- rules and risk notes
- account eligibility gates and whether the posting account currently meets them
- keyword/thread opportunities
- draft outputs
- exact repost/share targets for every standalone post draft, or `None`
- relevant-but-not-simple-repost exclusions when useful
- link/CTA decision
- disclosure notes
- DM eligibility and opt-in evidence when relevant
- manual posting/sending handoff
- metrics to capture

Constraints:
- resolve the active Ink profile first
- route discovery and rules through reddit-research
- route drafts through reddit-social-writer
- read Reddit promotion guardrails for any product, business, launch, review, download, website, Product Hunt, or DM goal
- do not automate posting, commenting, voting, scraping, chat requests, DMs, or follow-ups
- only recommend Reddit repost/share targets where the exact post can be shared unchanged without obvious rule or format conflicts
- do not recommend posting or exact repost/share where the current account does not meet known account-age, karma, local-karma, local-comment-karma, or prior-participation gates
- do not mass-share the same post across many communities
- do not ask for Product Hunt upvotes
- ask actual users for honest reviews only
- draft DMs only after explicit opt-in or direct invitation, or draft the public permission reply first
```
