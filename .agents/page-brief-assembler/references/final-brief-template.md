# Final Brief Template

Use the `# Page Brief` structure exactly.
Do not output this file's instructional text or hard rules.
The final artifact starts at `# Page Brief`.

The final brief is a locked execution spec. It tells the next agent exactly what to produce. It does not persuade, explain the research process, or offer options.

## Hard Rules

- Make decisions. Do not give directions.
- Write `H1: "..."`; never write advisory H1 language.
- Write `Title tag: "..."`; never write advisory title language.
- Write exact CTA labels, exact section names, exact supporting-content modules, and exact internal links.
- Do not include alternatives unless the user must choose before work can continue. If the user must choose, stop and ask.
- Do not include a source ledger, workflow note, research recap, rationale section, or explanation of why the brief has each section.
- Do not create a generic section named `FAQ And Related Pages`.
- Do not use `should`, `could`, `consider`, `maybe`, `likely`, `recommended`, `suggested`, `direction`, `option`, `TBD`, `TODO`, `placeholder`, `etc.`, or vague filler.
- Do not write generic instructions such as `add proof`, `improve CTA`, `tighten copy`, `make clearer`, or `use better examples`.
- If an instruction cannot be made exact from confirmed inputs and validated research, stop and ask the next verification questions.
- If a claim is not validated, either omit it from the brief or write `Do not claim: [exact claim]`.
- Keep the brief concise. Prefer tight bullets and tables over paragraphs.
- Do not output production code, HTML, CSS, JS, React, or component code.

# Page Brief

## 1. Locked Page Spec

- URL:
- Status:
- Page type:
- Audience:
- Page goal:
- Primary CTA:
- Secondary CTA:
- H1:
- Title tag:
- Meta description:
- URL slug:
- One-line mandate:
- Code boundary: This brief contains no production code.

## 2. Inputs And Constraints

- Confirmed user inputs:
- Confirmed site facts:
- Confirmed competitor facts:
- Business constraints:
- Page constraints:
- Claims to avoid:
- Open blockers: none

If `Open blockers` is not `none`, do not produce the brief. Ask the next verification questions instead.

## 3. Required Page Changes

For update briefs, use this table. For new pages, write `New page: no existing page changes.`

| Action | Current item | Final instruction |
| --- | --- | --- |
| Keep |  |  |
| Replace |  |  |
| Add |  |  |
| Remove |  |  |
| Move |  |  |

Every row must be an instruction, not an observation.

## 4. Final Page Structure

Create one subsection per page section in final order. Use section numbers.

### 1. [Exact section name]

- Placement:
- Section heading:
- Required content:
- Required proof or link:
- CTA:
- Do not include:

Repeat until the page structure is complete.

Rules:

- `Section heading` must be exact text.
- `Required content` must say what the section will include, not what the writer needs to explore.
- `Required proof or link` must name the proof, link, or `none`.
- `CTA` must be an exact label and destination, or `none`.
- `Do not include` must name exact claims, angles, or content to avoid.

## 5. Copy Contract

- H1:
- Hero subheading:
- Primary CTA label:
- Secondary CTA label:
- Title tag:
- Meta description:
- Required section headings:
- Supporting content module:
- Terms to use:
- Terms to avoid:
- Comparison wording rule:

All copy fields must be exact or the brief must stop and ask for the missing input.
Use `Supporting content module: none` when the page does not need an extra support block.
Use an FAQ only when the existing page already has one, the search intent clearly requires Q&A, or the user asks for it.
When support content is needed, name the exact module, such as `Docs CTA`, `Comparison table`, `Setup steps`, `Related integrations`, `Security note`, or `FAQ`.

## 6. SEO And Links

- Organic role:
- Primary query:
- Secondary queries:
- Internal links:
- External proof links:
- Structured data:
- Supporting content:
- Cannibalization rule:

Do not list keywords that do not change the page.
