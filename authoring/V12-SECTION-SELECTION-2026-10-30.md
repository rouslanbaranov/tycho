# V12 section selection experiment — 2026-10-30

Status: opt-in experiment only; production V12 guard unchanged. AI qrels
pool-relative; not human review, CI, owner acceptance or sufficient coverage.

## Method

For V12 queries, take the top pages from normal BM25, then rescore all sections
on those pages with the section-rerank term-hit score. Page order is unchanged;
only the displayed section changes.

## Results

| Dataset | n | Base section hit@1/3/5 | Reranked |
|---|---:|---|---|
| qrels v4 | 30 | .567/.733/.800 | **.600/.800/.867** |
| qrels v3 | 14 | .786/.857/.857 | .714/.929/1.000 |

## Interpretation

- v4: top-1 +3.3 points, top-3/top-5 +6.7.
- v3: top-1 -7.1, top-3 +7.1, top-5 +14.3; n=14, so unstable.
- The change does not justify enabling V12 section rerank by default.
- It is a candidate opt-in, not a production default.

## Decision

Keep the V12 guard. Do not change default or page order from this experiment.
If revisited, require more V12 section labels and a paired test focused on top-1.

## Limits

- AI labels; qrels V12 uses book pages, not artifact records.
- Candidate pools 4–10; no human review/CI/owner acceptance/sufficient coverage.
