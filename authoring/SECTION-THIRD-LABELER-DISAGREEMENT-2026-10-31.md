# Section third-labeler disagreement — 2026-10-31

Status: AI-adjudicated only. No change to v5.4, defaults, book or atlas.

## Method

- same 25 section disputes, same 700-character excerpts;
- two fresh independent empty-context DeepSeek third labelers;
- neither read prior labels, rankings or the committed adjudication;
- v5.4 and the committed adjudication were not modified.

## Grade distributions

| Source | 2 direct | 1 supporting | 0 hard |
|---|---:|---:|---:|
| run 1 | 6 | 16 | 3 |
| run 2 | 3 | 16 | 6 |
| committed v5.4 | 5 | 6 | 14 |

Run 1 is more permissive; run 2 and the committed adjudication are stricter.
Run 2 matches the committed adjudication on 15/25; run 1 on 11/25.

## Agreement

| Metric | Value |
|---|---:|
| exact run1/run2 | .680 |
| Cohen's kappa | .399 |
| consensus | 17 / 25 |
| unresolved | 8 / 25 |

## Unresolved disagreements

| Query | run1 | run2 | committed |
|---|---:|---:|---:|
| V4-A019 | 1 | 0 | 0 |
| V4-A022 | 1 | 0 | 0 |
| V4-A025 | 2 | 1 | 2 |
| V4-B015 | 1 | 0 | 0 |
| V4-B037 | 0 | 1 | 1 |
| V4-B039 | 1 | 0 | 0 |
| V4-B047 | 2 | 1 | 1 |
| V4-B077 | 2 | 1 | 2 |

Six of the eight are one-step support/hard or direct/support differences; the
committed adjudication is inside the run1/run2 range on all eight.

## Decision

- Do not retroactively change v5.4.
- Record the 17-consensus labels and the 8 unresolved units.
- Any future v5.5 section must use an explicit rule: consensus-only, median, or
  a fresh adjudication; this report does not choose one.

## Limits

- Two AI labelers only; no human review.
- Excerpt-only evidence; no full pages opened.
- The 25 disputes are not all section units.
- No CI, owner acceptance, sufficient coverage or production benchmark.
