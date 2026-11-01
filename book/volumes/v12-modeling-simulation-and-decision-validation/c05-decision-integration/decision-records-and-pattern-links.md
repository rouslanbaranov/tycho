---
metadata_version: 1
id: "tycho.page.b8e3757528ca1f60a472a6fd9deb7489"
kind: "page"
parent_id: "tycho.chapter.2147ec1471d027ef256437a345f9c1e7"
canonical_path: "book/volumes/v12-modeling-simulation-and-decision-validation/c05-decision-integration/decision-records-and-pattern-links.md"
title: "Decision records and pattern links"
topic_ids:
  - "decision-records"
  - "provenance"
perspectives:
  - "architecture"
  - "evaluation"
summary: "One-way links to existing patterns and a derived reverse index without write-back."
route_hints:
  questions:
    - "How does V12 link to existing patterns without editing them?"
    - "What does a pattern link not mean?"
  prerequisites: []
  related_ids:
    - "tycho.page.c7a43944f1d41e810eec0d17ec33b85a"
    - "tycho.page.3cfd08ee56330be9b7a2d37975c3fe26"
    - "tycho.page.ea9adae8cf8a3196a3515d383b075f53"
  excludes:
    - "No measurement, independent review, owner acceptance or pattern promotion is asserted."
  keywords:
    - "pattern link"
    - "reverse index"
    - "iron rule"
    - "promotion"
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

# Decision records and pattern links

**Question.** How can a V12 decision record point to existing patterns without editing their
cards, owner pages or evidence records?

**Short answer.** V12 links one way to stable tycho.pattern.* identifiers and canonical owner
pages. A derived reverse index maps pattern identifiers to V12 models, scenarios, runs and
decisions. No reverse link is written into an existing card or page.

## The iron rule

The binding rule for this volume is:

> V12 references existing patterns. Existing patterns do not reference V12.

The rule protects the evidence layer. Only a sufficient, promotion-bound card or owner page
has a promotion hash; all entries retain their source ledgers and review records. Adding a V12
backlink would change a canonical file, stale review and source records, and can invalidate a
promotion where one exists. The protection is not a matter of style; it is a requirement for
keeping existing evidence reproducible.

V12 therefore uses:

- a stable tycho.pattern.* identifier in the decision record;
- a canonical owner document identifier and path;
- a one-way Markdown link from the V12 page or prose;
- a derived reverse index for discovery.

## What a pattern link contains

Each candidate in a decision record can carry:

- pattern_id: the existing stable identifier, for example
  tycho.pattern.queue-based-load-leveling;
- owner_document_id: the existing page or chapter identifier;
- owner_page: the canonical path;
- relation: candidate, constraint, mechanism or reversal-trigger.

The relation is a V12 statement about why the pattern is relevant. It is not a change to the
pattern's coverage, review or promotion state.

## The derived reverse index

The reverse index is generated from V12 records, not maintained by hand. It maps:

    pattern_id -> [model, scenario, run, decision]

A reader or tool that consults the reverse index by pattern_id can find V12 artifacts that
mention it; pattern pages themselves do not link back. A reader who starts from a V12 decision
can follow the owner page to the technical explanation. The index is
regenerated when V12 records change; the existing pattern corpus is read-only.

The index is not a graph of semantic relationships. It is a lookup table with provenance. A
co-occurrence does not prove that the pattern causes the result or that the decision
validates the pattern.

## The candidate mapping

The checkout decision links three candidates:

- A: timeout and load shedding;
- B: bounded queue, retry with exponential backoff and bulkhead;
- C: horizontal scaling and bulkhead.

The owner pages are in V02 and V07. The decision record references them; those pages do not
reference V12. The candidate mapping is a reading route, not a claim that the pattern
caused the simulated metric.

The modernization decision links parallel run, controlled cutover and strangler fig. All three
are existing patterns with owner pages in V10. The decision record uses them to
explain coexistence and rollback; it does not edit them.

## What a link does not mean

- It does not promote the pattern. Simulation evidence never promotes a pattern to
  sufficient.
- It does not re-review the pattern's source evidence. V12 does not raise or lower the
  pattern's coverage.
- It does not create a second canonical explanation of the pattern. The owner page remains
  canonical.
- It does not establish that the pattern is applicable in production. The decision record
  states the conditions and limits.

## A one-way link diagram

~~~mermaid
flowchart LR
    V["V12 decision record"] --> P["tycho.pattern.* identifier"]
    P --> O["Existing canonical owner page"]
    V --> R["V12 derived reverse index"]
    R --> V
~~~

Text alternative: a V12 decision record points to a pattern identifier and the existing owner
page. A derived reverse index points back to V12 artifacts for discovery. The owner page has
no write-back edge to V12.

## Failure modes

- **Backlink contamination.** A V12 link is added to an existing card. The card hash changes
  and a promotion becomes stale.
- **Duplicate owner.** A V12 page explains the pattern mechanism in full and becomes a second
  canonical source.
- **Promotion by mention.** A reader treats a pattern link in a decision record as a
  promotion.
- **Manual reverse map.** The reverse index is edited by hand and drifts from the records.
- **Orphan link.** A pattern identifier or owner page does not exist in the registry.

The V12 validator resolves each linked pattern identifier in the edition-level registry and
checks the canonical triple: the owner document identifier and owner path must both match that
pattern's registry entry. A link to another pattern's valid owner page fails. It does not check
that the relation is semantically apt; that remains an editorial review.

## Evidence ledger

- [MADR](https://adr.github.io/madr/)
  supports context, options, outcome and consequences.
  It does not establish the pattern link's correctness.
- [Nygard, Documenting Architecture
  Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
  supports short, modular records.
  It does not establish a pattern's applicability.
- The edition-level pattern registry (edition/patterns/registry.v1.json), spanning V1-V11,
supplies the stable pattern
  identifiers and owner paths. It is read-only for this volume.

## Navigation

- Parent: [V12/C05 - Decision integration](../README.md)
- Next: [Comparative decision worked example](comparative-decision-worked-example.md)
- Reverse index: edition/v12/reverse-index.v1.json
