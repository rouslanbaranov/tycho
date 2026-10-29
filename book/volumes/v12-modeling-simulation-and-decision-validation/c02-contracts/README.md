---
metadata_version: 1
id: "tycho.chapter.3a47e8385cccb8a2ce764bfa765cc740"
kind: "chapter"
parent_id: "tycho.volume.fd0c1a798f9968eed4a679b048deea14"
canonical_path: "book/volumes/v12-modeling-simulation-and-decision-validation/c02-contracts/README.md"
title: "V12/C02 - Model, scenario, run and decision contracts"
topic_ids:
  - "simulation"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which contracts make a model, run and decision reviewable?"
route_hints:
  questions:
    - "Which contracts make a model, run and decision reviewable?"
  prerequisites: []
  related_ids:
    - "tycho.page.d8d9d15b402d8f65928ca0e3f3e5b939"
    - "tycho.page.dedc5f2d31912a9ba5f562a86009fda0"
    - "tycho.page.201248045fa3cd67e617ce04a1c56feb"
    - "tycho.page.c7a43944f1d41e810eec0d17ec33b85a"
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

# V12/C02 - Model, scenario, run and decision contracts

**Status:** self-checked chapter landing, 2026-10-29. The contracts are versioned JSON
objects with strict schemas; page prose explains their intent and limits.

## Purpose and mission

A simulation result is not reviewable if the model, workload, seed, engine and decision
context are scattered across prose. This chapter defines four contracts that make a V12
result reproducible and bounded:

- a **model specification** for state, parameters, invariants and verification;
- a **scenario specification** for workload, configuration, uncertainty and metrics;
- a **run and result provenance** record for hashes, seeds, convergence and limits;
- a **decision record** for candidates, hard constraints, evidence and reversal triggers.

The contracts are deliberately machine-readable and strict. A missing field is a
validation failure, not a note.

## Pages and reasoning route

- [Model specification contract](model-specification.md): state variables, units,
  parameters and evidence status.
- [Scenario specification contract](scenario-specification.md): identical workload rules,
  seeds, metrics and constraints.
- [Run and result provenance contract](run-and-result-provenance.md): hashes, replay and
  provenance vocabulary.
- [Decision record contract](decision-record.md): candidates, constraints and explicit
  insufficient-evidence outcomes.

Read the model contract before writing a scenario. Read the run contract before sharing a
number. Read the decision contract before turning a comparison into a recommendation.

## Diagram

~~~mermaid
flowchart LR
    M["Model spec"] --> S["Scenario spec"]
    S --> R["Run record"]
    R --> D["Decision record"]
    M --> H["Model hash"]
    S --> H
    R --> H2["Result hash"]
    D --> L["Pattern owner links, read-only"]
~~~

Text alternative: a model specification and scenario specification feed a run record. The
model and scenario hashes bind the run, and the run record feeds a decision record. The
decision links one way to existing pattern owners.

## Boundaries and evidence

The contracts are original V12 schemas. MADR and Nygard's decision-record article support
the context, options, outcome and consequences structure, but V12 uses a JSON-first form
and does not claim conformance. Sargent supports the separation of verification and
validation. PROV-O informs the provenance vocabulary; V12 claims inspiration, not
conformance.

The contracts do not replace source evidence, calibration, security review or owner
acceptance. They make those gaps visible.

## Navigation and prerequisites

- Previous: [V12/C01 - Foundations](../c01-foundations/README.md)
- Next: [V12/C03 - Deterministic and DES](../c03-deterministic-and-des/README.md)
- Model schema: schemas/v12/model-specification.v1.schema.json
