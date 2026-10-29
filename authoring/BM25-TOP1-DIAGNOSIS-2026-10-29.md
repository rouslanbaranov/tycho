# BM25 top-1 diagnosis — 2026-10-29

Status: diagnostic. No default ranking change and no quality claim.

## Top-1 is the weak point

| Qrels | n | hit@1 | exact rank 2–5 | page-only top-1 | no page in top-5 |
|---|---:|---:|---:|---:|---:|
| book v2 | 155 | 0.355 | 60 | 4 | 33 |
| phase3 | 19 | 0.316 | 5 | 2 | 5 |
| V12 | 14 | 0.357 | 8 | 0 | 1 |

V12 and book v2 have effectively identical top-1. The V12 hit@5 advantage is
acceptance density and short lexical questions, documented separately.

## H3 top-1 boost

Boosting H3-passage candidates by a constant score improved page-level book
top-1 but regressed phase3 section-level top-1:

| Variant | all hit@1 | v2 hit@1 | p3 hit@1 | V12 hit@1 | all hit@5 |
|---|---:|---:|---:|---:|---:|
| baseline | 0.351 | 0.355 | 0.316 | 0.357 | 0.742 |
| H3 +2, query <=18 | 0.378 | 0.400 | 0.211 | 0.357 | 0.739 |
| H3 +2, all lengths | 0.383 | 0.406 | 0.211 | 0.357 | 0.739 |

Adding a margin gate did not recover phase3; the regression is caused by H3
parent selection switching away from the accepted H2 section.

## Decision

- Do not enable H3 top-1 boost by default.
- Do not claim production top-1 quality: 35% strict hit@1 is insufficient for
  citation-style answers.
- The next valid step is top-1 relevance adjudication: determine whether the
  current top-1 is a valid answer that is simply absent from the accepted set.

## Limits

- qrels are author/agent labelled, not independently reviewed.
- phase3 has 19 answerable items; V12 has 14.
- Book v2 route snapshot is stale.
- No human review, CI, owner acceptance or sufficient coverage.
