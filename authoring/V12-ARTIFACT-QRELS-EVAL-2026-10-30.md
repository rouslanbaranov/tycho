# V12 artifact qrels evaluation — 2026-10-30

Status: external Codex artifact labels, AI-adjudicated only. Not human review,
CI, owner acceptance or sufficient coverage.

## Dataset

- `evaluation/v12-artifact-qrels.v1.json`
- 30 questions, 150 candidate judgments;
- exactly 5 candidates per question;
- accepted 69, direct 30;
- HEAD `448a6557`; snapshot `e7496a66…`;
- validator PASS.

## Query-aware artifact ranking

| Metric | Accepted | Direct |
|---|---:|---:|
| top-1 | .500 | .367 |
| top-3 | .600 | .500 |
| top-5 | .700 | .600 |

By direct artifact type (accepted):

| Type | n | top-1 | top-3 | top-5 |
|---|---:|---:|---:|---:|
| model | 7 | **.857** | .857 | .857 |
| decision | 7 | .571 | .714 | .714 |
| run | 8 | .375 | .500 | .750 |
| scenario | 8 | .250 | .375 | .500 |

A fixed no-term artifact list scored .133/.333/.467 accepted top-1/3/5.

## Interpretation

- Query-aware ranking beats an arbitrary artifact list.
- Model and decision records are strong; scenario and run artifact
  disambiguation is weak.
- With 5 candidates per query and n=30, the result is pool-relative and
  underpowered for tuning.
- Artifact lookup remains opt-in; no default change.

## Limits

- AI labels only; no human review, CI, owner acceptance or sufficient coverage.
- Small type cells (7–8 questions).
- Not a page/section qrels substitute.
