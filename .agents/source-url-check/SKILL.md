---
name: source-url-check
description: Verify cited, embedded, or recommended URLs in blog drafts using local research tools or equivalent web access. Use when a blog article contains source links, outbound links, citations, or recommended URLs that must be checked to confirm the page exists, is not a 404 or soft-404, and matches the expected content before publication.
---

# Source URL Check

Verify source URLs without turning the pass into a sourcing memo.

## Read

- the active writer skill's workflow file
- the active writer skill's review-passes file
- the active writer skill's MCP or research-tools reference when available

## Workflow

1. List the URLs that appear in the draft, notes, citations, or planned outbound links.
2. Check the exact URL first with the local research tools:
   - `fetch_page`
   - `web_search`
3. Treat the URL as verified only if the page resolves and the page content matches what the draft says it is.
4. Watch for failure modes:
   - hard 404s
   - soft 404s or "page not found" content on a 200 page
   - redirects to a homepage, category page, or login wall when the draft expects a specific article or doc page
   - a different article, product page, or domain than the draft implies
5. If the exact URL fails or looks wrong, use `web_search` to find the likely canonical page.
6. Replace broken or mismatched URLs when a clearly better canonical URL exists.
7. Remove or soften URLs you cannot verify.

## Guardrails

- check URL existence and page identity, not claim accuracy
- leave factual verification to the fact-check pass
- prefer canonical docs, company pages, or original publications over tracking links, mirrors, or syndication copies
- if no URLs are present, say so briefly and stop

## Output

Return:

- the revised draft if any URLs changed
- a short list of checked URLs and whether they passed
- any URLs replaced or removed
- what still remains uncertain
