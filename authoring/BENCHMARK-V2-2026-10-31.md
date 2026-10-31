# Benchmark v2 — 2026-10-31

Status: harness and rubric framework implemented; pilot only. No new 100-agent
quality claim. AI-only; no human review.

## Changes

- corpus-v2.json: core_claims and optional_claims; 50 dev / 50 holdout.
- deterministic holdout based on question id parity.
- dual judge: judge, judge2, agreement, strict consensus.
- split filter in harness.
- checklist prompt in evaluation/agent-benchmark/AGENT-PROMPT.md.
- CLI caps: max 6000 codepoints, outline limit 5, clearer argument errors.
- token contract: null/estimated is explicit; no fabricated token counts.

## Pilot

Two saved answers replayed through two identical rule judges:

- dual_judged 2/2;
- judge_agreement 1.0;
- pass 0 because the strict citation rubric rejects non-required citations.

This validates plumbing, not quality.

## Why 92% earlier

The previous 92/100 was semantic full coverage: 100/100 supported, 92/100
covered all expected points. The eight failures were coverage-only; no
unsupported or wrong answers. The expected points were heading-derived and four
of eight semantic judges passed everything, one passed 6/12. The score is
single-judge and rubric-sensitive, not a stable correctness estimate.

## Limits

- core_claims are a heuristic de-genericized subset of heading points;
- no semantic gold answer key yet;
- holdout has not been run with independent agents under v2;
- token usage remains unavailable;
- no human review, CI or owner acceptance.
