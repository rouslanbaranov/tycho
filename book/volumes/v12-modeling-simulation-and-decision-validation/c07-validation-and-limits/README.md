---
metadata_version: 1
id: "tycho.chapter.77831d9a57067de6faa1da630a83f49b"
kind: "chapter"
parent_id: "tycho.volume.fd0c1a798f9968eed4a679b048deea14"
canonical_path: "book/volumes/v12-modeling-simulation-and-decision-validation/c07-validation-and-limits/README.md"
title: "V12/C07 - Validation, reproducibility and limits"
topic_ids:
  - "simulation"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which verification, calibration and decision claims are supported?"
route_hints:
  questions:
    - "Which verification, calibration and decision claims are supported?"
  prerequisites: []
  related_ids:
    - "tycho.page.621e495fcadc4849d2f21d55be4c52e4"
    - "tycho.page.b0c704c825b2faf15a1d118dc9a6b1cc"
    - "tycho.page.6fd0d561e3e2900dc8b59a3011071cd2"
    - "tycho.page.6c54ed1288a4f0806889865916dc8ccf"
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

# V12/C07 - Validation, reproducibility and limits

**Status:** self-checked chapter landing, 2026-10-29. The validation gates are recorded
locally; independent review remains a separate gate.

## Purpose and mission

This chapter states what V12 actually verifies and what it does not. It separates model
verification, calibration, simulation evidence and decision validity, records the gate
matrix, and explains how a stored run is replayed.

The chapter answers which verification, calibration and decision claims are supported. It
does not claim production validity, security, compliance or migration safety.

## Pages and reasoning route

- [Model verification](model-verification.md): units, conservation, boundary cases, event
  ordering and deterministic reference cases.
- [Calibration and validity limits](calibration-and-validity-limits.md): measured, assumed,
  derived and unknown inputs.
- [V12 validation gates](validation-gates.md): the V12-A to V12-F matrix and evidence.
- [Reproducibility and replay](reproducibility-and-replay.md): hashes, seeds, environment
  and replay limits.

Read verification before calibration. Read calibration before a decision record. Read the
gate matrix before claiming the volume is complete. Read the replay page before sharing a
result hash.

## Diagram

~~~mermaid
flowchart LR
    A["V12-A Structure"] --> B["V12-B Model correctness"]
    B --> C["V12-C Statistical validity"]
    C --> D["V12-D Calibration"]
    D --> E["V12-E Decision validity"]
    E --> F["V12-F Independent review"]
~~~

Text alternative: structural checks precede model-correctness checks, statistical validity,
calibration, decision validity and independent review. A later gate cannot substitute for an
earlier one.

## Boundaries and evidence

Sargent supports the verification and validation distinction and the data/conceptual/
operational validity split. JCGM 100 supports uncertainty vocabulary. PLOS supports
reproducibility practices. PROV-O informs provenance vocabulary. None of those sources
validates a V12 model or decision.

The chapter does not claim CI execution, deployment acceptance, owner acceptance or pattern
promotion.

## Navigation and prerequisites

- Previous: [V12/C06 - Migration simulation](../c06-migration-simulation/README.md)
- Parent: [V12 - Architecture modeling and decision validation](../README.md)
- Validator: [scripts/validate_v12.py](../../../../scripts/validate_v12.py)
