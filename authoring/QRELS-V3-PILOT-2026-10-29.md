# Qrels v3 pilot — 2026-10-29

Status: one session-subagent AI pilot. Not human review, independent review,
CI, owner acceptance or sufficient coverage.

## Scope

- 3 queries: Q001, Q002, Q003.
- 17 candidate pages from the pooled v3 set.
- One independent reviewer subagent, read-only, at base HEAD 4e604b2f.
- All candidates graded; no prior label was treated as the answer.

## Grades

| Grade | Count |
|---|---:|
| 2 directly relevant | 11 |
| 1 partial | 4 |
| 0 not relevant | 2 |

Top-1 pilot results:

- Q001 top-1: grade 0 (invalid);
- Q002 top-1: grade 1 (partial);
- Q003 top-1: grade 2 (directly relevant).

So 2 of 3 strict top-1 misses were at least partially relevant and one was
directly relevant. This supports the qrels-incompleteness diagnosis but is a
three-query sample.

## Artifacts

- Pool: [corpus-qrels.v3.pool.json](../evaluation/corpus-qrels.v3.pool.json)
- Packet: [pilot-01.json](../evaluation/qrels-v3/pilot-01.json)
- Reviewed: [pilot-01.reviewed.json](../evaluation/qrels-v3/pilot-01.reviewed.json)

## Decision

- Do not merge this pilot as final qrels v3.
- Do not train or recalibrate on three queries.
- The review schema and packet flow work; proceed to the ten full packets with
  an independent reviewer.

## Limits

- Session subagent from the same vendor; not independent human review.
- Three queries selected from the beginning of the pool, not random.
- Page-level only.
- No owner acceptance, CI or sufficient coverage.
