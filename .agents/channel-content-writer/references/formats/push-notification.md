# Push Notification Format Playbook

Use this format for mobile or web push notifications, lock-screen nudges, retention prompts, feature reminders, and time-sensitive product messages. Load `../channels/direct-product.md` first.

## Source Guidance

- OneSignal Push Notification Best Practices 2026: https://onesignal.com/blog/onesignal-guide-push-notification-best-practices-2026/
- OneSignal sending and mobile push documentation: https://documentation.onesignal.com/docs/sending-notifications and https://documentation.onesignal.com/docs/mobile-push-setup
- Firebase Cloud Messaging documentation: https://firebase.google.com/docs/cloud-messaging
- Apple Mail Privacy Protection is not push, but use similar privacy caution around tracking assumptions: https://www.apple.com/legal/privacy/data/en/mail-privacy-protection/

## Use Cases

- Re-engage users, remind about unfinished actions, announce relevant updates, deliver transactional alerts, prompt habit loops, or support time-sensitive account/product moments.

## Required Inputs

- App/platform, audience segment, permission state, trigger, timing, time zone, urgency, and destination.
- Notification type: transactional, lifecycle, promotional, reminder, alert, content, or reactivation.
- Personalization fields, frequency cap, deeplink, image/action buttons, and fallback behavior.

## Output Shape

- Title and body variants.
- Deeplink/action-button notes.
- Trigger and audience rules.
- Timing/frequency recommendations.
- Manual configuration, QA, and metrics notes.

## Copy And Creative Rules

- Push is tiny. Use concrete language and remove filler.
- Make the value obvious before asking for a tap.
- Use numbers, specifics, or status when they are true and helpful.
- Avoid all caps, excessive punctuation, vague hype, and guilt.
- Do not send generic promotional push to everyone when segmentation is possible.
- If using images or buttons, describe their role and fallback.

## Psychological Levers

- Prompt: push works when motivation and ability already exist.
- Timeliness: the notification should arrive when action is useful.
- Loss aversion: use only for real deadlines, account risks, or expiring opportunities.
- Progress: remind users of a meaningful unfinished action.
- Autonomy: avoid pressure and preserve opt-out trust.

## Platform Adaptation

- iOS: permission is precious; use soft prompts before system permission where product flow allows.
- Android: notification channels and grouping affect experience.
- Web push: context and frequency need extra care because relationship may be weaker.
- Transactional push: clarity beats persuasion.
- Promotional push: segmentation and restraint are essential.

## Variants And Testing

- Test timing, title/body, trigger, segment, deeplink, image, button, and frequency.
- Track delivery, impressions, opens/taps, conversion, opt-outs, uninstall, session quality, and downstream retention.
- Compare against holdout groups when possible to avoid mistaking natural behavior for lift.

## Review Checklist

- The notification is triggered by a real user/product context.
- Title/body are short, specific, and non-manipulative.
- Deeplink or next action is clear.
- Frequency, quiet hours, permissions, and opt-out risk are flagged.
- Manual setup and platform QA are listed.

## Failure Diagnostics

- Low opt-in: permission ask lacks clear value or arrives too early.
- Low tap: message vague, timing wrong, or deeplink irrelevant.
- High opt-out/uninstall: frequency too high or message too promotional.
- No conversion: notification opens to the wrong screen or action is hard.

## Anti-Patterns

- Broadcast pushes with no segment logic.
- Fake urgency or generic "we miss you" nudges.
- Sending at bad local times.
- Pushes that open to a homepage instead of the promised action.
- Treating push as a replacement for product value.
