# Phase 3 topic-isolated agent qrels — 2026-10-24

Status: agent-authored and agent-adjudicated. Not human review, benchmark,
sufficiency or owner acceptance. No CI is claimed.

## Design and filtering

- 6 fresh authoring agents, one topic each, 8 answerable + 4 unanswerable.
- 72 unique questions; 4 fresh adjudicators mapped them to Tycho.
- 29 author-answerable claims had no Tycho support. They are preserved in
  evaluation/agent-qrels.phase3.json under "excluded" for audit, but removed
  from the scored set.
- Filtered scored set: 43 items, 19 answerable / 24 unanswerable.
- Split: 25 dev (T1-T3) / 18 held-out (T4-T6).
- 9-item human sample (20.9%), stratified across all six topics.
- Human sample: evaluation/phase3-human-sample.json and
  authoring/PHASE3-HUMAN-REVIEW-PACKET.md. Human review is pending.

## Current gate and retrieval on the filtered set

No retraining and no threshold tuning:

| Split | True abstain | False abstain | False answer | True answer | Answerable retained |
|---|---:|---:|---:|---:|---:|
| Dev | 12 | 12 | 0 | 1 | 1/13 |
| Held-out | 12 | 5 | 0 | 1 | 1/6 |

Retrieval page/section hit@5: 7/13 dev, 3/6 held-out.

The gate is conservative and the retrieval layer often misses the accepted
support. This is a retrieval/evidence problem, not a reason to tune the gate on
phase 3.

## Human sample

The sample contains five confirmed answerable and four unanswerable items. No
verdicts are filled; the status remains human-review-pending.

## Decision

- Keep phase 3 as a challenge set, not training data.
- Do not tune the evidence gate on it: 19 answerable items are too few.
- Fix retrieval/evidence support for the retained answerable items before any
  gate retraining.
- Do not re-admit excluded items without corpus support.

## Limits

- Agent-authored/agent-adjudicated, not human review.
- Adjudication is single-agent per batch; no inter-annotator agreement.
- Topic coverage is uneven; T5/T6 have five retained items each.
- Quotes are verbatim, but external sources were not re-fetched.
- The 20% human sample is pending, not passed.
