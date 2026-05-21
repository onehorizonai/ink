# Direct And Product Channel Family Guidance

Use this family guide for SMS, WhatsApp, push notifications, in-app messages, app-store listings, and marketplace listings.

## Source Guidance

- Twilio messaging policy, consent, sender identification, and opt-out guidance: https://www.twilio.com/en-us/legal/messaging-policy
- WhatsApp Business messaging and marketing-message best practices: https://business.whatsapp.com/policy and https://whatsappbusiness.com/wp-content/uploads/2026/04/Best-Practices-for-Marketing-Messages-on-WhatsApp-.pdf
- Firebase In-App Messaging guidance: https://firebase.google.com/docs/in-app-messaging
- OneSignal push notification best practices and metrics: https://onesignal.com/blog/onesignal-guide-push-notification-best-practices-2026/
- Apple App Store and Google Play listing guidance: https://developer.apple.com/app-store/product-page/ and https://support.google.com/googleplay/android-developer/answer/13393723

## Native Behavior

- Direct/product surfaces are high-sensitivity because they interrupt or sit inside a product decision moment.
- SMS/WhatsApp are conversational and permission-heavy. Push is interruptive and timing-sensitive. In-app messages are contextual and should appear when they help the current task. Listings are decision pages where clarity and proof matter.
- The shorter the surface, the more important trigger quality becomes. A weak trigger cannot be fixed by clever copy.

## Audience And Context Rules

- Define user state: prospect, new user, activated user, dormant user, buyer, admin, evaluator, churn risk, power user, or marketplace visitor.
- Define trigger: behavior, time, lifecycle stage, location, account state, feature eligibility, support event, price change, or release.
- Confirm permission and suppression rules before drafting direct messages.
- Match CTA friction to user intent. A push can deep-link; an in-app modal can educate; an app-store listing must help the visitor decide.
- For marketplace/listing pages, identify primary category, competing alternatives, and screenshots/assets needed.

## Creative Strategy

- Make value immediate and specific. Direct surfaces have no patience for brand preamble.
- Use the fewest words that preserve clarity, consent, and action.
- For push/SMS/WhatsApp, write with notification preview constraints and localization in mind.
- For in-app, write copy that fits component behavior: banner, modal, tooltip, checklist, empty state, paywall, or upgrade prompt.
- For listings, pair benefit-led copy with screenshot/gallery strategy and natural keywords.
- Include fallbacks and variants for personalization fields, localization, and unavailable data.

## Compliance And Risk

- Flag opt-in, opt-out, consent record, sender identity, STOP/HELP language, quiet hours, frequency caps, and regional requirements.
- Do not use dark patterns, fake urgency, shame, fear, or hidden dismiss behavior.
- For product surfaces, avoid blocking critical workflows without strong reason.
- For app-store/marketplace listings, avoid misleading claims, keyword stuffing, competitor impersonation, unsupported rankings, pricing references that vary by region, and policy-restricted content.

## Manual Boundary

Ink can draft message copy, variants, trigger notes, listing copy, screenshot briefs, QA checklists, and manual implementation handoffs. Sending, campaign configuration, segmentation, feature flags, SDK/app changes, app-store submission, marketplace submission, and analytics remain manual unless a real tool is used.

## Metrics

- Direct messages: opt-in rate, opt-out rate, delivery, direct open/tap, influenced opens, conversion, complaint rate, and retention impact.
- In-app: impressions, click/tap, dismiss, completion, feature adoption, upgrade/conversion, and downstream retention.
- Listings: impressions, product-page conversion, screenshot engagement, install/signup/start-trial rate, keyword visibility, reviews, and policy rejections.

## QA Checklist

- Trigger, audience state, permission state, and suppression rules are explicit.
- Copy fits the surface and component.
- CTA/deep link/destination matches the promise.
- Frequency and fatigue risks are flagged.
- Policy/compliance needs are listed for human review.
- Manual configuration and submission tasks are separated from final copy.

## Anti-Patterns

- Sending because the company has something to say, not because the user has a reason to care.
- Notification copy that says "Check this out" without value.
- In-app modals that block work for low-value announcements.
- SMS or WhatsApp without clear opt-out handling.
- App-store listings packed with keywords instead of decision-making clarity.
