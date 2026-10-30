# Qrels v4.1 evaluation — 2026-10-30

Status: AI-adjudicated, pool-expanded qrels. Not human review, CI, owner
acceptance or sufficient coverage.

## Dataset

- 150 queries, same IDs/questions/splits as v4.
- 10–11 candidates/query (1,509 page and 1,509 section judgments).
- 784 accepted and 230 direct at each level.
- All v4 grades preserved; 15/15 batches PASS.

## Results

All queries (page / section):

| Mode | page hit@1/3/5 | section hit@1/3/5 |
|---|---|---|
| BM25 | **.687/.867/.967** | **.527/.760/.860** |
| margin .05 | .700/.853/.953 | .560/.760/.860 |
| best/semantic | .633/.860/.953 | .480/.760/.860 |

By split (BM25 page):

| Split | n | hit@1/3/5 |
|---|---:|---|
| book | 90 | .711/.856/.956 |
| atlas | 30 | .433/.833/.967 |
| v12 | 30 | .867/.933/1.000 |

## Comparison with v4

| v4 | page | section |
|---|---|---|
| BM25 | .593/.847/.953 | .480/.700/.793 |
| margin | .620/.833/.940 | .513/.700/.800 |

v4.1 values are **not directly comparable**: accepted pages grew from 447 to
784 and pool from 4.07 to 10.06. Higher top-1 can reflect more accepted labels,
not better ranking.

## Decision

- Default stays BM25, no section rerank.
- Margin remains opt-in at .05; it trades top-1 for top-3/5.
- Best/semantic remains opt-in.
- v4.1 is a diagnostic set; it does not replace v4 or prove production quality.

## Limits

- AI labels only; structural candidates; pool-relative.
- No human review, CI, owner acceptance or sufficient coverage.
- No production-client benchmark.
