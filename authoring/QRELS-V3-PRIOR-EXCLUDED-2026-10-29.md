# Prior-excluded qrels v3 evaluation — 2026-10-29

Status: diagnostic on AI-adjudicated qrels v3. Not human review, independent
review, CI or owner acceptance.

## Question

Does best mode improve discovery of **new** accepted pages, or only retrieve
pages that were already accepted in the prior qrels?

## Method

- Start from qrels v3 accepted pages (grade >= 1).
- Remove pages listed in the query's prior_paths.
- Evaluate BM25 and best top-1/3/5 against the remaining pages.
- Queries with no remaining new page are skipped.

## Result

| Split | n | BM25 hit@1/3/5 | best hit@1/3/5 |
|---|---:|---|---|
| v2 | 154 | .487/.896/.968 | .494/.916/.981 |
| phase3 | 18 | .500/1.000/1.000 | .556/1.000/1.000 |
| V12 | 14 | .643/1.000/1.000 | .643/1.000/1.000 |
| **all** | **186** | **.500/.914/.973** | **.511/.930/.984** |

Two queries had no new accepted page and were skipped.

## Interpretation

On prior-accepted targets, best top-1 was .920 versus BM25 .878 (+4.2 points).
After removing prior-accepted pages, the gap falls to **.511 versus .500**
(+1.1 points), with top-3 +1.6 and top-5 +1.1.

Most of the apparent best-mode advantage is retrieval of pages already accepted
in the old qrels. New-page discovery is nearly at parity. This is consistent
with the non-significant McNemar result and does not justify a default change.

## Limits

- AI-adjudicated labels.
- Page-level; pool is BM25/best top-10, not exhaustive.
- Prior paths are stale author/agent labels and may include valid pages without
  being exhaustive.
- No human review, CI, owner acceptance or sufficient coverage.
