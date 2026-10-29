---
metadata_version: 1
id: "tycho.page.d860bc57cdfe6c6163912819f7679d17"
kind: "page"
parent_id: "tycho.chapter.6006603befaacfc1baadc486a0f7007a"
canonical_path: "book/volumes/v12-modeling-simulation-and-decision-validation/c01-foundations/model-scope-and-abstraction.md"
title: "Model scope, boundary and abstraction"
topic_ids:
  - "simulation"
  - "model-validation"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Smallest model that distinguishes alternatives; state the validity domain."
route_hints:
  questions:
    - "How is a model boundary derived from a decision?"
    - "When is a stock-and-flow model sufficient?"
  prerequisites: []
  related_ids:
    - "tycho.page.870e64da1f925c52109a602440048603"
    - "tycho.page.1a3833c3b4431428b25fa9896bcdd072"
    - "tycho.page.d8d9d15b402d8f65928ca0e3f3e5b939"
  excludes:
    - "No production measurement, independent review or owner acceptance is asserted."
  keywords:
    - "model scope"
    - "abstraction"
    - "validity"
    - "boundary"
evidence_scope:
  source_ids:
    - "src.sargent-vv"
    - "src.mit-esd-system-dynamics"
  claim_ids: []
  status: "source-linked"
  notes: "Page-local source records and limits; not independent review."
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

# Model scope, boundary and abstraction

**Question.** How should a modeling team choose what to include, what to omit and how much
detail a decision actually needs?

**Short answer.** Start from the decision, not from the system. State the purpose, the
decision owner, the alternatives, the constraints and the observations that could change the
choice. Then choose the smallest model that can distinguish those alternatives inside a
declared validity domain. Everything outside that domain is an explicit omission, not an
unstated assumption.

## From decision to boundary

A model boundary is the line between the model's state and the rest of the world. It is not
the same as a service boundary or a team boundary. A checkout model may include a queue and
a server pool while omitting the payment network, the database and the deployment platform.
That is acceptable only if the omitted parts cannot change the comparison under the declared
conditions.

A useful boundary statement answers five questions:

1. **Purpose:** which decision does this model inform?
2. **Alternatives:** which candidates are compared?
3. **Observable:** which metric would distinguish them?
4. **Excluded:** which actors, dependencies and failures are outside the model?
5. **Validity:** under which ranges and conditions is the result intended to hold?

The V12 model contract makes these fields explicit. A model that cannot answer them is not
ready for a scenario.

## Abstraction is a choice about resolution

Three model families cover most V12 questions:

- **Stock-and-flow** for accumulation, feedback, delay and capacity. It is cheap to run and
  good for showing conservation and backlog growth. It does not represent individual
  request latency.
- **Discrete-event** for queueing, deadlines, retries and tail latency. It represents
  individual requests and event ordering. It costs more to verify and can hide numerical
  detail behind a plausible average.
- **Hybrid** for a staged path where traffic shares, reconciliation backlog and rollback
  coexist. It is a purposeful simplification, not a claim that the underlying system is
  fluid.

The choice is not a maturity ladder. A stock-and-flow model is not an inferior discrete-event
model; it answers a different question. A discrete-event model is not automatically more
accurate; it can be wrong at a finer resolution.

## A scope statement that can be reviewed

A reviewable scope statement has the form:

    Purpose: compare three checkout candidates on success, p95 latency and relative
    cost under a synthetic 20 requests/second workload.
    Boundary: request admission, a bounded queue, a server pool, per-attempt deadlines
    and bounded retries. Excluded: dependency calls, storage, network and deployment.
    Resolution: event-level for individual latency; one request class; no priorities.
    Validity: synthetic arrivals and service times only; no production claim.

This statement is short enough to challenge. A reader can ask whether the omitted dependency
is material, whether one request class is enough, and whether the synthetic workload is
representative. Those questions are the review.

## Worked example: why the checkout comparison needs events

A stock-and-flow model can show that a 20-requests-per-second load against a 24-request-per-
second capacity has a utilization of 0.833 and a stable backlog. It cannot show the p95
latency of successful requests, because it has no individual requests. If the decision is
"which candidate meets a 1.5-second p95 constraint", the stock-and-flow model cannot answer
it. The discrete-event model is required not because it is more sophisticated but because
the decision depends on a distribution that the coarser model does not contain.

Conversely, if the decision is "does the backlog grow when offered load exceeds capacity?",
the stock-and-flow model is sufficient. Running a detailed event model would add cost and
verification burden without changing the answer.

## Failure modes of scope

- **Model scope creep.** A queue model quietly grows a database, a cache and a deployment
  model. The comparison becomes hard to review and the original question is lost.
- **False precision.** A model reports four decimal places for an input measured to one
  significant figure. Precision is not accuracy.
- **Boundary mismatch.** The decision is about a caller-visible outcome, but the model
  boundary starts after admission. The missing admission behavior can reverse the result.
- **Omitted dependency.** A downstream timeout is externalized as a constant service time.
  The model then cannot show the failure that motivates the decision.
- **Validity drift.** The model is calibrated for one workload and reused for another
  without restating the domain.

Sargent separates conceptual-model validity from operational validity. A scope statement
addresses the conceptual side: are the theories, assumptions and structure reasonable for
the purpose? Operational validity asks whether the model's output matches the problem
entity over the intended domain. A model can be conceptually reasonable and operationally
unvalidated; the record must say which condition holds.

## A checklist before adding detail

- Does the added detail change a metric that can reverse the decision?
- Can the new state or parameter be measured, assumed or marked unknown?
- Does the addition preserve units and conservation?
- Does it create a new failure mode that the tests do not cover?
- Can a reader see the boundary in the model contract without reading the engine?
- Is the added cost proportionate to the decision's consequence of error?

If the answer to the first question is no, the detail is probably not worth the verification
burden. If the answer is yes, add it and record the new validity limit.

## Evidence ledger

- [Sargent, WSC 2011](https://informs-sim.org/wsc11papers/016.pdf)
  supports purpose-dependent validity and conceptual/operational validity.
  It does not establish any V12 scope choice.
- MIT ESD.00 lectures 2-4 (source src.mit-esd-system-dynamics; see the reading ledger)
  supports system dynamics as a purpose-built simulation method.
  It does not establish a general theory of abstraction.

## Navigation

- Parent: [V12/C01 - Foundations](../README.md)
- Previous: [Stock-and-flow modeling](stock-and-flow-vs-stock-to-flow.md)
- Next: [Evidence and validation vocabulary](evidence-and-validation-vocabulary.md)
