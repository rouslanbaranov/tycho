# Phase 3 topic-isolated agent qrels — 2026-10-24

Status: agent-authored and agent-adjudicated. Not human review, benchmark,
sufficiency or owner acceptance. No CI is claimed.

## Design

- 6 fresh authoring agents, one topic each, 8 answerable + 4 unanswerable.
- 72 unique questions; 15 public-source citations per topic range.
- 4 fresh Reviewer adjudicators, 18 items each, mixed across topics.
- Topic split: T1-T3 dev, T4-T6 held-out.
- 20% human sample: 15 items, selected before any gate evaluation.

Authoring agents did not read Tycho, qrels, gate code or other author files.
Adjudicators did not read gate code, qrels or other batches.

## Adjudication result

- 19 answerable / 53 unanswerable.
- 29 phase-3 answerable claims were unsupported by Tycho and became unanswerable.
- 2 invalid H2 anchors were cleared to page-level.
- All accepted quotes are verbatim; all retained section IDs exist.
- Split: 36 dev / 36 held-out.

The high unsupported rate is a corpus-coverage finding, not proof that the
external answer keys are false. Topics T5/T6 are especially thin in Tycho.

## Current evidence gate on phase 3

No retraining and no threshold tuning. This is a topic-held-out challenge for the
phase-2 model:

| Split | True abstain | False abstain | False answer | True answer | Answerable retained |
|---|---:|---:|---:|---:|---:|
| Dev (T1-T3) | 22 | 12 | 1 | 1 | 1/13 |
| Held-out (T4-T6) | 30 | 5 | 0 | 1 | 1/6 |

The gate is extremely conservative on these items: it abstains on 30/30 held-out
unanswerable items but retains only 1/6 answerable items. Phase 3 therefore does
not support promoting the gate; it shows that many author questions require
facts absent from Tycho.

## Human sample

[phase3-human-sample.json](../evaluation/phase3-human-sample.json) contains 15
items (20.8%), including confirmed answerable, unanswerable and contested
answerable-to-unanswerable relabels. [PHASE3-HUMAN-REVIEW-PACKET.md](PHASE3-HUMAN-REVIEW-PACKET.md)
is the review form.

**human_review: not-performed**. No verdicts are filled; the sample is pending.

## Decision

- Preserve phase 3 as an adjudicated challenge set.
- Do not train on it: only 19 answerable items, and held-out has 6.
- Do not tune the evidence gate on this set.
- Next data step is to resolve the 29 unsupported items: either add corpus
  support or replace them with questions the book can answer.
- Gate work remains blocked on a larger, more balanced independent set.

## Limits

- Agent-authored/agent-adjudicated, not human review.
- Adjudication is single-agent per batch; no inter-annotator agreement.
- Topic coverage is uneven; T5/T6 are thin.
- Quotes are verbatim but external sources were not re-fetched by adjudicators.
- The 20% human sample is pending, not passed.
