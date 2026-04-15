# Workflow

## 1. Clarify the content job

Capture:

- goal
- audience
- timing window
- channel constraint if any
- product area or theme
- required source, launch, event, or claim if any

If the goal, audience, or timing is unclear, ask at most 3 short questions total for this workflow.

## 2. Load the minimum context

Start with `../../context/index.md`.

Load:

- `.local/context/profile.md` for voice and identity basics
- `.local/context/current-work.md` for the active company, positioning, audience, and safe themes
- `.local/context/work-history.md` only when founder background or credibility is part of the angle

Do not load personal files just because they exist.

## 3. Check the archive first

- Search the LinkedIn corpus in `../../content/linkedin/posts/`.
- If blog is a possible channel, read `../../context/blog-publishing.md` and `../../../.local/context/blog-publishing.local.md`.
- If the local file is missing, ask the user for the existing blog articles folder and create the local file before scanning blog coverage.
- If `source_articles_dir` is `[unset]` or missing on disk, ask the user for the existing blog articles folder and update the local file before scanning blog coverage.
- Search the configured blog source folder for the same keywords, adjacent concepts, launches, and recent dates.
- Pull 3-6 relevant examples total across blog and LinkedIn.
- Note repeated angles, under-covered areas, and any very recent post you should not cannibalize.
- Prefer recent examples when the voice or positioning may have shifted.

## 4. Build a seed list

- Derive 5-10 seed phrases from the goal, the current-work themes, and any current event already in play.
- Prefer phrases specific enough to test, such as `spec-driven development`, `roadmap-first AI development`, `AI coding task context`, `engineering standup automation`, or `trust-first work capture`.
- Avoid broad consumer terms that mostly return unrelated noise.

## 5. Research current signals

- Use `google_trends_keyword_insights` on the best 2-5 seeds.
- Use `google_trends_trending_searches` only to discover timely hooks within the target geography.
- Use `web_search` and `fetch_page` to verify what the signal actually refers to.
- Prefer primary docs, vendor announcements, canonical essays, and credible reporting over generic summaries.

## 6. Turn signals into content angles

For each candidate:

- write the claim in one sentence
- explain why now
- explain why the team can credibly say it
- decide whether it should be a LinkedIn post or a blog article
- list proof, examples, screenshots, or sources still needed

## 7. Rank and narrow

Score ideas against:

- goal fit
- audience fit
- freshness
- uniqueness versus the archive
- proof availability
- channel fit

Cut anything that depends on hype, weak evidence, or a point of view the repo does not own.

## 8. Handoff

- Pick one recommended idea.
- Write a short handoff brief with format, audience, goal, thesis, proof points, sources, and CTA or next step.
- Route to `../../blog-post-writer/SKILL.md` or `../../linkedin-social-writer/SKILL.md` once the user picks a direction.
