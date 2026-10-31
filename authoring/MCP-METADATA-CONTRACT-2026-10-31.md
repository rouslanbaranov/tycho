# MCP metadata and onboarding contract — 2026-10-31

Status: implementation and AI tests. No book/atlas content change. Not human
review, CI or owner acceptance.

## What agents receive

Every tool now exposes:

- a closed inputSchema;
- an outputSchema with described fields;
- tycho_describe.metadata catalog;
- frontmatter on page/read;
- explicit pagination and drill-down rules.

### Metadata catalog

tycho_describe.metadata contains:

- closed enums for kind, evidence_status, artifact_type and volume;
- frontmatter fields with type, description and boundary;
- search-result fields with type, description and boundary;
- pagination rules for read/page/search/patterns;
- output schemas by tool.

### Frontmatter

tycho_page and tycho_read return parsed frontmatter. Page/read also return
resolved related entries. Search results expose summary, topics, perspectives
and related_ids.

The page body still starts after frontmatter; frontmatter is no longer silently
lost.

### Pagination

- page/read: offset, budget_chars, total_chars, next_offset, truncated;
- continuation rule: call again with offset=next_offset;
- search: no offset/cursor; refine the query, max limit 20;
- patterns: offset/limit.

### Onboarding

INSTRUCTIONS now describes the iterative search/page/read workflow, pagination,
metadata catalog location and agent default abstain=false.
MCP-READ-ONLY-MVP.md documents input/output schemas, frontmatter, related
navigation and pagination.

The stale claim that hybrid ranking is not implemented was removed; the
describe answerability block now reports the score-floor gate instead of an
uncalibrated placeholder.

## Verification

- all 11 tools have outputSchema;
- all input and output schema properties have descriptions;
- contract tests: 4/4 PASS;
- page frontmatter and related entries verified;
- search summary/related_ids verified.

## Limits

- Output schemas describe key fields with additionalProperties allowed; they
  are not a code-generated exhaustive type graph.
- Frontmatter is returned by page/read; search carries selected projections,
  not the complete frontmatter object.
- Topic values remain dynamic; no artificial closed enum.
- Search still has no cursor; iterative refinement is the intended drill-down.
- No human review, CI, owner acceptance or production benchmark.
