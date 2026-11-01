---
metadata_version: 1
id: "tycho.page.1041c9d24f1b41e69e41f4089dcb6b54"
kind: "page"
parent_id: "tycho.chapter.bee261b76181706235dd8fa7ccde01a9"
canonical_path: "book/volumes/v11-pattern-atlas/c08-coordination/fencing-tokens.md"
title: "Fencing Tokens"
topic_ids:
  - "distributed-systems"
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for Fencing Tokens; bounded owner evidence and explicit limits."
route_hints:
  questions:
    - "Should every write carry an epoch/token so the destination rejects a stale owner?"
  prerequisites:
    - "tycho.chapter.bee261b76181706235dd8fa7ccde01a9"
  related_ids:
    - "tycho.chapter.bee261b76181706235dd8fa7ccde01a9"
  excludes:
    - >-
      Bounded owner section; no new review, benchmark or owner acceptance is
      claimed for the moved page.
  keywords:
    - "pattern atlas"
    - "fencing tokens"
    - "distributed coordination"
evidence_scope:
  source_ids:
    - "src.kleppmann-distributed-locking"
  claim_ids: []
  status: "source-linked"
  notes: "Card cites read.batch4-fencing.2026-10-21; owner section and limits are bounded."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-21"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-21"
updated_at: "2026-10-30"
source_inspection_date: "2026-10-21"
content_verified_at: null
---
# Fencing Tokens

**Identity.** Fencing Tokens; family Distributed coordination; kind coordination-pattern;
priority core.

**Decision question.** Should every write carry an epoch/token so the destination rejects
a stale owner?

**Good-fit conditions.** The destination can compare and persist tokens; each new ownership
epoch carries a strictly greater token; stale owners may still run but cannot commit.

**Hard contraindications.** Reject when the resource cannot enforce tokens, when token values
can be reused, or when the lock is only an efficiency optimization.

**Competing alternative.** A best-effort single-node lock is sufficient when duplicate work is
only an efficiency cost; use fencing when a stale write could corrupt state.

**Failure and recovery.** A paused former owner is rejected when it resumes only where the
destination checks and persists the token; non-monotonic issuance defeats that rejection. If the
destination cannot enforce tokens, use an authoritative effect owner or an idempotent operation
identity.

**Technical owner.** [Fencing Tokens](../../v04-distributed-coordination-and-events/c02-replication-consensus-and-leader-changes/leader-recovery.md#fencing-tokens) — destination fencing is bounded, not a universal token protocol.

**Sources.**
[src.kleppmann-distributed-locking](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-fencing.2026-10-21: all nine served headings read.
The Conclusion recommends a best-effort single-node lock for efficiency-only
work, and a consensus system with fencing tokens enforced on every access when
correctness matters. The source is a public article, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Distributed Lock; Lease-Based Ownership; Leader Election; Idempotent
Receiver.
