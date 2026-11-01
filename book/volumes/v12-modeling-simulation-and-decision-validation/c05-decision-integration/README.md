---
metadata_version: 1
id: "tycho.chapter.2147ec1471d027ef256437a345f9c1e7"
kind: "chapter"
parent_id: "tycho.volume.fd0c1a798f9968eed4a679b048deea14"
canonical_path: "book/volumes/v12-modeling-simulation-and-decision-validation/c05-decision-integration/README.md"
title: "V12/C05 - Decision integration and pattern links"
topic_ids:
  - "simulation"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How does a simulation become a bounded decision without editing patterns?"
route_hints:
  questions:
    - "How does a simulation become a bounded decision without editing patterns?"
  prerequisites: []
  related_ids:
    - "tycho.page.b8e3757528ca1f60a472a6fd9deb7489"
    - "tycho.page.3cfd08ee56330be9b7a2d37975c3fe26"
    - "tycho.page.ea9adae8cf8a3196a3515d383b075f53"
  excludes:
    - "No measurement, independent review, owner acceptance or pattern promotion is asserted."
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

# V12/C05 - Decision integration and pattern links

**Status:** self-checked chapter landing, 2026-10-29. Decision records are present; owner
acceptance and pattern promotion are not.

## Purpose and mission

This chapter turns a simulation comparison into a bounded decision record. It links one way
to existing tycho.pattern.* identifiers and canonical owner pages, keeps hard constraints
separate from weighted preferences, and makes insufficient-evidence a first-class outcome.

The chapter answers how a simulation becomes a bounded decision without editing existing
patterns. It does not replace the technical owner of a pattern.

## Pages and reasoning route

- [Decision records and pattern links](decision-records-and-pattern-links.md): the one-way
  link rule and the derived reverse index.
- [Comparative decision worked example](comparative-decision-worked-example.md): the A/B/C
  checkout comparison with actual run values.
- [Insufficient-evidence outcomes](insufficient-evidence-outcomes.md): when no
  recommendation is the correct result.

Read the pattern-link page before adding a V12 reference. Read the worked example before
writing a decision record. Read the insufficient-evidence page before forcing a score.

## Diagram

~~~mermaid
flowchart LR
    R["Run evidence"] --> D["Decision record"]
    D --> C["Hard constraints"]
    D --> Q["Quantitative comparison"]
    D --> N["Non-quantitative limits"]
    D --> P["Existing pattern owner, read-only"]
    D --> I["Insufficient evidence"]
    D --> T["Reversal triggers"]
~~~

Text alternative: run evidence feeds a decision record. The record separates hard
constraints, quantitative comparison, non-quantitative limits, one-way pattern links, an
insufficient-evidence outcome and reversal triggers.

## Boundaries and evidence

The [decision-record contract](../c02-contracts/decision-record.md) cites MADR and Nygard for the
record structure. The validation chapter cites Sargent for separating verification from validity for
a purpose. This landing adds no source claim of its own. The pattern links use the
edition-level registry and owner pages without modifying them.

The chapter does not promote a pattern, claim owner acceptance or create a second canonical
explanation of a pattern.

## Navigation and prerequisites

- Previous: [V12/C04 - Monte Carlo](../c04-monte-carlo/README.md)
- Next: [V12/C06 - Migration simulation](../c06-migration-simulation/README.md)
- Decision: [checkout-candidate.json](../../../../edition/v12/decisions/checkout-candidate.json)
