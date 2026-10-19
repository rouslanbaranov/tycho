# Tycho manuscript acceptance and owner-approved gate dispositions

Decision recorded: 2026-10-20, Europe/Zurich.

Authority: the project owner's explicit instruction in the Rocinante project
conversation at 00:50:09 +02:00. Faithful English translation: "We cancel visual
rendering and live MCP checks. Independent acceptance has been completed."

## Applicable manuscript

This decision applies to the integrated Tycho manuscript in PR #216 at
`a584857eb2947feef2d19c0a6b187efe9b02f7b6`: the 69 proposed primary chapter
owners and the 29 historical cases plus six comparative decision playbooks.
Subsequent documentation-only recording of this decision does not change the
accepted technical content.

| Gate | Current disposition | Basis |
|---|---|---|
| Independent acceptance | COMPLETED — owner-confirmed | Explicit owner confirmation in the project conversation |
| Visual/browser rendering | CANCELLED — owner-approved waiver | Explicit owner cancellation; no visual execution is claimed |
| Live MCP scenario execution | CANCELLED — owner-approved waiver | Explicit owner cancellation; the 60 fixture definitions are not runtime results |
| Full pinned Python validation | PASSED | 178 main tests and 17 M9 tests, no failures or skips, on the SHA above |
| Complete metadata, navigation and routing checks | PASSED | 136 documents; strict knowledge and index freshness checks passed |
| Mermaid syntax parsing | PASSED | All 191 diagrams parsed by Mermaid 11.17.2; distinct from the cancelled visual gate |

This record supersedes earlier statements that independent acceptance, browser
rendering or live MCP execution remain outstanding manuscript acceptance
blockers. It is the current disposition for the unified gate map and both core
and M9 acceptance ledgers; their dated pre-review tables remain historical.

## Evidence and scope preservation

Independent acceptance is recorded as completed based on the owner's
confirmation. No external reviewer identity, individual review date, per-claim
verdict, separate copyright certificate or inspection log was supplied in that
instruction; this record does not invent those details. Existing source
uncertainties, bounded historical claims and citation limitations remain part
of the accepted content.

The book-level acceptance event is recorded here. Page-level metadata and
portable example records are not relabelled as independently verified source
claims, nor assigned fabricated reviewer details. The existing 36 documents with
normalized global-source references and 100 unknown metadata evidence states remain
unchanged; package acceptance does not constitute provenance normalization.

Cancellation of live checks does not assert that a hosted MCP service exists,
nor cancel future MCP implementation scope. Cancelled checks must be described
as waived/cancelled, never as executed or passed. The parser and existing
fixtures remain available.

## Repository actions

Recording this decision does not merge PR #216, close issues or milestones,
publish an edition, change CI triggers, or alter the original source PRs.
Those actions require their own explicit release decision. Draft/open GitHub
states therefore do not contradict the acceptance event recorded here.

## Related registers

- [Unified manuscript map](UNIFIED_BOOK_M1_M9_INTEGRATION.md)
- [Core chapter ledger](CHAPTER_EDITORIAL_ACCEPTANCE_LEDGER.md)
- [M9 acceptance matrix](cases/M9_REVIEW_ACCEPTANCE_MATRIX.md)
- [Executed corpus migration and checks](CORPUS_METADATA_MIGRATION_2026-10-20.md)
