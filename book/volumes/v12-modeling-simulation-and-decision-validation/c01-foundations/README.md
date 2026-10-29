---
metadata_version: 1
id: "tycho.chapter.6006603befaacfc1baadc486a0f7007a"
kind: "chapter"
parent_id: "tycho.volume.fd0c1a798f9968eed4a679b048deea14"
canonical_path: "book/volumes/v12-modeling-simulation-and-decision-validation/c01-foundations/README.md"
title: "V12/C01 - Foundations of architecture modeling"
topic_ids:
  - "simulation"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which concepts and evidence vocabulary must precede a simulated decision?"
route_hints:
  questions:
    - "Which concepts and evidence vocabulary must precede a simulated decision?"
  prerequisites: []
  related_ids:
    - "tycho.page.870e64da1f925c52109a602440048603"
    - "tycho.page.d860bc57cdfe6c6163912819f7679d17"
    - "tycho.page.1a3833c3b4431428b25fa9896bcdd072"
  excludes:
    - "No production measurement, independent review or owner acceptance is asserted."
  keywords:
    - "simulation"
    - "architecture decision"
    - "model evidence"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Chapter landing; page-local sources carry the evidence."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-29"
  reviewer: "DeepSeek Harness authoring agent"
  proof_uri: null
authored_at: "2026-10-29"
updated_at: "2026-10-29"
source_inspection_date: null
content_verified_at: null
---

# V12/C01 - Foundations of architecture modeling

**Status:** self-checked chapter landing, 2026-10-29. The pages carry the detail and
source limits. No production measurement or independent review is asserted.

## Purpose and mission

This chapter establishes the conceptual minimum before a simulation can inform an
architecture decision: what a stock is, what a flow is, how a model boundary is chosen,
and how source evidence, verification, calibration, simulation evidence and decision
evidence differ. Without that vocabulary, a plausible diagram or a single run is easily
mistaken for evidence.

The chapter answers one bounded question: which concepts and evidence vocabulary must
precede a simulated decision? It does not teach a general systems-science curriculum and
does not claim that a stock-and-flow model predicts a real organization.

## Pages and reasoning route

- [Stock-and-flow modeling versus stock-to-flow shorthand](stock-and-flow-vs-stock-to-flow.md):
  accumulation, rates, units and the error of conflating a stock with a flow.
- [Model scope, boundary and abstraction](model-scope-and-abstraction.md): what to include,
  what to omit and how to state the validity domain.
- [Evidence and validation vocabulary](evidence-and-validation-vocabulary.md): the five
  layers and the labels that must never be conflated.

Read the stock-and-flow page first if the question is about accumulation or delay. Read
the scope page before choosing a model family. Read the vocabulary page before writing a
decision record.

## Diagram

~~~mermaid
flowchart LR
    Q["Architecture question"] --> B["Boundary and purpose"]
    B --> S["Stocks and flows"]
    B --> E["Event detail"]
    S --> M["Model contract"]
    E --> M
    M --> V["Verification"]
    V --> C["Calibration and validity limits"]
    C --> D["Decision evidence"]
~~~

Text alternative: an architecture question defines a boundary and purpose. The boundary
selects either stock-and-flow or event-level description, and both feed a model contract.
Verification, calibration and validity limits are separate stages before decision evidence.

## Boundaries and evidence

The chapter relies on public methodological sources: MIT OpenCourseWare lectures on system
dynamics for stock, flow and feedback vocabulary, and Sargent's verification and validation
paper for the validation distinctions. Those sources support method vocabulary, not any
V12 parameter or run. Exact units and omissions are recorded in the V12 reading ledger.

The chapter does not cover control theory, econometrics, system-identification algorithms or
the full system-dynamics literature. It does not claim that a conceptual diagram is a
calibrated model.

## Navigation and prerequisites

- Parent: [V12 - Architecture modeling and decision validation](../README.md)
- Next: [V12/C02 - Contracts](../c02-contracts/README.md)
- Source ledger: [V12 reading ledger](../../../../edition/v12/reading-ledger.v1.json)
