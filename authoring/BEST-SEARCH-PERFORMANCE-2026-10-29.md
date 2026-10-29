# Cached best-search latency — 2026-10-29

Status: operational diagnostic. No quality, capacity or SLA claim.

## Method

- 20 answerable qrels-v2 questions.
- best_search composition with contextual embeddings.
- First request after explicit cache clear = cold.
- Next 19 requests in the same process = warm.
- Local machine, single process, no concurrency.

## Results

| Measurement | ms |
|---|---:|
| cold first request | 4743.4 |
| warm p50 | 111.6 |
| warm p95 | 132.3 |
| warm max | 132.3 |

The cold request pays model and embedding-index loading. Warm requests reuse
the process-local model and matrix caches. A long-lived MCP/HTTP process is the
intended deployment shape; a fresh CLI process pays cold cost again.

## Limits

- One host, one model, one snapshot.
- Mixed BM25/hybrid routes; no per-route breakdown.
- Not a capacity forecast or SLA.
- No human review, CI, owner acceptance or sufficient coverage.
