# V12 versus book search quality gap — 2026-10-29

Status: diagnostic analysis. No quality, sufficiency, review or acceptance
claim.

## Question

Why does BM25 look much stronger on V12 qrels (hit@5 0.929) than on the general
book qrels (0.742), when both use the same section search?

## Same-ranker comparison

Generic BM25 section search on the current snapshot:

| Qrels | n | hit@1 | hit@3 | hit@5 | mean query terms | accepted/query | unique accepted pages |
|---|---:|---:|---:|---:|---:|---:|---:|
| book v2 | 155 | 0.355 | 0.600 | 0.742 | 15.9 | 1.4 | 129 |
| phase3 | 19 | 0.316 | 0.421 | 0.579 | 24.3 | 2.9 | 17 |
| V12 | 14 | 0.357 | 0.857 | 0.929 | 10.9 | 2.0 | 23 |

The V12 advantage is concentrated at hit@5. At hit@1 it is effectively the same
as book v2 (0.357 vs 0.355), and phase3 is lower. V12 does not demonstrate
better top-result precision.

## Why hit@5 is easier on V12

1. **Acceptance density.** V12 has 31 indexed pages and 23 unique accepted
   pages; 74% of the volume is relevant somewhere. Book v2 has 129 accepted
   pages in 423 (30%).
2. **Multiple accepted pages.** V12 has 2.0 accepted pages per query; book v2
   has 1.4. A top-5 page hit is easier even when the first result is wrong.
3. **Shorter, more lexical questions.** V12 questions average 10.9 terms,
   versus 15.9 for v2 and 24.3 for phase3.
4. **Higher lexical overlap.** V12 query/accepted-page overlap is 0.86, versus
   0.75 for v2 and 0.73 for phase3. The questions were written from V12
   contracts and use their vocabulary.
5. **Corpus scope.** V12 is a 31-page isolated volume; the general qrels compete
   across 423 pages with cross-cutting distractors.
6. **Qrels provenance.** V12 labels are author-labelled, derived from the volume
   contracts, and marked not independently reviewed. Fourteen answerable items
   produce a wide confidence interval; 0.929 is 13/14.

## What is not the explanation

No V12-specific ranker was used in this comparison. V12 artifact facets and
lookup are separate JSON helpers; the page ranking evaluated here is the same
generic BM25 path as the book. The dedicated V12 index does not by itself give
the qrels a better ranking.

## Implication

Do not compare raw hit@5 across qrels with different acceptance density, corpus
scope or query style. Report at least hit@1, MRR, accepted-page density, query
length and corpus size. The general book qrels are the harder and more relevant
test for the adaptive/hybrid route.

The next fair check is a V12-only-index run versus the full-index run on the same
V12 questions; that is not established here.

## Limits

- qrels are author-labelled; V12 says explicitly not independently reviewed.
- Book v2 route snapshot is stale.
- The V12 sample is 14 answerable questions.
- No human review, CI, owner acceptance or sufficient coverage.
