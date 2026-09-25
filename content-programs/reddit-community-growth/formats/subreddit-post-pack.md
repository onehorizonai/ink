# Subreddit Post Pack

Use this format for standalone Reddit posts after subreddit rules and recent norms are known.

## Required Inputs

- Target subreddit and rule snapshot.
- Audience inside that subreddit.
- Recommended angle and reason it belongs there.
- Link, screenshot, flair, and CTA permissions.
- Account eligibility gates and whether the posting account meets them.
- Adjacent subreddit candidates and whether the finished post can be shared there unchanged through Reddit's repost/share feature.
- Campaign goal and safe ask.

## Output Shape

- Target subreddit.
- Rules and risk notes.
- Link and CTA decision.
- Optional modmail permission draft when rules are unclear.
- Title options or one final title, depending on the run request.
- Body draft.
- First-comment draft only when the subreddit format makes that useful and allowed.
- Simple repost/share targets per draft: target subreddit, why the exact post fits unchanged, account eligibility, account posture, link/media compatibility, rule notes, and timing/cadence limit.
- Not-simple-repost notes: subreddits that are relevant but require edits, removed links, a megathread/comment, mod approval, more account/community karma, a different account, or a different disclosure.
- Follow-up reply notes for likely objections or questions.

## Checks

- The post must be useful without a link.
- The title should sound native to the subreddit, not like ad copy.
- Product affiliation must be disclosed before or at the product mention.
- Product Hunt goals must ask for visits, comments, tries, or feedback, never upvotes.
- Review goals must ask actual users for honest reviews only.
- Do not copy-paste posts across communities. Exact repost/share is allowed only for listed simple targets and must stay low-volume.
- Only mark a subreddit as a simple repost/share target when the exact post can be shared unchanged.
- If the posting account does not meet a known account-age, karma, local-karma, local-comment-karma, or participation gate, the subreddit is not a simple repost/share target yet.
- If a subreddit needs any rewrite, different link, different account posture, thread-only placement, mod approval, or account warm-up, it is not a simple repost/share target.
- If no exact target is safe, output `None`.
