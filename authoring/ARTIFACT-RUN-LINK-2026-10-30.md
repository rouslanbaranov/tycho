# Run artifact ↔ scenario link — 2026-10-30

Status: opt-in artifact lookup improvement. 30 AI-adjudicated queries; not human
review, CI, owner acceptance or sufficient coverage.

## Change

Run artifact match text now includes the linked scenario JSON (via
`scenario_id`), so inputs such as queue capacity, attempts and rates are visible
when selecting a run. The detail cache stores scenario path/mtime/size as
dependencies; a scenario edit invalidates the run text.

## Results

| Metric | Before link | After link |
|---|---|---|
| accepted top-1 | .733 | **.800** |
| accepted top-3 | .933 | .933 |
| accepted top-5 | .933 | .933 |
| direct top-1 | .733 | **.800** |
| direct top-3 | .900 | **.933** |
| direct top-5 | .933 | .933 |

By type (accepted, after):

| Type | n | top-1 | top-3 | top-5 |
|---|---:|---:|---:|---:|
| model | 7 | 1.000 | 1.000 | 1.000 |
| run | 8 | **.875** | 1.000 | 1.000 |
| decision | 7 | .857 | .857 | .857 |
| scenario | 8 | .500 | .875 | .875 |

## Interpretation

- Run top-1 jumps from .625 to .875 when scenario inputs are visible.
- Scenario top-1 remains .500; several scenario questions use relative
  comparisons ("slower", "higher cost") not literal values.
- Decision top-1 is .857; one query still ranks a run first.
- Artifact lookup remains opt-in; page/section defaults unchanged.

## Limits

- AI qrels, 30 queries, 5 candidates.
- No human review, CI, owner acceptance or sufficient coverage.
