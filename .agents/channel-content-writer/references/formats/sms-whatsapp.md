# SMS And WhatsApp Format Playbook

Use this format for SMS, MMS, RCS-style short messages, WhatsApp Business messages, reminders, alerts, promotions, and conversational follow-ups. Load `../channels/direct-product.md` first.

## Source Guidance

- Twilio Messaging Policy, updated April 13, 2026: https://www.twilio.com/en-us/legal/messaging-policy
- Twilio US SMS guidance and consent resources: https://www.twilio.com/en-us/guidelines/us/sms and https://www.twilio.com/docs/verify/consent-opt-in
- WhatsApp Business Messaging Policy: https://business.whatsapp.com/policy
- WhatsApp 2026 marketing-message best practices: https://whatsappbusiness.com/wp-content/uploads/2026/04/Best-Practices-for-Marketing-Messages-on-WhatsApp-.pdf
- CASL guidance for commercial electronic messages including SMS: https://www.crtc.gc.ca/eng/com500/faq500.htm

## Use Cases

- Time-sensitive reminders, delivery/order updates, appointment prompts, support follow-ups, opt-in promotions, account nudges, WhatsApp template messages, or two-way customer conversations.

## Required Inputs

- Channel, country/region, consent source, sender identity, use case, message category, and opt-out handling.
- Audience state, trigger, timing, frequency cap, personalization fields, and support path.
- Whether links, phone numbers, media, templates, or automation are allowed.

## Output Shape

- Message copy variants with character-conscious wording.
- Sender identification and opt-out language where needed.
- Template variables and fallback copy.
- Conversation/reply handling notes.
- Manual compliance, carrier/platform setup, and send QA.

## Copy And Creative Rules

- Be unmistakably useful. Direct messages interrupt people more than email.
- Put sender identity and reason for contact early.
- Use plain language, one CTA, and one link only when necessary.
- Avoid abbreviations that reduce trust. Short does not mean cryptic.
- For WhatsApp, respect template category and make the message feel conversational, not like bulk blast copy.
- For reminders, include who/what/when/where/action.
- For promotions, include eligibility, offer, deadline only if real, and opt-out path.

## Psychological Levers

- Timeliness: send when the message helps a current task.
- Ability: make reply or action very easy.
- Trust: identify sender and purpose clearly.
- Autonomy: make opt-out simple and honor it.
- Reciprocity: provide useful status or support before promotion.

## Platform Adaptation

- SMS: concise, sender-identifying, consent-backed, and opt-out-ready.
- WhatsApp: more conversational, can support templates/media, but still requires policy/category fit and opt-in.
- RCS/MMS: media can help, but only if supported by the sender setup and audience device context.
- International messaging: jurisdiction, opt-in, sender ID, quiet hours, and content rules can differ materially.

## Variants And Testing

- Test timing, CTA wording, personalization, offer framing, message length, and link presence.
- Track delivery, opt-out, reply, click, conversion, complaint/filtering, and support outcomes.
- Diagnose by carrier/region/channel because failures are often infrastructure or consent-related.

## Review Checklist

- Consent, sender identity, opt-out, and message category are explicit.
- The message is useful enough for an interruptive channel.
- It has one action and no hidden conditions.
- Personalization fields have safe fallbacks.
- Manual provider setup, compliance, template approval, and send tasks are listed.

## Failure Diagnostics

- Filtering/blocks: check consent, sender registration, forbidden categories, links, content, and number strategy.
- High opt-outs: message not expected, too frequent, or insufficiently useful.
- Low clicks/replies: CTA unclear, timing poor, or link trust weak.
- Template rejection: category mismatch, vague opt-in, unsupported claims, or policy issue.

## Anti-Patterns

- Buying, renting, or transferring consent.
- Bundling SMS consent into unrelated terms.
- Sending promotions without clear opt-in.
- Multiple asks in one message.
- Making opt-out difficult or continuing after STOP/unsubscribe.
