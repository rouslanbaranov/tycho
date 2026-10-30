# BM25 body weight — 2026-10-30

Status: weight grid and paired uncertainty on AI qrels v3/v4. Pool-relative; not
human review, CI, owner acceptance or sufficient coverage.

## Finding

Default weights were title 5, heading 2, body 0.25. A body weight of 0.5 is
better on qrels v4 and also improves v3 top-1. Body 1.0 overfits v4 and reduces
v3 section quality.

## Grid

Page/section hit@1/3/5, all queries:

| Weights | v4 page | v4 section | v3 page | v3 section |
|---|---|---|---|---|
| 5/2/.25 | .520/.807/.893 | .420/.647/.720 | .878/.952/.973 | .803/.941/.979 |
| 5/2/.5 | **.593/.847/.953** | **.480/.700/.793** | **.920/.984/.989** | **.846/.952/.968** |
| 5/2/.75 | .607/.887/.953 | .493/.740/.807 | .926/.984/.984 | .830/.915/.941 |
| 5/2/1.0 | .607/.887/.953 | .507/.747/.820 | .910/.973/.984 | .793/.899/.926 |
| 5/2/1.5 | .620/.880/.953 | .500/.733/.807 | .894/.963/.979 | .729/.888/.915 |

## Paired uncertainty: 5/2/.5 vs 5/2/.25

| Dataset | Level | Top-1 diff | 95% CI | p |
|---|---|---|---:|---:|
| v4 | page | +.0733 | [.0200, .1267] | .0127 |
| v4 | page top-5 | +.0600 | [.0267, .1000] | .0039 |
| v4 | section | +.0600 | [.0067, .1133] | .0490 |
| v4 | section top-5 | +.0733 | [.0333, .1200] | .0034 |
| v3 | page | +.0426 | [.0106, .0798] | .0215 |
| v3 | page top-5 | +.0160 | [.0000, .0372] | .250 |
| v3 | section | +.0426 | [.0053, .0851] | .0768 |
| v3 | section top-5 | -.0106 | [-.0266, .0000] | .5 |

## Decision

Use **5/2/0.5** as the BM25 default. It has the best cross-qrels tradeoff. Body
1.0 is not selected because it loses v3 section top-1/top-5. This was applied
to `section_search.py` in issue #739.

## Limits

- AI labels; v4 pool 4–10 candidates; v3 in-sample for prior defaults.
- No human review, CI, owner acceptance or sufficient coverage.
- No production-client benchmark.
