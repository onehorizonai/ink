# Email Sequence Format Playbook

Use this format for multi-email nurture, onboarding, event, sales, partner, customer-success, or education sequences. Load `../channels/email.md`. Use `email-cold-outreach.md` for unsolicited B2B outreach.

## Source Guidance

- Google, Yahoo, and Microsoft sender requirements: https://support.google.com/a/answer/81126, https://senders.yahooinc.com/best-practices/, and https://sendersupport.olc.protection.outlook.com/pm/policies
- FTC CAN-SPAM guide: https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business
- Mailchimp subject, preview, and deliverability guidance: https://mailchimp.com/help/best-practices-for-email-subject-lines/, https://mailchimp.com/help/about-preview-text/, and https://mailchimp.com/resources/email-content-for-deliverability/
- Apple Mail Privacy Protection: https://www.apple.com/legal/privacy/data/en/mail-privacy-protection/

## Use Cases

- Welcome, nurture, educate, onboard, invite, re-engage, trial-assist, sell, follow up after events, or coordinate partners/customers.
- Move a known audience from one state to another over time without repeating the same ask.

## Required Inputs

- Audience, permission state, entry trigger, exit criteria, cadence, sequence length, and success metric.
- Desired behavior per step, offer/proof, segmentation, exclusions, and suppression logic.
- Sender identity, CTA destination, legal/compliance constraints, and manual ESP owner.

## Output Shape

- Sequence map: step, timing, trigger, audience state, goal, subject, preview, body, CTA, exit rule.
- Full body copy for each email or modular snippets when the user asks for a brief.
- Variant ideas, reply handling, manual setup notes, and metrics.

## Copy And Creative Rules

- Every email needs a distinct job. Do not resend the same argument with a new subject line.
- Sequence from orientation to value to proof to action to reminder or closure.
- Keep CTAs consistent enough to avoid confusion, but vary supporting reasons.
- Use trigger context early: why the recipient is getting this now.
- Include stop conditions: converted, replied, opted out, bounced, inactive, wrong segment, or event date passed.
- Make each message useful if read alone.

## Psychological Levers

- Commitment: ask for smaller steps before larger ones.
- Ability: reduce effort with templates, links, examples, or one-click actions.
- Timing: use the trigger moment while motivation is real.
- Social proof: introduce it when the recipient needs confidence.
- Reactance reduction: avoid pressure and preserve choice.

## Platform Adaptation

- Nurture: teach and build belief before conversion.
- Onboarding: remove friction and point to the next product action.
- Event: register, prepare, attend, replay, and follow up with a logical arc.
- Sales: focus on buyer problem, proof, objections, and reply paths.
- Customer success: drive adoption, renewal, expansion, or risk recovery.

## Variants And Testing

- Test sequence length, cadence, first-email angle, proof type, CTA, and segmentation.
- Measure conversion by step, reply rate, click rate, unsubscribes, complaints, bounces, time-to-action, and downstream revenue or activation.
- Analyze where recipients exit or stall before changing copy.

## Review Checklist

- Entry trigger, permission state, cadence, and exit rules are explicit.
- Each email has a unique role and one primary CTA.
- Compliance, unsubscribe, suppression, and sender identity are addressed.
- The sequence does not continue after conversion, opt-out, negative reply, or hard bounce.
- Manual ESP configuration and analytics tasks are listed.

## Failure Diagnostics

- High first-email drop-off: weak trigger relevance or misleading subject.
- Mid-sequence fatigue: too many emails, repeated value, or cadence too tight.
- Low conversion: CTA too high-friction or proof introduced too late.
- High opt-outs: list expectation mismatch or commercial pressure.

## Anti-Patterns

- "Just checking in" repeated across steps.
- Multiple CTAs in every email.
- No suppression or exit logic.
- Sending nurture to people who need transactional support.
- Treating the sequence as a Content Program's reusable rules instead of a format.
