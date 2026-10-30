# V12 section diagnostics — qrels v4

Status: diagnostic on AI qrels v4; no production change. Pool-relative; not human
review, CI, owner acceptance or sufficient coverage.

## Counts

Layer-scoped V12 (`volume=v12`), BM25 body 0.5, n=30:

- page top-1: 23/30 (.767);
- section top-1: 17/30 (.567);
- page/section/gap.

Section first-accepted rank:

| Rank | Queries |
|---:|---:|
| 1 | 17 |
| 2 | 4 |
| 3 | 1 |
| 4 | 1 |
| 5 | 1 |
| not in top-10 | 6 |

Page first-accepted rank: 1 (23), 2 (4), 3 (1), 4 (2).

Six queries have the correct page at top-1 but the wrong section. Six more have
the accepted section outside the top-10, usually because the section was on a
page ranked 4.

## Interpretation

The V12 page retriever is stronger than the section selector. The section
failure is not a page-routing problem. V12 section rerank is currently disabled
by guard; enabling it requires a separate safe experiment, not a default change.

## Next

- Test section rerank/selection for V12 only as an explicit opt-in experiment.
- Do not change the V12 guard from this diagnostic alone.
- Keep the BM25 default.

## Limits

- AI labels; candidate pools 4–10; qrels V12 uses book pages, not artifacts.
- No human review, CI, owner acceptance or sufficient coverage.
