# Section rerank latency — 2026-10-29

Status: local benchmark, not production capacity evidence. No human review,
independent review, CI or owner acceptance.

## Setup

- 54 answerable phase2 queries.
- 3 repeats per mode; 162 measurements per mode.
- Query cache cleared before each call; index snapshot opened per call.
- Warm process; no cold model load.

## Result

| Mode | p50 | p95 | mean |
|---|---:|---:|---:|
| default BM25 | 99.1 ms | 104.3 ms | 104.0 ms |
| section_rerank | 103.0 ms | 105.1 ms | 103.0 ms |

Delta: p50 **+3.9 ms**, p95 **+0.8 ms**, mean **-1.0 ms**.

The extra section query is inside the existing snapshot/index cost and is small
relative to the full search call in this setup. This does not establish
production latency under concurrency, larger corpora or network clients.

## Decision

- Keep section_rerank optional.
- No default change.
- Benchmark should be repeated with the production client and concurrent load.

## Limits

- Local single-process benchmark.
- Query cache cleared; repeated-query traffic would be cheaper.
- No p99, no concurrency, no cold start.
- AI/agent labels are irrelevant to latency but quality remains unverified.
