# Best optional search composition — 2026-10-29

Status: diagnostic. BM25 remains the default.

## Composition

1. BM25 top-20.
2. If the query is V12-specific or the top result is V12, return BM25 (V12 gate).
3. If the top BM25 result covers at least 60% of unique query terms, use BM25.
4. Otherwise use page-level RRF hybrid with contextual H2 embeddings.
5. Apply the frozen V12-gated top-1 logistic reranker when eligible.

## Results

| Query set | hit@1 | hit@3 | hit@5 |
|---|---:|---:|---:|
| all | 0.388 | 0.622 | **0.771** |
| book v2 | 0.400 | 0.619 | 0.774 |
| phase3 | 0.316 | 0.474 | 0.632 |
| V12 | 0.357 | 0.857 | 0.929 |

Comparison points:

| Retriever | all hit@5 | v2 hit@5 | phase3 hit@5 | V12 hit@5 |
|---|---:|---:|---:|---:|
| BM25 | 0.739 | 0.742 | 0.579 | 0.867 |
| Hybrid RRF | 0.764 | 0.774 | 0.632 | 0.867 |
| Best composition | **0.771** | 0.774 | 0.632 | 0.929 |

V12 hit@1/3/5 are preserved. Phase3 top-1 is preserved; top-3/top-5 improve.

## Use

```sh
python3 scripts/best_search.py search --query "..."
python3 scripts/best_search.py evaluate
```

## Limits

- Diagnostic composition; no production default.
- Frozen reranker trained on v2 dev; author-labelled, stale qrels.
- V12/phase3 samples are small.
- No human review, CI, owner acceptance or sufficient coverage.
