# Phase3 section-aware reranking pilot — 2026-10-29

Status: diagnostic pilot on 19 phase3 queries. Not human review, independent
review, CI or owner acceptance. Not integrated into production search.

## Method

For each query:

1. Take BM25 top-5 pages.
2. Fetch every matching H2 section on those pages from the snapshot DB.
3. Rank sections by query-term coverage in heading+content, heading hits, then
   BM25 score.
4. Take the top five sections.

## Result

| Metric | BM25 | section rerank |
|---|---:|---:|
| section hit@1 | .263 | **.316** |
| section hit@3 | .368 | **.526** |
| section hit@5 | .526 | **.684** |

The oracle check found the accepted section somewhere in the top-5 pages for
15/19 queries (.789), so section selection, not page recall, is the bounded
target.

## Interpretation

This is a real diagnostic signal: section-aware ranking can improve section
hit@3/@5 by 15.8 points and top-1 by 5.3 points on this sample. It is not
production evidence:

- only 19 queries;
- one feature set chosen after inspecting the same sample;
- top-1 improves from 5 to 6 queries, not statistically stable;
- no held-out section qrels.

Do not enable by default. The next step is a held-out section set or an
independent adjudication packet before any integration.

## Limits

- Phase3 labels are agent-adjudicated, not human.
- Page-level qrels v3 cannot validate section precision.
- No human review, CI, owner acceptance or sufficient coverage.
