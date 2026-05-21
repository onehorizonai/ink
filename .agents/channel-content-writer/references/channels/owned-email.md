# Owned And Email Channel Family Guidance

Use this family guide for owned surfaces such as newsletters, email sequences, lifecycle email, docs, changelog, help center, and other company-controlled publishing surfaces.

## Source Guidance

- Google, Yahoo, and Microsoft sender requirements: https://support.google.com/a/answer/81126, https://senders.yahooinc.com/best-practices/, and https://sendersupport.olc.protection.outlook.com/pm/policies
- FTC CAN-SPAM, ICO B2B marketing, and CASL guidance: https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business, https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/, and https://crtc.gc.ca/eng/com500/guide.htm
- Mailchimp preview text, subject line, and deliverability guidance: https://mailchimp.com/help/about-preview-text/, https://mailchimp.com/help/best-practices-for-email-subject-lines/, and https://mailchimp.com/resources/email-content-for-deliverability/
- Product communication and changelog guidance: https://www.intercom.com/blog/what-is-a-changelog/ and https://docs-style-guide.unity.com/content-types/release-notes

## Native Behavior

- Owned channels depend on trust. The audience expects relevance because the company controls the send or publish surface.
- Email competes inside an inbox; docs/help-center compete with a user's task; changelog/release notes compete with attention after a product change.
- Permission state changes the copy. Subscriber email, lifecycle email, cold outreach, transactional email, docs, and release notes are different modes.
- Owned content often has a longer half-life than social. Avoid short-term hype that ages badly.

## Audience And Context Rules

- Classify the audience relationship: subscriber, prospect, user, customer, trial user, admin, developer, partner, buyer, support seeker, or public visitor.
- Name the reader's intent: learn, decide, fix, activate, renew, upgrade, discover a change, or complete a workflow.
- Identify whether the message is expected, triggered, editorial, commercial, operational, or cold.
- Use the selected profile's source of truth for facts, product names, pricing, customer proof, and publishing boundaries.
- Load `channels/email.md` for email-specific deliverability and compliance.

## Creative Strategy

- Put the main value where the reader first looks: subject/preview text for email, title/summary for docs, headline/date/category for changelog.
- Use plain language and active structure. Owned content should reduce uncertainty, not showcase copywriting.
- Use links to deepen, not to replace, the core explanation.
- For docs and help center, optimize for task completion: prerequisites, steps, expected result, edge cases, and related links.
- For product updates, write what changed, who it affects, why it matters, and what to do next.
- For email, align the subject, preview text, opening, body, and CTA. Each field should add information instead of repeating itself.

## Compliance And Risk

- For email, flag consent, unsubscribe, physical address/company identity, suppression, authentication, list source, and jurisdiction risks.
- For docs/help content, flag inaccurate product behavior, obsolete UI labels, unsupported workarounds, privacy/security implications, and missing screenshots.
- For changelog/release notes, flag unreleased features, feature-flag confusion, internal-only changes, customer names, and legal/contractual claims.
- Do not use owned channels to hide promotional material in operational or transactional messages.

## Manual Boundary

Ink can draft copy, subject lines, preview text, metadata, docs outlines, changelog entries, QA notes, and review packages. Sending, publishing, CMS edits, email-platform configuration, segmentation, product verification, support-center updates, and analytics remain manual unless a real tool is available.

## Metrics

- Email: replies, clicks, conversions, unsubscribes, spam complaints, bounces, positive reply rate, and downstream activation or pipeline.
- Docs/help: search success, task completion, support deflection, bounce rate, feedback votes, and support-ticket references.
- Changelog: views, feature adoption, clicks to docs, user feedback, support volume change, and sales/customer-success usage.

## QA Checklist

- Permission/relationship state is explicit.
- The output has one primary reader job.
- Critical facts are verified against source-of-truth context.
- Email risks are separated from docs/release-note risks.
- Manual publishing/sending/configuration steps are not implied as done.
- The copy can be understood without internal context.

## Anti-Patterns

- Treating every owned surface as a marketing blast.
- Writing release notes like PR descriptions.
- Turning docs into thought leadership.
- Using preview text as a duplicate subject line.
- Sending email before authentication, suppression, or list quality is known.
- Hiding important limitations or breaking changes behind vague benefit copy.
