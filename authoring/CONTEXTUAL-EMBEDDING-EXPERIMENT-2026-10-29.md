# Contextual embedding experiment — 2026-10-29

Status: diagnostic only. No semantic default is enabled.

## Setup

- Model: sentence-transformers/all-MiniLM-L6-v2 (384-dimensional).
- H2 sections: 2,328; batch size 64; embeddings normalized.
- Query set: 155 qrels-v2 answerable plus 19 filtered phase3 answerable.
- BM25 baseline: current H3-aware section search, limit 5.
- Vector: cosine nearest H2 section.
- Hybrid: RRF (k=60) of BM25 and vector parent sections.

## Results (hit@5)

| Retriever | All | qrels v2 | phase3 |
|---|---:|---:|---:|
| BM25 | 0.753 | 0.774 | 0.579 |
| Contextual H2 vector | 0.655 | 0.652 | 0.684 |
| Contextual H2 hybrid | 0.649 | 0.645 | 0.684 |
| Static H2 vector (8M) | 0.621 | 0.626 | 0.579 |

Contextual embeddings improve over static embeddings overall and on phase3,
but remain below BM25 overall. RRF hybrid does not improve the contextual
vector result.

## Decision

- Keep BM25 as the default.
- Add optional sentence-transformers backend to semantic_search.py; no default
  integration.
- Do not tune fusion weights on phase3.
- Do not claim embedding quality, sufficient coverage or production readiness.

## Limits

- One small model, one host, one snapshot.
- Phase3 has only 19 answerable items.
- qrels v2 is author-labelled and its route snapshot is stale.
- No human review, CI, owner acceptance or sufficient coverage.
