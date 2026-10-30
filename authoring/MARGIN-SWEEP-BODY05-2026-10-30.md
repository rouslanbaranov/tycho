# Margin sweep at body 0.5 — 2026-10-30

Status: opt-in tuning on AI qrels v4; production default remains BM25. Pool-
relative; not human review, CI, owner acceptance or sufficient coverage.

## Page hit@1/3/5, all

| Threshold | Page | Section |
|---|---|---|
| BM25 | .593/.847/.953 | .480/.700/.793 |
| .05 | **.620/.833/.940** | **.513/.700/.800** |
| .10 | .607/.840/.920 | .493/.713/.787 |
| .15 | .587/.847/.913 | .473/.707/.787 |
| .20 | .567/.847/.913 | .447/.700/.780 |
| .30 | .573/.847/.907 | .453/.713/.787 |
| .50 | .560/.847/.907 | .420/.727/.800 |
| global | .560/.847/.907 | .420/.733/.807 |

## Splits at .05

| Split | n | Page | Section |
|---|---:|---|---|
| book | 90 | .633/.822/.922 | .522/.667/.756 |
| atlas | 30 | .433/.800/.933 | .433/.800/.933 |
| V12 | 30 | .767/.900/1.000 | .567/.700/.800 |
| all | 150 | .620/.833/.940 | .513/.700/.800 |

## Interpretation

- .05 gives the best opt-in top-1: page +2.7, section +3.3.
- It loses 1.3 page top-3 and 1.3 page top-5.
- Atlas top-1 is unchanged; top-5 loses 3.4.
- .15 is worse than .05 and is not supported by v4.
- Global rerank improves section top-3/5 but lowers top-1.

## Decision

Keep BM25 default. If margin rerank is exposed, use .05 as the preferred
opt-in; do not restore a margin default. The current .15 opt-in should be
revisited before any future default change.

## Limits

- AI labels; candidate pools 4–10; no human review, CI, owner acceptance or
  sufficient coverage.
- No production-client benchmark.
