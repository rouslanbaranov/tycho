# Section hard-negative audit and v5.4 — 2026-10-31

Status: AI-adjudicated only. No default change. Not human review, CI, owner
acceptance or sufficient coverage.

## Coverage

- 150 queries, one section per query outside v5;
- two independent empty-context DeepSeek labelers;
- 25 A/B disagreements adjudicated by an independent third labeler;
- no Codex used.

Agreement over 150 section units:

| Metric | Value |
|---|---:|
| exact | .8333 |
| both hard negative | 48 |
| both relevant | 86 |
| disagreements | 25 |

Third-labeler outcome: 5 direct, 6 supporting, 14 hard negative.

## v5.4 section

- section: 4,650 candidates, 1,083 accepted, 304 direct;
- page: unchanged v5;
- all v5 labels preserved.

Section metrics:

| Mode | P@5 | R@5 | MRR | NDCG@5 |
|---|---:|---:|---:|---:|
| 10/5/1 | **.4053** | .2986 | **.9139** | **.5989** |

Do not compare v5.4 section directly with v5. The pool and accepted set changed;
the gain is largely coverage, not ranking.

## Cross-check with page coverage

The page top-5 audit v5.3 remains page-only. Its page-path hit is much higher
than exact section hit; this section audit is the necessary exact-section
counterpart. No page labels were copied into section labels.

## External aliases / atlas

- external alias expansion from edition/patterns/registry.v1.json expanded 4
  queries and is rejected (no page gain, section top-1 drops).
- explicit volume=atlas maps to v11 and is the atlas path; no global forcing.
- default BM25 10/5/1 unchanged.

## Limits

- One section per query; not a top-5 section audit.
- 25 disputes resolved by one AI third labeler.
- No human review, CI, owner acceptance, sufficient coverage or production-client
  benchmark.
