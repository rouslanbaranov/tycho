# Agent prompt v3 — 2026-11-01

Status: prompt, onboarding command and pilot implemented. No benchmark quality
claim from the two-task pilot. AI-only; no human review.

## Changes

- agent_session_cli.py describe exposes the typed metadata catalog, layers and
  aliases without needing the MCP transport.
- AGENT-PROMPT-V3.md requires onboarding, a facet matrix, 2-3 query
  formulations per facet, saturation instead of a fixed call cap, a per-claim
  evidence ledger and a detailed justified answer template.
- Output now carries an evidence array; judge-facing citations remain unchanged.
- README documents the v3 onboarding step.

## Pilot

Two dev questions, one fresh agent each:

| Task | CLI calls | Citations | Evidence rows |
|---|---:|---:|---:|
| Q000 | 36 | 15 | 15 |
| Q002 | 32 | 13 | 14 |

Both runs began with describe, used book and atlas evidence, and returned
sections for direct answer, mechanism, boundaries, evidence map and unknowns.
Q000 also included a facet matrix in the answer.

This validates onboarding and answer shape, not answer quality or benchmark
performance.

## Limits

- two questions only;
- no judge pass on the pilot;
- no token usage;
- no human review;
- no claim that v3 improves the 19/50 result.
