# Artifact decision intent priority — 2026-10-30

Status: opt-in artifact lookup fix. 30 AI-adjudicated queries; not human review,
CI, owner acceptance or sufficient coverage.

## Bug

The type-intent heuristic checked `runs/results` before `decision`. A query
such as "Which decision links ... to their runs?" was classified as run and
returned runs before the decision artifact.

## Fix

`decision` now takes priority over run/result, then scenario input, then model.
Page/section defaults unchanged.

## Results

| Metric | Before | After |
|---|---|---|
| accepted top-1 | .800 | **.833** |
| accepted top-3 | .933 | **.967** |
| accepted top-5 | .933 | **.967** |
| direct top-1 | .800 | **.833** |
| direct top-3 | .933 | **.967** |
| direct top-5 | .933 | **.967** |

By type (accepted):

| Type | n | top-1 | top-3 | top-5 |
|---|---:|---:|---:|---:|
| model | 7 | 1.000 | 1.000 | 1.000 |
| decision | 7 | **1.000** | 1.000 | 1.000 |
| run | 8 | .875 | 1.000 | 1.000 |
| scenario | 8 | .500 | .875 | .875 |

## Limits

- AI qrels, 30 queries, 5 candidates.
- Scenario top-1 remains weak.
- No human review, CI, owner acceptance or sufficient coverage.
