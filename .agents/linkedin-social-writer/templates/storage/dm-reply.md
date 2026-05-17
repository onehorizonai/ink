---
channel: linkedin
format: dm-reply
published_at: {{published_at_yaml}}
title: {{title_yaml}}
format_template: {{format_template_yaml}}
program_id: {{program_id_yaml}}
format_id: {{format_id_yaml}}
run_id: {{run_id_yaml}}
campaign_id: {{campaign_id_yaml}}
context: {{context_yaml}}
author: {{author_yaml}}
audience: {{audience_yaml}}
goal: {{goal_yaml}}
topic_tags: {{topic_tags_yaml}}
asset_type: {{asset_type_yaml}}
asset_summary: {{asset_summary_yaml}}
source_url: {{source_url_yaml}}
thread_summary: {{thread_summary_yaml}}
outcome_notes: {{outcome_notes_yaml}}
---

## Published Copy

{{body}}

## Context Notes

- Inbound message context: {{thread_summary_plain}}
- Reason for the reply: {{context_plain}}
- Intended next step: {{goal_plain}}

## Asset Notes

- Asset type: {{asset_type_plain}}
- Asset summary: {{asset_summary_plain}}

## Outcome Notes

{{outcome_notes_plain}}
