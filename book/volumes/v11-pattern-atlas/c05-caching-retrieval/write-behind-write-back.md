---
metadata_version: 1
id: tycho.page.fe3f955b38dd07f80d34987f70a37d4e
kind: page
parent_id: tycho.chapter.87e52392e206a451ea5c79a4194c384b
canonical_path: book/volumes/v11-pattern-atlas/c05-caching-retrieval/write-behind-write-back.md
title: Write-Behind / Write-Back
topic_ids:
- caching
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Write-Behind / Write-Back.
route_hints:
  questions:
  - Should writes land in the cache first and reach the store asynchronously?
  prerequisites:
  - tycho.chapter.87e52392e206a451ea5c79a4194c384b
  related_ids:
  - tycho.chapter.87e52392e206a451ea5c79a4194c384b
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - write behind write back
evidence_scope:
  source_ids:
  - src.microsoft-caching-guidance
  claim_ids: []
  status: source-linked
  notes: Source-level bindings remain in the owner unit.
content_review:
  status: self-checked
  reviewed_at: '2026-11-01'
  reviewer: Automated authoring agent
  proof_uri: null
authored_at: '2026-11-01'
updated_at: '2026-11-01'
source_inspection_date: '2026-10-21'
content_verified_at: null
---

# Write-Behind / Write-Back

**Identity.** Write-Behind / Write-Back; family Caching and retrieval; kind
caching-pattern; priority advanced.

**Decision question.** Should writes land in the cache first and reach the store
asynchronously?

**Good-fit conditions.** The cache can durably buffer writes; loss tolerance is explicit;
ordering and retry are owned; the store can catch up.

**Hard contraindications.** Reject when a cache loss would lose accepted writes, when
ordering is mandatory, or when no reconciliation path exists.

**Competing alternative.** Write-through or direct store writes. Reverse the choice when
durability and replay complexity exceed latency benefit.

**Failure and recovery.** Cache loss and reordering are common; verify durability in the
owner section.

**Technical owner.**
 [Local and distributed caching: authority, freshness and
placement](../../v06-caching-indexing-and-retrieval/c01-local-and-distributed-caching/local-and-distributed-cache-design.md#write-behind-write-back)
— write-behind durability and ordering are bounded; flush retry policy is page-specific.

**Sources.**
[src.microsoft-caching-guidance](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-ms-caching.2026-10-21: sections "Caching in distributed
applications", "Manage concurrency in a cache". The record covers caching write consistency
generally, not write-behind buffering or durability; that mechanism is synthetic owner guidance.
The source is a public pattern/documentation unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Write-Through; Write-Around; Distributed Cache; Transactional Outbox.
