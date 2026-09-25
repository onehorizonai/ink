# Social DM Automation Format Playbook

Use this format for Instagram, TikTok, Facebook Messenger, and similar social messaging automations when the goal is to turn a platform interaction into a compliant direct-message flow. Load the relevant channel guide first.

## Source Guidance

- Meta Messenger Platform and Instagram Messaging policy: https://developers.facebook.com/documentation/business-messaging/messenger-platform/policy
- Meta Instagram Private Replies: https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/private-replies
- Manychat Free plan: https://help.manychat.com/hc/en-us/articles/25800197498652-Free-plan
- Manychat Instagram Follow to DM: https://manychat.com/use-case/follow-to-dm
- TikTok API for Business: https://ads.tiktok.com/help/article/marketing-api
- TikTok Messaging Partners: https://ads.tiktok.com/help/article/about-message-management-tools

## Use Cases

- Welcome new followers when the platform and account are eligible.
- Send a link, free resource, app download, or FAQ answer after a comment keyword, Story reply, inbound DM keyword, paid messaging ad, or explicit user request.
- Segment people by goal, platform, product fit, or question before sending the next message.
- Route high-intent conversations to a human inbox without requiring manual work for every low-intent interaction.

## Required Inputs

- Channel, account type, automation tool, and eligibility status.
- Trigger: new follow, comment keyword, Story reply, inbound DM keyword, paid messaging ad, or manual handoff.
- Audience state: cold follower, warm follower, commenter, inbound DM, current user, support seeker, or launch visitor.
- Desired outcome: download, answer FAQ, collect feedback, collect email, route to support, or qualify intent.
- Link destination and whether the user explicitly asked for it.
- Suppression rules, frequency caps, opt-out language, and human handoff criteria.

## Output Shape

- Automation recommendation: use, avoid, or defer.
- Trigger map with eligible and ineligible triggers.
- Flow copy: opening message, buttons/quick replies, branch replies, link message, fallback, opt-out/help note, and human handoff note.
- Tool setup handoff: steps for Manychat, official API partner, or manual inbox rule.
- Review notes: compliance windows, trigger eligibility, rate/frequency risk, link risk, and claims to avoid.
- Metrics fields: trigger volume, sends, button clicks/replies, link clicks, installs/signups, human handoffs, opt-outs, negative replies, and tool-limit hits.

## Copy And Creative Rules

- Prefer opt-in and segmentation before links. Ask what the person wants or what they train for before sending a conversion link unless they explicitly requested the link.
- Keep the first message short, conversational, and easy to answer. One question is usually enough.
- Use buttons or quick replies when available; they create cleaner intent signals than open-ended questions.
- Send one useful link after the user interacts. Do not stack multiple CTAs in the first message.
- Make the message feel account-native. A founder or creator account can sound personal; a brand account should be clear and helpful.
- Include a fallback for people who type something unexpected.

## Psychological Levers

- Permission: the user should feel they asked for or welcomed the message.
- Agency: buttons and short questions let the user choose the next branch.
- Relevance: segment by goal, device, or problem before making the link feel useful.
- Reciprocity: answer the request first, then ask a light follow-up only when it helps.
- Low friction: keep the action small enough to complete inside the inbox.

Avoid pressure, fake urgency, fake personalization, guilt, shame, or engagement manipulation.

## Platform Adaptation

- Instagram Follow-to-DM: use only when the account and tool expose the eligible trigger; delay briefly and segment before linking.
- Instagram comment-to-DM: make the public CTA explicit, use a private reply as the opening, and continue only after a click or reply.
- Instagram Story replies: treat the Story as the opt-in prompt and send the promised answer or link quickly.
- TikTok: prefer inbound keyword DMs or comment prompts; treat follower-triggered automation as unavailable unless an official partner feature explicitly supports it.
- Paid messaging ads: match the DM opening to the ad promise and keep the branch path short.

## Variants And Testing

- Test one trigger at a time: follower welcome, comment keyword, Story reply, inbound keyword, or paid message.
- Test first-message framing before testing longer sequences.
- Compare ask-first versus direct-link only when the user explicitly requested the link.
- Track trigger volume, replies/button clicks, link clicks, installs/signups, opt-outs, negative replies, and human handoffs.
- Keep a note of account eligibility, tool plan limits, trigger copy, content asset, and landing link for each run.

## Compliance And Risk

- Do not use browser bots, scraping, password-sharing tools, or unofficial cold-DM software.
- Do not cold-DM followers unless the platform, official partner, and account eligibility explicitly allow that trigger.
- Treat Instagram Follow-to-DM as account- and Meta-eligibility-dependent. If unavailable, use comment-to-DM, Story replies, or inbound keyword DMs instead.
- Respect the 24-hour messaging window after user interaction. Follow-up automation after the window requires the platform's approved opt-in mechanism and should not be assumed.
- Instagram private replies to comments are one-message openings unless the user replies or interacts.
- Treat TikTok DM automation as partner/API/region-gated. Prefer inbound keyword/comment triggers over follower-triggered DMs.
- Do not ask for fake reviews, upvotes, ratings, or engagement manipulation.
- Provide a clear human handoff path for support, safety, billing, medical, legal, or account-specific questions.

## Manual Boundary

Ink can draft automation strategy, flow copy, setup instructions, decision rules, and metric fields. A human or external tool must connect social accounts, configure automations, verify eligibility, publish triggers, send messages, handle inbox conversations, and record analytics unless a real integration is explicitly used.

## Review Checklist

- Trigger is user-initiated or officially/partner-supported.
- First message asks or segments before linking, unless the user explicitly requested the link.
- Link destination matches the promise and is safe for the channel.
- Tool limits, eligibility, messaging window, and suppression rules are called out.
- Copy avoids fake personalization, pressure, engagement bait, and unsupported claims.
- Metrics and human handoff rules are included.

## Failure Diagnostics

- Low trigger volume: the public CTA is unclear, the content topic is weak, or the account does not yet have enough reach.
- Low reply/button rate: the first message asks too much, sounds too automated, or does not match the trigger promise.
- Low link clicks: the branch copy does not make the link relevant, the wrong device link is shown, or the CTA arrives before enough intent.
- Negative replies or opt-outs: the trigger feels unsolicited, the delay is strange, the brand affiliation is unclear, or messages are too frequent.
- Tool errors: account eligibility, plan limits, channel permissions, or messaging-window constraints need to be rechecked inside the automation tool.

## Anti-Patterns

- Sending every new follower a download link as the first message.
- Treating TikTok follower DMs as universally available.
- Using a Chrome extension, scraped follower list, or mobile emulator to send DMs.
- Hiding that the message is from a brand or product account.
- Building long automated sequences before validating whether people reply to the first message.
