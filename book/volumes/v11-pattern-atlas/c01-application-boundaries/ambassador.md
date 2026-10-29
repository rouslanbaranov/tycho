---
metadata_version: 1
id: "tycho.page.0465c87ed370438db997a1fcfcbe54cd"
kind: "page"
parent_id: "tycho.chapter.e996607f707421ca388796732547cafd"
canonical_path: "book/volumes/v11-pattern-atlas/c01-application-boundaries/ambassador.md"
title: "Ambassador"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
summary: "Decision card for Ambassador; bounded owner evidence and limits."
route_hints:
  questions:
    - "Should client connectivity be offloaded to a colocated out-of-process proxy?"
  prerequisites:
    - "tycho.chapter.e996607f707421ca388796732547cafd"
  related_ids:
    - "tycho.chapter.e996607f707421ca388796732547cafd"
  excludes:
    - "provider-specific proxy implementations"
  keywords:
    - "pattern atlas"
    - "ambassador"
evidence_scope:
  source_ids:
    - "src.microsoft-cloud-patterns"
  claim_ids: []
  status: "source-linked"
  notes: "Moved card page; source binding remains in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-29"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-28"
updated_at: "2026-10-29"
source_inspection_date: "2026-10-21"
content_verified_at: null
---

# Ambassador

**Identity.** Ambassador; family Application architecture and boundaries; kind
deployment-pattern; priority advanced.

**Decision question.** Should client connectivity be offloaded to a colocated out-of-process proxy?

**Good-fit conditions.** Many languages need common connectivity; a legacy application is hard to
modify; monitoring or resilience belongs outside the client.

**Hard contraindications.** Reject ambassador-managed retries on non-idempotent
operations; other offload uses remain viable. Reject when proxy latency outweighs
offloading.

**Competing alternative.** A client library invoked directly by the application when proxy overhead
outweighs offloading.

**Failure and recovery.** Ambassador-managed retries might not be safe unless all
operations are idempotent; other offload uses remain viable.

**Technical owner.** [Static stability and colocated helpers](../../v08-delivery-deployment-and-recovery/c03-vms-containers-orchestration-and-serverless/static-stability.md#ambassador) — bounded to the client-side proxy pattern.

**Sources.** [src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microsoft-ambassador.2026-10-21: Ambassador pattern page.
The source is public documentation, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Sidecar; Gateway Routing; Service Mesh; Retry with Jitter.
