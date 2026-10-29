# V12-gated top-1 reranker — 2026-10-29

Status: optional diagnostic. BM25 remains the default.

## Model

- Pointwise logistic model trained on the v2 dev split.
- Frozen artifact: evaluation/top1-reranker.v1.json.
- Features: BM25 score, rank, heading coverage, body coverage, H3 match,
  generic-section indicator, query length.
- Applied only when:
  - no top-5 result belongs to V12;
  - the query has at most 16 unique terms.

V12 is deliberately excluded because the generic reranker reduced V12 hit@3
from 0.857 to 0.714.

## Results

| Variant | all hit@1 | all hit@3 | all hit@5 | v2 hit@1 | p3 hit@1 | V12 hit@1 | V12 hit@3 |
|---|---:|---:|---:|---:|---:|---:|---:|
| BM25 | 0.351 | 0.601 | 0.739 | 0.355 | 0.316 | 0.357 | 0.857 |
| Gated reranker | **0.404** | **0.628** | 0.739 | **0.419** | 0.316 | 0.357 | 0.857 |

V12 hit@1/3/5 are preserved at 0.357/0.857/0.929. Phase3 hit@1 is preserved.
The gain is concentrated in the page-level book qrels.

## Use

```sh
python3 scripts/top1_rerank.py train
python3 scripts/top1_rerank.py evaluate
```

The artifact is frozen; do not retrain on phase3 or V12.

## Limits

- Trained on author-labelled v2 dev; no independent review.
- Book v2 route snapshot is stale.
- The model is diagnostic; no production default or quality claim.
- No human review, CI, owner acceptance or sufficient coverage.
