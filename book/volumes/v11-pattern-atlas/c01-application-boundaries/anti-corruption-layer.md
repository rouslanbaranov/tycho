---
metadata_version: 1
id: "tycho.page.849bdcae7fb65f6daa4d9db920961789"
kind: "page"
parent_id: "tycho.chapter.e996607f707421ca388796732547cafd"
canonical_path: "book/volumes/v11-pattern-atlas/c01-application-boundaries/anti-corruption-layer.md"
title: "Anti-Corruption Layer"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
summary: "Decision card for Anti-Corruption Layer; bounded owner evidence and explicit limits."
route_hints:
  questions:
    - "Should a boundary translate between a legacy or external model with different semantics?"
  prerequisites:
    - "tycho.chapter.e996607f707421ca388796732547cafd"
  related_ids:
    - "tycho.chapter.e996607f707421ca388796732547cafd"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed."
  keywords:
    - "pattern atlas"
    - "anti-corruption-layer"
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
# Anti-Corruption Layer

**Identity.** Anti-Corruption Layer; alias ACL, translation layer; family Application
architecture and boundaries; kind integration-pattern; priority core.

**Decision question.** Should a boundary translate between a legacy or external model with different semantics?

**Good-fit conditions.** The external model has different meanings or invariants; the
domain must remain independent of vendor or legacy types; coexistence is transitional;
the mapping and its errors can be owned and tested.

**Hard contraindications.** Reject the claim when the models already align; when the
layer adds no semantic translation; when latency or data duplication violates a hard
constraint; when the mapping has no owner; or when the ACL would become a second domain
model.

**Competing alternative.** No ACL when the new and legacy systems have no significant
semantic differences.

**Failure and recovery.** The ACL can become a single point of failure; use retry, circuit
breaker, bulkhead and health endpoint monitoring.

**Technical owner.** [Anti-Corruption Layer](../../v02-application-boundaries-and-contracts/c06-integration-adapters-and-anti-corruption-boundaries/anti-corruption-adapters-and-coexistence.md#anti-corruption-layer).

**Sources.**
[src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record `read.microsoft-acl.2026-10-21`: all nine served headings read. This is a
vendor pattern page, not a comparative study.

**Decision state.** `applicable-under-conditions`.

**Related entries.** Domain-Driven Design / Bounded Context; Hexagonal Architecture;
Strangler Fig; Adapter.
