# Search performance baseline — 2026-10-27

Status: operational sample only. Not a quality, sufficiency, CI or capacity
claim.

## Method

- Snapshot: b65285cb3ff648c32f94c5fa2d240127eda7b2fb0f5aac620bc11db35ca01873
- Index: 16,363,520 bytes; 2,751 H2 sections; 504 H3 passages.
- 20 answerable qrels-v2 questions, one warm-up, one measured repeat.
- Local machine; no concurrent workload; no network.

## Results

| Metric | ms |
|---|---:|
| mean | 1708.3 |
| p50 | 1703.6 |
| p95 | 1884.0 |
| p99 | 2157.3 |
| max | 2157.3 |

This is a **small sample**, not a statistical benchmark. The dominant cost is
the per-query canonical route scan in the current search API, not a claim about
BM25 or H3 quality.

## Implication

Before any post-enrichment quality work, measure with a larger sample and remove
or cache the repeated snapshot scan. Do not present this baseline as capacity
planning or a latency SLA.

## Limits

- 20 questions, one repeat.
- No cold-start, concurrent-user or memory measurement.
- No relevance or sufficient-coverage claim.
