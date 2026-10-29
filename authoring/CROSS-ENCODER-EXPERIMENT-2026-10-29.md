# Cross-encoder reranker experiment — 2026-10-29

Status: diagnostic only. No reranker is enabled by default.

## Setup

- Model: cross-encoder/ms-marco-MiniLM-L-6-v2.
- Candidate set: BM25 top-20, current H3-aware section search.
- Rerank input: query plus section heading and excerpt (1200 chars max).
- Queries: 155 qrels-v2 answerable plus 19 filtered phase3 answerable.
- Metric: hit@1/3/5 on parent H2 sections.

## Results (hit@5)

| Retriever | All | qrels v2 | phase3 |
|---|---:|---:|---:|
| BM25 top-5 | 0.753 | 0.774 | 0.579 |
| Cross-encoder rerank | 0.523 | 0.510 | 0.632 |

The reranker improves phase3 hit@5 but substantially degrades overall and v2.
It is not safe to enable or tune on this snapshot.

## Decision

- Do not integrate the cross-encoder into default search.
- Do not tune reranker weights or candidate depth on phase3.
- Keep the result as negative diagnostic evidence.

## Limits

- One small cross-encoder, one host, one snapshot.
- Candidate excerpts may omit surrounding context.
- Phase3 has only 19 answerable items; qrels v2 is author-labelled.
- No human review, CI, owner acceptance or sufficient coverage.
