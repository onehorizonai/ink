# Docs, Changelog, And Help Center Format Playbook

Use this format for docs pages, changelog entries, release notes, help-center articles, support macros, and product update content. Load `../channels/owned-email.md` first.

## Source Guidance

- Unity release notes style guide as a practical release-note reference: https://docs-style-guide.unity.com/content-types/release-notes
- Intercom changelog guidance: https://www.intercom.com/blog/what-is-a-changelog/
- Google developer documentation style guidance can inform clear task docs: https://developers.google.com/style
- FTC guidance for claims and endorsements if customer quotes or marketing claims appear: https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides

## Use Cases

- Help users complete a task, understand a release, troubleshoot, adopt a feature, or evaluate a change.
- Turn product changes into durable support, customer-success, and self-serve assets.

## Required Inputs

- Content type, audience, product/version, source-of-truth behavior, screenshots, release date, and owner.
- Task goal, prerequisites, steps, expected result, edge cases, known issues, and related links.
- What changed, who is affected, migration/breaking-change risk, and support path.

## Output Shape

- For docs/help: title, summary, prerequisites, steps, expected result, troubleshooting, related links, and metadata.
- For changelog/release notes: date/version, category, change summary, user impact, action required, docs/support links.
- Manual verification and publishing QA.

## Copy And Creative Rules

- Optimize for task completion before brand voice.
- Use exact UI labels, product names, versions, and commands.
- Write steps in the order users perform them.
- Put prerequisites and limitations before the user starts.
- For changelogs, explain user impact, not internal implementation trivia.
- Separate new, improved, fixed, deprecated, and breaking changes.
- Avoid clever headings in support content; searchability matters.

## Psychological Levers

- Certainty reduces support burden.
- Progress cues help users complete tasks.
- Trust grows when limitations and known issues are clear.
- Reciprocity: useful docs make product communication feel respectful.
- Agency: give next steps, alternatives, and support routes.

## Platform Adaptation

- Docs: precise, complete, version-aware, and searchable.
- Help center: problem-led, plain-language, and support-deflecting.
- Changelog: concise, chronological, categorized, and customer-impact focused.
- Release notes: include fixes and breaking changes without burying risks.
- Developer docs: code accuracy and command verification matter more than persuasion.

## Variants And Testing

- Test titles, summaries, article structure, screenshots, and related links.
- Track search success, article helpfulness, support-ticket deflection, task completion, clicks to related docs, and feedback.
- Use support tickets and sales/customer-success questions as source material for improvements.

## Review Checklist

- Product behavior and UI labels are verified.
- The page answers who, what, when, why, and what to do next.
- Steps, screenshots, links, limitations, and support path are included.
- Internal-only details, unreleased features, and sensitive data are removed.
- Manual publish and maintenance owner are clear.

## Failure Diagnostics

- Support tickets persist: article is hard to find, incomplete, or does not match real UI.
- Users fail task: missing prerequisite, unclear step, wrong screenshot, or edge case omitted.
- Changelog ignored: impact unclear or buried under implementation language.
- Trust issue: breaking changes or limitations hidden.

## Anti-Patterns

- Writing docs like marketing copy.
- Writing release notes like commit logs.
- Omitting prerequisites.
- Hiding breaking changes.
- Publishing product instructions without verification.
