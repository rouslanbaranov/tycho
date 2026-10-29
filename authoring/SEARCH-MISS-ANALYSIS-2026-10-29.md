# BM25 retrieval misses — 2026-10-29

Status: diagnostic error analysis. No ranking change and no quality claim.

## Baseline drift

The earlier pre-enrichment baseline recorded hit@5 0.7529 and 43 misses. On the
current main snapshot the same 174 queries produce 127 hits / 47 misses
(hit@5 0.7299). B9 content landed after the baseline, so the qrels and baseline
are stale. This is a drift observation, not a regression claim.

## Method

- BM25 top-20, current H3-aware search.
- 155 qrels-v2 answerable plus 19 filtered phase3 answerable.
- Accepted sets as recorded in qrels; a page-level accepted item also matches
  any section on that page.
- Classification:
  - hit: accepted within top-5;
  - section-granularity: accepted page in top-5, accepted section is not;
  - exact-rank-6-20: accepted section/page in ranks 6-20;
  - page-rank-6-20: accepted page in ranks 6-20 but no exact section;
  - not-top-20: accepted page absent from top-20.

## Results

| Status | v2 | p3 | Total |
|---|---:|---:|---:|
| exact-rank-6-20 | 22 | 2 | 24 |
| section-granularity | 7 | 3 | 10 |
| page-rank-6-20 | 1 | 1 | 2 |
| not-top-20 | 9 | 2 | 11 |
| **Misses** | **39** | **8** | **47** |

36 of 47 misses have the accepted page in top-20; 11 do not.

## Reading

- 24 misses are a ranking-depth problem: the right section/page exists in
  top-20 but not top-5. A reranker or better fusion could address these.
- 10 misses are section selection: the right page is already top-5 but another
  section wins. H3 parent selection or a section-level reranker is the relevant
  lever, not document recall.
- 11 misses are candidate-generation failures: semantic/union retrieval could
  help only if it brings the accepted page into the candidate set.
- 2 misses are page ranking in 6-20 with no exact section, between those cases.

Cross-encoder reranking already regressed overall on the prior snapshot
(hit@5 0.523), so it is not a ready fix; it must be retried after labels and
content stabilize.

## Next experiments

1. Measure semantic recall@20 for the 11 not-top-20 misses before adding a
   vector stage.
2. For section-granularity misses, test H3 parent-aware section selection
   without changing citation units.
3. For exact-rank-6-20 misses, compare listwise reranking on longer section
   context rather than 1200-char excerpts.
4. Rebuild the baseline only after enrichment and qrels re-adjudication.

## Limits

- qrels are not exhaustive; a returned section outside accepted sets may still
  be relevant.
- qrels v2 is author-labelled; phase3 has only 19 answerable items.
- The current route snapshot is stale relative to qrels v2.
- No human review, CI, owner acceptance or sufficient coverage.
