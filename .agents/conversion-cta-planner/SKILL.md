---
name: conversion-cta-planner
description: Plan the conversion path for a website page brief by mapping funnel stage, desired user action, friction points, exact CTA labels, exact CTA placements, support for the primary CTA, the role of the secondary CTA, and trust or reassurance elements needed near conversion moments. Use when Codex needs CTA and conversion strategy for a new or updated web page. Do not use it to write full page copy or to replace the broader messaging strategy.
---

# Conversion CTA Planner

## Overview

Define how the page moves the user toward action.

This skill is responsible for conversion logic, not the whole brief.

## Workflow

1. Confirm the audience awareness stage or funnel stage.
2. Confirm the desired primary action and any secondary action.
3. Identify likely friction points for this audience and page type.
4. Recommend CTA placement logic across the page.
5. Define how the page supports the primary CTA.
6. Define the role of the secondary CTA so it reduces friction instead of competing.
7. Identify trust, reassurance, or proof elements needed near conversion moments.
8. State exact CTA labels, destinations, and section-level CTA behavior for the final brief.

## Rules

- Read `../page-brief-builder/references/clarification-loop.md` before deciding the conversion inputs are locked enough to proceed.
- Read `../page-brief-copy-playbook/SKILL.md` and `../page-brief-copy-playbook/references/copy-rules.md` before finalizing guidance.
- Use `../page-brief-page-playbook/SKILL.md` when the page type materially changes CTA logic, especially for landing, help, comparison, and integration pages.
- Keep one clear primary CTA. Use a secondary CTA only when it serves a distinct stage or risk profile.
- Match CTA intensity to page type, traffic source, and funnel stage.
- Use support elements that remove friction, such as proof, examples, pricing clarity, security notes, demos, FAQs, or implementation reassurance.
- Keep the CTA guidance concrete. State exactly what appears where.
- For every CTA moment, specify the exact label, destination or route, and supporting proof.
- Do not output CTA `direction`, `options`, `could`, or `should` language.
- If the exact CTA destination, secondary CTA role, or reassurance model is still unclear, ask 1-3 targeted verification questions instead of drafting around it.
- Do not output code or polished full-page copy.

## Stop Conditions

- If the primary CTA is unknown, stop and use `../website-brief-intake/SKILL.md` to ask targeted verification questions.
- If the chosen direction is unresolved, stop and use `../page-positioning-strategist/SKILL.md`.
- If funnel stage is unknown, stop and use `../website-brief-intake/SKILL.md` to ask targeted verification questions.
- If exact section-level CTA behavior still depends on unresolved user-answerable inputs, stop and ask the next conversion verification questions before continuing.

## Output Shape

Return these exact headings:

- `Funnel-stage summary`
- `Desired actions`
- `Key friction points`
- `CTA placement logic`
- `Exact section-level CTA requirements`
- `Support for the primary CTA`
- `Role of the secondary CTA`
- `Trust and reassurance elements`

If the workflow is blocked on missing conversion inputs, return only `Known conversion inputs`, `Open conversion gaps`, `Next verification questions`, and `Why these are next`.
