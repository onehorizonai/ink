---
name: content-humanizer
description: Remove AI tells from drafts early in the review loop while keeping the intended meaning, stance, and voice. Use when Codex has a raw content draft such as a LinkedIn post, blog article, reply, or other editorial copy and needs a first cleanup pass before tone, style, and fact review.
---

# Content Humanizer

Use this as one of the first passes after a raw draft exists.

## Read

- the active writer skill's workflow file
- the active writer skill's review-passes file
- the resolved author's `Profile` One Horizon context doc if you need a voice anchor

## Scope

- remove obvious AI writing patterns
- preserve meaning
- preserve the intended stance
- keep the writing compatible with the saved voice in the active corpus

## Priorities

- remove em dashes
- remove canned “thought-leader” phrasing
- remove filler transitions
- break mechanical symmetry
- keep some texture and edge when the draft supports it
- turn listy scaffolding back into prose when the active format is an article
- do not flatten the writing into generic corporate prose

## Do Not Do

- do not fact-check here
- do not rebuild the whole draft unless it is unusable
- do not make the CTA stronger just because the prose got cleaner
- for blog articles, do not scrub away the sharper editorial edge into safe SaaS copy

## Output

Return:

- the revised draft
- a short note on the biggest AI tells removed
