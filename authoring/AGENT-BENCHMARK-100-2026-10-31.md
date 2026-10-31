# 100 independent external-agent sessions — 2026-10-31

Status: 100 independent agent sessions executed. AI agents and AI judges only;
no human review, CI, owner acceptance or production benchmark.

## Execution

- one fresh subagent per corpus question;
- each used only the read-only CLI;
- per-session JSONL logs;
- pinned snapshot;
- no corpus/qrels/answer leakage in prompts;
- 100/100 answer files produced.

## Results

| Metric | Value |
|---|---:|
| agents | 100 |
| non-empty answers | 100 |
| abstentions | 0 |
| answer_support=2 | **100 / 100** |
| coverage=2 | **92 / 100** |
| citation_valid | **99 / 100** |
| semantic pass | **92 / 100** |
| citations | 348 |
| tool calls | 1,104 |
| mean calls/agent | 11.04 |
| failed calls | 46 |
| tokens | **unavailable** |

Token usage is unavailable: every agent reported total null; the harness does
not receive provider usage. No token mean or z-score is claimed.

## By layer

| Layer | n | pass | support=2 | coverage=2 | citations | calls |
|---|---:|---:|---:|---:|---:|---:|
| book | 50 | 46 | 50 | 46 | 181 | 596 |
| atlas | 25 | 22 | 25 | 22 | 82 | 285 |
| modeling-and-simulation | 25 | 24 | 25 | 24 | 85 | 223 |

## Failures

Coverage-only failures: Q015, Q020, Q031, Q036, Q052, Q060, Q068, Q084.
Q066 passed but had one citation-validity flag (a cross-reference citation).

The strict rule judge (citations must be in the required-evidence list) passed
17/100; that is a lower-bound citation rubric, not semantic correctness. The
semantic judges graded support/coverage from the answers and cited evidence.

## Observations

- all 348 citations resolve to indexed sections;
- only 158/348 citations are in the precomputed required-evidence lists, which
  explains the strict-rule judge gap;
- 46 failed CLI calls were mostly the old max-chars/argument mismatch and were
  retried or worked around;
- book sessions needed the most calls (596) and had 21 failed calls;
- modeling-and-simulation had the best pass rate (24/25).

## Limits

- corpus expected points are qrels-derived headings, not a semantic gold key;
- semantic judges are AI-only and not independent humans;
- tokens are unavailable, so no token-efficiency conclusion;
- no human review, CI or owner acceptance.
