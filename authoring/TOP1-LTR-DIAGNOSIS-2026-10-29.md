# Top-1 LTR diagnosis — 2026-10-29

Status: diagnostic. No reranker is enabled by default.

## Experiment

Pointwise logistic reranker over BM25 top-5 with features:

- BM25 score and candidate rank;
- heading coverage and body coverage;
- H3-passage match;
- generic-section indicator;
- query length.

Trained on the v2 dev split; evaluated on v2 heldout, phase3 and V12.

## Results

| Variant | all hit@1 | v2 hit@1 | p3 hit@1 | V12 hit@1 | all hit@3 | V12 hit@3 |
|---|---:|---:|---:|---:|---:|---:|
| BM25 | 0.351 | 0.355 | 0.316 | 0.357 | 0.601 | 0.857 |
| LTR, all lengths | 0.399 | 0.432 | 0.158 | 0.357 | 0.644 | 0.714 |
| LTR, <=16 terms | **0.410** | 0.426 | 0.316 | 0.357 | 0.617 | 0.714 |
| LTR, <=18 terms | **0.410** | 0.426 | 0.316 | 0.357 | 0.622 | 0.714 |

The length gate preserves phase3 top-1 but V12 hit@3 falls from 0.857 to
0.714. V12 hit@5 remains 0.929.

## Decision

- Do not enable LTR by default.
- Do not claim production top-1 quality: 0.410 is better but still low.
- A production version needs a V12-volume gate, frozen coefficients and fresh
  qrels adjudication; training on the current qrels would overfit.

## Limits

- One small model, one host, stale book qrels.
- V12 sample is 14 answerable questions; phase3 is 19.
- No human review, CI, owner acceptance or sufficient coverage.
