# Fresh v5 holdout results — 2026-11-01

Status: 50 fresh agents on 50 new questions, two independent AI judge passes and
third adjudication. AI-only; no human review; no book/atlas changes.

## Design

- Q150-Q199, absent from prior corpora.
- 25 book / 12 atlas / 13 modeling-and-simulation.
- Concise v3 prompt: onboarding, facet/evidence matrix, 150-220 words.
- One fresh agent per question.
- Two AI judges per question; adjudication of four disagreements.

## Results

| Metric | Value |
|---|---:|
| agents | 50 |
| consensus pass | **16 / 50** |
| judge agreement | **46 / 50 (92%)** |
| support=2 | **50 / 50** |
| core coverage=2 | **16 / 50** |
| citation valid | **40 / 50** |
| mean calls | 30.58 |
| mean words | 209.7 |
| mean citations | 6.92 |
| adjudicated | 4 |
| adjudicated pass | 0 |
| final pass | **16 / 50** |

## By layer

| Layer | n | pass | support=2 | coverage=2 | citation valid |
|---|---:|---:|---:|---:|---:|
| book | 25 | 8 | 25 | 8 | 20 |
| atlas | 12 | 1 | 12 | 1 | 9 |
| modeling-and-simulation | 13 | 7 | 13 | 7 | 11 |

## Interpretation

The concise prompt meets its length target (209.7 words) and every answer is
evidence-supported. Coverage remains the limiting metric: 16/50; the two judge
passes agree on 92% of tasks, and all four disagreements failed adjudication.

This is not comparable with v4 (19/50), the older 92%, or the 20-question pilot:
the questions, claims and prompt differ. It is a single AI-judged holdout.

## Limits

- claims and questions are AI-generated, not human-reviewed;
- judges did not read evidence and are the same model family;
- citation validity is judge-assessed, 40/50;
- tokens unavailable;
- this holdout is consumed and must not be reused.
