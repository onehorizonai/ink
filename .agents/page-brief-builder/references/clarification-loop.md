# Clarification Loop

Use this as the shared questioning contract for website page briefs.

Website brief work is a guided discovery workflow, not a one-shot brief generator.
Do not assume the user's first prompt contains enough context to lock the strategy.
Keep asking verification questions until the next stage can be completed without guesswork.

## Questioning Rules

- Ask 2-4 tightly related questions in one turn when they unlock the same decision.
- Ask a single question only when one blocking uncertainty remains.
- Do not dump a long questionnaire unless the user explicitly asks for one.
- Prefer concrete verification questions over vague prompts such as `Anything else?`
- After each user answer, update what is confirmed, name what is still open, and ask the next highest-value verification pack.
- If an answer is vague, follow up on the vague part before moving on.
- Do not use assumptions for user-answerable strategy inputs until at least one verification round has been attempted.
- If the user explicitly asks to move faster or make assumptions, state the assumption and keep it out of locked brief fields when it would materially change the output.

## Stage Gates

Before moving forward, verify that the inputs for the current gate are actually locked.

### Identification Gate

- target site
- page status
- live URL if update
- page type

### Update Diagnosis Gate

- why the page needs to change
- what is not working now
- what must stay
- what success looks like

### Strategy Gate

- audience
- page goal
- offer
- main promise or value proposition
- differentiator
- proof available or missing

### Conversion Gate

- primary CTA
- CTA destination
- secondary CTA role or intentional absence
- funnel stage
- main friction points

### Brief-Lock Gate

- exact H1
- exact title tag
- exact meta description
- exact CTA labels
- exact section headings
- required links
- claims to avoid or proof still missing

## High-Value Question Packs

Use these packs instead of stopping after the first obvious question.

### For Updates To Existing Pages

Ask for:

- why the page needs to change
- what is not working
- what must stay
- what success looks like

### For Thin Strategy Prompts

Ask for:

- target audience
- page goal
- primary CTA
- business-specific context such as offer, differentiator, proof, or constraints

### For Unresolved Positioning

Ask for:

- core promise
- most important differentiator
- strongest proof available
- biggest objection to overcome

### For Unresolved Conversion Details

Ask for:

- exact primary CTA destination
- whether a secondary CTA is needed
- user readiness level
- friction or reassurance needs

## Blocked Output Shape

When the workflow is blocked on missing inputs, return:

- `Normalized request`
- `Confirmed inputs`
- `Open gaps`
- `Next verification questions`
- `Why these are next`

Under `Next verification questions`, ask direct plain-language questions.
Use numbered questions only when there is more than one.
