# Email Channel Guidance

Use this channel guide for `newsletter`, `email-sequence`, `lifecycle-email`, and cold outreach handoffs. Load `owned-email.md` first, then pair this file with the relevant format guide such as `../formats/newsletter-issue.md`, `../formats/lifecycle-email.md`, or `../formats/email-cold-outreach.md`.

Ink can draft email copy, variants, follow-up plans, QA notes, and manual handoffs. Ink does not send, schedule, scrape, enrich, verify, warm up, or upload email lists unless a real integration is available and explicitly used.

## Source Guidance

- FTC CAN-SPAM guide: https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business
- Google email sender guidelines, FAQ, and Workspace sending limits: https://support.google.com/a/answer/81126, https://support.google.com/a/answer/14229414, and https://support.google.com/a/answer/166852
- Yahoo Sender Hub best practices: https://senders.yahooinc.com/best-practices/?is_listing=false
- Microsoft Outlook sender requirements: https://sendersupport.olc.protection.outlook.com/pm/policies
- ICO B2B marketing guidance: https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/
- CRTC CASL guidance: https://crtc.gc.ca/eng/com500/guide.htm
- M3AAWG sender, vetting/list-acquisition, and complaint/bounce-handling guidance: https://www.m3aawg.org/sites/default/files/doc_files/M3AAWG_Senders_BCP_Ver3-2015-02.pdf, https://www.m3aawg.org/documents/en/maawg-vetting-best-common-practices-bcp, and https://www.m3aawg.org/documents/en/m3aawg-recommendations-for-senders-handling-of-complaints
- Mailchimp subject, preview text, content deliverability, and click-tracking guidance: https://mailchimp.com/help/best-practices-for-email-subject-lines/, https://mailchimp.com/help/about-preview-text/, https://mailchimp.com/resources/email-content-for-deliverability/, and https://mailchimp.com/help/troubleshooting-click-tracking/
- Apple Mail Privacy Protection: https://www.apple.com/legal/privacy/data/en/mail-privacy-protection/

This guide is an operational guardrail, not legal advice. If jurisdiction, consent basis, data source, or suppression process is unclear, flag the risk and require human review before a campaign is considered ready to send.

## Native Behavior

- Email is a permission and trust channel before it is a copy channel. The same sentence can be welcome in a subscribed newsletter, suspicious in cold outreach, and inappropriate in a transactional email.
- The first screen is sender name, subject, preview text, and recipient expectation. Body copy cannot rescue a misleading or irrelevant inbox impression.
- Deliverability depends on authentication, reputation, complaint rate, bounce rate, list quality, suppression, and engagement. Copy improvements are secondary when the sender setup is unhealthy.
- Email is asynchronous but personal. Strong email copy feels like a specific message to a known audience, not a landing page squeezed into an inbox.
- Sender identity is part of the message. Reply-bearing mail should come from a real, monitored person or team identity; `noreply` belongs only on messages where replies are genuinely not useful and support paths are obvious.
- Provider sending limits are ceilings, not safe campaign targets. A technically allowed daily quota can still be far too aggressive for a new domain, new mailbox, weak list, cold audience, or low-trust offer.
- Open-rate measurement is noisy because privacy features can preload or hide open behavior. Use clicks, replies, opt-outs, complaints, bounces, conversions, and downstream outcomes for decisions.

## Audience And Context Rules

- Classify the send before writing: `newsletter`, `lifecycle`, `cold outreach`, `sales follow-up`, `transactional`, `event`, `support`, `partner`, or `internal handoff`.
- Name the permission state: subscribed, customer/user relationship, event registrant, existing commercial relationship, legitimate-interest style B2B outreach, explicit consent, implied consent, or unknown.
- Identify the recipient's decision context: skimming for value, trying to complete a task, evaluating a purchase, reacting to a product trigger, or deciding whether to reply.
- For newsletters, write to the list promise. Do not smuggle a sales blast into an editorial subscription.
- For lifecycle email, write to the triggering behavior or account state. Do not send generic nurture copy when the product knows exactly what happened.
- For cold outreach, use a real relevance reason and load `../formats/email-cold-outreach.md`.
- For transactional email, keep marketing secondary and clearly separated, and do not weaken the operational purpose.
- For direct-message escalation such as SMS or WhatsApp, require separate channel permission, opt-out mechanics, and local compliance review. Do not move someone to a more interruptive channel just because it may have higher open rates.

## Creative Strategy

- Align the inbox triad: sender name establishes relationship, subject names the value or task, preview text adds a second useful detail instead of repeating the subject.
- Keep body structure simple: context, value, proof or next step, single primary CTA. Add secondary links only when the format truly needs them.
- Write skimmable paragraphs. One idea per paragraph, with the most important sentence early.
- Use personalization only when it changes relevance. Merge tags that do not affect the message are not personalization.
- For promotional sends, state the offer, audience, deadline, eligibility, exclusions, and landing path plainly.
- For educational sends, make the reader smarter before asking them to click.
- For sequences, every email needs a new angle, not just a rephrased reminder.
- For HTML email, include alt text needs, plain-text fallback notes, image/link QA, and mobile preview checks.
- For cold outreach, default to plain, low-link, low-tracking copy unless the user explicitly accepts the deliverability and trust tradeoff. For subscribed marketing, normal ESP click tracking can be appropriate, but links should still be descriptive, expected, and transparent.
- Treat links as trust signals. Avoid URL shorteners, hidden redirects, unrelated tracking domains, and link text that obscures the destination.

## Compliance And Risk

- Commercial email handoffs must use truthful sender identity, routing information, reply-to, subject lines, and claims.
- Do not use fake `RE:`, fake `FWD:`, fake internal notes, fake referrals, fake deadlines, disguised advertising, or deceptive subject lines.
- Include physical/company contact identity, unsubscribe or opt-out mechanism, and suppression handling where required by send type and jurisdiction.
- Honor opt-outs and do-not-contact requests immediately in the handoff. Never draft follow-ups after an opt-out.
- Suppress hard bounces, repeated soft-failure patterns, unsubscribes, spam complaints, do-not-contact requests, previous negative replies, customers who should not receive outreach, competitors where relevant, and any recipient whose consent or relevance cannot be justified.
- For UK/EU-style B2B work, distinguish corporate subscribers from sole traders or individual subscribers, respect objections, and minimize personal data use.
- For Canada, CASL can require consent, sender identification, and unsubscribe mechanics for commercial electronic messages.
- Flag regulated claims, comparative claims, customer proof, security/privacy claims, pricing, medical/financial/legal content, and guarantees.
- For bulk or high-volume senders, flag SPF, DKIM, DMARC, one-click unsubscribe where required, TLS, spam complaint thresholds, and domain reputation checks.
- Treat new-domain ramping as a risk-control practice, not a guaranteed waiting period. Flag brand-new or dormant domains/mailboxes for conservative volume, strong authentication, clean lists, and human monitoring before any scale-up.
- Do not recommend disposable domains, mailbox replacement, domain cycling, artificial warmup networks, or other tactics designed to evade reputation systems. Separate sending domains can be legitimate for brand, product, region, or stream separation, but not for hiding unwanted mail.

## Manual Boundary

Ink may prepare copy, subject options, preview text, segmentation notes, sequence logic, QA checklists, suppression warnings, reply-handling notes, and ESP implementation instructions. A human or connected tool must perform sending, scheduling, domain authentication, list import, list verification, consent verification, unsubscribe infrastructure, testing, approvals, reply monitoring, CRM updates, and analytics capture.

## Metrics

- Primary: positive reply rate, qualified conversation rate, click rate, conversion rate, activation, purchase, meeting booked, event registration, and downstream pipeline or retention.
- Risk: spam complaint rate, hard bounce rate, unsubscribe rate, block rate, deferrals, placement problems, and negative replies.
- Diagnostic: subject/preview performance, CTA click distribution, segment-level engagement, sequence-step drop-off, device/client rendering, and reply quality.
- Operational: time to first meaningful response for positive replies, suppression processing time, list verification freshness, domain/provider placement tests, and CRM handoff completion.
- Treat opens as directional only. Apple Mail Privacy Protection can obscure whether and how often people actually opened.

## QA Checklist

- Permission state, sender identity, list source, and audience segment are explicit.
- Subject and preview text are truthful, specific, and not duplicate.
- The email has one primary job and one primary CTA.
- Claims, customer references, pricing, dates, integrations, and legal statements are verified or flagged.
- Unsubscribe, suppression, postal/company identity, and jurisdiction risks are addressed when relevant.
- Deliverability prerequisites are not implied as complete unless the user confirmed them.
- Reply-bearing mail has a monitored reply owner and a clear handoff path.
- Link/tracking choices are visible, descriptive, and appropriate for the permission state.
- New-domain, high-volume, or cold-list risks are flagged without claiming a warmup or waiting period guarantees inbox placement.
- Manual ESP, segmentation, test-send, approval, and analytics steps are listed separately from the copy.

## Anti-Patterns

- Treating opens as the main success metric.
- Writing long landing-page copy inside an email.
- Using urgency, scarcity, or personalization that is not true.
- Sending the same generic sequence to weak or bought lists.
- Hiding unsubscribe language, making opt-out awkward, or continuing after a negative reply.
- Overusing images, links, tracking, attachments, URL shorteners, and spammy punctuation.
- Reusing newsletter tone for cold outreach or cold-outreach tone for customer lifecycle email.
- Treating mailbox/domain replacement as a fix for bad targeting, complaints, or bounces.
- Using artificial warmup, spintax, or random wording variation as a substitute for real relevance and clean sending practices.
