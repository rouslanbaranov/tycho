# Optional section rerank API — 2026-10-29

Status: opt-in implementation, not default. Diagnostic validation on
agent-adjudicated section qrels; not human review, independent review, CI or
owner acceptance.

## Change

- `section_search.search(..., section_rerank=False)`.
- Default remains best-section-per-document BM25.
- `section_rerank=True` ranks matching H2 sections across the top pages by
  query-term coverage and heading hits, with BM25 as tie-breaker.
- `all_sections=True` and `section_rerank=True` are mutually exclusive.
- CLI: `--section-rerank`.

## Validation

| Split | n | BM25 section hit@1/3/5 | section_rerank hit@1/3/5 |
|---|---:|---|---|
| phase2 held-out | 54 | .130/.315/.352 | **.185/.370/.426** |
| phase3 pilot | 19 | .263/.368/.526 | **.316/.526/.684** |

The API reproduces the diagnostic experiment after the BM25 tie-breaker.
Combined 73 queries: .164/.329/.397 -> .219/.411/.493.

## Decision

- Keep default BM25.
- Section rerank is optional and not enabled by default.
- It still needs a held-out independent review and production latency tests.
- No human/owner/CI/sufficiency claim.

## Limits

- 73 section-labelled queries, agent-adjudicated.
- Absolute section top-1 remains 21.9%.
- No section rerank for filters/all_sections combinations beyond the guard.
- Performance of the extra per-page section query is not yet benchmarked.
