# AI section qrels v3 — 2026-10-29

Status: AI-adjudicated section-level pool. Not human review, independent review,
CI or owner acceptance.

## Artifact

- 188 queries: 155 v2, 19 phase3, 14 V12.
- 1,397 candidate sections from default and section_rerank top-5.
- Grades: 446 zero, 545 partial, 406 direct.
- Accepted (>=1): 951 section judgments; direct: 406.
- Snapshot: e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa
- File: [section-qrels.v3.json](../evaluation/section-qrels.v3.json)

## Metrics

| Split | n | BM25 section hit@1/3/5 | section_rerank hit@1/3/5 |
|---|---:|---|---|
| v2 | 155 | .813/.948/.987 | **.910/.955/.974** |
| phase3 | 19 | .737/.895/.895 | **.842/.895/.947** |
| V12 | 14 | .786/.929/1.000 | .786/1.000/1.000 |
| **all** | **188** | **.803/.941/.979** | **.894/.952/.973** |

Section rerank raises top-1 by 9.0 points and top-3 by 1.1, but loses 0.6 at
top-5. The top-5 loss is a real trade-off, not noise in the aggregate.

## Uncertainty

- Paired difference: +.0904.
- 95% bootstrap CI: **[.0319, .1489]**.
- Rerank-only correct: 24; BM25-only: 7.
- Exact McNemar p: **.0033**.

This is statistically significant on the AI-adjudicated pool.

## Why it is still not a default switch

- Labels are AI, not human or independent review.
- The candidate pool was built from both default and rerank outputs; it is not
  an unbiased independent sample.
- Accepted sets are broad (951 section judgments).
- Top-5 is slightly worse.
- No separate held-out section adjudication.

Keep section_rerank optional; do not change the default on this evidence alone.

## Limits

- AI labels, same session family.
- Pool is not exhaustive beyond default/rerank top-5.
- No human review, CI, owner acceptance or sufficient coverage.
