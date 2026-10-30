---
metadata_version: 1
id: "tycho.page.93c4ffc9488f4e23904cb23ff519f516"
kind: "page"
parent_id: "tycho.chapter.e9c650012060143639af44b0cfdc4236"
canonical_path: "book/volumes/v11-pattern-atlas/c04-consistency-events/two-phase-commit-2pc.md"
title: "Two-Phase Commit (2PC)"
topic_ids:
  - "data-architecture"
  - "distributed-systems"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for Two-Phase Commit (2PC) with bounded owner evidence."
route_hints:
  questions:
    - "Should a distributed transaction use a prepare/commit protocol across resource managers?"
  prerequisites:
    - "tycho.chapter.e9c650012060143639af44b0cfdc4236"
  related_ids:
    - "tycho.chapter.e9c650012060143639af44b0cfdc4236"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "two-phase-commit-2pc"
    - "distributed transaction"
evidence_scope:
  source_ids:
    - "src.postgresql"
    - "src.oracle-distributed-transactions"
    - "src.microservices-patterns"
    - "src.microsoft-cloud-patterns"
  claim_ids: []
  status: "source-linked"
  notes: "Dedicated card page; source bindings remain in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-30"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-30"
updated_at: "2026-10-30"
source_inspection_date: "2026-10-30"
content_verified_at: null
---

# Two-Phase Commit (2PC)

**Identity.** Two-Phase Commit (2PC); family Data consistency, transactions and event
sourcing; kind transaction-pattern; priority advanced.

**Decision question.** Should a distributed transaction use a prepare/commit protocol
across resource managers?

**Good-fit conditions.** Participants support a prepare phase; the coordinator is highly
available; blocking and recovery are acceptable; the invariant spans resources.

**Hard contraindications.** Reject when participants cannot prepare, when coordinator
failure would block critical resources, or when compensation-based saga is sufficient.

**Competing alternative.** Saga/compensation or one local transaction. The public Saga pattern
says "2PC is not an option" in its context and replaces atomic commit with local transactions
and compensating actions, accepting visible intermediate states and non-atomic outcomes. Reverse
the choice when blocking and coordinator complexity exceed atomicity benefit.

**Failure and recovery.** A failure after prepare leaves the transaction in doubt while prepared
data stays locked; a commit-point log and an external transaction manager track the decision, and
resolution may be automatic or forced. Verify protocol limits in the owner section.

**Technical owner.** [Two-Phase Commit (2PC)](../../v04-distributed-coordination-and-events/c03-consistency-and-distributed-transactions/invariants-isolation.md#two-phase-commit-2pc) — local/global commit limits are bounded, not a 2PC protocol reference.

**Sources.**
[src.postgresql](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-pg-2pc.2026-10-21: §66.4, the single served heading.
[src.postgresql](../../../../edition/patterns/reading-ledger.v1.json)
read record read.pg-prepare-transaction.2026-10-30: Description and Notes.
[src.oracle-distributed-transactions](../../../../edition/patterns/reading-ledger.v1.json)
read record read.oracle-distributed-transactions.2026-10-30: Prepare Phase, Commit Phase and
In-Doubt Transactions.
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-saga.2026-10-21: Forces, Solution and Resulting context.
[src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microsoft-saga-azure.2026-10-30: Problems and considerations.
The sources are public documentation and a public pattern description, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Saga; Compensating Transaction; Transactional Outbox; Distributed
Transactions.
