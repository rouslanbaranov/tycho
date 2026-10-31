# External-agent benchmark — 2026-10-31

Status: harness implemented; corpus and pilot are AI-generated/rule-based.
Not human review, not 100 completed independent sessions.

## Corpus

evaluation/agent-benchmark/corpus.json contains 100 questions:

- 50 book;
- 25 atlas;
- 25 modeling-and-simulation.

Each item has required evidence, expected answer points, difficulty, token and
time budgets and rubric weights. The fallback corpus is derived from v5.3/v5.5
qrels; it is a retrieval benchmark, not a semantic answer-key corpus.

## Harness

scripts/agent_benchmark.py:

- dispatches one question to one independent subprocess in a fresh environment;
- parallel workers;
- pinned snapshot;
- per-session JSONL logs;
- optional external judge command;
- deterministic telemetry counters;
- token accounting and z-score anomalies;
- limit pilot mode and validate-only.

scripts/agent_judge.py is a rule-based citation/evidence judge, not semantic
and not human.

## Telemetry

evaluation/agent-benchmark/telemetry-schema.json defines:

- tool calls and errors;
- pages/sections/artifacts;
- atlas/modeling usage;
- evidence calls and citations;
- token usage with estimated flag;
- cohort anomalies;
- judge scores.

## Pilot

Pilot plumbing was exercised with a deterministic dummy agent and rule judge:
2/2 then 100/100 dispatched and judged; pass rate 1.0. This validates batch
dispatch, logging, judging and token accounting only, not agent quality.

## Limits

- The 100 corpus is retrieval-derived and has no semantic gold answer.
- The bundled judge is deterministic, not an independent semantic judge.
- The 100 independent agent runs are not executed here.
- No human review, production benchmark or owner acceptance.
