---
metadata_version: 1
id: "tycho.page.8158481f0f2443e6bfaf00d85f0a6999"
kind: "page"
parent_id: "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
canonical_path: "book/volumes/v11-pattern-atlas/c10-deployment-modernization/dark-launching.md"
title: "Dark Launching / Shadow Traffic"
topic_ids:
  - "deployment-architecture"
  - "software-delivery"
perspectives:
  - "architecture"
  - "migration"
summary: "Decision card for Dark Launching; bounded owner evidence and limits."
route_hints:
  questions:
    - "Should new code receive shadow traffic before it is authoritative?"
  prerequisites:
    - "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
  related_ids:
    - "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
  excludes:
    - "provider-specific mirroring implementations"
  keywords:
    - "pattern atlas"
    - "dark-launching"
evidence_scope:
  source_ids:
    - "src.istio-traffic-mirroring"
    - "src.fowler-dark-launching"
  claim_ids: []
  status: "source-linked"
  notes: "Moved card page; source binding remains in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-28"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-28"
updated_at: "2026-10-28"
source_inspection_date: "2026-10-26"
content_verified_at: null
---

# Dark Launching / Shadow Traffic

**Identity.** Dark Launching / Shadow Traffic; family Deployment and legacy modernization;
kind modernization-pattern; priority advanced.

**Decision question.** Should new code receive real or shadow traffic before it is
authoritative?

**Good-fit conditions.** Traffic can be mirrored to a shadow service; responses are discarded;
the old path remains authoritative.

**Hard contraindications.** Reject when shadow requests cause writes, when traffic cannot
be mirrored safely, or when load cost is prohibitive.

**Competing alternative.** Canary release when the decision depends on a user choice.

**Failure and recovery.** A worrying performance impact can be switched off with a feature
flag before users notice.

**Technical owner.** [Dark Launching-Shadow Traffic](../../v08-delivery-deployment-and-recovery/c04-gitops-rollout-and-progressive-delivery/dark-launching-shadow-traffic.md#dark-launching-shadow-traffic) — dark launch/shadow traffic is bounded to progressive exposure.

**Sources.** [src.fowler-dark-launching](../../../../edition/patterns/reading-ledger.v1.json)
read record read.fowler-dark-launching.2026-10-26: section "Dark Launching".
[src.istio-traffic-mirroring](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch7-istio-mirroring.2026-10-26: sections "Mirroring", "Before you begin",
"Creating a default routing policy", "Mirroring traffic to httpbin-v2", "Cleaning up",
"See also". The first supports hidden invocation, load assessment, feature-flag rollback and
old/new comparison; the second supports request mirroring, fire-and-forget responses and fractional
mirroring. Measurement method, side-effect
suppression and capacity bounds are synthetic. The sources are public
articles/documentation, not benchmarks.

**Decision state.** applicable-under-conditions.

**Related entries.** Canary Release; Parallel Run; Feature Flags; Strangler Fig.
