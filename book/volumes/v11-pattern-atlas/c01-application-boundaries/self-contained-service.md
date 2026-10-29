---
metadata_version: 1
id: "tycho.page.08f5561565b24db2a8dbc7dbdc63a1e6"
kind: "page"
parent_id: "tycho.chapter.e996607f707421ca388796732547cafd"
canonical_path: >-
  book/volumes/v11-pattern-atlas/c01-application-boundaries/self-contained-service.md
title: "Self-Contained Service"
topic_ids:
  - "application-architecture"
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for Self-Contained Service with bounded owner evidence."
route_hints:
  questions:
    - "Should a service respond to a synchronous request without waiting for another service?"
  prerequisites:
    - "tycho.chapter.e996607f707421ca388796732547cafd"
  related_ids:
    - "tycho.chapter.e996607f707421ca388796732547cafd"
  excludes:
    - "provider-specific replication and reconciliation implementations"
  keywords:
    - "pattern atlas"
    - "self-contained service"
    - "boundaries"
evidence_scope:
  source_ids:
    - "src.microservices-patterns"
  claim_ids: []
  status: "source-linked"
  notes: "Moved card page; source binding remains in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-29"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-29"
updated_at: "2026-10-29"
source_inspection_date: "2026-10-21"
content_verified_at: null
---

# Self-Contained Service

**Identity.** Self-Contained Service; family Application architecture and boundaries;
kind service-decomposition-pattern; priority advanced.

**Decision question.** Should a service respond to a synchronous request without waiting for another
service?

**Good-fit conditions.** Runtime availability coupling is material; the service can own a local read
model; asynchronous reconciliation is acceptable.

**Hard contraindications.** Reject when strong consistency is mandatory or data
cannot be replicated.

**Competing alternative.** Synchronous request/response or retry; retry increases response time and
synchronous calls reduce availability.

**Failure and recovery.** A local read replica plus asynchronous reconciliation
lets the service respond while a collaborator is unavailable; duplication,
reconciliation and staleness are the costs.

**Technical owner.** [Independent deployment and its costs](../../v02-application-boundaries-and-contracts/c04-soa-microservices-and-distributed-boundaries/service-independence.md#self-contained-service) — bounded to response independence.

**Sources.** [src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microservices-self-contained.2026-10-21: Self-contained service pattern page.
The source is public documentation, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** API Composition; Backend for Frontend; CQRS; Saga.
