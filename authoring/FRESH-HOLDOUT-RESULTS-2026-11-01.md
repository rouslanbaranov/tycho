# Fresh v4 holdout results — 2026-11-01

Status: 50 fresh agents and two independent AI judge passes completed. No human
review; no book/atlas changes.

## Results

| Metric | Value |
|---|---:|
| agents | 50 |
| consensus pass | **19 / 50** |
| judge agreement | **45 / 50 (90%)** |
| support=2 | 48 / 50 |
| core coverage=2 | 19 / 50 |
| citation valid | 46 / 50 |
| adjudicated disagreements | 5 |
| adjudicated pass | 0 |
| final pass after adjudication | **19 / 50** |
| tokens | unavailable |

## By layer

| Layer | n | pass | support=2 | coverage=2 |
|---|---:|---:|---:|---:|
| book | 25 | 12 | 24 | 12 |
| atlas | 12 | 3 | 11 | 3 |
| modeling-and-simulation | 13 | 4 | 13 | 4 |

## Judge disagreement

Five disagreements were adjudicated by a third AI adjudicator; all five failed
on at least one core claim. A-pass was 21/50, B-pass 22/50, consensus 19/50.

## Claims review

An AI editorial review of 10 new holdout claims (20%) found 6 accept and
4 revise. The four revisions were not applied before this run, so the frozen
claims remain as judged. Human review was not performed.

## Limits

- questions and claims are AI-generated, not human-reviewed;
- judge evidence reads were disabled for the B pass to avoid stalls;
- token usage is unavailable;
- this holdout is consumed and must not be used for tuning;
- no comparison with the previous 92% is valid.
