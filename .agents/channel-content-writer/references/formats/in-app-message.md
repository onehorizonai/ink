# In-App Message Format Playbook

Use this format for in-app banners, modals, tooltips, cards, feature announcements, upgrade prompts, onboarding nudges, and contextual product education. Load `../channels/direct-product.md` first.

## Source Guidance

- Firebase In-App Messaging documentation: https://firebase.google.com/docs/in-app-messaging
- OneSignal in-app and cross-channel notification resources: https://documentation.onesignal.com/
- Nielsen Norman Group guidance on interruptions and UX messaging can be useful when product UX risk is high: https://www.nngroup.com/articles/popups/

## Use Cases

- Help active users discover a feature, complete onboarding, recover from friction, upgrade at the right moment, understand a change, or take a context-specific action.

## Required Inputs

- User state, product screen, trigger, eligibility, desired action, and frequency cap.
- Message type: banner, modal, tooltip, coach mark, card, checklist, empty state, or embedded message.
- Product constraints, deeplink/action, success metric, dismiss behavior, and experiment plan.

## Output Shape

- Message copy by component: title, body, CTA, secondary action, dismiss text, and accessibility label.
- Trigger/eligibility notes and fallback copy.
- Placement, timing, and frequency guidance.
- Manual implementation, QA, and metrics notes.

## Copy And Creative Rules

- Respect the user's current task. An in-app message should help the task, not ambush it.
- Use context from the screen or behavior. Generic marketing copy inside product feels intrusive.
- Keep modal copy short and decision-oriented. If explanation is long, link to docs.
- CTA label should say the action, not "Learn more" by default.
- Always include a humane dismissal path unless the message is mandatory operational information.
- For feature announcements, show what changed, who it is for, and what to do next.

## Psychological Levers

- Ability: reduce friction at the moment of action.
- Salience: show the message where the feature or problem lives.
- Progress: checklists and completion cues can motivate onboarding.
- Commitment: ask for the next small product step.
- Autonomy: dismiss/snooze options reduce reactance.

## Platform Adaptation

- Onboarding: guide progressively; do not teach everything at once.
- Upgrade: connect prompt to a limit, value moment, or user intent.
- Feature discovery: use behavioral eligibility instead of blasting all users.
- Incident/change notice: prioritize clarity, status, and support path.
- Mobile: shorter text, larger touch targets, and safer timing.

## Variants And Testing

- Test trigger timing, placement, title, CTA, modal versus banner, image, and frequency.
- Track view, dismiss, click, conversion, feature adoption, downstream retention, support tickets, and annoyance signals.
- Use holdouts where possible because active users may convert without the prompt.

## Review Checklist

- Message is tied to a real screen, behavior, or user state.
- Copy is short, specific, and task-aware.
- CTA, secondary action, dismiss behavior, and fallback are clear.
- Accessibility, mobile constraints, and privacy concerns are flagged.
- Manual implementation and experiment notes are included.

## Failure Diagnostics

- High dismiss: message appears too early, too often, or in the wrong context.
- Low conversion: CTA unclear, action hard, or value not tied to current task.
- Support increase: message overpromises or creates confusion.
- Retention decline: prompt feels like interruption rather than help.

## Anti-Patterns

- Full-screen modals for low-value announcements.
- Upgrade prompts before users experience value.
- Hiding dismiss options.
- Teaching too much at once.
- Using in-app messages as ads disconnected from product context.
