---
metadata_version: 1
id: "tycho.page.277dbc6a75e842ee9105dcc953ceb283"
kind: "page"
parent_id: "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
canonical_path: "book/volumes/v11-pattern-atlas/c10-deployment-modernization/strangler-fig.md"
title: "Strangler Fig"
topic_ids:
  - "deployment-architecture"
  - "software-delivery"
perspectives:
  - "architecture"
  - "migration"
summary: "Decision card for Strangler Fig; bounded owner evidence and explicit limits."
route_hints:
  questions:
    - >-
      Should a legacy capability be replaced incrementally behind a routing
      seam rather than by a rewrite?
  prerequisites:
    - "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
  related_ids:
    - "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "strangler fig"
    - "legacy modernization"
evidence_scope:
  source_ids:
    - "src.fowler-strangler"
    - "src.aws-strangler"
  claim_ids: []
  status: "source-linked"
  notes: "Moved card page; failure/recovery binding remains in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-29"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-29"
updated_at: "2026-10-29"
source_inspection_date: "2026-10-29"
content_verified_at: null
---

# Strangler Fig

**Identity.** Strangler Fig; family Deployment and legacy modernization; kind
modernization-pattern; priority core.

**Decision question.** Should a legacy capability be replaced incrementally behind a
routing seam rather than by a rewrite?

**Good-fit conditions.** A seam can intercept and route old/new; coexistence is funded;
routing and data compatibility are explicit; rollback is possible until a no-return point.

**Hard contraindications.** Reject when the legacy has no seam, when dual-running data
cannot be reconciled, or when the team cannot own two paths.

**Competing alternative.** Branch by abstraction, parallel run or a big-bang replacement.
Reverse the choice when coexistence cost exceeds incremental replacement benefit.

**Failure and recovery.** Interception may be impossible, callers may bypass the façade,
and old/new state can diverge. AWS Prescriptive Guidance states the conditions directly:

> Cannot be used in systems where requests to the backend system cannot be intercepted and
> routed. The proxy or facade layer can become a single point of failure or a performance
> bottleneck if it isn't designed properly. Requires a rollback plan for each refactored
> service to revert to the old way of doing things quickly and safely if things go wrong.

Detect bypass, hold and route back until proven; a bypass detector, routing inventory and
data reconciliation remain Tycho guidance. The page supports interception as a
prerequisite, façade single-point risk and a per-service rollback plan; it does not define
those checks or a no-return gate.

**Technical owner.** [Strangler Fig](../../v10-decision-support-and-modernization/c05-target-architecture-versus-transition-states/target-and-transition-architecture-states.md#strangler-fig) — strangler is bounded to transition-state reasoning.

**Sources.** [src.fowler-strangler](../../../../edition/patterns/reading-ledger.v1.json)
read record read.fowler-strangler.2026-10-21: sections "Strangler Fig", "Further Reading".
Failure and recovery also binds
[src.aws-strangler](../../../../edition/patterns/reading-ledger.v1.json) read record
read.aws-strangler.2026-10-29: sections "Strangler fig pattern", "Transform", "Coexist",
"Eliminate", "Advantages and disadvantages"; revision
`787962ad56fbc52feb9e3198749ceb7e3b9cea44bca6f9c2bb50530e30c66044`.
The page states the interception, façade-failure and rollback conditions; it does not
define bypass-detection, routing-reconciliation or no-return checks.
The sources are public documentation, not benchmarks.

**Decision state.** applicable-under-conditions.

**Related entries.** Branch by Abstraction; Parallel Run; Dark Launching; Controlled
Cutover.
