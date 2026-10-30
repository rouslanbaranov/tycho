# MCP default latency — 2026-10-29

Status: historical benchmark of the former margin default; MCP now defaults to
BM25. Bounded local smoke, not production capacity evidence. No human review,
independent review, CI or sufficient coverage.

## Setup

- 20 qrels-v3 queries.
- 2 repeats.
- Query cache cleared before each call.
- Pure BM25 versus MCP default (`section_rerank_margin=0.15`).
- 2 V12-guarded samples skipped in the default arm.

## Result

| Mode | n | p50 | p95 | p99 | mean |
|---|---:|---:|---:|---:|---:|
| pure BM25 | 40 | 126.7 ms | 289.5 ms | 779.9 ms | 171.1 ms |
| MCP default | 38 | 164.7 ms | 180.1 ms | 190.0 ms | 160.8 ms |

The default adds ~38 ms at p50 in this sample. Its p95/p99 are lower because the
BM25 arm contains a large outlier; this is not evidence that the default is
faster at the tail.

## Limits

- 20 queries, 2 repeats.
- Single process, no concurrency/network.
- High variance.
- No production-client benchmark; owner waived one before the switch.
