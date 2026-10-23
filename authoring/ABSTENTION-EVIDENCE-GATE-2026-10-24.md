# Evidence-aware abstention gate — 2026-10-24

Status: agent-adjudicated diagnostic. Not human review, answer correctness,
benchmark or sufficient coverage. No CI or owner acceptance is claimed.

## Data

Phase 2 adjudicated the frozen 80-item phase-1 set against Tycho pages:

- 54 answerable and 26 unanswerable;
- 6 phase-1 answerable items had no supporting section and became unsupported;
- 159 accepted support entries across 52 pages and 82 H2 sections;
- 8 non-existent H2 anchors were cleared to page-level acceptance;
- split: 40 dev / 40 held-out; phase 1 remains a separate challenge set.

Files:

- [agent-qrels.phase2.json](../evaluation/agent-qrels.phase2.json)
- [independent phase 1](../evaluation/independent-agent-qrels.phase1.json)

Phase 2 was produced by a fresh Reviewer agent with no access to the current
gate, qrels v2 or abstention reports.

## Model

[evidence-gate.v1.json](../edition/patterns/evidence-gate.v1.json) is a small
logistic model over:

- BM25 score and score per term;
- top-result term coverage, heading coverage and score margin;
- result count and unknown-term rate;
- longest query phrase in the excerpt;
- five query-scope signals: vendor, current-fact, production, exact-measurement
  and organisation-specific;
- a 233-token bag learned from phase-2 dev only.

Threshold 0.21 was selected on phase-2 dev cross-validation. Phase-2 held-out
and phase-1 were not used for tuning.

## Results

| Split | TP | FP | FN | TN | Precision | Recall | Answerable retained |
|---|---:|---:|---:|---:|---:|---:|---:|
| phase-2 dev | 12 | 0 | 0 | 28 | 1.000 | 1.000 | 28/28 |
| phase-2 held-out | 10 | 2 | 4 | 24 | 0.833 | 0.714 | 24/26 |
| phase-1 challenge | 19 | 5 | 1 | 55 | 0.792 | 0.950 | 55/60 |

- Phase-2 held-out: 10/14 unanswerable abstained, 2/26 answerable refused,
  4/14 false answers.
- Phase-1 challenge: 19/20 unanswerable abstained, 5/60 answerable refused,
  1/20 false answers.
- The old regex/score gate on phase 1 abstained on only 6/20 and produced
  14 false answers.

## Decision

Search uses the evidence model when it is present; `abstain=False` remains a
diagnostic bypass. The old heuristic remains only as a fallback when the model
artifact is missing. Agent-adjudicated labels are not human review; do not
describe this as calibrated production quality.

## Limits

- 40 dev and 40 held-out items are small; token features can overfit topics.
- Phase 1 is a second challenge sample, not a representative query distribution.
- The model does not prove answer correctness or evidence entailment; it uses
  lexical and retrieval evidence.
- No human adjudication, inter-annotator agreement, owner acceptance or CI.
- `sufficient` remains 0.
