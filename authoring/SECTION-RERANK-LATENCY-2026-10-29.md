# Section rerank latency — 2026-10-29

Status: local benchmark, not production capacity evidence. No human review,
independent review, CI or owner acceptance.

## Setup

- 54 answerable phase2 queries.
- 3 repeats per mode; 162 measurements per mode.
- Query cache cleared before each call; index snapshot opened per call.
- Warm process; no cold model load.

## Result

| Mode | n | p50 | p95 | p99 | mean |
|---|---:|---:|---:|---:|---:|
| default BM25 | 162 | 98.0 ms | 99.5 ms | 101.1 ms | 101.8 ms |
| section_rerank | 156 | 103.2 ms | 105.0 ms | 105.5 ms | 102.9 ms |

Delta: p50 **+5.2 ms**, p95 **+5.5 ms**, p99 **+4.4 ms**, mean **+1.1 ms**.

Two phase2 queries were skipped for section_rerank because the V12 guard
rejected them; their six measurements are absent from the rerank sample.

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
