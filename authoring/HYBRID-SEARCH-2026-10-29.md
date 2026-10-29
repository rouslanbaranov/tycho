# BM25 production baseline and hybrid search — 2026-10-29

Status: diagnostic. BM25 remains the default; hybrid is optional. No quality,
sufficiency, CI or owner-acceptance claim.

## BM25 production contract

- Field weights: title=5, heading=2, body=0.25; H3 passage weight=1.0.
- Porter unicode61 index; one best section per document; H3 passages map to
  parent H2.
- Snapshot validation, query cache, atomic rebuild and deep verify are in place.
- Weight grids (5,3,1; 8,4,1; 4,3,1; 6,3,0.5; 10,5,1; 2,2,1), adaptive
  weights, stopword variants, coverage filters and page aggregation did not
  improve hit@5 on the frozen qrels. The baseline weights remain.

## Hybrid

Page-level RRF combines BM25 top-20 with H2 semantic top-20:

- BM25 rank weight 1.0;
- semantic rank weight 0.1;
- page score = 1/(60+bm25_rank) + 0.1/(60+semantic_rank);
- BM25 section wins when the page exists; semantic supplies missing pages.
- Linear score fusion was also tested but measured 0.741 hit@5 in the actual
  evaluator; it is not the selected mode.

Embeddings: model2vec potion-base-8M, 256-dimensional, H2 heading + content,
snapshot-bound. Rebuild with:

```sh
python3 scripts/hybrid_search.py build
python3 scripts/hybrid_search.py evaluate --weight 0.1
```

## Current results

| Retriever | hit@1 | hit@3 | hit@5 |
|---|---:|---:|---:|
| BM25 | 0.351 | 0.580 | 0.724 |
| Hybrid | 0.391 | 0.644 | **0.753** |

By split:

| Split | BM25 hit@5 | Hybrid hit@5 |
|---|---:|---:|
| qrels v2 | 0.742 | 0.768 |
| phase3 | 0.579 | 0.632 |

The earlier dev/held run selected weight 0.1 with v2 held hit@5 0.808, but that
was on a different content snapshot; do not transfer the number as a current
metric.

## Decision

- Keep BM25 as the production default.
- Hybrid is opt-in, requiring a built semantic index and model2vec/numpy.
- Do not claim the hybrid gain is stable until qrels are re-adjudicated after
  enrichment.

## Limits

- qrels v2 route snapshot is stale; labels are author-labelled.
- phase3 has 19 answerable questions.
- One model, one host, one content snapshot.
- No human review, CI, owner acceptance or sufficient coverage.
