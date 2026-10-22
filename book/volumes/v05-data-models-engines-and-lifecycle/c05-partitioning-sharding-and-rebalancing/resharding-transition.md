---
metadata_version: 1
id: "tycho.page.94165346d83c4ff79634d4400f4a9ba7"
kind: "page"
parent_id: "tycho.chapter.3e2e1da8f99c4a7ba05121baf1ef4d91"
canonical_path: "book/volumes/v05-data-models-engines-and-lifecycle/c05-partitioning-sharding-and-rebalancing/resharding-transition.md"
title: "Resharding and alternatives"
topic_ids:
  - "scaling-mechanisms"
perspectives:
  - "architecture"
summary: "How can ownership move without accepting conflicting writes or unnecessary distribution?"
route_hints:
  questions:
    - "How can ownership move without accepting conflicting writes or unnecessary distribution?"
  prerequisites:
    - "tycho.page.3b048fab91c24b9f8121564b9b0e59bb"
  related_ids:
    - "tycho.chapter.3e2e1da8f99c4a7ba05121baf1ef4d91"
    - "tycho.page.0d34dd26886340b89fd4f1499d790a81"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "resharding"
    - "transition"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.0d34dd26886340b89fd4f1499d790a81; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
# Resharding and alternatives

**Owning question:** How can ownership move without accepting conflicting writes or unnecessary distribution?

This page belongs to [V05/C05 — Partitioning, sharding and rebalancing](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.0d34dd26886340b89fd4f1499d790a81:4 -->
## 4. Resharding is a multi-state data transition

A correct target topology is insufficient: clients, source stores, replica/backfill state, transaction changes and destination ownership must remain consistent **during** migration.

```mermaid
stateDiagram-v2
    [*] --> Existing
    Existing --> Prepare: Version target routing and compatibility
    Prepare --> Copy: Copy historical data to target ownership
    Copy --> CatchUp: Replay ongoing committed changes
    CatchUp --> Verify: Compare counts, identities and invariant state
    Verify --> Switch: Freeze/route/fence source writes and cut over
    Verify --> Repair: Divergence detected
    Repair --> CatchUp: Correct and revalidate
    Switch --> Observe: Route requests, compare errors and lag
    Observe --> Final: Retirement after rollback window
    Observe --> Repair: Unexpected issue; assess forward repair
    Final --> [*]
```

Text alternative: prepare compatible routing, copy source data, catch up in-flight changes, verify exact business invariants, fence conflicting writers and switch ownership before retiring old storage. If a mismatch is found, reconcile rather than declaring success. This is a **synthetic safe-transition outline**, not a real Vitess command sequence.

The current Vitess 24.0 resharding guide includes an online workflow and staged cutover, but its described behavior depends on exact source/target configuration. It must not be copied as a generic, zero-downtime promise for any datastore. [E01]

### Migration validation checklist

1. Identify shard authority and data ownership for each key; record old/new mapping epoch.
2. Test read/write compatibility while old and new clients coexist.
3. Design snapshot/backfill with source change capture and a determinate resume position; prevent loss/double-application.
4. Verify counts **and domain invariants**; equal row counts alone do not prove referential correctness.
5. Fence stale writers and stale mapping caches at cutover.
6. Observe hot-key traffic, transaction retry rate, tail latency and replication lag before and after.
7. Define a *forward repair* if new writes cannot be safely read by old shard ownership; do not promise reversible rollback after irreversible changes.


### Original migration trace: moving a hot tenant while writes continue

A **fictional** catalog stores bookings by tenant and item ID. Tenant A has become hot, and engineers propose moving its records from shard S1 to S2. The authoritative reservation invariant is **one successful booking per physical item and interval**, including during rebalancing. Merely copying equal row counts does not enforce it.

| Stage | Allowed writer / routing | Acceptance gate | Crash and recovery response |
|---|---|---|---|
| S0 baseline | S1 alone owns the tenant; fixed routing revision | Snapshot identifiers, committed-operation IDs and skew are measured | Remain on S1 |
| S1 shadow | S1 alone accepts writes; copy and ordered catch-up populate S2 | Key/tenant ownership, deletes and late updates reconcile | Resume bounded copy/checkpoint, do not expose S2 as an independent writer |
| S2 fenced handover | New routing epoch authorizes a *single* writer only after previous epoch is fenced | Concurrent client retries and stale routers cannot commit on both shards | Freeze new writes or return to S1 **only if** no S2-only effects occurred |
| S3 stable | S2 is authoritative; S1 is read-only/retired according to a documented compatibility horizon | Bookings, access policies, delayed messages and restore path verified | Forward-repair/reconcile if old epoch later reappears |
| S4 retire | Old data and routing removed only after replay/restore requirements pass | No unsupported historical reader remains | No image-only rollback across incompatible new state |

A dangerous counterexample occurs when an old client caches the S1 routing epoch and commits after another client has switched to S2. Even a perfect initial data copy cannot prevent two writers without an authority/fencing protocol. Another failure is a delete followed by a delayed old-version update that resurrects a record in S2. Stable event identity and source ordering must be specified before exposing the new owner.

The [Vitess 24 resharding workflow documentation](https://vitess.io/docs/24.0/user-guides/configuration-advanced/resharding/) and its [versioned MoveTables reference](https://vitess.io/docs/24.0/reference/vreplication/movetables/) describe copy, verification, traffic switch and, with suitable preconditions, reverse traffic. These are examples of product-specific mechanisms; **reverse routing is not a universal promise that a business write can always be undone**, and a destructive completion step is not an ordinary rollback. The fictional stages above are a design-level synthesis, not a tested Vitess sequence.

**Alternative:** repair a hot query, introduce a bounded per-tenant work queue, cache genuinely immutable reads, or isolate a high-traffic tenant without general sharding if the real bottleneck supports it. **Proposed, not run:** inject stale routing, interrupted copy, duplicate retry, deletion replay and two simultaneous writers; refuse cutover unless the single-authority invariant and recoverability can be demonstrated. The [semantic-migration owner](../c06-schema-evolution-data-migration-and-retention/schema-lifecycle-and-semantic-migration.md) covers domain identity; this chapter owns physical ownership transfer and key skew.

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [Consistent Hashing](../../v11-pattern-atlas/c06-database-storage/README.md#consistent-hashing) — decision conditions and contraindications.

<!-- tycho-question-source:tycho.page.0d34dd26886340b89fd4f1499d790a81:5 -->
## 5. Alternatives before sharding

Database query/index optimization, bounded connection pools, increasing storage/CPU, read replicas, caching suitable immutable/read-mostly data and removing unnecessary cross-domain locks can delay or remove the need for sharding. These tools address different bottlenecks; read replicas usually do not expand single-authority write serialization capacity.

**Insufficient evidence:** "The database has 500 million records; we must shard by user ID into 64 clusters." Cannot determine. Need growth, actual key and query distributions, hot tuples, disk and index IO, transactional ownership, compliance constraints, restore objectives, operational support and a measured comparison of simpler improvements.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](shard-strategies.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](shard-keys-hotspots-and-resharding.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

## Bounded pattern ownership notes

These notes define the decision boundary for atlas cards whose mechanism is not the main subject of
this page. They are synthetic design guidance, not measured evidence, and they do not create a new
source claim.

### Consistent Hashing

Consistent hashing maps keys onto a ring so adding or removing a node moves only the adjacent share
of keys instead of remapping the whole keyspace. Clients and owners must agree on a versioned
mapping, and a key must retain one authoritative owner at any mapping epoch.

A ring change temporarily routes a key to the wrong owner or serves an incomplete copy; dual-read or
version-check during the transition and record the epoch. Explicit key-range assignment gives direct
control of hot ranges; choose consistent hashing when node membership changes often and manual range
planning is impractical.

**Limits.** Virtual nodes improve balance but add metadata and lookup cost; a ring without epoch
fencing can route a write to two owners during a change.
