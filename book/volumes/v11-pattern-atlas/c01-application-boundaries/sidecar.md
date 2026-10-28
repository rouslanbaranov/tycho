---
metadata_version: 1
id: "tycho.page.755a7467ba4ec16c2f288b69dd8be7ee"
kind: "page"
parent_id: "tycho.chapter.e996607f707421ca388796732547cafd"
canonical_path: "book/volumes/v11-pattern-atlas/c01-application-boundaries/sidecar.md"
title: "Sidecar"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
summary: "Decision card for Sidecar; bounded owner evidence and explicit limits."
route_hints:
  questions:
    - "Should auxiliary runtime behavior run in a colocated helper beside"
  prerequisites:
    - "tycho.chapter.e996607f707421ca388796732547cafd"
  related_ids:
    - "tycho.chapter.e996607f707421ca388796732547cafd"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed."
  keywords:
    - "pattern atlas"
    - "sidecar"
evidence_scope:
  source_ids:
    - "src.microsoft-cloud-patterns"
  claim_ids: []
  status: "source-linked"
  notes: "Moved card page; source binding remains in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-27"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-27"
updated_at: "2026-10-27"
source_inspection_date: "2026-10-21"
content_verified_at: null
---
# Sidecar

**Identity.** Sidecar; family Application architecture and boundaries; kind
deployment-pattern; priority core.

**Decision question.** Should auxiliary runtime behavior run in a colocated helper beside
the main workload rather than inside it?

**Good-fit conditions.** The helper is colocated with the application instance and shares
its lifecycle; the platform can schedule and manage it.

**Hard contraindications.** Reject when a language-specific library or traditional
extension's deeper integration and lower network overhead dominate the colocated-helper benefits.

**Competing alternative.** A language-specific library or traditional extension when
deeper integration and lower network overhead matter.

**Failure and recovery.** Startup and shutdown ordering between the application and
sidecar must avoid races.

**Technical owner.** [Sidecar](../../v08-delivery-deployment-and-recovery/c03-vms-containers-orchestration-and-serverless/static-stability.md#sidecar) — sidecar lifecycle, proxy data plane and coupling are bounded, not a service-mesh guide.

**Sources.**
[src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microsoft-sidecar.2026-10-21: sections "Sidecar pattern", "Context
and problem", "Solution", "Problems and considerations", "When to use this pattern",
"Workload design", "Example", "Next steps", "Related resource". This is a vendor
pattern page, not a comparative study.

**Related entries.** Ambassador; Service Mesh; Immutable Infrastructure.

**Decision state.** `applicable-under-conditions`.
