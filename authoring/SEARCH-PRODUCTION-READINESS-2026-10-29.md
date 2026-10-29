# Search production readiness — 2026-10-29

Status: **not production-certified**. Owner accepted AI labels as evidence on
2026-10-29; that is not human review, CI or a sufficient-coverage claim.

Update 2026-10-29: MCP `tycho_search` now defaults to
`section_rerank=true, section_rerank_margin=0.15`. Core API and CLI remain
explicit. See [MCP-MARGIN-DEFAULT-2026-10-29.md](MCP-MARGIN-DEFAULT-2026-10-29.md).

## Acceptance

- Owner accepted AI labels for diagnostics in
  [OWNER-ACCEPTANCE-AI-LABELS-2026-10-29.md](OWNER-ACCEPTANCE-AI-LABELS-2026-10-29.md).
- This is not human review and does not remove the phase3 regression.

## Defaults

- MCP default: margin-gated section rerank, `section_rerank=true` and
  `section_rerank_margin=0.15`.
- Core API/CLI default remains explicit BM25.
- Best mode is optional and requires semantic artifacts/model cache.
- Global section rerank remains optional (`section_rerank_margin=null`).
- V12 explicit/top-page/query guard prevents known section-rerank regression.

## Evidence

Page-level qrels v3 (188 queries, AI-adjudicated):

| Mode | hit@1/3/5 |
|---|---|
| BM25 | .878/.952/.973 |
| best mode | .920/.963/.979 |

Best v3 gap is not significant (p=.0768); after excluding prior pages it falls
to +1.1 points. Do not default best mode.

Section-qrels v3 guarded (188 queries, AI-adjudicated):

| Mode | hit@1/3/5 |
|---|---|
| BM25 | .803/.941/.979 |
| section_rerank | .883/.941/.968 |

Guarded section top-1 is significant (p=.0041), but phase3 page top-1 still
regresses .895 -> .842. Default section_rerank is not safe.

## Performance

- best mode warm p50 112 ms, p95 132 ms.
- section_rerank local p50 +3.9 ms, p95 +0.8 ms.
- Section rerank cache key and query-cache behavior are tested.

## Tests

- 727 tests pass.
- MCP search schema is closed; section_rerank opt-in tested.
- V12 guards tested.
- Local premerge checks pass; milestone acceptance is separate.

## Open gates before any default change

1. Phase3 page-level regression needs a guard or a dedicated section rerank
   variant that does not reorder the top page.
2. Independent human/owner adjudication is still absent; all qrels v3 labels
   are AI.
3. The section pool was built from both default and rerank candidates; a
   mode-independent pool is needed for an unbiased estimate.
4. Default switch requires owner acceptance and a production client benchmark.

## Artifacts

- [BEST-SEARCH-2026-10-29.md](BEST-SEARCH-2026-10-29.md)
- [QRELS-V3-AI-ADJUDICATION-2026-10-29.md](QRELS-V3-AI-ADJUDICATION-2026-10-29.md)
- [SECTION-QRELS-V3-AI-2026-10-29.md](SECTION-QRELS-V3-AI-2026-10-29.md)
- [SECTION-RERANK-GUARDED-2026-10-29.md](SECTION-RERANK-GUARDED-2026-10-29.md)
- [SECTION-RERANK-PAGE-TRADEOFF-2026-10-29.md](SECTION-RERANK-PAGE-TRADEOFF-2026-10-29.md)
- [MCP-SECTION-RERANK-2026-10-29.md](MCP-SECTION-RERANK-2026-10-29.md)

## Limits

- AI labels; same session family.
- Stale/loose accepted sets; page-level majority.
- No human review, CI, owner acceptance or sufficient coverage.
- No concurrency, network or p99 benchmark.
