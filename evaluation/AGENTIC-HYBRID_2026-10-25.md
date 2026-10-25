# Hybrid reranker probe - 2026-10-25

> Issue [#413](https://github.com/rouslanbaranov/tycho/issues/413), E18-08.
> **Status:** bounded hashed-vector probe and decision; not a neural embedding
> benchmark and not an adoption. No file under `book/` was modified.

## Method

The probe uses one `tycho_search` call per answerable task with `limit=20`
and `abstain=false`. It builds deterministic 512-dimensional hashed
bag-of-words vectors from the question, title, heading and excerpt, then blends
the normalised BM25 score with cosine similarity:

`score = (1 - alpha) * bm25_norm + alpha * cosine`

It evaluates alpha 0, 0.25, 0.5, 0.75 and 1.0 on the frozen 32 answerable
tasks. This is a lexical hybrid probe, not a semantic model.

## Results

Snapshot `60b3f77f...`; 32 tasks; 20 candidates per task.

| alpha | Recall@10 | nDCG@10 | MRR | Top-1 |
|---:|---:|---:|---:|---:|
| 0.00 | 1.000 | 0.503445 | 0.571801 | 0.40625 |
| 0.25 | 1.000 | 0.530857 | 0.606858 | 0.46875 |
| 0.50 | 1.000 | 0.552145 | 0.647929 | 0.53125 |
| 0.75 | 1.000 | 0.518309 | 0.616517 | 0.50000 |
| 1.00 | 1.000 | 0.340548 | 0.345548 | 0.15625 |

Mean search latency was 1,079 ms per task. The alpha=0.5 blend improves nDCG
and top-1 relative to the same-candidate BM25 ordering. This is a real signal,
but it is not sufficient for adoption:

- the vectors are lexical hashes, not semantic embeddings;
- one 32-task author-labelled set is not a significance test;
- the probe is outside the default server and adds complexity;
- no production latency or remote Vercel measurement was made.

## Decision

**Defer adoption.** Keep BM25 as the default. A follow-up may test a real
public embedding model or cross-encoder only after an independent evaluation
set and a reproducible latency/cost budget. The default server, image and
tools are unchanged by this task.

## Limits

- 32 answerable tasks; no unanswerable behavior comparison.
- Hashed lexical vectors are not semantic embeddings.
- No independent review, human answer key, remote run or production claim.
- `human_review: not-performed; sufficient: 0`.
