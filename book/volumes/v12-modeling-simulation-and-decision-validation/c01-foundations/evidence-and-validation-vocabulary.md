---
metadata_version: 1
id: "tycho.page.1a3833c3b4431428b25fa9896bcdd072"
kind: "page"
parent_id: "tycho.chapter.6006603befaacfc1baadc486a0f7007a"
canonical_path: "book/volumes/v12-modeling-simulation-and-decision-validation/c01-foundations/evidence-and-validation-vocabulary.md"
title: "Evidence and validation vocabulary"
topic_ids:
  - "model-validation"
  - "decision-records"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Five separate layers: source, verification, calibration, simulation, decision."
route_hints:
  questions:
    - "Which evidence layer does a V12 result support?"
    - "Which cross-layer inferences are forbidden?"
  prerequisites: []
  related_ids:
    - "tycho.page.d860bc57cdfe6c6163912819f7679d17"
    - "tycho.page.201248045fa3cd67e617ce04a1c56feb"
    - "tycho.page.ea9adae8cf8a3196a3515d383b075f53"
  excludes:
    - "No production measurement, independent review or owner acceptance is asserted."
  keywords:
    - "verification"
    - "validation"
    - "calibration"
    - "evidence status"
evidence_scope:
  source_ids:
    - "src.sargent-vv"
    - "src.jcgm-100"
    - "src.owen-monte-carlo"
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

# Evidence and validation vocabulary

**Question.** Which evidence labels may be used for a V12 result, and which inferences are
forbidden because they conflate different layers?

**Short answer.** V12 keeps five layers separate: source and claim evidence, model
verification, calibration, simulation evidence and decision evidence. Each layer answers a
different question. A result can be strong in one layer and weak in another. The labels are
not a ladder, and a later layer never upgrades an earlier one automatically.

## The five layers

- **Source and claim evidence:** does a public, admitted source support the method or claim?
  This is the layer of the reading ledger and page citations.
- **Model verification:** is the model implemented as specified? This is the layer of units,
  conservation, boundary cases, event ordering and deterministic tests.
- **Calibration:** do the parameters match measured reality? This is the layer of measured,
  assumed, derived and unknown inputs.
- **Simulation evidence:** what happens under the declared assumptions? This is the layer of
  scenario, seed, replication and convergence records.
- **Decision evidence:** does the decision follow from the model and the constraints? This is
  the layer of candidates, hard constraints, non-quantitative limits and reversal triggers.

A source can support a method without validating a model. A model can be verified without
being calibrated. A calibrated model can produce a simulation result that does not support a
decision because a hard constraint was omitted. A decision record can be decision-supported
while the underlying pattern remains unchanged and while the model remains uncalibrated, as
long as the record states the condition.

## What verification and validation mean here

Sargent defines model verification as ensuring that the computer program of the model is
correct, and model validation as ensuring that the model is adequate for its intended
purpose. Validity is purpose- and domain-dependent. A model change requires verification and
validation again.

V12 uses the same distinction:

- Verification evidence says the engine preserves conservation, non-negativity, event order,
  timeout behavior and boundary cases. The model-verification section lists the tests.
- Validation evidence says the model's structure, data and output are adequate for the
  decision. V12 has no operational validation against a real system. Every model records
  that limit.

The absence of operational validation is not a hidden failure. It is a declared condition
that shapes what a decision record may claim.

## Calibration statuses

V12 uses four input statuses:

- **measured:** a value comes from a named measurement with a method, sample size and period.
- **assumed:** a value is chosen for the model and is not a measurement.
- **derived:** a value is computed from measured or assumed inputs by a stated formula.
- **unknown:** no defensible value exists; the model must not invent one.

A measured input without a source and a measurement record is not measured. An assumed
input repeated in a decision record does not become measured. A derived input inherits the
weakest status of its inputs unless the derivation itself is validated.

JCGM 100 supports the measurement vocabulary: a measurement result includes a value and an
uncertainty, and a coverage interval is stated with a coverage probability. V12 uses that
vocabulary to describe uncertainty, but it does not perform a metrological uncertainty
budget. Every model in this volume is uncalibrated.

## Evidence statuses used in decision records

A decision record separates three statuses:

- model-verified, partially-verified or unverified for the engine and model;
- calibrated, partially-calibrated or uncalibrated for the inputs;
- decision-supported or insufficient-evidence for the outcome.

A decision-supported outcome with an uncalibrated model is a conditional result. It says
the decision follows from the declared assumptions and constraints. It does not say the
assumptions are true. The record must state the condition and the measurements that would
reverse it.

## Forbidden inferences

The following inferences are invalid in V12:

- "The model is verified, so the design is correct."
- "The source supports the pattern, so the simulation parameter is measured."
- "The simulation succeeded, so production will succeed."
- "The decision record recommends B, so B is safe to deploy."
- "The pattern is mentioned in a decision record, so the pattern is promoted."
- "The confidence interval excludes zero, so the business case is proven."

Each inference crosses a layer boundary without the required evidence. The decision record
may still be useful; it is useful as a bounded, conditional result, not as a certificate.

## A worked separation

The checkout comparison has:

- source support for queueing and event semantics from SimPy and Little's law;
- model verification for conservation, boundary cases and event ordering;
- uncalibrated arrival and service-time inputs;
- simulation evidence from 30 seeded replications per candidate;
- a decision-supported outcome for candidate B under the declared constraints;
- an explicit statement that the operability constraint and production behavior are not
  established.

A reader who wants to deploy B still needs a measured pilot, a cost review and an operational
readiness check. The decision record tells them what to measure, not what to assume.

## Evidence ledger

- [Sargent, WSC 2011](https://informs-sim.org/wsc11papers/016.pdf)
  supports verification, validation, data and conceptual validity.
  It does not establish V12 operational validity.
- JCGM 100:2008 (source src.jcgm-100; see the V12 reading ledger)
  supports measurement result, uncertainty and coverage vocabulary.
  It does not establish a V12 uncertainty budget.
- [Owen, Monte Carlo chapters](https://artowen.su.domains/mc/)
  supports sampling error and convergence vocabulary.
  It does not establish a calibrated V12 input distribution.

## Navigation

- Parent: [V12/C01 - Foundations](../README.md)
- Previous: [Model scope, boundary and abstraction](model-scope-and-abstraction.md)
- Next: [V12/C02 - Contracts](../c02-contracts/README.md)
