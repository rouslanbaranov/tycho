# Full page top-5 hard-negative audit and v5.3 — 2026-10-31

Status: AI-adjudicated only. No default change. Not human review, CI, owner
acceptance or sufficient coverage.

## Coverage

- all 150 v5 queries considered;
- 675 page units across ranks 1-5 outside v5 (147 top-1 + 528 ranks 2-5);
- 30 labels: two independent empty-context DeepSeek labelers;
- 113 A/B disagreements adjudicated by independent third labelers;
- no Codex used.

Agreement over 675 page units:

| Metric | Value |
|---|---:|
| exact | .8326 |
| Cohen kappa | .6965 |
| both hard negative | 371 |
| exact positive agreement | 191 |
| disagreements | 113 |

Third-labeler outcome: 92 relevant, 21 hard negative. Final audit: 283 relevant
page units and 392 hard negatives.

## v5.3 page

v5.3 page adds all 675 audited pages to v5. Section qrels are unchanged.

- page: 5,175 candidates, 1,280 accepted, 380 direct;
- section: unchanged from v5;
- all v5 labels preserved.

Page metrics:

| Mode | P@5 | R@5 | MRR | NDCG@5 |
|---|---:|---:|---:|---:|
| 10/5/1 | **.6947** | .4292 | **.9589** | **.7612** |

Do not compare v5.3 page directly with v5. The page pool and accepted set
changed; the gain is largely coverage, not ranking.

## External alias expansion

Alias dictionary from edition/patterns/registry.v1.json, independent of qrels:

- expanded 4 / 150 queries;
- page .727/.913/.973 unchanged;
- section .560/.827/.893 vs base .573/.827/.893.

Rejected: no page gain and section top-1 drops.

## Atlas decision

Atlas split on v5, 10/5/1:

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
- No default change from v5.3 or alias expansion.
- v5.3 page is a coverage-corrected diagnostic set.
- v5.3 section is unchanged from v5.

## Limits

- Page candidates are one per rank slot; duplicates across queries are graded
  per query.
- 113 disputes resolved by two AI third labelers.
- No human review, CI, owner acceptance, sufficient coverage or production
  client benchmark.
- Labels remain AI-adjudicated only.
