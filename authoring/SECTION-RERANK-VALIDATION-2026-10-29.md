# Section rerank validation — 2026-10-29

Status: diagnostic validation on section-labelled qrels. Not human review,
independent review, CI or owner acceptance. Not integrated into production.

## Method

Fixed section-aware reranker:

1. BM25 top-5 pages.
2. Fetch every matching H2 section on those pages.
3. Rank by query-term coverage in heading+content, heading hits, then BM25.
4. Take the top five sections.

The feature was fixed before the held-out phase2 run.

## Result

| Split | n | BM25 section hit@1/3/5 | rerank hit@1/3/5 |
|---|---:|---|---|
| phase2 held-out | 54 | .130/.315/.352 | **.185/.370/.426** |
| phase3 pilot | 19 | .263/.368/.526 | **.316/.526/.684** |
| combined | 73 | .164/.329/.397 | **.219/.411/.493** |

Improvements:

- phase2: +5.5 / +5.5 / +7.4 points;
- phase3: +5.3 / +15.8 / +15.8 points;
- combined: +5.5 / +8.2 / +9.6 points.

## Interpretation

The held-out phase2 result confirms the direction: section-aware ranking
improves section retrieval beyond the phase3 pilot. It is still not production
evidence:

- labels are agent-adjudicated, not human;
- section top-1 is only 21.9% combined;
- n=73 is modest;
- the feature is simple and may not generalize to other volumes;
- no integration, no default change.

The next step is an optional implementation with regression tests and a
held-out review, not a default switch.

## Artifacts

- [section_rerank_eval.py](../scripts/section_rerank_eval.py)
- [section-rerank-validation.json](../evaluation/section-rerank-validation.json)

## Limits

- Agent-adjudicated labels; not human review.
- Section ids are exact; quotes may be H2 anchors.
- No CI, owner acceptance or sufficient coverage.
