# Agent page/read budget — 2026-10-31

Status: measured index statistics and a bounded change. No book/atlas content
change.

## Measurement

3,075 indexed sections:

| Budget | Share of sections covered | Sections longer |
|---:|---:|---:|
| 2,000 | 89.2% | 332 |
| 2,500 | 94.5% | 168 |
| 3,000 | 96.3% | 113 |
| 6,000 | 99.3% | 21 |
| 8,000 | 99.6% | 13 |

Percentiles: p50 772, p90 2,063, p95 2,645, p99 4,991, max 25,424.

## Decision

- default soft budget: **2,500 codepoints** (was 2,000);
- maximum: **6,000 codepoints** (was 5,000);
- Mermaid blocks may exceed the soft budget to finish;
- page/read metadata reports requested budget, overrun and diagram completion.

## Rationale

2,500 covers about 94.5% of sections and reduces continuation calls without
returning most full pages. 6,000 covers 99.3% of sections while keeping a
single response bounded; pages still paginate by design.

## Limits

- The thresholds are index-derived, not a token-cost optimum.
- Long sections above 6,000 still require pagination.
- No human review or production benchmark.
