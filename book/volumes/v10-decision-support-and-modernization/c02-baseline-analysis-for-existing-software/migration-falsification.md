---
metadata_version: 1
id: "tycho.page.fbf4c3d642d14ce2a69f009efd17b1a8"
kind: "page"
parent_id: "tycho.chapter.8605018cb9224f99bea9dd49be2b79e3"
canonical_path: "book/volumes/v10-decision-support-and-modernization/c02-baseline-analysis-for-existing-software/migration-falsification.md"
title: "Migration failure tests and decision reversal"
topic_ids:
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "migration"
summary: "Which recovery observation would reject the attractive target?"
route_hints:
  questions:
    - "Which recovery observation would reject the attractive target?"
  prerequisites:
    - "tycho.page.19145078d87143b28387ab187d345c32"
  related_ids:
    - "tycho.chapter.8605018cb9224f99bea9dd49be2b79e3"
    - "tycho.page.b2d1285c1c1a4a698a2306c4e766a4f1"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "migration"
    - "falsification"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.b2d1285c1c1a4a698a2306c4e766a4f1; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Migration failure tests and decision reversal

**Owning question:** Which recovery observation would reject the attractive target?

This page belongs to [V10/C02 — Baseline analysis for existing software](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.b2d1285c1c1a4a698a2306c4e766a4f1:6 -->
## 6. A correct migration must test failure and recovery

### Failure A — response acknowledgment is lost

A contributor edits photo metadata; the transaction commits but the response disappears. The client retries. Correct behavior requires a durable operation identity or other safe retry contract; otherwise two update effects or duplicate notifications may result. [Outbox/idempotency](../../../distributed/transactional-outbox-and-idempotency.md) explains why local transaction boundaries do not cover external notifications.

### Failure B — old and new clients interpret the same field differently

A previously optional metadata field becomes mandatory under the new implementation. Old clients continue submitting records without it, while the new server silently defaults to a materially different value. **Wire parsing succeeds but behavioral compatibility fails.** Fix by retaining documented default meaning, staging field requirements or versioning the client contract; prove each pairing before removal.

### Failure C — import cutover halfway through a batch

An imported data file partially applies and then its worker crashes. Restart may reread already processed records. Safe recovery needs durable import identity, checkpoint semantics, row-level logical identity and an explicit partial/error policy. An in-memory cursor is not evidence of idempotent restart.

### Failure D — deployment rollback after irreversible writes

New code persists records that old code cannot parse. Returning to the older container image does not restore the database. A release gate needs either a backward-compatible period, a reversible tested migration, or explicit **forward recovery**. A runtime deploy rollback and a data correctness rollback are distinct.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.b2d1285c1c1a4a698a2306c4e766a4f1:7 -->
## 7. The evidence-based selection outcome

For the synthetic catalog, available evidence is insufficient to prove that the workload needs microservices, a new database or Kafka. A **provisional recommendation** is:

1. Record the current data authority, external clients, release assumptions and import workflow at pinned versions.
2. Reproduce the import slowdown with timing broken down by stage and query plan; record offered versus completed work and error/timeout outcomes.
3. Establish contract tests and a reversible runtime upgrade path while preserving one metadata writer.
4. Use an internal abstraction for import behavior only if it reduces known change coupling.
5. Revisit extraction if measured requirements demand independent deployment or isolation, and the data/consumer ownership is demonstrably separable.

**Decision state:** INVESTIGATE_AND_RETAIN_BASELINE, with conditional incremental modernization. There is no confirmed target architecture, operational win or approved plan because the case is hypothetical and key evidence is deliberately absent.

### Evidence that would reverse the choice

A signed functional contract that requires isolating import failures from public reads; measured separate resource bottlenecks not addressable in the existing deployable; a fully owned data subset; independently deployable teams with compatible consumer timelines; reproducible benefit greater than the overhead of network, data and operational boundaries. Every such statement still needs a testable criterion and a transition strategy.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](modernization-options.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](legacy-baseline-and-modernization-evidence.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
