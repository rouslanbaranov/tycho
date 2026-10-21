---
metadata_version: 1
id: "tycho.page.d1fa0462922e4a37922cea279975a3bd"
kind: "page"
parent_id: "tycho.chapter.7d434d1a41e142d38bb729ee124ac548"
canonical_path: "book/volumes/v08-delivery-deployment-and-recovery/c05-backward-compatible-database-change/no-return-recovery.md"
title: "No-return points and forward repair"
topic_ids:
  - "software-delivery"
perspectives:
  - "architecture"
  - "operations"
summary: "Which persisted effect makes reverting an old binary unsafe?"
route_hints:
  questions:
    - "Which persisted effect makes reverting an old binary unsafe?"
  prerequisites:
    - "tycho.page.48d9c34e755c4f7ab912ecad14f5794f"
  related_ids:
    - "tycho.chapter.7d434d1a41e142d38bb729ee124ac548"
    - "tycho.page.77957bf0f2d44c4a9bc819fc5b3e1ddb"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "no"
    - "return"
    - "recovery"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.77957bf0f2d44c4a9bc819fc5b3e1ddb; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# No-return points and forward repair

**Owning question:** Which persisted effect makes reverting an old binary unsafe?

This page belongs to [V08/C05 — Backward-compatible database change](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.77957bf0f2d44c4a9bc819fc5b3e1ddb:5 -->
## 5. Rollback has a no-return boundary

Code image rollback is safe only when old N can correctly read and mutate every persisted state written by N+1 during exposure. Once N+1 commits a genuinely new-only state, restoring N containers may reproduce errors or violate business invariants.

| Condition | Possible response |
|---|---|
| Candidate failed before incompatible writes | Route/replica rollback may be valid after checks |
| Candidate wrote additive values N correctly handles | Revert only with verified mixed-version tests |
| Candidate wrote new-only business state N misreads | Hold traffic; forward compatibility/repair or verified restore |
| DDL dropped mandatory N field | Cannot assume N image can operate |
| External effects after cutover | Reconciliation required even if DB schema restored |
| Old event replay after field retirement | Retained decoder or explicitly accepted archival limitation |

A revert command is not recovery of acknowledged reservations or external effects.


### Original compatibility matrix: new writer, old reader, delayed event

A fictional booking application adds a new durable state code `CONFIRMED_V2`. Release N accepts only legacy `CONFIRMED`; N+1 reads both and wants to write the new code. During rolling deployment, old API instances and delayed event consumers can outlive the candidate rollout. An additive SQL column does **not** by itself establish semantic compatibility.

| Reader / writer combination | Proposed permitted behavior | Deployment gate |
|---|---|---|
| N reads N writes | Existing contract | Baseline still checked |
| N+1 reads N writes | New reader must preserve old meaning | Test legacy records and historical replay |
| N reads N+1 writes | **Unsafe** if `CONFIRMED_V2` is not understood | Keep N+1 on old write format until N readers are retired |
| N+1 reads N+1 writes | Target functionality | Verify authorization, meaning and downgrade/repair strategy |
| Delayed N event consumer reads N+1 writes | Separate history version boundary | No old codec may silently discard or misinterpret the event |

A schema rollout requires an actual **capability inventory**, not a belief that all deployed pods have a new image. Mobile/partner clients, queues, batch jobs, database views and backups can retain older semantics. The [Parallel Change description](https://martinfowler.com/bliki/ParallelChange.html) supports coexistence as a change pattern, while [PostgreSQL 17 ALTER TABLE](https://www.postgresql.org/docs/17/sql-altertable.html) documents DDL operations and lock considerations. Neither proves N/N+1 application meaning or migration reversibility.

**Failure:** N+1 canary commits a new-only value, fails its latency checks, then a deployment controller rolls the image back to N. N can no longer read the record; **image rollback is not business rollback**. A safe intermediate stage keeps writes compatible, or otherwise requires a proven forward repair and a separately authorized no-return gate.

**Proposed, unexecuted test:** run the compatibility matrix for each reader/writer/event cohort, inject an interrupted backfill, ensure the old decoder fails explicitly rather than corrupting state, and time DDL under representative table load. Semantic field migration belongs to [V05/C06](../../v05-data-models-engines-and-lifecycle/c06-schema-evolution-data-migration-and-retention/schema-lifecycle-and-semantic-migration.md); progressive exposure to [V08/C04](../c04-gitops-rollout-and-progressive-delivery/gitops-canary-and-progressive-rollout.md).

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.77957bf0f2d44c4a9bc819fc5b3e1ddb:6 -->
## 6. Acceptance tests must include failures

Proposed test fixture (not executed):
1. N clients use N API and N+1 API against expanded schema.
2. N+1 clients exercise both API versions where supported.
3. Old queued event consumed by N+1, and new event by N where still supported.
4. Crash during backfill, then resume without mapping divergence.
5. Concurrent writer changes an identifier while old/new reads occur.
6. Abort a migration after a long lock; measure queue wait and replica lag.
7. Roll back the binary after N+1 produced valid new data.
8. Restore/replay historical state after contract step; verify completeness.

Acceptance includes correct user effects, database invariants, bounded downtime and actual recovery. Green migration SQL alone cannot close the gate.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](ddl-events.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](mixed-version-database-compatibility-and-online-ddl.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
