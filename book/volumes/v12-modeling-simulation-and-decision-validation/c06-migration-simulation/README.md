---
metadata_version: 1
id: "tycho.chapter.26ddd5ca6c1bea39738561c3bdb1cf23"
kind: "chapter"
parent_id: "tycho.volume.fd0c1a798f9968eed4a679b048deea14"
canonical_path: "book/volumes/v12-modeling-simulation-and-decision-validation/c06-migration-simulation/README.md"
title: "V12/C06 - Modernization-path simulation"
topic_ids:
  - "simulation"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which coexistence, reconciliation and rollback conditions must be exposed?"
route_hints:
  questions:
    - "Which coexistence, reconciliation and rollback conditions must be exposed?"
  prerequisites: []
  related_ids:
    - "tycho.page.ea00bb677b242deed4a1ff3fa91f948a"
    - "tycho.page.7732cad079d3148dd26b24cc1fdef318"
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

# V12/C06 - Modernization-path simulation

**Status:** self-checked chapter landing, 2026-10-29. The modernization model is synthetic;
no migration was performed.

## Purpose and mission

A modernization decision is not a single cutover date. It is a path through coexistence,
traffic shift, reconciliation and rollback. This chapter models that path with explicit
stage schedules, dual-write lag, reconciliation capacity and divergence.

The chapter answers which coexistence, reconciliation and rollback conditions must be
exposed. It does not claim that a staged cutover is safe or that a rollback will succeed.

## Pages and reasoning route

- [Coexistence and rollback](coexistence-and-rollback.md): parallel run, dual write,
  reconciliation backlog and rollback drain.
- [Modernization-path experiment](modernization-path-experiment.md): the staged scenario,
  the no-cutover baseline and the observed results.

Read the coexistence page for the model semantics. Read the experiment page for the
comparison and the reason the decision record returns insufficient evidence.

## Diagram

~~~mermaid
stateDiagram-v2
    [*] --> Legacy
    Legacy --> DualWrite: stage 1
    DualWrite --> Shadow: stage 2
    Shadow --> Cutover: stage 3
    Cutover --> Rollback: divergence trigger
    Rollback --> Legacy: drain complete
    Cutover --> [*]: accepted
~~~

Text alternative: the path moves from legacy to dual write, shadow and cutover. A divergence
trigger moves cutover to rollback, and rollback returns to legacy only after the drain
completes.

## Boundaries and evidence

Sargent supports the requirement to state data validity, conceptual validity and
operational validity separately. The modernization model uses assumed dual-write lag and
reconciliation capacity; the decision record treats those assumptions as a reason for
insufficient evidence.

The chapter does not model record-level reconciliation, schema compatibility, deployment
orchestration or business continuity ownership.

## Navigation and prerequisites

- Previous: [V12/C05 - Decision integration](../c05-decision-integration/README.md)
- Next: [V12/C07 - Validation and limits](../c07-validation-and-limits/README.md)
- Modernization run:
  [modernization-staged.json](../../../../edition/v12/runs/modernization-staged.json)
