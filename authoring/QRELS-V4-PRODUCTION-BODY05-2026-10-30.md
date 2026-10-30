# Qrels v4 production baseline — body 0.5

Status: AI-adjudicated qrels v4 evaluation after body-weight 0.5 default. Pool-
relative; not human review, CI, owner acceptance or sufficient coverage.

## Page hit@1/3/5

| Split | n | BM25 | margin | best |
|---|---:|---|---|---|
| book | 90 | .589/.833/.933 | .600/.856/.911 | .600/.844/.944 |
| atlas | 30 | **.433/.833/.967** | .367/.767/.867 | .267/.733/.900 |
| V12 | 30 | **.767/.900/1.000** | .767/.900/.967 | .767/.900/1.000 |
| all | 150 | **.593/.847/.953** | .587/.847/.913 | .567/.833/.947 |

## Section hit@1/3/5

| Split | n | BM25 | margin | best |
|---|---:|---|---|---|
| book | 90 | .467/.656/.733 | .478/.689/.767 | .478/.667/.744 |
| atlas | 30 | **.433/.833/.967** | .367/.767/.867 | .267/.733/.900 |
| V12 | 30 | **.567/.700/.800** | .567/.700/.767 | .567/.700/.800 |
| all | 150 | **.480/.700/.793** | .473/.707/.787 | .453/.687/.787 |

## Decision

- Keep BM25 default at title/heading/body 5/2/0.5.
- Keep margin gate opt-in; it loses page top-5 and atlas.
- Best mode remains optional; it loses aggregate page/section.
- Atlas top-1 is the weakest split; investigate separately.

## Limits

- AI labels; candidate pools 4–10; pool-relative.
- No human review, CI, owner acceptance or sufficient coverage.
- No production-client benchmark.
