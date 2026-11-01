---
metadata_version: 1
id: "tycho.page.c7a43944f1d41e810eec0d17ec33b85a"
kind: "page"
parent_id: "tycho.chapter.3a47e8385cccb8a2ce764bfa765cc740"
canonical_path: "book/volumes/v12-modeling-simulation-and-decision-validation/c02-contracts/decision-record.md"
title: "Decision record contract"
topic_ids:
  - "decision-records"
  - "model-validation"
perspectives:
  - "architecture"
  - "evaluation"
summary: "A decision record keeps constraints, evidence statuses, outcomes and triggers separate."
route_hints:
  questions:
    - "Which fields make a decision record reviewable?"
    - "When is insufficient evidence complete?"
  prerequisites: []
  related_ids:
    - "tycho.page.201248045fa3cd67e617ce04a1c56feb"
    - "tycho.page.b8e3757528ca1f60a472a6fd9deb7489"
    - "tycho.page.ea9adae8cf8a3196a3515d383b075f53"
  excludes:
    - "No measurement, independent review, owner acceptance or pattern promotion is asserted."
  keywords:
    - "decision record"
    - "constraints"
    - "alternatives"
    - "reversal triggers"
evidence_scope:
  source_ids:
    - "src.madr"
    - "src.nygard-adr"
  claim_ids: []
  status: "source-linked"
  notes: "Source-level citations; claim IDs not mapped. Page-local limits; not independent review."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-29"
  reviewer: "DeepSeek Harness authoring agent"
  proof_uri: null
authored_at: "2026-10-29"
updated_at: "2026-10-29"
source_inspection_date: "2026-10-29"
content_verified_at: null
---

# Decision record contract

**Question.** Which fields turn a simulation comparison into a reviewable architecture
decision without hiding a hard constraint or a missing measurement?

**Short answer.** A V12 decision record states the question, context, constraints,
candidates, metrics, evidence statuses, outcome, reversal triggers, limitations and one-way
pattern links. It may recommend a candidate or return insufficient evidence; both are
complete outcomes.

## Why a decision record is not a score

A weighted score can make a decision look objective while hiding the weights. A hard
constraint can be traded away for a small gain in a composite number. A missing measurement
can be replaced by a plausible value and forgotten. The decision record prevents those moves
by keeping constraints, evidence statuses and unknowns in separate fields.

MADR and Nygard support the structure: context and problem statement, considered options,
decision outcome, status and consequences. V12 keeps that structure but adds machine-readable
candidate and run references, evidence statuses and reversal triggers.

## Required structure

The contract contains:

- id, version, title and status;
- question and context;
- constraints: hard, soft (optional) and non-quantitative;
- candidates: identifier, scenario, runs, pattern identifiers and owner pages;
- metrics: identifier, unit, direction and business-comparable flag. The flag means
  candidates use the same metric definition; it does not mean the metric is measured or
  business-valid;
- evidence: model verification, calibration, simulation and source identifiers. In the current
  schema `evidence.simulation` carries the decision status by convention; it describes the
  decision, not whether the simulation executed;
- outcome: recommendation, rationale and non-quantitative constraints;
- constraint evaluation, reversal triggers, limitations and pattern links. Each
  `constraint_evaluation.status` applies to the recommended candidate; other candidates
  are described in the rationale. When `outcome.recommendation` is `none`, the status
  applies to the candidate evaluated in the rationale.

The status is one of proposed, decision-supported, insufficient-evidence or rejected. A
record with recommendation none can still be insufficient-evidence; it is not an invalid
record.

## Hard constraints versus preferences

A hard constraint is a condition a candidate must satisfy. If candidate C exceeds a declared
cost ceiling, C is eliminated even if it has the highest success rate. A soft constraint is a
preference that can be traded. A non-quantitative constraint is a condition the model cannot
measure, such as operability by the existing team or a regulatory approval.

The V12 checkout record declares two hard model invariants (conservation and no silent
drop), two hard quantitative limits (cost and p95 latency) and one non-quantitative
constraint (operability). C is eliminated by the cost and latency limits. B and A pass
C1/C2/C4/C5; C3 operability is not-tested. B wins on success rate and cost per successful
request; A wins on p95 latency, which is a tradeoff rather than a failed constraint. No
undeclared success threshold is applied. The record states that the operability constraint
remains unverified, so the recommendation is conditional.

## Pattern links without write-back

A candidate can name existing tycho.pattern.* identifiers and owner pages. The link is
one-way: V12 points to the pattern owner; the owner does not point back to V12. The derived
reverse index supplies discovery without editing the pattern corpus.

A pattern link is not a promotion. It does not change the pattern's coverage state, source
ledger or review status. A simulation result never promotes a pattern to sufficient.

## Example excerpt

~~~json
{
  "id": "tycho.decision.v12-checkout-candidate",
  "status": "decision-supported",
  "constraints": [
    {"id": "C4", "kind": "hard", "statement": "cost <= 3.0"},
    {"id": "C5", "kind": "hard", "statement": "p95 latency <= 1.5 s"}
  ],
  "outcome": {"recommendation": "B"},
  "reversal_triggers": ["arrival rate above 22 requests/second"]
}
~~~

The excerpt is a non-normative, non-schema-valid fragment; the full record adds candidates,
metrics, evidence, limitations, reversal triggers and pattern owner pages.

## Insufficient evidence is a result

A decision record can conclude that the evidence is insufficient. The modernization record
does exactly that: the staged candidate has a large synthetic divergence, rollback does not complete
within the 2,400-second horizon in 90% of replications; those durations are censored, and
the dual-write inputs are assumed. M2 is marked fail because completion inside the window
is required. The correct outcome is
insufficient evidence, not a recommendation to cut over and not a claim that modernization
is impossible.

The record lists what would change the outcome: measured dual-write lag, measured
reconciliation capacity, a rehearsed rollback and a measured divergence below the business
threshold.

## Failure modes

- **Recommendation without constraints.** A candidate is recommended because it has the best
  average, while a hard constraint is ignored.
- **Score laundering.** A composite score hides the weights and the eliminated candidates.
- **Evidence inflation.** A model-verified engine is presented as a validated system.
- **Promotion by mention.** A pattern link is treated as a pattern promotion.
- **Missing reversal trigger.** A decision has no condition under which it should be
  revisited.
- **Recommendation by default.** A record with no recommendation is treated as incomplete,
  so an analyst invents one.

## Evidence ledger

- [MADR](https://adr.github.io/madr/)
  supports context, considered options, decision outcome and consequences.
  It does not establish the correctness of a decision.
- [Nygard, Documenting Architecture
  Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
  supports short, modular records with context, decision, status and consequences.
  It does not replace measurement or review.

## Navigation

- Parent: [V12/C02 - Contracts](README.md)
- Previous: [Run and result provenance contract](run-and-result-provenance.md)
- Next: [V12/C03 - Deterministic and DES](../c03-deterministic-and-des/README.md)
- Schema: [decision-record.v1.schema.json](../../../../schemas/v12/decision-record.v1.schema.json)
