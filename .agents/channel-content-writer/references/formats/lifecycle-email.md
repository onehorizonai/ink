# Lifecycle Email Format Playbook

Use this format for behavior-triggered, account-triggered, lifecycle, onboarding, activation, reactivation, retention, renewal, and expansion emails. Load `../channels/email.md`.

## Source Guidance

- Google, Yahoo, and Microsoft sender requirements: https://support.google.com/a/answer/81126, https://senders.yahooinc.com/best-practices/, and https://sendersupport.olc.protection.outlook.com/pm/policies
- Mailchimp deliverability and email content guidance: https://mailchimp.com/resources/email-content-for-deliverability/
- Apple Mail Privacy Protection: https://www.apple.com/legal/privacy/data/en/mail-privacy-protection/
- FTC CAN-SPAM guide: https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business

## Use Cases

- Welcome new users, complete setup, recover abandoned actions, educate trial users, announce relevant product changes, prevent churn, prompt renewal, win back inactive users, or expand usage.

## Required Inputs

- Trigger, audience state, product behavior, data available, desired next action, and business goal.
- Timing, frequency cap, exclusion/suppression logic, personalization fields, support resources, reply/support owner, and any cross-channel escalation plan.
- Whether the message is transactional, relationship, marketing, or mixed.

## Output Shape

- Trigger summary and audience state.
- Subject, preview, body, CTA, fallback copy, and optional variants.
- Personalization/data fields and guardrails for missing data.
- Manual automation setup, QA, and metrics notes.
- Cross-channel caveats when the flow proposes SMS, WhatsApp, push, or in-app escalation.

## Copy And Creative Rules

- Start from what just happened or what the user is trying to do.
- Make the next action easier than it was before the email arrived.
- Use product-specific language, screenshots, docs links, or examples when they reduce friction.
- Keep promotional content subordinate to the lifecycle moment.
- Avoid shaming inactive users. Use helpful context and clear value.
- For renewal/risk messages, be direct, specific, and useful.
- Include support paths when friction or confusion is likely.
- Do not escalate to SMS, WhatsApp, push, or another direct channel merely to chase higher opens. Use another channel only when the user opted in for that channel, the message category fits that channel, and the escalation helps the user's current task.

## Psychological Levers

- Ability: simplify the next step with direct links, clear instructions, and small actions.
- Timeliness: trigger messages work because the need is recent or predictable.
- Progress: show what is complete and what remains.
- Loss aversion: use only when the consequence is real and stated calmly.
- Autonomy: let users choose a route such as finish setup, learn more, snooze, or contact support.

## Platform Adaptation

- Onboarding: orient, activate, and build habit.
- Trial: move from "trying" to "seeing value" with proof and guidance.
- Reactivation: remind users of unfinished value, not just discounts.
- Renewal: clarify value received, risk of lapse, and next steps.
- Expansion: use behavior-based fit, not generic upsell pressure.
- Cross-channel lifecycle: load the relevant direct/product format guide before drafting channel-specific copy, especially `sms-whatsapp.md`, `push-notification.md`, or `in-app-message.md`.

## Variants And Testing

- Test trigger timing, subject, value framing, CTA, help content, personalization depth, and frequency cap.
- Measure activation, feature adoption, task completion, reactivation, renewal, expansion, support deflection, opt-outs, and complaints.
- Review by segment and trigger, not only aggregate performance.

## Review Checklist

- Trigger and audience state are explicit.
- The copy uses available product context accurately and safely.
- Missing personalization fields have fallback behavior.
- Transactional versus marketing status is flagged.
- Suppression, frequency, support, and manual automation tasks are included.
- Any direct-message escalation has a documented opt-in, channel fit, opt-out path, and manual configuration owner.

## Failure Diagnostics

- Low action rate: trigger is wrong, CTA too vague, or email arrives too late.
- High support tickets: instructions unclear or product state mismatched.
- High opt-outs: marketing pressure exceeds relationship context.
- Low retention: email solves communication but not product value.
- Cross-channel complaints: escalation was unexpected, too interruptive, or missing channel-specific consent.

## Anti-Patterns

- Generic nurture emails pretending to be triggered.
- Personalization that exposes creepy or sensitive data.
- "We miss you" without a useful reason to return.
- Upselling before activation.
- No fallback for missing or stale product data.
- Using WhatsApp, SMS, or push as an open-rate hack instead of a consented lifecycle channel.
