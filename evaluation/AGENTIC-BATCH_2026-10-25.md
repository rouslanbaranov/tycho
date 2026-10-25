# Bounded batch read and evidence - 2026-10-25

> Issue [#412](https://github.com/rouslanbaranov/tycho/issues/412), E18-07.
> **Status:** implemented and tested; not answer-quality acceptance and not
> independent review. No file under `book/` was modified.

## What changed

Added `tycho_batch` for bounded verification:

- up to eight combined section reads and document/claim/source evidence IDs;
- per-item result, status and error isolation;
- a per-section `budget_chars` and a response `max_chars`;
- a partial status when any item fails;
- no unbounded fetching and no source text from evidence resolution.

Single-item `tycho_read` and `tycho_evidence` remain unchanged.

## Evidence

Unit and HTTP-facing tests cover successful reads, registered evidence,
missing-section isolation, partial status and the response notice. No separate
latency benchmark was run; the task reduces round trips rather than changing
retrieval quality.

## Limits

- Batch size is deliberately small (eight combined items).
- Evidence resolution returns metadata, not source text.
- No remote agent trace, answer-quality benchmark, human review or independent
  review.
- `human_review: not-performed; sufficient: 0`.
