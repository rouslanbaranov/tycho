# Page hard-negative audit and v5.2 — 2026-10-31

Status: AI-adjudicated only. No default change. Not human review, CI, owner
acceptance or sufficient coverage.

## Page audit

- 147 of 150 queries have a page candidate outside v5; 3 have none;
- one page per query, not all five;
- 30 labels: two independent empty-context DeepSeek labelers;
- 24 page disputes were adjudicated by a third independent labeler;
- current A/B set has 13 disagreements; all are covered by the third labeler.

Agreement over 147 page units:

| Metric | Value |
|---|---:|
| exact | .8299 |
| Cohen kappa | .7352 |
| both hard negative | 60 |
| both relevant | 74 |
| disagreements | 13 |

## v5.2 page

v5.2 page adds the 147 audited pages to v5. Section qrels are unchanged.

- page: 4,647 candidates, 1,080 accepted, 309 direct;
- section: unchanged from v5;
- all v5 labels preserved.

Page P/NDCG:

| Mode | P@5 | R@5 | MRR | NDCG@5 |
|---|---:|---:|---:|---:|
| 10/5/1 | **.5333** | .3934 | **.9550** | **.7089** |

Do not compare v5.2 page directly with v5. The page pool and accepted set
changed; the gain is largely coverage, not ranking.

## Top-5 depth

This audit is top-1 page per query. The prior 30-query top-5 sample remains the
only top-5 depth audit; it is not extended here. Do not claim full top-5 page
coverage.

## Query expansion with external aliases

Alias dictionary from edition/patterns/registry.v1.json, independent of qrels:

- expanded 4 / 150 queries;
- page unchanged .727/.913/.973;
- section .560/.827/.893 vs base .573/.827/.893.

Rejected: no page gain and section top-1 drops.

## Atlas decision

Atlas split, 10/5/1:

| Mode | P@5 | R@5 | NDCG@5 |
|---|---:|---:|---:|
| global | .220 | .276 | .482 |
| explicit volume=v11 | **.487** | **.593** | **.818** |

Decision:

- do not make volume=v11 mandatory globally;
- use explicit volume=v11 for the atlas path;
- keep automatic routing rejected.

## Decision

- Default remains BM25 10/5/1.
- No default change from v5.2 or alias expansion.
- v5.2 page is a coverage-corrected diagnostic set.

## Limits

- 147 queries, one page each; not full top-5 page audit.
- 3 queries have no page candidate.
- 24 disputes were adjudicated; current disagreement set is 13, all covered.
- Third labeler is AI-only.
- No human review, CI, owner acceptance, sufficient coverage or production-client
  benchmark.
