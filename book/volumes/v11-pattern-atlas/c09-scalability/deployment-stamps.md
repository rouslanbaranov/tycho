---
metadata_version: 1
id: "tycho.page.30d7c7363ec26491f644977876c16ea4"
kind: "page"
parent_id: "tycho.chapter.3b9ec227ed58b92c0004eb0d39099142"
canonical_path: "book/volumes/v11-pattern-atlas/c09-scalability/deployment-stamps.md"
title: "Deployment Stamps"
topic_ids:
  - "scaling-mechanisms"
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: >-
  Decision card for Deployment Stamps; invariant and alternative bound;
  coverage remains partial-bounded, no promotion.
route_hints:
  questions:
    - >-
      Should independent deployment units be replicated as stamps for scale,
      isolation or locality?
  prerequisites:
    - "tycho.chapter.3b9ec227ed58b92c0004eb0d39099142"
  related_ids:
    - "tycho.chapter.3b9ec227ed58b92c0004eb0d39099142"
  excludes:
    - >-
      No sufficient coverage, promotion or owner acceptance is claimed for this
      moved page.
  keywords:
    - "pattern atlas"
    - "deployment stamps"
    - "scalability"
evidence_scope:
  source_ids:
    - "src.microsoft-cloud-patterns"
    - "src.sre-workbook"
    - "src.cell-boundaries"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.batch5-deployment-stamps.2026-10-21,
    read.microsoft-deployment-stamps.2026-10-31,
    read.sre-workbook-canarying.2026-10-30 and
    read.batch7-cell-boundaries.2026-10-22; owner section and limits are
    bounded.
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-31"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-31"
updated_at: "2026-10-31"
source_inspection_date: "2026-10-31"
content_verified_at: null
---
# Deployment Stamps

**Identity.** Deployment Stamps; family Scalability and load distribution; kind
scalability-pattern; priority core.

**Decision question.** Should independent deployment units be replicated as stamps for
scale, isolation or locality?

**Good-fit conditions.** Each stamp can be operated and upgraded independently; a routing
key and a state authority are explicit; shared global dependencies are enumerated
and owned; duplication cost is acceptable.

**Hard contraindications.** Reject when one deployment suffices, when stamps would share a
hidden global dependency, or when routing, state, upgrade or tested rollback is unowned.

**Competing alternative.** Cell-based architecture when fault isolation is the primary
goal, or one shared deployment when isolation does not justify duplication. AWS describes
cells this way: "Each cell is independent, does not share state with other cells, and
handles a subset of the overall workload requests." A cell routing layer "distributes
requests to individual cells based on the partition key". AWS also says that "Building a
cell-based architecture doesn't necessarily mean having to double, triple, or more your
application's infrastructure"; Tycho reads that as making scale secondary to isolation.
Reverse the choice when stamp operations and duplication exceed the isolation benefit; the
isolation-first comparison and reversal condition are Tycho's.

**Failure and recovery.** Configuration drift, split state and shared dependencies may
occur; verify routing, state reconciliation and upgrade ownership in the owner section.

**Technical owner.** [Deployment Stamps](../../v08-delivery-deployment-and-recovery/c06-high-availability-and-failure-domain-placement/cells-shuffle-sharding.md#deployment-stamps) — independent deployment units for scale, isolation or locality, with routing keys, state authority and upgrade ownership.

**Sources.**
[src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
record read.microsoft-deployment-stamps.2026-10-31 (superseding retained
read.batch5-deployment-stamps.2026-10-21), canonical text revision `e6659312...`, raw HTML
`429616c390132dc77dcd6432addf59f29c57dd156d946d54424faf71dfedf668`; [src.sre-workbook] record
read.sre-workbook-canarying.2026-10-30; [src.cell-boundaries] record
read.batch7-cell-boundaries.2026-10-22. The units are public documentation,
not benchmarks.

**Decision state.** applicable-under-conditions.

**Related entries.** Cell-Based Architecture; Geode; Tenant Isolation; Multi-Region.
