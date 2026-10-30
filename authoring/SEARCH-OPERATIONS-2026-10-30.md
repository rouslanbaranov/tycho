# Search operations runbook — 2026-10-30

Status: local operational guidance; not production monitoring, CI, human review,
owner acceptance or sufficient coverage.

## Defaults

- BM25 field weights: title 5, heading 2, body 0.5.
- MCP section_rerank=false.
- Opt-in margin: 0.05.
- Best/semantic mode: opt-in only.
- V12/all_sections/best fallbacks remain in core.

## Layer routing

Use volume for layer-specific queries:

| Layer | Request |
|---|---|
| Atlas | volume=v11 |
| V12 | volume=v12 |
| Global | omit volume |

Atlas v11 reached 1.000/1.000/1.000 on qrels v4; global atlas top-1 is a
cross-layer routing problem.

## Deployment

- Start with 4 MCP server processes for concurrent clients; each is a separate
  read-only process.
- Keep the in-process semaphore at 2.
- Bound process count by memory: each process opens the index and caches
  validation/query data.
- Do not increase threads beyond the semaphore; 16 threads degraded throughput.

## Healthcheck

    python3 scripts/search_healthcheck.py

It checks index/qrels snapshot, 150 queries, BM25 weights and MCP defaults.

## Troubleshooting

- Stale index/qrels: rebuild the index or refresh qrels; healthcheck fails on
  snapshot mismatch.
- Missing artifacts: artifact payload is opt-in; use include_artifacts=true and
  a query with matching metadata.
- Slow first query: expected index validation; later queries use the
  validated-manifest cache.
- Best mode slow: model load/rerank is opt-in; do not use for the default path.

## Known limits

- Artifact-level qrels labels do not exist.
- Qrels v4 pools are 4–10, not exhaustive.
- V12 section top-1 is 17/30; guard retained.
- No production-client benchmark or external validation.
- AI qrels; no human review, CI, owner acceptance or sufficient coverage.
