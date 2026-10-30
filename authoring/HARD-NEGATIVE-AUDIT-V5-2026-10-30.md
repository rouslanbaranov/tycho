# Hard-negative and metric audit on v5 — 2026-10-30

Status: AI-adjudicated only. No default change; not human review, CI, owner
acceptance or sufficient coverage.

## Precision/NDCG baseline

v5, BM25 10/5/1, top-5:

| Level | P@5 | R@5 | MRR | NDCG@5 |
|---|---:|---:|---:|---:|
| page | .4267 | .3396 | .8232 | .6045 |
| section | .2893 | .2367 | .7027 | .4701 |

## Hard-negative audit

- sample: 30/150 queries, stratified 18 book / 6 atlas / 6 v12;
- top-5 search results outside the v5 pool;
- 76 page + 111 section units;
- two independent empty-context DeepSeek labelers per batch.

Agreement over 187 units:

- exact: **.8503**
- Cohen's kappa: **.7613**
- quadratic weighted kappa: **.9994**

Consensus:

- both hard negative: **85**
- both relevant: **86**
- disagreement: **16**

The 86 both-relevant units were outside the v5 labels. Current v5 P@5 and
NDCG@5 are therefore **lower bounds**: the pool misses relevant top results.
This is an evaluation-coverage problem, not a ranking improvement.

## Atlas ranking

Atlas split, BM25 10/5/1:

| Mode | P@5 | R@5 | NDCG@5 |
|---|---:|---:|---:|
| global | .220 | .276 | .482 |
| explicit volume=v11 | **.487** | **.593** | **.818** |

Explicit layer scoping gives a large atlas gain; automatic routing is still not
validated. No default routing change.

## Decision

- Keep default BM25 10/5/1.
- Do not merge the hard-negative sample into v5; it is a coverage audit.
- Do not claim the 86 relevant units as search gains.
- Explicit atlas layer selection remains available; auto-routing remains rejected.

## Limits

- Hard-negative sample is 30/150, not full.
- Candidate selection used current top-5; it is pool-aware.
- 16 disagreements unresolved; no third adjudicator.
- AI labelers only; no human review, CI, owner acceptance or sufficient coverage.
- No production-client benchmark.
