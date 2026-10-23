# Independent agent qrels and abstention failure — 2026-10-23

Status: agent-adjudicated challenge set. This is not human review, not a
benchmark and not a sufficiency claim. No Tycho page, qrels or search output was
shown to the phase-1 author before the questions were frozen.

## What was produced

A fresh Reviewer-preset agent researched 15 public topics and froze:

- 60 answerable questions, four per topic;
- 20 unanswerable questions: vendor-specific, current-fact, exact-measurement
  and out-of-scope;
- 79 public source URLs, 2–4 per answerable item;
- no Tycho paths, page IDs or existing qrels.

Files:

- [independent-agent-qrels.phase1.json](../evaluation/independent-agent-qrels.phase1.json)
- [INDEPENDENT-AGENT-QRELS-2026-10-23.md](INDEPENDENT-AGENT-QRELS-2026-10-23.md)

The set is frozen. It is used as a challenge set, not as training data.

## Current gate on the challenge set

| Metric | Qrels v2 (author) | Independent agent |
|---|---:|---:|
| Unanswerable abstained | 58/65 (89.2%) | 6/20 (30.0%) |
| False answer rate | 7/65 (10.8%) | 14/20 (70.0%) |
| Answerable retained | 147/155 (94.8%) | 51/60 (85.0%) |
| Abstention precision | 0.879 | 0.400 |

The independent set exposes the overfit: 14 of 20 unanswerable questions
received a normal result. Only three triggered the scope gate; the rest were
missed because their wording did not match the authored cues. Nine answerable
questions were refused, mostly by the low-score or unknown-term rules.

Examples of false answers:

- "Which caching product gives the lowest read latency for a 100 GB working set?"
- "What does a managed cache provider charge per million reads this month?"
- "How many nodes does our production etcd cluster run?"
- "Which region pair should our company choose for data residency?"

## Classifier experiment

A logistic scope classifier trained only on qrels v2 dev features was also
tested. On the independent challenge set it reached precision 0.29–0.58 and
recall 0.35–0.60, depending on regularization; it was not shipped. Bag-of-words
and BM25 features from the author-labelled set do not transport to the
agent-adjudicated wording.

## Decision

- Do not tune on this challenge set; that would destroy its value.
- Do not claim that the current gate is calibrated or production-ready.
- Keep `abstain` as an experimental diagnostic until a larger independent set
  and an evidence-aware gate exist.
- The next gate should combine query intent, retrieval confidence and evidence
  entailment, and should be validated on a held-out independent set.

## Limits

- Agent-adjudicated, not independent human review; no inter-annotator agreement.
- 80 items are a challenge sample, not a representative query distribution.
- Answerable items were not mapped to Tycho pages in this phase; the result is
  about refusal behaviour, not page relevance.
- The book's vendor-neutral scope itself is a judgment; some out-of-scope labels
  are arguable.
- No CI, owner acceptance or sufficiency claim.
