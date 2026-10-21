---
metadata_version: 1
id: "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
kind: "volume"
parent_id: "tycho.book.37c50125355948f1b52ec66229ef59bd"
canonical_path: "book/volumes/v11-pattern-atlas/README.md"
title: "V11 — System Design pattern atlas"
topic_ids:
  - "system-design"
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
  - "operations"
summary: "Navigation layer over 145 entries: 144 self-checked cards, bounded owners; not accepted."
route_hints:
  questions:
    - "Which pattern fits a problem, and what reverses the choice?"
  prerequisites: []
  related_ids:
    - "tycho.chapter.e996607f707421ca388796732547cafd"
    - "tycho.chapter.9825cb82eb2142754c638aea1ba8d845"
    - "tycho.chapter.a4b31346a691566550633efe0cf2693e"
    - "tycho.chapter.e9c650012060143639af44b0cfdc4236"
    - "tycho.chapter.87e52392e206a451ea5c79a4194c384b"
    - "tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9"
    - "tycho.chapter.69085752a11c69305aa2a369b8ec9d29"
    - "tycho.chapter.bee261b76181706235dd8fa7ccde01a9"
    - "tycho.chapter.3b9ec227ed58b92c0004eb0d39099142"
    - "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
    - "tycho.chapter.419769c372ccaa569796954878e3bef9"
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
    - "tycho.book.37c50125355948f1b52ec66229ef59bd"
  excludes:
    - "No independent review, sufficient coverage or owner acceptance is asserted."
  keywords:
    - "pattern atlas"
    - "system design"
    - "applicability"
    - "contraindications"
    - "decision layer"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Navigation layer; chapter landings and cards carry source records. No volume-level claim."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-21"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-21"
updated_at: "2026-10-21"
source_inspection_date: null
content_verified_at: null
---
# V11 — System Design pattern atlas

**Status:** Phase 5 structural candidate, 2026-10-21. This volume is a navigation and
decision layer. It does not replace technical owners and does not establish technical
sufficiency.

## Purpose and mission

The atlas helps a reader move from a bounded problem to a conditional pattern choice. It
records applicability, contraindications, alternatives, failure and recovery questions,
candidate technical owners and exact source routes. The technical chapters remain
canonical for mechanism, guarantees and deep evidence.

Each of the 145 catalog entries has one stable heading in its family chapter. The 144
authored cards record applicability, contraindications, an alternative, failure and
recovery, a decision state, an exact owner link and a read source record. Polyglot
Persistence remains blocked and uncarded because no technical owner exists. Decision
coverage is partial-bounded for every card. Technical coverage remains partial or
partial-bounded; no entry is sufficient without independent review.

## How to use this volume

1. Start with the chapter that matches the decision family.
2. Read the card and its exact owner link; a bounded owner note is not a dedicated
  mechanism chapter.
3. Read the technical owner before trusting a mechanism claim.
4. Return to the atlas for alternatives, contraindications and reversal questions.
5. Record missing evidence as missing; do not score it as a pass.

```mermaid
flowchart LR
    Q["Bounded question"] --> A["V11 card"]
    A --> C["Conditions and contraindications"]
    A --> T["Technical owner"]
    A --> S["Exact public sources"]
```

Text alternative: a bounded question leads to one atlas card, which gives conditions,
points to the technical owner and routes to exact sources. The atlas does not replace
the technical owner.

## A worked cross-chapter synthesis

A fictional partner-facing service needs one request to assemble data from three owners,
enforce a per-client quota and keep a degraded but explicit response when one owner is
unavailable.

Use the atlas to turn that scenario into bounded questions: which ownership and contract
conditions hold, which alternatives compete, which failure mode is acceptable, and which
technical owner and exact source must be read before deciding.

The worked decision is not a recommendation for a real service. It is a synthetic route
that shows how the atlas, the technical owners and the source ledger must be read
together.

## Questions and chapters

- [V11/C01](c01-application-boundaries/README.md) — Application architecture and
  boundaries (12 entries).
- [V11/C02](c02-api-communication/README.md) — API and service communication (12
  entries).
- [V11/C03](c03-messaging-integration/README.md) — Messaging and event-driven integration
  (20 entries).
- [V11/C04](c04-consistency-events/README.md) — Data consistency, transactions and event
  sourcing (14 entries).
- [V11/C05](c05-caching-retrieval/README.md) — Caching and retrieval (14 entries).
- [V11/C06](c06-database-storage/README.md) — Database and storage architecture (13
  entries).
- [V11/C07](c07-resilience/README.md) — Resilience and fault tolerance (16 entries).
- [V11/C08](c08-coordination/README.md) — Distributed coordination (9 entries).
- [V11/C09](c09-scalability/README.md) — Scalability and load distribution (10 entries).
- [V11/C10](c10-deployment-modernization/README.md) — Deployment and legacy modernization
  (12 entries).
- [V11/C11](c11-security-operations/README.md) — Security, isolation and operational
  architecture (13 entries).

The chapter list is a route, not a fixed page quota. A chapter may need one page or many;
the split follows content and ownership.

## Counterexample and handoff

Naming a pattern does not establish fit: a hot single-writer workload can make a sharded
or event-driven design worse, and a passing link check is not technical evidence.

Handoff: when a decision needs a mechanism guarantee, leave the atlas and read the named
technical owner. If no owner is confirmed, record the gap instead of inventing one.

## Evidence and known limits

- 144 of 145 entries have self-checked cards with exact owner links and read source
  records; Polyglot Persistence is blocked and uncarded.
- Technical coverage is 96 partial-bounded and 48 partial on 65 owner pages; no entry is
  sufficient. Decision coverage is partial-bounded for all 144 cards.
- The owner-unit audit records 118 section-level units on those pages. Thirty shared pages
  have 14 keep, 13 deepen and 3 split decisions; the three splits are deferred with
  migration gates and no split was performed.
- The 40 related labels outside the catalog are recorded as deliberate non-routes, and
  the three catalog-index reads are marked intentionally unused. The semantic audit of
  all 419 pages remains open in
  [#288](https://github.com/rouslanbaranov/tycho/issues/288).
- No independent technical or editorial review and no owner acceptance exist. No
  release, deployment, hosted retrieval or CI result is claimed.
- The registry, owner-unit evidence, delivery evidence and audit record are the
  machine-readable sources for these counts.

## Navigation and prerequisites

- Parent: [Tycho book contents](../../README.md).
- Previous volume: [V10](../v10-decision-support-and-modernization/README.md) — decision support.
- First chapter: [V11/C01](c01-application-boundaries/README.md).
- Existing applicability owner: V10/C03 — pattern applicability and contraindications.
- Registry: [pattern registry](../../../edition/patterns/registry.v1.json).
- Coverage map: [candidate coverage](../../../edition/patterns/coverage-map.v1.json).
- Owner units: [section-level ownership](../../../edition/patterns/owner-units.v1.json).
- Delivery evidence: [Phase 5 evidence](../../../edition/patterns/delivery-evidence.v1.json).
- Owner-unit audit: [audit record](../../../authoring/PATTERN-OWNER-UNIT-AUDIT_2026-10-21.md).
- Contract: [pattern atlas contract](../../../authoring/PATTERN-ATLAS-CONTRACT.md).
- Next task: [E17-29 semantic page audit](https://github.com/rouslanbaranov/tycho/issues/288).
