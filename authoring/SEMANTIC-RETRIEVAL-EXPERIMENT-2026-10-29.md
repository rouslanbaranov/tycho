# Semantic retrieval experiment — 2026-10-29

Status: diagnostic experiment. No semantic default is enabled. Not a quality,
sufficiency, CI or production claim.

## Setup

- Static embeddings via model2vec: minishlab/potion-base-8M (256-dim) and
  potion-base-32M.
- H2 sections: 2,328; H3 passages: 504.
- BM25 baseline: current H3-aware section search, limit 5.
- Vector: cosine over H2 sections or H3 passages mapped to parent H2.
- Hybrid: RRF (k=60) of BM25 and vector parent sections.
- Diagnostics: hit@1/3/5 on qrels v2 answerable and filtered phase3.

## Results (hit@5)

| Retriever | All | qrels v2 | phase3 |
|---|---:|---:|---:|
| BM25 | 0.753 | 0.774 | 0.579 |
| H3 vector, 8M | 0.494 | 0.516 | 0.316 |
| H3 hybrid, 8M | 0.713 | 0.716 | 0.684 |
| H2 vector, 8M | 0.621 | 0.626 | 0.579 |
| H2 hybrid, 8M | 0.684 | 0.690 | 0.632 |
| H2 vector, 32M | 0.672 | 0.671 | 0.684 |

BM25 remains the strongest overall retriever. H2 embeddings beat H3 embeddings
but still trail BM25; RRF hybrid does not close the gap. The 32M model improves
over 8M but not enough to justify a default change.

## Decision

- Do not enable semantic retrieval by default.
- Keep [semantic_search.py](scripts/semantic_search.py) as an optional
  diagnostic CLI.
- Do not tune hybrid weights on phase3 or qrels v2.
- Do not claim that embeddings improve relevance; this experiment does not
  establish that.
- Next semantic experiment, if any: contextual transformer embeddings or a
  cross-encoder reranker, evaluated on an independent set after enrichment.

## Limits

- Static model2vec embeddings are not contextual transformers.
- Small 19-item phase3 answerable subset and author-labelled qrels v2.
- One host, one index snapshot, no latency or memory claim.
- No human review, CI, owner acceptance or sufficient coverage.
