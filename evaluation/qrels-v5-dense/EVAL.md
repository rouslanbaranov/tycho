# Qrels v5-dense evaluation — 2026-10-30

Status: AI-adjudicated, dense pool. Not human review, CI, owner acceptance or
sufficient coverage.

## Dataset

- 150 queries, same IDs/questions/splits as v4.
- 30 candidates/query: 4,500 page and 4,500 section judgments.
- 997 accepted page / 996 accepted section; 259/256 direct.
- 213 new accepted pages and 212 new accepted sections over v4.1.
- All v4.1 labels preserved.

## Results

All queries:

| Mode | page hit@1/3/5 | section hit@1/3/5 |
|---|---|---|
| BM25 | **.713/.873/.967** | **.540/.780/.867** |
| margin .05 | .727/.867/.953 | .567/.780/.867 |
| best/adaptive hybrid | .653/.867/.953 | .493/.780/.867 |

BM25 by split (page):

| Split | n | hit@1/3/5 |
|---|---:|---|
| book | 90 | .744/.856/.956 |
| atlas | 30 | .433/.833/.967 |
| v12 | 30 | .900/.967/1.000 |

## Comparison

| Dataset | candidates | accepted | page top-1 |
|---|---:|---:|---:|
| v4 | 4.07 | 447 | .593 |
| v4.1 | 10.06 | 784 | .687 |
| v5-dense | 30.00 | 997 | .713 |

These are **not directly comparable**: accepted sets and pools differ. The rise
in top-1 partly follows from more accepted labels.

## Decision

- Default remains BM25; no section rerank.
- Margin stays opt-in at .05; it trades top-1 for top-3/5.
- Best/adaptive hybrid stays opt-in.
- v5-dense is a diagnostic dense benchmark, not proof of exhaustive recall.

## Limits

- 30 candidates from 498 pages and 3,075 sections; still pool-relative.
- New candidates are structural/random, not current rankings; 213/2,991 new page
  labels are accepted.
- AI-adjudicated by 30 empty-context subagents; no human review, CI, owner
  acceptance or sufficient coverage.
- No production-client benchmark.
