---
metadata_version: 1
id: "tycho.page.b0c704c825b2faf15a1d118dc9a6b1cc"
kind: "page"
parent_id: "tycho.chapter.77831d9a57067de6faa1da630a83f49b"
canonical_path: "book/volumes/v12-modeling-simulation-and-decision-validation/c07-validation-and-limits/calibration-and-validity-limits.md"
title: "Calibration and validity limits"
topic_ids:
  - "calibration"
  - "model-validation"
perspectives:
  - "evaluation"
  - "architecture"
summary: "Every V12 model is uncalibrated; each input status and missing measurement is explicit."
route_hints:
  questions:
    - "Which inputs are measured, assumed, derived or unknown?"
    - "Which claims do those statuses forbid?"
  prerequisites: []
  related_ids:
    - "tycho.page.621e495fcadc4849d2f21d55be4c52e4"
    - "tycho.page.6fd0d561e3e2900dc8b59a3011071cd2"
    - "tycho.page.ea9adae8cf8a3196a3515d383b075f53"
  excludes:
    - "No production measurement, independent review or owner acceptance is asserted."
  keywords:
    - "calibration"
    - "validity limits"
    - "assumed"
    - "measured"
    - "unknown"
evidence_scope:
  source_ids:
    - "src.jcgm-100"
    - "src.sargent-vv"
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

# Calibration and validity limits

**Question.** Which V12 inputs are measured, assumed, derived or unknown, and what does each
status forbid us to claim?

**Short answer.** Every V12 model is uncalibrated. Arrival rates, service times, timeouts,
dual-write lag and reconciliation capacity are assumed. The valid claim is conditional: under
the declared inputs, the model produces the reported result. The invalid claim is that the
result describes a real system.

## The four statuses

- **Measured:** a named source and a measurement method, sample size and period.
- **Assumed:** a value chosen for the model, with no measurement claim.
- **Derived:** a value computed from other inputs by a stated formula.
- **Unknown:** no defensible value; the model must not invent one.

A parameter can change status only with new evidence. Repeating an assumed value in a
decision record does not make it measured. A derived value inherits the weakest status of its
inputs.

## The V12 input table

| Input | Status | What is missing |
|---|---|---|
| Arrival rate | assumed | A measured arrival trace for the target workload |
| Service mean | assumed | A measured service-time sample and tail |
| Service CV | assumed | A measured distribution, not a chosen shape |
| Servers | assumed | A measured deployment capacity |
| Queue capacity | assumed | A measured admission policy |
| Timeout | assumed | A measured client deadline and retry policy |
| Dual-write lag | assumed | A measured lag distribution |
| Reconciliation capacity | assumed | A measured throughput under target load |
| Divergence threshold | assumed | A business-defined data-quality threshold |

The table is the same in the model contracts. The decision records repeat the statuses in
their evidence blocks.

## JCGM 100 and uncertainty language

JCGM 100 describes a measurement result as a measured value plus an uncertainty, with a
coverage interval at a stated coverage probability. It distinguishes Type A and Type B
uncertainty components and shows how to combine them.

V12 uses the vocabulary but not the full method. A uniform range in a scenario is not a
Type A or Type B component. It is an assumed input range. A confidence interval across
replications is a sampling interval, not a metrological coverage interval. The page says so
to prevent a reader from treating a synthetic interval as a calibrated uncertainty budget.

## Validity limits

Each model records limits such as:

- valid only for the synthetic workload in a scenario;
- no individual latency in the stock-flow model;
- no dependency calls or storage in the checkout model;
- no record-level reconciliation in the modernization model;
- no production claim without measurement.

A validity limit is not a disclaimer appended to a result. It is a condition on the result's
use. If a decision needs the omitted mechanism, the model is outside its domain.

## What measurement would change

For the checkout comparison:

- an arrival trace from the target environment;
- a service-time sample, including the tail;
- a measured timeout and retry policy;
- a measured deployment capacity and cost.

For the modernization comparison:

- a measured dual-write lag distribution;
- a measured reconciliation throughput under target load;
- a rehearsed rollback duration;
- a measured divergence over a sustained period.

Until those exist, the decisions remain conditional or insufficient evidence. The model can
still rank what to measure first; it cannot substitute for the measurement.

## Failure modes

- **Assumed as measured.** A parameter is labeled measured because it has a number.
- **Precision without accuracy.** A value is reported to four decimals from a one-significant-
  figure assumption.
- **Extrapolation.** A model calibrated for one workload is used for a different one.
- **Uncertainty theater.** A confidence interval across replications is presented as an
  uncertainty budget for the input parameters.
- **Validity drift.** A model is reused after its boundary or mechanism changes.

## Evidence ledger

- JCGM 100:2008 (source src.jcgm-100; see the reading ledger)
  supports measurement result, uncertainty components and coverage vocabulary.
  It does not establish a V12 measurement.
- [Sargent, WSC 2011](https://informs-sim.org/wsc11papers/016.pdf)
  supports data validity and operational validity as separate concerns.
  It does not provide the missing data.

## Navigation

- Parent: [V12/C07 - Validation and limits](../README.md)
- Previous: [Model verification](model-verification.md)
- Next: [V12 validation gates](validation-gates.md)
- Calibration records: edition/v12/models/
