# Artifact type-intent prior — 2026-10-30

Status: opt-in artifact lookup improvement. 30 AI-adjudicated queries; not human
review, CI, owner acceptance or sufficient coverage.

## Change

Query terms select an intended artifact type:

- run/result -> run;
- input/configuration -> scenario;
- decision -> decision;
- model -> model.

Type-matched artifacts sort first, preserving the remaining relevance order.
Page/section search and defaults are unchanged.

## Results

| Metric | No prior | Type prior |
|---|---|---|
| accepted top-1 | .633 | **.733** |
| accepted top-3 | .900 | **.933** |
| accepted top-5 | .967 | .933 |
| direct top-1 | .500 | **.733** |
| direct top-3 | .767 | **.900** |
| direct top-5 | .933 | .933 |

By type (accepted):

| Type | n | top-1 before | top-1 after |
|---|---:|---:|---:|
| model | 7 | 1.000 | 1.000 |
| decision | 7 | 1.000 | .857 |
| run | 8 | .375 | **.625** |
| scenario | 8 | .250 | **.500** |

## Interpretation

- Type intent fixes much of the scenario/run top-1 confusion.
- Top-5 accepted loses one query; direct top-5 is unchanged.
- Decision top-1 loses one query; model unchanged.
- The set is small; no default change and no broad claim.

## Limits

- AI qrels, 30 queries, 5 candidates.
- Heuristic intent; no human review, CI, owner acceptance or sufficient coverage.
