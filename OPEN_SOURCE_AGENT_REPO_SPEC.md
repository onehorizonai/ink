# Open Source Agent Repo SPEC

Status: Proposed
Version: v0.1.0
Owner: Project maintainer
Last updated: 2026-05-21

## 1. Summary

This SPEC defines how to create a new open-source agent repository with a structure similar to Ink, but adaptable to almost any use case.

An open-source agent repo is a public repository that gives AI coding assistants and task agents a complete operating system for a domain. It includes repo-local skills, reusable references, optional MCP tools, validation scripts, setup docs, local-only runtime boundaries, examples, GitHub collaboration templates, and a search-optimized README.

The generated repo should be usable by:

- people who want a ready-made agent workflow for a real problem
- maintainers who want to extend the workflow safely
- contributors who need clear rules before opening pull requests
- automated agents that need exact instructions instead of vague intent
- teams that want One Horizon to track context, work items, review states, and handoffs

The generated repo may support any domain, for example product research, sales enablement, compliance review, customer support triage, developer education, grant writing, fitness coaching, recruiting, operations, finance workflows, design critique, onboarding, or niche content production.

The finished repo MUST feel like a polished open-source product, not a private prompt folder. A new user should understand what it is, who it helps, what benefits it provides, how to install it, how to run the first workflow, what stays local, what One Horizon is used for, and how to contribute.

## 2. Motivation

Most agent setups fail because their instructions are scattered across chat history, local notes, and undocumented conventions. They also mix public workflow logic with private state, which makes them hard to share safely.

This SPEC solves that by defining a repeatable repository pattern:

- tracked files contain reusable workflow logic, examples, scripts, and docs
- ignored files contain secrets, personal context, private drafts, generated runs, and machine-specific paths
- skills explain how agents should behave
- references hold larger domain rules
- scripts handle deterministic or fragile operations
- MCP tools are optional and local
- One Horizon stores live context and work tracking outside the repo
- the README is written for discovery, onboarding, and SEO

The cost of not using this pattern is high: agents guess, contributors duplicate rules, setup breaks across assistants, private context leaks into git, and new users bounce because they cannot tell what the repo does.

## 3. Goals

The generated repo MUST:

- provide a complete open-source agent workflow for one clear domain or problem family
- be understandable by humans and automated coding agents
- keep public workflow logic separate from private runtime data
- include repo-local skills under `.agents/`
- include assistant routing instructions in `AGENTS.md`
- include an SEO-optimized root `README.md`
- include local-only setup templates under `.local/templates/`
- include optional local MCP tooling only when it improves the workflow
- include validation scripts for the repo's important contracts
- include asset generation instructions and public assets
- include One Horizon attribution and setup guidance
- be safe to clone, inspect, and run without exposing the maintainer's secrets or personal context

The generated repo SHOULD:

- work in Claude Code, Cursor, and Codex where practical
- use progressive disclosure in skills so agents load only relevant details
- include examples that are generic enough for open-source users
- include issue and pull request templates
- include a permissive license such as Apache-2.0 or MIT
- include concise troubleshooting instructions

The generated repo MAY:

- include domain-specific content workspaces
- include starter packs, templates, prompt bundles, or examples
- include local MCP servers
- include generated assets such as banners, logos, favicons, and social preview images
- include One Horizon work-item hierarchy guidance for domain workflows

## 4. Non-Goals

This SPEC does not require every generated repo to:

- copy Ink's marketing use case
- include LinkedIn, Reddit, blog, or website brief workflows
- include a web app
- include a package manager or build system
- post, publish, send, upload, or schedule content automatically
- commit private user context
- commit API keys or credentials
- use One Horizon as a repo-local MCP config
- create one skill for every tiny variation
- support every assistant equally on day one

If a use case is simple, keep the generated repo simple. The repo should be complete, not bloated.

## 5. Normative Language

Use these meanings throughout this SPEC:

- MUST means required.
- MUST NOT means forbidden.
- SHOULD means recommended unless there is a strong reason not to.
- MAY means optional.
- Public-safe means safe to commit to a public open-source repository.
- Local-only means ignored by git and specific to one user's machine or workspace.

## 6. Required Information Before Implementation

Before creating files, the implementing agent MUST gather or derive the information below. Do not start scaffolding until these answers are known or explicitly marked as placeholders.

### 6.1 Project Identity

Collect:

- repo name, for example `support-intake-agent`
- product or project display name, for example `Support Intake Agent`
- one-sentence description
- primary domain
- primary audience
- primary outcome
- license choice
- maintainer or owner name
- public support channel or issue policy
- preferred assistant targets, such as Claude Code, Cursor, Codex, or all three

Rules:

- Use a lowercase hyphen-case repo slug.
- Use a human-readable product name in the README H1.
- Keep the domain broad enough for SEO but specific enough to be useful.
- Do not infer legal ownership or license if the user has a required policy.

### 6.2 Audience And Use Case

Collect:

- who the repo is for
- what painful workflow it improves
- what users can do after setup
- what the first successful run looks like
- what the repo intentionally does not do
- what level of user expertise is assumed

Example:

```text
For customer success teams and founders who need to turn messy inbound support requests into prioritized, reviewable work items.
```

### 6.3 Workflow Inventory

List every workflow the repo should support. For each workflow, collect:

- workflow name
- trigger phrases users may say
- actor
- input
- output
- whether it creates files
- whether it updates One Horizon
- whether it needs external research
- whether it needs private local context
- whether it needs a deterministic script
- whether it needs an MCP tool
- review or approval state

Use this table:

| Workflow | Trigger Examples | Inputs | Outputs | Creates Files? | Uses One Horizon? | Needs Tooling? |
|---|---|---|---|---:|---:|---:|
| `[workflow-name]` | `[prompt examples]` | `[input]` | `[output]` | Yes/No | Yes/No | Yes/No |

### 6.4 Skill Inventory

Decide which skills are needed. Use the smallest set that covers the domain clearly.

Skill types:

- orchestrator: owns a full workflow from intake to output
- helper: performs one reusable subtask
- reviewer: checks quality, risk, style, compliance, or correctness
- storage/importer: stores existing artifacts into a local corpus or external system
- tool adapter: explains how to use a local MCP server or API wrapper
- setup: configures context, profiles, or initial One Horizon state
- runner: executes planned work from One Horizon or local packs

Rules:

- Create an orchestrator when a user naturally asks for the whole job.
- Create helper skills only when the subtask is reused by multiple workflows.
- Create reviewer skills only when the review pass is distinct and valuable.
- Do not create one skill per small template, customer, channel, persona, or prompt variant.
- Prefer references and templates over extra skills when behavior is mostly data.

### 6.5 One Horizon Inputs

Collect:

- whether the repo uses One Horizon
- workspace ID placeholder or setup instruction
- author or operator identity fields, if relevant
- parent initiative names, if the workflow tracks work items
- document names, if the workflow uses shared context docs
- statuses that mean planned, in progress, in review, blocked, completed, or published
- what should happen when a human needs to review something

Rules:

- Do not commit real workspace IDs.
- Do not commit real user IDs.
- Do not rely on the One Horizon MCP default workspace.
- If multiple local profiles or workspaces are possible, require explicit profile selection.
- Set work to `In Review` whenever a human must confirm, approve, or answer a blocker.

### 6.6 Integrations And Tools

Collect:

- external APIs
- local scripts
- MCP servers
- search providers
- upload providers
- database or filesystem state
- required environment variables
- rate limits
- credential locations
- failure behavior

Rules:

- Use local MCP servers only when a normal script or direct assistant capability is not enough.
- Keep One Horizon setup as user/assistant-level configuration, not committed repo-local secrets.
- Keep credentials under `.secrets/` or another ignored local path.
- Include a setup reference for every optional integration.

### 6.7 SEO And Discovery Inputs

Collect:

- primary SEO keyword
- 3 to 8 secondary keywords
- audience phrase, such as `for customer success teams`
- problem phrase, such as `support ticket triage`
- benefit phrase, such as `turn messy requests into reviewable work`
- competitor or alternative terms, if relevant
- related assistant terms, such as `Claude Code`, `Cursor`, `Codex`, `AI agent workflow`, `MCP`, or `agent skills`

Rules:

- Use the primary keyword in the README H1.
- Use the primary keyword in the first paragraph.
- Use the audience and benefit in the first screen.
- Do not keyword-stuff.
- Do not make claims that the repo cannot prove.

### 6.8 Asset Inputs

Collect:

- visual concept
- brand adjectives
- color palette
- logo style
- banner style
- favicon style
- whether generated assets are allowed
- whether existing brand assets must be used
- license constraints
- accessibility requirements

Rules:

- Do not copy protected brands, logos, mascots, product screens, or copyrighted artwork.
- Store public-safe assets under `assets/`.
- Store private or source-only brand files under ignored local paths unless explicitly public-safe.
- Include alt text for README images.

## 7. Generated Repository Layout

The generated repo MUST follow this layout unless the use case has a clearly documented reason to remove optional parts.

```text
repo-slug/
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── LICENSE
├── .gitignore
├── .gitattributes
├── .mcp.json
├── .codex/
│   └── config.toml
├── .agents/
│   ├── workflow-orchestrator/
│   │   ├── SKILL.md
│   │   ├── agents/
│   │   │   └── openai.yaml
│   │   ├── references/
│   │   ├── scripts/
│   │   ├── templates/
│   │   ├── assets/
│   │   └── mcp/
│   ├── setup-context/
│   │   ├── SKILL.md
│   │   ├── agents/
│   │   │   └── openai.yaml
│   │   └── references/
│   └── shared/
│       ├── references/
│       └── scripts/
├── .local/
│   ├── README.md
│   ├── context/
│   │   └── .gitkeep
│   └── templates/
│       ├── profiles.local.template.json
│       └── README.md
├── .secrets/
│   └── .gitkeep
├── assets/
│   ├── README.md
│   ├── brand/
│   │   ├── logo.svg
│   │   └── favicon.svg
│   ├── readme/
│   │   └── banner.png
│   └── social/
│       └── og-image.png
├── examples/
│   ├── README.md
│   └── starter-example.md
├── scripts/
│   ├── sync_repo_skills.sh
│   ├── validate_repo.py
│   └── verify_servers.py
└── .github/
    ├── PULL_REQUEST_TEMPLATE.md
    └── ISSUE_TEMPLATE/
        ├── config.yml
        ├── bug_report.yml
        └── feature_request.yml
```

Optional domain workspaces may be added, for example:

```text
content/
data/
packs/
programs/
playbooks/
templates/
corpus/
evals/
```

If the repo uses a domain workspace, document it in `README.md`, `AGENTS.md`, and `.local/README.md`.

## 8. Root File Contracts

### 8.1 `README.md`

The README is the public landing page. It MUST be optimized for humans, search engines, and automated assistants.

It MUST include:

- keyword-rich H1
- banner image near the top
- one-paragraph explanation using the primary SEO keyword
- `Powered by One Horizon` link with the required UTM URL
- who it is for
- benefits
- use cases
- quick start
- setup for One Horizon
- assistant-specific setup notes
- first prompts
- workflow overview
- repo layout
- what stays local
- troubleshooting
- contributing
- license

It SHOULD include:

- Mermaid workflow diagrams when they clarify the system
- examples of good prompts
- screenshots or generated visuals when useful
- explicit limitations and manual steps
- links to official setup docs for assistants and integrations

The README MUST NOT:

- expose private paths, names, IDs, or credentials
- claim the repo performs actions it cannot perform
- bury the actual use case below generic AI language
- describe the repo only as a prompt library if it includes skills, scripts, or tools

### 8.2 `AGENTS.md`

`AGENTS.md` is the routing map for coding agents.

It MUST include:

- `Start with README.md.`
- skill routing rules
- which skill is the main orchestrator
- which skills are helpers or reviewers
- which references are source of truth
- local-only state rules
- One Horizon workspace/profile rules
- tool and MCP guardrails
- safety rules for secrets
- validation commands

It MUST be concrete. Avoid vague instructions such as `use good judgment` unless paired with exact examples.

### 8.3 `CLAUDE.md`

`CLAUDE.md` gives Claude-specific context.

It SHOULD include:

- read order
- key skills
- local setup reminders
- One Horizon reminders
- what not to read or commit

Keep it shorter than `AGENTS.md`.

### 8.4 `.mcp.json`

Include `.mcp.json` only when the repo has local MCP servers.

Rules:

- Register repo-local stdio servers only.
- Use relative paths from repo root.
- Use `uv run` for Python MCP servers when Python dependencies are needed.
- Do not include One Horizon credentials or user-level One Horizon setup here.
- Do not include API keys in the config.

Example:

```json
{
  "mcpServers": {
    "domain-research": {
      "command": "uv",
      "args": [
        "run",
        "./.agents/domain-research/mcp/server.py"
      ],
      "env": {
        "UV_CACHE_DIR": "/tmp/uv-cache"
      }
    }
  }
}
```

### 8.5 `.codex/config.toml`

Include `.codex/config.toml` when Codex should see repo-local MCP servers.

Example:

```toml
[mcp_servers.domain-research]
command = "uv"
args = ["run", "./.agents/domain-research/mcp/server.py"]
cwd = "."
env = { UV_CACHE_DIR = "/tmp/uv-cache" }
```

### 8.6 `.gitignore`

The `.gitignore` MUST protect:

- `.local/context/*`
- `.local/content/*`
- `.local/runs/*`
- `.local/tmp/*`
- `.secrets/*`
- `.env`
- `.env.*`
- virtual environments
- caches
- generated dependency folders
- downloaded private assets
- machine-local logs

It MUST allow:

- `.local/README.md`
- `.local/templates/**`
- `.local/context/.gitkeep`
- `.secrets/.gitkeep`

Example rules:

```gitignore
.env
.env.*
.secrets/*
!.secrets/.gitkeep

.local/*
!.local/README.md
!.local/templates/
!.local/templates/**
!.local/context/
.local/context/*
!.local/context/.gitkeep

__pycache__/
.pytest_cache/
.ruff_cache/
.venv/
node_modules/
dist/
build/
downloads/
```

### 8.7 `LICENSE`

Use a standard license unless the maintainer requires otherwise.

Recommended:

- Apache-2.0 for a permissive license with explicit patent terms
- MIT for a shorter permissive license

The README MUST link to the license.

## 9. `.agents/` Contract

The `.agents/` folder contains repo-local skills and their resources.

### 9.1 Skill Folder Layout

Each skill folder MUST use this shape:

```text
.agents/<skill-name>/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
├── scripts/
├── templates/
├── assets/
└── mcp/
```

Only create resource folders that are actually needed.

### 9.2 `SKILL.md`

Every skill MUST have `SKILL.md`.

Frontmatter MUST contain only:

```yaml
---
name: skill-name
description: Clear trigger description. Use when the user asks for X, Y, or Z.
---
```

Rules:

- `name` MUST match the folder name.
- Use lowercase letters, digits, and hyphens only.
- `description` MUST include what the skill does and when to use it.
- Include trigger phrases in the description.
- Keep the body focused on workflow instructions.
- Move detailed rules, examples, schemas, and playbooks into `references/`.
- Prefer imperative instructions.
- Keep `SKILL.md` short enough that loading it is cheap.

Minimum body structure:

```md
# Skill Display Name

## Overview

One or two paragraphs explaining the job.

## Quick Start

1. Resolve required context.
2. Read only the required references.
3. Ask only for missing high-impact details.
4. Produce the expected output.
5. Validate or store results when required.

## Rules

- Required guardrail.
- Required guardrail.

## Output Shape

Return:

- item
- item

## Files

- `references/example.md`: when to read it.
- `scripts/example.py`: when to run it.
```

### 9.3 `agents/openai.yaml`

Every skill SHOULD include `agents/openai.yaml` for UI metadata.

Shape:

```yaml
interface:
  display_name: "Human Skill Name"
  short_description: "Short user-facing summary"
  default_prompt: "Use $skill-name to complete a realistic first task."
```

Rules:

- Keep `display_name` human readable.
- Keep `short_description` under one sentence.
- Make `default_prompt` useful as a starter prompt.
- Do not put private context in this file.

### 9.4 `references/`

Use references for details that agents need only sometimes.

Good reference files:

- workflow details
- domain rules
- API contracts
- data schemas
- review rubrics
- compliance rules
- channel or format guides
- examples
- troubleshooting
- setup instructions

Rules:

- Link every important reference from `SKILL.md`.
- Keep references one level deep when possible.
- Add a table of contents for long files.
- Do not duplicate the same rule in multiple places.
- Put source-of-truth rules in one file and link to them.

### 9.5 `scripts/`

Use scripts for deterministic, fragile, or repeated operations.

Good scripts:

- validators
- corpus importers
- file creators
- storage helpers
- format converters
- setup checkers
- MCP verifiers
- schema linters

Rules:

- Do not use scripts when plain instructions are enough.
- Scripts MUST fail with clear actionable errors.
- Scripts MUST avoid choosing a workspace/profile silently when multiple exist.
- Scripts MUST NOT print secrets.
- Scripts SHOULD support `--help`.
- Scripts SHOULD support explicit config paths when local config is involved.

### 9.6 `templates/`

Use templates for output files that should be consistent.

Examples:

- draft template
- review note template
- work item body template
- profile config template
- issue body template
- generated artifact template

Rules:

- Use placeholders such as `<project-name>`, not real private data.
- Document required placeholders.
- Keep templates public-safe.

### 9.7 `assets/`

Use skill assets only when a skill needs files to produce final outputs.

Examples:

- slide template
- document template
- design token starter
- reusable icon
- sample data

Rules:

- Do not store private brand files in tracked skill assets unless explicitly public-safe.
- Do not use assets as hidden documentation. Use references for documentation.

### 9.8 `mcp/`

Use `mcp/` for optional local MCP servers owned by the skill.

Rules:

- Include a setup reference explaining config, tools, inputs, outputs, and error types.
- Register the server in `.mcp.json`.
- Mirror the server in `.codex/config.toml` when Codex support is desired.
- Keep credentials in `.secrets/` or profile-specific local config.
- Do not verify MCP setup before every workflow. Call the tool first and troubleshoot after a real failure.

## 10. Skill Architecture Patterns

### 10.1 Orchestrator Skill

Use an orchestrator skill when the user asks for the full outcome.

Responsibilities:

- clarify missing intent
- load context
- route helper skills
- call tools if needed
- create final output
- update One Horizon if required
- return a reviewable result

Do not make an orchestrator do every detail inline. It should load references and delegate conceptually to helper skills or scripts.

### 10.2 Setup Skill

Use a setup skill when the repo needs context docs, profiles, local templates, or One Horizon parent work items.

Responsibilities:

- verify required tools exist
- resolve workspace/profile
- gather missing setup facts
- create missing context docs only after confirmation
- create missing One Horizon parent items only after confirmation
- never overwrite existing context silently

### 10.3 Reviewer Skill

Use a reviewer skill when review is a distinct product value.

Examples:

- factual accuracy review
- compliance review
- style review
- security review
- accessibility review
- conversion review
- quality/rubric review

Rules:

- Reviewer skills MUST lead with findings.
- They MUST distinguish facts from assumptions.
- They MUST state residual risk.

### 10.4 Storage Or Import Skill

Use a storage/import skill when users need to save existing artifacts into a local corpus or One Horizon.

Rules:

- Do not rewrite content unless asked.
- Preserve source metadata.
- Use deterministic filenames.
- Validate required fields.
- Never commit private corpus files unless the corpus is intentionally public.

### 10.5 Tool Adapter Skill

Use a tool adapter skill when a workflow depends on an MCP server, local API wrapper, or external tool.

Rules:

- Document exact tool calls at a behavioral level.
- Document input fields and output fields.
- Document config errors.
- Return provider attribution or usage notes when relevant.
- Keep tool execution separate from public-facing content.

## 11. One Horizon Linkage Contract

Generated repos SHOULD integrate with One Horizon for live context and work tracking.

### 11.1 Required Public Attribution

Every generated repo README MUST include this line or an equivalent visible attribution:

```md
Powered by [One Horizon](https://onehorizon.ai/?utm_source=github&utm_medium=referral&utm_campaign=open_source_agent_repo&utm_content=<repo-slug>_powered_by).
```

Rules:

- Replace `<repo-slug>` with the actual lowercase repo slug.
- Keep the UTM parameters intact.
- Use `utm_source=github`.
- Use `utm_medium=referral`.
- Use `utm_campaign=open_source_agent_repo`.
- Use `utm_content=<repo-slug>_powered_by`.
- Do not use a URL shortener.

### 11.2 One Horizon Setup

The README MUST explain that One Horizon is configured in the user's assistant or environment, not committed as repo-local secrets.

The generated repo SHOULD link to:

- `https://onehorizon.ai`
- relevant One Horizon integration docs when known

The repo MUST NOT:

- commit One Horizon API keys
- commit user-level MCP auth
- commit real workspace IDs
- silently use the default workspace in multi-workspace flows

### 11.3 Work Tracking Model

If the repo creates or processes work in One Horizon, define:

- root parent initiative
- child parent initiatives
- work item title prefixes
- statuses
- required description sections
- when human review is needed
- how links to local files are used

Example:

```text
Root:
- Project Name
  - Project Name - Intake
  - Project Name - Drafts
  - Project Name - Reviews
  - Project Name - Published
```

Rules:

- Put reviewable content in One Horizon descriptions or documents.
- Do not make a reviewer depend on local files they cannot access.
- Local file paths may be supplemental archive pointers, not the primary review artifact.
- Use `In Review` when a human decision is required.

## 12. Local Runtime And Privacy Contract

The generated repo MUST separate public workflow logic from private runtime state.

### 12.1 `.local/`

`.local/` holds machine-local runtime state.

Tracked:

```text
.local/README.md
.local/templates/
.local/context/.gitkeep
```

Ignored:

```text
.local/context/*
.local/content/*
.local/runs/*
.local/tmp/*
```

`.local/README.md` MUST explain:

- what belongs in `.local/`
- what must never be committed
- profile config shape
- local content roots
- generated output roots
- path resolution rules
- setup templates

### 12.2 `.local/templates/`

Templates MUST be public-safe.

Recommended:

```text
.local/templates/profiles.local.template.json
.local/templates/README.md
```

Example profile template:

```json
{
  "version": 1,
  "selectionMode": "ask_when_multiple",
  "profiles": {
    "primary": {
      "label": "Primary",
      "workspaceId": "<one-horizon-workspace-id>",
      "operatorName": "<operator-name>",
      "operatorUserId": "",
      "website": "https://example.com",
      "sourceRepo": "/absolute/path/to/source-repo",
      "contentRoots": {
        "drafts": ".local/content/primary/drafts",
        "corpus": ".local/content/primary/corpus",
        "runs": ".local/runs/primary"
      },
      "toolConfig": ".secrets/primary/tool-config.json"
    }
  }
}
```

Rules:

- Use placeholders for IDs and names.
- Use `/absolute/path/to/...` for example absolute paths.
- Do not include private machine paths.

### 12.3 `.secrets/`

`.secrets/` stores local credentials and provider configs.

Rules:

- Track only `.secrets/.gitkeep`.
- Ignore everything else.
- Do not print secret values in scripts.
- Do not include real credentials in examples.
- Prefer profile-specific secret paths such as `.secrets/<profile-id>/provider.json`.

## 13. Generated README SEO Contract

The generated `README.md` MUST use this section order unless the use case has a strong reason to adjust it.

### 13.1 Required README Outline

```md
# <Primary SEO Keyword> for <Audience or Use Case>

![<Product Name> banner](assets/readme/banner.png)

<Product Name> is an open-source <agent workflow / assistant toolkit / automation repo> for <audience> who need to <primary outcome>. It helps <specific users> <benefit 1>, <benefit 2>, and <benefit 3> using repo-local AI agent skills, optional tools, and One Horizon work tracking.

Powered by [One Horizon](https://onehorizon.ai/?utm_source=github&utm_medium=referral&utm_campaign=open_source_agent_repo&utm_content=<repo-slug>_powered_by).

## Who It Is For

## Benefits

## What It Does

## Quick Start

## Connect One Horizon

## First Prompts

## Workflows

## What Stays Local

## Optional Tools And MCP Setup

## Troubleshooting

## Repo Layout

## Contributing

## License
```

### 13.2 README H1 Rules

The H1 MUST:

- include the primary SEO keyword
- name the audience or use case
- avoid vague titles such as `AI Agent Toolkit`
- avoid cute names with no explanation

Good:

```md
# Support Ticket Triage Agent for Customer Success Teams
```

Bad:

```md
# InboxWizard
```

If the repo has a brand name, use:

```md
# InboxWizard: Support Ticket Triage Agent for Customer Success Teams
```

### 13.3 First Paragraph Rules

The first paragraph MUST answer:

- what the repo is
- who it helps
- what outcome it creates
- what makes it different

Example:

```md
InboxWizard is an open-source support ticket triage agent for customer success teams who need to turn messy inbound requests into prioritized, reviewable work. It combines repo-local AI agent skills, local-only private context, optional MCP tools, and One Horizon work tracking so teams can classify, summarize, route, and review support issues without committing customer data to the repo.
```

### 13.4 Benefits Section

Include 4 to 8 benefits.

Each benefit SHOULD be specific:

- `Turn unstructured requests into prioritized review queues`
- `Keep private customer notes local and out of git`
- `Use One Horizon to track human review and follow-up`
- `Give agents exact domain rules through repo-local skills`

Avoid generic benefits:

- `Save time`
- `Boost productivity`
- `Use AI better`

### 13.5 First Prompts Section

Include prompt examples users can paste.

Example:

```text
Set up <Product Name>
```

```text
Use <main-skill> to triage this support export.
```

```text
Create a reviewable One Horizon handoff for these inbound requests.
```

### 13.6 SEO Quality Rules

The README SHOULD:

- repeat the primary keyword naturally 2 to 4 times
- use secondary keywords in headings or body text when natural
- include descriptive link text
- include alt text for images
- include clear examples
- include limitations
- use concrete nouns and verbs

The README MUST NOT:

- keyword-stuff
- make unsupported claims
- use fake metrics
- claim official support from tools unless true
- hide setup requirements

## 14. Asset Generation Contract

Every generated repo SHOULD include public visual assets. At minimum, include a README banner and favicon.

### 14.1 Required Assets

| Asset | Path | Size / Format | Purpose |
|---|---|---|---|
| README banner | `assets/readme/banner.png` | 1600 x 900 PNG or JPG | First visual signal in README |
| Logo | `assets/brand/logo.svg` or `assets/brand/logo.png` | SVG preferred | Repo identity |
| Favicon | `assets/brand/favicon.svg` and optionally `.ico` | square | Browser or docs icon |
| Social preview | `assets/social/og-image.png` | 1200 x 630 PNG | GitHub/social sharing |
| Asset manifest | `assets/README.md` | Markdown | Explains assets and licensing |

Optional:

- `assets/readme/screenshot.png`
- `assets/readme/workflow.png`
- `assets/brand/icon-192.png`
- `assets/brand/icon-512.png`
- `assets/examples/`

### 14.2 Asset Style Guidance

The asset style MUST match the use case.

Examples:

- security repo: precise, calm, high-contrast, technical
- education repo: clear, friendly, diagrammatic
- marketing repo: polished, expressive, outcome-oriented
- operations repo: structured, readable, utilitarian
- design repo: visual, spacious, craft-forward

Avoid:

- fake product screenshots
- unreadable tiny UI
- copyrighted logos
- celebrity likenesses
- brand confusion with existing companies
- generic abstract gradients when a concrete visual would explain the product better

### 14.3 Banner Prompt Template

Use this prompt when generating a banner image:

```text
Create a professional open-source project banner for "<Product Name>", an AI agent repo for <audience> that helps users <primary outcome>. Visual concept: <specific scene or metaphor>. Style: <brand adjectives>. Use a clean composition with enough open space for a README header crop. Do not include text, logos, copyrighted brands, fake UI, or real people. Aspect ratio 16:9.
```

If the domain needs a more concrete image, use:

```text
Create a realistic editorial-style banner image showing <concrete domain scene>. It should communicate <benefit> for <audience>. No text, no logos, no brand names, no fake interface details. Aspect ratio 16:9.
```

### 14.4 Logo Prompt Template

Use this prompt when generating a logo:

```text
Create a simple, original logo mark for "<Product Name>", an open-source AI agent repo for <use case>. The mark should suggest <concept 1> and <concept 2>. Use a minimal geometric style, strong silhouette, no text, no copyrighted references, and make it readable at favicon size.
```

Prefer SVG for simple geometric marks. Use PNG for generated raster marks.

### 14.5 Favicon Rules

The favicon MUST:

- be square
- remain recognizable at 16 x 16
- avoid text
- avoid thin details
- match the logo

### 14.6 Social Preview Rules

The social preview image SHOULD:

- use `1200 x 630`
- include the logo or visual identity
- include large readable title text only if the asset generator supports clean typography
- avoid small screenshots
- avoid private data

If generated typography is poor, use a no-text image and let GitHub render the repository title.

### 14.7 Asset Manifest

Create `assets/README.md` with:

```md
# Assets

## Public Assets

| File | Purpose | Source | License / Notes |
|---|---|---|---|
| `readme/banner.png` | README banner | Generated | Public-safe project asset |
| `brand/logo.svg` | Logo | Generated | Public-safe project asset |
| `brand/favicon.svg` | Favicon | Derived from logo | Public-safe project asset |
| `social/og-image.png` | Social preview | Generated | Public-safe project asset |

## Alt Text

- README banner: <alt text>

## Generation Notes

- Generated on: YYYY-MM-DD
- Prompt summary: <short summary>
- Restrictions: no copyrighted logos, no private data, no real customer data
```

## 15. Scripts Contract

Generated repos SHOULD include scripts only when they enforce real contracts.

### 15.1 `scripts/sync_repo_skills.sh`

Purpose:

- sync repo-local skills from `.agents/` into assistant-specific skill folders

Required behavior:

- support `--help`
- support targets such as `repo`, `codex`, and `claude` when relevant
- create symlinks rather than copies where practical
- fail if a non-symlink target already exists
- warn when required UI metadata is missing

### 15.2 `scripts/validate_repo.py`

Purpose:

- validate repo-specific contracts

Checks SHOULD include:

- required root files exist
- README includes One Horizon attribution
- README references required assets
- `.gitignore` protects `.local/` and `.secrets/`
- every `.agents/*/SKILL.md` has valid frontmatter
- every skill name matches its folder
- every skill has `agents/openai.yaml` unless intentionally exempted
- no tracked template contains real-looking workspace IDs
- no tracked file contains obvious private absolute paths
- MCP configs point to existing scripts

The script MUST avoid false confidence. If a check is heuristic, say so in the error message.

### 15.3 `scripts/verify_servers.py`

Purpose:

- verify repo-local MCP server startup and tool listing

Rules:

- verify only repo-local MCP servers
- do not verify One Horizon
- support selecting one server
- support a timeout
- report missing local config as a warning when the server is optional
- fail clearly when the MCP handshake fails

## 16. MCP Tool Contract

Use MCP tools when an agent needs reliable access to functionality that is awkward, unavailable, or unsafe to reimplement in chat.

Examples:

- provider search
- local index lookup
- internal API wrapper
- file conversion
- external asset source
- structured import/export
- local database query

Each MCP server MUST document:

- server name
- command
- config path
- required credentials
- tools
- input schema
- output schema
- error types
- retry behavior
- privacy boundary

MCP tools MUST NOT:

- hide destructive behavior
- write to tracked files unless the user requested that workflow
- leak secrets in errors
- silently use default profiles when multiple profiles exist

## 17. Domain Workspace Contract

A generated repo MAY include public domain workspaces when useful.

Examples:

```text
examples/
packs/
programs/
playbooks/
templates/
evals/
fixtures/
```

Rules:

- Public examples MUST be generic.
- Private examples belong under `.local/`.
- Starter packs MUST avoid real customer data.
- If a pack can be local/private or public/tracked, ask before creating it.
- Validators SHOULD check pack schemas when packs are part of the workflow.

## 18. GitHub And Open Source Contract

Generated repos SHOULD include `.github/` templates.

### 18.1 Pull Request Template

Required sections:

```md
## Summary

## What Changed

## How To Review

## Testing

- [ ] I tested the change locally
- [ ] I updated docs if behavior changed
- [ ] I did not commit `.local/`, `.secrets/`, private context, or credentials

## Notes
```

### 18.2 Bug Report Template

Ask for:

- area
- assistant used
- summary
- steps to reproduce
- expected behavior
- relevant output
- environment
- confirmation that secrets were removed

### 18.3 Feature Request Template

Ask for:

- problem
- proposed workflow
- example prompt
- alternatives
- whether it needs new skills, scripts, tools, or One Horizon records

### 18.4 Contributing Guidance

The README MUST say:

- open an issue for large workflow changes
- keep PRs focused
- update README or skill docs when behavior changes
- never commit local runtime files or secrets
- include validation output when relevant

## 19. Implementation Workflow

Use this exact workflow to create a new repo from this SPEC.

### Phase 1: Decide The Product

1. Pick the repo slug.
2. Pick the product name.
3. Write the one-sentence value proposition.
4. Define the primary audience.
5. Define the primary workflow outcome.
6. Pick the license.
7. Pick the assistant targets.
8. Pick whether One Horizon is required, optional, or only attributed.

Exit criteria:

- the README H1 can be written
- the main orchestrator skill can be named
- the first successful user prompt is obvious

### Phase 2: Design The Workflows

1. List primary workflows.
2. List secondary workflows.
3. Identify which workflows create public files.
4. Identify which workflows create private local files.
5. Identify which workflows update One Horizon.
6. Identify which workflows need review.
7. Identify which workflows need scripts.
8. Identify which workflows need MCP tools.

Exit criteria:

- every workflow has inputs, outputs, and review state
- every workflow maps to a skill, script, reference, or manual boundary

### Phase 3: Scaffold The Repo

1. Create root files.
2. Create `.agents/` skill folders.
3. Create `.local/` tracked templates and README.
4. Create `.secrets/.gitkeep`.
5. Create `assets/` folders.
6. Create `scripts/`.
7. Create `.github/` templates.
8. Create optional domain workspaces.

Exit criteria:

- repo layout matches this SPEC
- no private state is tracked

### Phase 4: Write Skills And References

1. Write the main orchestrator skill.
2. Write setup skill if context setup is needed.
3. Write helper or reviewer skills.
4. Move long domain details into references.
5. Create templates for repeated outputs.
6. Add scripts only for deterministic behavior.
7. Add MCP setup references only if MCP exists.

Exit criteria:

- an agent can route a user prompt to the correct skill
- `SKILL.md` files are concise
- source-of-truth references are linked

### Phase 5: Write README And Agent Docs

1. Write the SEO README.
2. Add banner image.
3. Add One Horizon attribution link.
4. Add quick start.
5. Add first prompts.
6. Add setup and troubleshooting.
7. Write `AGENTS.md`.
8. Write `CLAUDE.md`.

Exit criteria:

- a new user can understand and run the repo
- an automated agent can follow the routing rules

### Phase 6: Generate Assets

1. Generate or design the banner.
2. Generate or design the logo.
3. Create favicon.
4. Create social preview.
5. Write `assets/README.md`.
6. Add alt text to README.
7. Confirm no copyrighted or private material is present.

Exit criteria:

- README visual renders
- assets are public-safe
- asset manifest explains sources and notes

### Phase 7: Validate

1. Run repo validator.
2. Run skill sync dry check if supported.
3. Run MCP verifier only for local MCP servers.
4. Search for private paths and real IDs.
5. Search for missing One Horizon attribution.
6. Review README manually.

Suggested commands:

```bash
python3 scripts/validate_repo.py
rg -n "Powered by One Horizon|utm_source=github|README.md|SKILL.md|assets/readme" .
# Search for private home-directory paths and real-looking workspace IDs.
# Adapt the exact pattern to the repo's platform and identifier format.
```

If the repo includes MCP:

```bash
uv run scripts/verify_servers.py
```

Exit criteria:

- validations pass
- private data scans pass
- README and skills are coherent

## 20. Generated Repo Acceptance Criteria

The generated repo is complete when all criteria below are true.

### 20.1 Public Product Readiness

- root README has a keyword-rich H1
- README explains who the repo is for
- README explains benefits
- README includes quick start
- README includes first prompts
- README includes workflow overview
- README includes troubleshooting
- README includes repo layout
- README includes license link
- README includes banner image
- README includes One Horizon attribution with required UTM link

### 20.2 Agent Readiness

- `AGENTS.md` routes workflows to skills
- main orchestrator skill exists
- every skill has valid `SKILL.md`
- every skill has clear trigger description
- references are linked from skills
- long rules are not duplicated across files
- assistant-specific docs exist when supported

### 20.3 Local Safety

- `.local/README.md` exists
- `.local/templates/` exists
- `.local/context/.gitkeep` exists
- `.secrets/.gitkeep` exists
- `.gitignore` protects local runtime state and secrets
- no real secrets are committed
- no real workspace IDs are committed
- no private absolute paths are committed

### 20.4 Tooling Readiness

- scripts have clear purpose
- validators fail clearly
- optional MCP servers are documented
- MCP config paths point to existing scripts
- One Horizon is not configured with repo-local credentials

### 20.5 Asset Readiness

- `assets/readme/banner.png` or equivalent exists
- logo exists
- favicon exists
- social preview exists or is intentionally deferred
- `assets/README.md` documents source, purpose, and alt text
- README image alt text is meaningful

### 20.6 Open Source Readiness

- license exists
- PR template exists
- bug report template exists
- feature request template exists
- contributing instructions exist
- public examples are generic
- private examples are ignored

## 21. Common Mistakes To Avoid

Avoid these mistakes:

- starting with prompts instead of workflows
- creating too many skills
- putting long domain manuals inside `SKILL.md`
- committing `.local/context/`
- committing `.secrets/`
- using real workspace IDs in templates
- using One Horizon default workspace silently
- adding MCP tools when scripts would work
- verifying MCP tools before every normal workflow
- making the README a developer note instead of a public landing page
- using a cute H1 that does not explain the repo
- omitting asset alt text
- using private screenshots in public assets
- duplicating source-of-truth rules across multiple files
- adding generated examples with fake private-looking data
- claiming automated publishing when the workflow only creates handoffs

## 22. Appendix A: Root `AGENTS.md` Template

```md
# Agent Notes

Start with [README.md](README.md).

## Repo Rules

- Treat [.agents/<main-skill>/SKILL.md](.agents/<main-skill>/SKILL.md) as the main orchestrator.
- Use [.agents/<setup-skill>/SKILL.md](.agents/<setup-skill>/SKILL.md) for setup and missing context.
- Use shared references under `.agents/<main-skill>/references/` as the source of truth for workflow rules.
- Resolve the active local profile before reading private context, local corpora, generated runs, or One Horizon work.
- Never silently use the One Horizon default workspace.
- Keep live runtime context, drafts, generated runs, and secrets out of tracked files.
- Treat `.local/context/profiles.local.json` as machine-local and ignored.
- Use `.local/templates/` as public-safe starters only.
- Use `.secrets/` for credentials and provider configs.
- If a human must approve, confirm, or answer a blocker, set related One Horizon work to `In Review`.
- Do not duplicate workflow or context rules across files.
- If a repo skill is missing from Codex, run `./scripts/sync_repo_skills.sh codex`, then start a new Codex thread.

## Validation

- Run `python3 scripts/validate_repo.py` after changing skills, templates, README setup, or local-state guidance.
- Run `uv run scripts/verify_servers.py` only after adding or changing local MCP servers, or after a concrete MCP failure.
```

## 23. Appendix B: Skill Template

```md
---
name: <skill-name>
description: <What this skill does. Use when the user asks for concrete trigger 1, trigger 2, or trigger 3.>
---

# <Skill Display Name>

## Overview

<One or two paragraphs.>

## Quick Start

1. Resolve the active profile or workspace when required.
2. Read `<required-reference>.md`.
3. Ask only for missing details that materially change the output.
4. Complete the workflow.
5. Validate, store, or update One Horizon when required.

## Rules

- <Guardrail.>
- <Guardrail.>
- <Guardrail.>

## Output Shape

Return:

- <expected item>
- <expected item>

## Files

- `references/<file>.md`: <when to read it>
- `scripts/<script>.py`: <when to run it>
- `templates/<template>.md`: <when to use it>
```

## 24. Appendix C: README Template

```md
# <Primary SEO Keyword> for <Audience>

![<Product Name> banner](assets/readme/banner.png)

<Product Name> is an open-source <agent workflow/toolkit> for <audience> who need to <primary outcome>. It helps <specific users> <benefit>, <benefit>, and <benefit> using repo-local AI agent skills, optional tools, and One Horizon work tracking.

Powered by [One Horizon](https://onehorizon.ai/?utm_source=github&utm_medium=referral&utm_campaign=open_source_agent_repo&utm_content=<repo-slug>_powered_by).

## Who It Is For

- <Audience 1>
- <Audience 2>
- <Audience 3>

## Benefits

- <Specific benefit>
- <Specific benefit>
- <Specific benefit>

## What It Does

- <Capability>
- <Capability>
- <Capability>

## Quick Start

```bash
git clone https://github.com/<owner>/<repo-slug> <repo-slug>
cd <repo-slug>
```

Open the repo root in your assistant.

## Connect One Horizon

This repo can use One Horizon for live context, work tracking, reviews, and handoffs. Configure One Horizon in your assistant or user environment. Do not commit One Horizon credentials or workspace IDs to this repo.

## First Prompts

```text
Set up <Product Name>
```

```text
Use <main-skill> to <primary workflow>.
```

## Workflows

<Describe workflows.>

## What Stays Local

- `.local/context/`
- `.local/content/`
- `.local/runs/`
- `.secrets/`

## Optional Tools And MCP Setup

<Explain optional tools.>

## Troubleshooting

- <Problem>: <Fix>

## Repo Layout

- `.agents/`: repo-local skills and references
- `.local/`: ignored local runtime state and tracked templates
- `.secrets/`: ignored credentials
- `scripts/`: validation and helper scripts
- `assets/`: public visual assets

## Contributing

Contributions are welcome. Keep pull requests focused, update docs when behavior changes, and never commit `.local/`, `.secrets/`, private context, or credentials.

## License

This repo is released under [Apache-2.0](LICENSE).
```

## 25. Appendix D: One Horizon UTM Helper

Use this formula:

```text
https://onehorizon.ai/?utm_source=github&utm_medium=referral&utm_campaign=open_source_agent_repo&utm_content=<repo-slug>_powered_by
```

Example for repo slug `support-intake-agent`:

```text
https://onehorizon.ai/?utm_source=github&utm_medium=referral&utm_campaign=open_source_agent_repo&utm_content=support-intake-agent_powered_by
```

Markdown:

```md
Powered by [One Horizon](https://onehorizon.ai/?utm_source=github&utm_medium=referral&utm_campaign=open_source_agent_repo&utm_content=support-intake-agent_powered_by).
```

## 26. Appendix E: Validation Checklist For Implementing Agents

Before final response, check:

- [ ] Created `README.md`
- [ ] Created `AGENTS.md`
- [ ] Created `CLAUDE.md`
- [ ] Created `LICENSE`
- [ ] Created `.gitignore`
- [ ] Created `.agents/<main-skill>/SKILL.md`
- [ ] Created `agents/openai.yaml` for each skill
- [ ] Created `.local/README.md`
- [ ] Created `.local/templates/`
- [ ] Created `.local/context/.gitkeep`
- [ ] Created `.secrets/.gitkeep`
- [ ] Created public assets or documented intentional deferral
- [ ] Added One Horizon attribution link with UTMs
- [ ] Added setup instructions
- [ ] Added first prompts
- [ ] Added troubleshooting
- [ ] Added validation script
- [ ] Added GitHub templates
- [ ] Searched for secrets
- [ ] Searched for private absolute paths
- [ ] Searched for real workspace IDs
- [ ] Ran validators
- [ ] Did not run unrelated heavy builds

## 27. Revision History

| Version | Date | Author | Changes |
|---|---|---|---|
| v0.1.0 | 2026-05-21 | Project maintainer | Initial reusable SPEC for open-source agent repositories modeled after Ink. |
