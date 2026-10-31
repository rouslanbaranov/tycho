# Section top-5 hard-negative audit and v5.5 — 2026-10-31

Status: AI-adjudicated only. No default change. Not human review, CI, owner
acceptance or sufficient coverage.

## Coverage

- 750 section units: 150 top-1 plus 600 ranks 2-5 outside v5;
- two independent empty-context DeepSeek labelers;
- 95 A/B disagreements;
- 98 third-labeler units (two 48-unit runs plus two missing units);
- no Codex used.

Agreement over 750 units:

| Metric | Value |
|---|---:|
| exact | .8733 |
| both hard negative | 377 |
| both relevant | 310 |
| disagreements | 95 |

Third outcome: 24 direct, 57 supporting, 17 hard negative.

## v5.5 section

- section: 5,250 candidates, 1,352 accepted, 390 direct;
- page: unchanged v5;
- all v5 labels preserved.

Section metrics:

| Mode | P@5 | R@5 | MRR | NDCG@5 |
|---|---:|---:|---:|---:|
| 10/5/1 | **.6653** | .3816 | **.9372** | **.7080** |

Do not compare v5.5 section directly with v5. The pool and accepted set changed;
the gain is largely coverage, not ranking.

## Where this leaves page/section

- page top-5: v5.3, P@5 .6947, NDCG .7612;
- section top-5: v5.5, P@5 .6653, NDCG .7080;
- both are coverage-corrected diagnostics, not production sign-off.

## Limits

- AI labels only; two independent plus third.
- 95 disagreements resolved; no human adjudication.
- 98 third units for 95 final disagreements; extra units are retained in the
  adjudication files but do not affect v5.5.
- No CI, owner acceptance, sufficient coverage or production-client benchmark.
