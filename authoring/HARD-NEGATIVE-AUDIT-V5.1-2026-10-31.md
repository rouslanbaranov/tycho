# Full hard-negative audit and qrels v5.1 — 2026-10-31

Status: AI-adjudicated only. No default change. Not human review, CI, owner
acceptance or sufficient coverage.

## Full audit

- all 150 queries;
- one section hard-negative unit per query outside v5;
- 30 labels: two independent empty-context DeepSeek labelers per batch;
- 17 disagreements resolved by a third independent empty-context labeler;
- no Codex used.

Agreement over 150 units:

| Metric | Value |
|---|---:|
| exact | .8867 |
| Cohen kappa | .8293 |
| quadratic weighted kappa | .9994 |

Consensus before third labeler:

- both hard negative: 54
- both relevant: 79
- disagreements: 17

Third labeler on the 17 disputes: 3 hard negative, 10 supporting, 4 direct.
Final: 57 hard negatives, 93 relevant units outside v5.

## v5.1

v5.1 adds the 150 audited section units to v5. Page qrels are unchanged; no
page-level hard-negative units were audited.

- page: 4,500 candidates, 997 accepted, 259 direct (unchanged);
- section: 4,650 candidates, 1,089 accepted, 300 direct;
- all v5 labels preserved; validator PASS.

v5.1 section P/NDCG:

| Mode | P@5 | R@5 | MRR | NDCG@5 |
|---|---:|---:|---:|---:|
| 10/5/1 | .4133 | .3014 | .9139 | .5980 |
| 5/2/.5 | .3907 | .2873 | .8693 | .5645 |
| 3/2/1 | .4107 | .3011 | .9189 | .5946 |

Page remains:

- P@5 .4267; R@5 .3396; MRR .8232; NDCG@5 .6045.

**Do not compare v5.1 directly with v5.** The section pool and accepted set
changed; the gain is largely coverage, not ranking.

## Query expansion

Bounded PRF expansion (two title terms from top-3):

- page .700/.933/.967 vs base .727/.913/.973;
- section .540/.827/.880 vs base .573/.827/.893.

PRF is rejected; top-1 drops.

## Atlas card-level / layer

Atlas split, 10/5/1:

| Mode | P@5 | R@5 | NDCG@5 |
|---|---:|---:|---:|
| global | .220 | .276 | .482 |
| explicit volume=v11 | .487 | .593 | .818 |

Decision:

- **Do not make volume=v11 mandatory for all queries.** It would remove book
  and V12 candidates from non-atlas queries.
- **Use volume=v11 as the explicit atlas path.** When the caller selects the
  atlas layer, scope to v11 rather than global.
- Automatic atlas routing remains rejected: the earlier metadata router and
  score-ratio router both failed.

## Decision

- Default remains BM25 10/5/1.
- No production default change from v5.1.
- v5.1 is a coverage-corrected diagnostic set.
- Explicit atlas layer is the atlas path; no global forcing.

## Limits

- Only one section unit per query was audited; top-5/page hard negatives remain
  outside this audit.
- 17 disagreements resolved by a single third AI labeler.
- No human review, CI, owner acceptance, sufficient coverage or production
  client benchmark.
- All labels are AI-adjudicated.
