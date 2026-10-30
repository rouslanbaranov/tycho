# V12 artifact detail enrichment — 2026-10-30

Status: product improvement for opt-in artifact lookup. AI qrels; not human
review, CI, owner acceptance or sufficient coverage.

## Change

Artifact ranking now includes read-only scalar field names/values from the
referenced V12 model/scenario/run/decision JSON, cached by path/mtime/size.
Private match text is stripped from the public payload.

## Before/after

| Metric | Before | After |
|---|---|---|
| accepted top-1 | .500 | **.633** |
| accepted top-3 | .600 | **.900** |
| accepted top-5 | .700 | **.967** |
| direct top-1 | .367 | **.500** |
| direct top-3 | .500 | **.767** |
| direct top-5 | .600 | **.933** |

By direct type (accepted, after):

| Type | n | top-1 | top-3 | top-5 |
|---|---:|---:|---:|---:|
| model | 7 | 1.000 | 1.000 | 1.000 |
| decision | 7 | 1.000 | 1.000 | 1.000 |
| run | 8 | .375 | **1.000** | **1.000** |
| scenario | 8 | .250 | .625 | .875 |

## Interpretation

- Scenario/run top-3/5 improve sharply when inputs and metrics are visible.
- Top-1 remains weak for scenario/run: several artifacts share title/questions,
  and the query often names a value rather than an artifact.
- Artifact lookup remains opt-in; no page/section default change.

## Limits

- 30 queries, 5 candidates each; AI labels.
- No human review, CI, owner acceptance or sufficient coverage.
