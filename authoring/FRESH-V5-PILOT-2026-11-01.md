# Fresh v5 holdout pilot — 2026-11-01

Status: 20 of 50 frozen v5 questions executed; all 20 are from the book layer.
No 50-question result is claimed. AI-only; no human review.

## Design

- 50 new questions Q150-Q199, layer split 25 book / 12 atlas / 13
  modeling-and-simulation.
- Concise v3 prompt: onboarding, facet/evidence matrix, 150-220 word answer.
- Executed the first 20 book questions only.
- Two AI judges per question; third adjudicator for two disagreements.

## Results for the 20-question book prefix

| Metric | Value |
|---|---:|
| agents | 20 |
| consensus pass | **7 / 20** |
| judge agreement | **18 / 20** |
| support=2 | **20 / 20** |
| citation valid | 16 / 20 |
| mean CLI calls | 30.35 |
| mean answer words | 208.4 |
| mean citations | 6.9 |
| mean evidence rows | 9.55 |
| adjudicated | 2 |
| adjudicated pass | 0 |

The two disagreements were Q154 and Q164; both failed adjudication.

## Interpretation

The concise prompt produced evidence-grounded, length-controlled answers:
all 20 have full support and 208 words mean. Coverage is the limiting metric:
7/20 consensus.

This is a book-only 20-question pilot, not a holdout result. It cannot be compared
with v4, the previous 92%, or any 50-question number.

## Remaining

Q170-Q199 (5 book, 12 atlas, 13 modeling-and-simulation) are frozen but not
executed. The v5 holdout is incomplete and must not be tuned or reported as a
50-question result.

## Limits

- AI judges, no evidence reads, no human;
- citation validity is judge-assessed, 16/20;
- one judge pair per question;
- token usage unavailable;
- no book/atlas changes.
