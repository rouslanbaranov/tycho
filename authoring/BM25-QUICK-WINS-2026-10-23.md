# BM25 quick wins — 2026-10-23

Status: measured on the bootstrap author-labelled qrels; not an independent review,
not a sufficiency claim and not a benchmark.

## Change

The section FTS5 search now weights fields as `title=5, heading=2, body=0.25`
instead of `title=4, heading=3, body=1`. The old body weight let long sections
outrank precise headings. The ranker version is `tycho-section-fts5-bm25-v4`.

The weights can be overridden for experiments with `TYCHO_BM25_WEIGHTS`
(three positive comma-separated numbers). Query semantics, tokenization, filters,
snapshot checks and the one-result-per-document rule are unchanged.

## Results

Corpus: 100 author-labelled items, 95 answerable, 5 unanswerable; limit 10.

| Metric | 4/3/1 baseline | 5/2/0.25 selected |
|---|---:|---:|
| nDCG@10 | 0.5597 | **0.6261** |
| Page hit@1 | 0.3789 | **0.4526** |
| Page hit@3 | 0.6526 | **0.7053** |
| Page hit@5 | 0.7579 | **0.8947** |
| Page MRR | 0.5416 | **0.6174** |
| Section hit@5 | 0.7158 | **0.8526** |
| Section MRR | 0.4980 | **0.5832** |

Split check:

| Split | Baseline page@5 | Selected page@5 |
|---|---:|---:|
| dev (50) | 0.7400 | **0.8600** |
| held-out (50) | 0.7778 | **0.9333** |

The held-out nDCG@10 moved from 0.5576 to 0.6408. The five unanswerable items
still return results; abstention was not changed by this work.

## Limits

- Labels are bootstrap author-labelled, not independently adjudicated.
- One corpus and one snapshot; no confidence interval is claimed.
- The gain is a weighting change, not semantic retrieval.
- Search remains a discovery/citation tool, not an answer engine.
- `sufficient` remains 0; no human review, owner acceptance or CI is claimed.

## Reproduction

```sh
python3 scripts/section_fts_index.py build --full
python3 scripts/evaluate_corpus_qrels.py --split all
```
