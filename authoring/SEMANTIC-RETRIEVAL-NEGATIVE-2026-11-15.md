# Semantic retrieval experiment — negative result, 2026-11-15

Status: implemented diagnostics; **not enabled** because they did not improve
BM25 on the held-out v5-dense qrels.

## Implemented

- 180-250 word chunks, 40-word (20%) overlap, sentence/paragraph boundaries;
- 3263 chunks over 2578 H2 sections, parent section retained;
- snapshot-bound chunk embedding index;
- section-level RRF BM25 + semantic fusion;
- cross-encoder reranker;
- evaluation on 150 v5-dense page/section qrels.

## Baseline BM25

| level | hit@1 | hit@3 | hit@5 | MRR |
|---|---:|---:|---:|---:|
| page | 0.720 | 0.900 | 0.973 | 0.822 |
| section | 0.567 | 0.820 | 0.893 | 0.704 |

## Tested variants

- semantic only (potion-8M, potion-32M, MiniLM, BGE-small): page hit@5 0.69-0.75,
  section hit@5 0.61-0.71; all below BM25;
- RRF hybrid at weights 0.01-1.0: page hit@1 0.58-0.72, section hit@1 0.46-0.57;
  no aggregate improvement;
- semantic-as-reranker inside BM25 top20: at weight 0.05 page hit@1 0.727
  vs 0.720, page MRR 0.824 vs 0.822, but section hit@1 0.560 vs 0.567 and
  section hit@5 0.880 vs 0.893 — within noise, no usable gain;
- MiniLM cross-encoder rerank: page hit@1 0.560 vs 0.720; worse;
- BGE cross-encoder: worse;
- logistic reranker trained on v2: page hit@1 0.580 vs 0.720; worse;
- semantic query expansion: page hit@1 0.507 vs 0.720; worse.

## Conclusion

BM25 is already very strong on this qrels; chunk semantic retrieval and these
rerankers add false positives and do not improve held-out page or section
metrics. The correct action is **not to enable** semantic or rerank by default.
A future attempt needs a stronger domain-tuned embedding/reranker, or a query
set with more conceptual/lexical mismatch; the current result is negative, not
a quality claim.

## Files

- scripts/semantic_chunks.py
- scripts/semantic_chunk_index.py
- scripts/hybrid_rerank.py
- scripts/evaluate_semantic_v6.py
- tests/test_semantic_chunks.py

No book/atlas content changed.
