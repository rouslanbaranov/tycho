---
metadata_version: 1
id: "tycho.page.d8d9d15b402d8f65928ca0e3f3e5b939"
kind: "page"
parent_id: "tycho.chapter.3a47e8385cccb8a2ce764bfa765cc740"
canonical_path: "book/volumes/v12-modeling-simulation-and-decision-validation/c02-contracts/model-specification.md"
title: "Model specification contract"
topic_ids:
  - "simulation"
  - "model-validation"
perspectives:
  - "architecture"
  - "evaluation"
summary: "A versioned contract for state, parameters, invariants, verification and limits."
route_hints:
  questions:
    - "Which fields make a model specification reviewable?"
    - "How are assumed and measured parameters separated?"
  prerequisites: []
  related_ids:
    - "tycho.page.dedc5f2d31912a9ba5f562a86009fda0"
    - "tycho.page.1a3833c3b4431428b25fa9896bcdd072"
    - "tycho.page.621e495fcadc4849d2f21d55be4c52e4"
  excludes:
    - "No production measurement, independent review or owner acceptance is asserted."
  keywords:
    - "model spec"
    - "state variables"
    - "parameters"
    - "invariants"
    - "verification"
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

# Model specification contract

**Question.** Which fields must a model specification carry so that a reader can see its
state, units, assumptions and verification evidence without reading the engine?

**Short answer.** A V12 model specification is a versioned JSON object with a stable
identifier, purpose, scope, abstraction, state variables, parameters, dynamics, invariants,
verification cases, calibration status, validity limits, assumptions and unknowns. The strict
schema rejects missing or unexpected fields.

## Why a contract instead of a diagram

A diagram can show the shape of a model and still leave every decision hidden. Is the
backlog measured in requests or batches? Is the service rate a constant or a distribution?
Was the arrival rate measured or assumed? The diagram does not say. A contract forces those
choices into named fields that a validator can check and a reader can challenge.

The contract does not prove the model is useful. It makes the model's claims inspectable.

## Required structure

The model contract has these top-level fields:

- id and version: a stable tycho.model.* identifier and semantic version.
- title and purpose: the bounded question and why the model exists.
- scope: what is included and what is explicitly excluded.
- abstraction: time unit, state unit, boundary and resolution.
- state_variables: name, unit, description and non-negativity.
- parameters: name, unit, value type, evidence status, source identifiers and note.
- dynamics: model family, equations and integration step.
- invariants: the properties that must hold in every run.
- verification: status, cases, observed result and test path.
- calibration: status, per-parameter evidence and limits.
- validity_limits, assumptions and unknowns.

A parameter with an assumed value cannot claim a measured source. A measured parameter must
name a source and a measurement method, sample size and period. A verification case must
name the test that exercised it. A calibration status of uncalibrated is a complete value,
not a missing one.

## Example: the order-intake model

The V12 order-intake model declares three stocks (backlog, completed, rejected) and five
parameters (arrival rate, mean service time, servers, queue capacity, relative cost). Each
parameter is marked assumed, with an empty source list or a source that supports only the
method. The dynamics are a fixed-step fluid model with a 0.1-second step. The invariants are
request conservation, non-negative backlog and capacity-bounded admission.

The verification block records three cases: a below-capacity run, a saturation run and a
zero-arrival boundary. Each case names a test in tests/test_tycho_v12_engine.py and states
the observed result. The calibration block records that no production data were used. The
validity limits say the model is valid only for the synthetic workload recorded in a
scenario.

A shortened contract excerpt:

~~~json
{
  "id": "tycho.model.order-intake",
  "version": "1.0.0",
  "abstraction": {"time_unit": "second", "state_unit": "request"},
  "dynamics": {"kind": "stock-flow", "time_step": 0.1},
  "invariants": [{"name": "request-conservation"}],
  "calibration": {"status": "uncalibrated"}
}
~~~

The excerpt is illustrative; the full object is in edition/v12/models/order-intake.json.

## How the contract is validated

The V12 validator checks four things:

1. The object matches the strict JSON Schema for model specifications.
2. The identifier is unique and starts with tycho.model.
3. Every scenario that names the model resolves to this identifier.
4. Every parameter with evidence status measured has a source and a measurement record.

The validator cannot check that a source actually supports a parameter. That is an editorial
and review task. The contract only prevents an obvious mismatch between the label and the
record.

## Failure modes

- **Orphan model.** A model file exists but no scenario or decision references it. The
  validator treats it as an unused artifact, not as evidence.
- **Parameter drift.** A scenario overrides a parameter without updating the model's
  calibration note. The run is still executable, but the evidence status becomes ambiguous.
- **Verification theater.** A case is marked pass without a test path or an observed result.
  The strict schema rejects the missing fields; it cannot detect a false claim.
- **Unit mismatch.** A state variable says request while the dynamics equation uses a rate.
  The unit fields make the mismatch visible but do not compute dimensional analysis.
- **Calibration laundering.** An assumed value is copied into a measured field. The source
  and measurement requirements make this harder but not impossible.

The contract is a guardrail, not a reviewer.

## Evidence ledger

- [Sargent, WSC 2011](https://informs-sim.org/wsc11papers/016.pdf)
  supports the separation of verification, data validity and conceptual validity.
  It does not validate any V12 model.
- MIT ESD.00 lectures 2-4 (source src.mit-esd-system-dynamics; see the reading ledger)
  support stock, flow and integration vocabulary.
  They do not establish the model's parameters.

## Navigation

- Parent: [V12/C02 - Contracts](../README.md)
- Next: [Scenario specification contract](scenario-specification.md)
- Schema:
  [model-specification.v1.schema.json](../../../../schemas/v12/model-specification.v1.schema.json)
