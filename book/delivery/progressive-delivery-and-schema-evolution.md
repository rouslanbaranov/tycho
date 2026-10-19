---
metadata_version: 1
id: "tycho.page.81add4a0d86b4053ae77f9301fd2281d"
kind: "page"
parent_id: "tycho.landing.fe2eace7b2df4ae480adbdf844b68100"
canonical_path: "book/delivery/progressive-delivery-and-schema-evolution.md"
title: "Progressive delivery, mixed-version contracts and database evolution"
topic_ids:
  - "software-delivery"
perspectives:
  - "architecture"
  - "operations"
summary: "Reader entry for Progressive delivery, mixed-version contracts and database evolution. Scope includes 1. Four distinct deployment modes; 2. Compatibility is a matrix, not a Boolean; 3. Expand → migrate → contract with explicit gates."
route_hints:
  questions:
    - "What are the scope, mechanisms and limits of Progressive delivery, mixed-version contracts and database evolution?"
  prerequisites: []
  related_ids:
    - "tycho.page.7921e82a71b9446790f185c818326911"
    - "tycho.page.1e89567050974052b13ba62b3b44484f"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Progressive"
    - "delivery"
    - "mixed-version"
    - "contracts"
    - "and"
    - "database"
    - "evolution"
evidence_scope:
  source_ids:
    - "src.k8s-deployments"
  claim_ids: []
  status: "source-linked"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---

# Progressive delivery, mixed-version contracts and database evolution

> Tycho E14-10 [#88](https://github.com/rouslanbaranov/tycho/issues/88), original source-bounded research 2026-10-19. The migration stages and failure timeline are fictional. No controlled rollout, restored backup, upgrade or independent review was performed.

## Purpose and mission

A release can be deployed successfully yet fail when old and new binaries coexist, when records written by a new version cannot be read by older workers, or when delayed events arrive after contract removal. Progressive delivery controls **exposure**, whereas schema compatibility controls **interpretation of shared state**. Both require independently verified invariants.

**Primary question:** How should rolling, canary and blue/green deployments be coordinated with schema, event and API changes so that a failed rollout is recoverable without making unsupported rollback promises?

Companion chapters: [CI/CD identity and GitOps](ci-cd-provenance-and-gitops.md), [safe rollout and recovery](safe-rollout-and-recovery.md), and [target-versus-transition architecture](../../authoring/models/target-transition-architecture.md).

## 1. Four distinct deployment modes

| Mode | Mechanism and benefit | Required acceptance and hidden cost |
|---|---|---|
| **Rolling update** | Gradually replace old replicas with new while bounding unavailable capacity and temporary surge. Kubernetes Deployments documents maxUnavailable and maxSurge. [E01] | N and N+1 may operate simultaneously; reads/writes/API/events must coexist; readiness is not business correctness. |
| **Blue/green** | Maintain two environment versions and switch traffic to the candidate after preview. | Extra standing capacity, traffic/session routing, durable data shared or separately synchronized; switching traffic back cannot reverse N+1 writes. |
| **Canary / progressive** | Route selected users or a measured fraction to the candidate and advance or abort according to outcomes. Argo Rollouts supports setWeight, pause and metric analysis. [E02] | Traffic weights only approximate actual business mixture; rare failures need sufficient statistical exposure; old and new share state under partial traffic. |
| **Recreate / bounded downtime** | Stop N and start N+1 without serving mixed versions. | Explicit downtime/restart risk, restore gates; old clients and background consumers may still hold incompatible contracts. |

A canary does not remove the need for version compatibility: even if only 1% of requests enter N+1, writes may become visible to all N readers and all asynchronous consumers.

## 2. Compatibility is a matrix, not a Boolean

For a fictional workshop-registration API, release N uses key workshop_code, while N+1 wants a new opaque workshop_identifier. The desired business invariant is one confirmed registration per accepted idempotency identity, bounded by workshop capacity.

| Producer or reader | Old storage/event schema | Additive transitional schema | New-only/destructive schema |
|---|---|---|---|
| Old API N | Baseline contract must be tested | Must tolerate new nullable columns/defaults while preserving old semantics | **Unsafe until proved**; old code may not find its required identifier |
| New API N+1 | May require adapter/dual-read | Must preserve identity and transactional outcome | Candidate target, only after old readers retire |
| Background worker N | Existing event format | Must ignore optional fields or use version-specific codec | Unknown; queues may outlive rollout |
| Background worker N+1 | Old messages may remain in retention | Must decode old and new | Candidate, but must still handle replay |
| External client N | Existing API contract | Response/request compatibility must hold | Breaking behavior requires negotiated version/transition |
| Replay/restore process | Historic event and DB records | Must reconstruct correct business identity | Destructive clean-up could defeat historical replay |

Tests must exercise every **actually deployed combination**, not only a new client against a new server. Event-format compatibility depends on serialization type, optionality, default values and subject/version history; a schema registry's BACKWARD compatibility does not automatically guarantee every older consumer can read new messages. Confluent's official Schema Registry documentation distinguishes BACKWARD, FORWARD, FULL and transitive variants, and notes format-dependent behavior. [E04]

## 3. Expand → migrate → contract with explicit gates

Danilo Sato's *Parallel Change* describes the expand/migrate/contract approach for changing published interfaces while allowing clients to transition. [E03] The same discipline is useful, by analogy, for database and event-schema evolution—but database operations have independent locks, rewrite and integrity consequences.

**S0 — Baseline.** Record N's API/event/database schema, writer list, read paths, held locks, queued message age, recovery points and exact owner of truth. The measured starting state is required before designing a migration.

**S1 — Expand.** Add a new nullable column or companion table without removing the old one. Define a stable mapping between old and new IDs, uniqueness and concurrent update rules. An additive DDL statement may still take substantial locks or trigger rewriting depending on engine/version/type. PostgreSQL 17's ALTER TABLE documentation explains operation-dependent lock levels; ACCESS EXCLUSIVE is the default unless otherwise specified. [E05]

**S2 — Compatible read.** N+1 reads both representations, but maintains a single clearly defined canonical business identity. If the new representation is absent, use an explicit fallback that can be instrumented; never silently assign different identifiers on retry.

**S3 — Controlled write and backfill.** Select one authoritative writer or validate dual-write consistency under failure. Backfill in small, replay-safe ranges, track checkpoint and version, and reconcile by business key and semantic state. Two independently committed writes cannot be assumed atomic. Use a local transaction/outbox or conditional update when it fits the actual data store.

**S4 — Migrate clients/consumers.** Measure all active N clients, services and retained events; run old/new cross-version tests under realistic concurrency. Move traffic gradually while checking counts, checksums, business invariants, duplicates, lag and replay.

**S5 — Contract.** Remove old columns/contracts only after N writers and historic readers are demonstrably retired, replay/restore requirements are satisfied and irreversible effects have an approved recovery strategy. This is not simply a calendar date.

The contract step is often the riskiest: removing old data destroys the easiest rollback path. The ability to run an earlier image is not proof that it can interpret newer records.

### Original transition state sequence

Baseline N → additive schema → N+1 dual-read → single-authority write/backfill → mixed N/N+1 rollout → verified N retirement → destructive cleanup → accepted N+1.

At any state with data incompatible with N, the recovery choice must be **forward repair or tested data restore**, not a blind reversion of the application image.

## 4. Illustrative failed canary

Assume entirely synthetic initial conditions: 10% of HTTP requests hit N+1, which writes only workshop_identifier, while 90% still hit N expecting workshop_code.

1. N+1 successfully commits a registration and returns an HTTP success, then the exposure gate detects increased errors.
2. The rollout controller returns traffic to N; from its perspective, replica rollback succeeds.
3. N retrieves the N+1 record and cannot interpret the missing old identifier; a previously successful user request becomes unreadable.
4. The correct response is **stop accepting risky writes**, identify all affected records and clients, reconcile business state, and execute a tested forward compatibility patch or restoration.
5. Verification must include logical registration count, committed transaction IDs, downstream notifications, consumer acknowledgements, duplicates and user-visible results.

This is a deliberately unsafe design illustration. It does not imply the chosen database or controller actually produces the failure without specific version/configuration conditions.

## 5. Online DDL and resource contention

Schema migration is itself a workload. It may need metadata locks, row/table rewrites, index creation and transaction log space. While backfill runs, it competes with normal queries for CPU, storage bandwidth, connections, replication throughput and lock time.

- Choose **bounded batches** and idempotent checkpoints rather than one unbounded transaction. Treat a checkpoint as evidence of the last durable completed range, not proof that all records reconcile.
- For relevant indexes and constraints, inspect the exact supported database/version for online/concurrent mechanisms and lock modes. Do not generalize a syntax from one database to all engines.
- Capture offered business load, affected tenants/keys, p95/p99 waits and long-running transactions, WAL/binlog/CDC lag, replica state, lock waits, backfill age and restore-point freshness.
- Set stop conditions and recovery before the run: max queue age, failed validations, lag budgets, unexpected uniqueness conflicts and restore coverage.
- Test a process crash between backfill commit and checkpoint persist; retry must be safe and produce one authoritative logical result.

Adding a new nullable column alone cannot prove a safe upgrade if old mapping code assumes a fixed projection, old clients require a removed field or triggers modify semantics.

## 6. Compatibility and deployment strategy jointly constrain choice

| Constraint | Safer initial option to evaluate | Dangerous shortcut |
|---|---|---|
| Old clients cannot upgrade at once | Additive API/schema, feature negotiation, retained old readers | Breaking endpoint and storage change in one canary |
| Strict downtime target with one writer | Expand-contract and measured low-lock/backfill operation | Long exclusive migration during peak load |
| Heavy async event replay | Versioned event schemas and transitive historical decode tests | Deleting historic codecs after current consumer rollout |
| Fast image rollback requirement | Prove N reads/writes after N+1 changes or enforce read-only exposure | Assume successful controller rollback reverses data |
| Provider-managed rolling services | Verify platform-specific order, health and data owner | Infer product data correctness from green resource status |
| Unknown baseline and queue retention | Retain existing architecture; inventory first | Choose microservice split or tool solely from team preference |

## 7. Evidence and acceptance

A meaningful release review requires:

1. Exact old/new application, database and event schema versions; immutable artifact digests and deployment modes.
2. A fixture matrix with actual old/new client-server and consumer-producer combinations; explicit source/format versions.
3. Concurrency tests for double writes, conflict detection and idempotency; successful backfill restart after failure.
4. Business-level counts and checksums after each stage; user-visible success/error and performance envelope.
5. The earliest irreversible data write/DDL/side effect and tested forward recovery or restore.
6. Named acceptance reviewer and recorded stop decisions; no assumption that no error means no corruption.

| Ref | Exact public source inspected 2026-10-19 | Supports, and does not support |
|---|---|---|
| E01 | [Kubernetes Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/), *Rolling Update*, *maxUnavailable* and *maxSurge* | Controller mechanics, not data compatibility or observed uptime |
| E02 | [Argo Rollouts Canary](https://argo-rollouts.readthedocs.io/en/stable/features/canary/), *Canary Deployment Strategy / steps / analysis* | Candidate exposure and analysis, not business correctness |
| E03 | [Danilo Sato, Parallel Change](https://martinfowler.com/bliki/ParallelChange.html), May 2014, *expand/migrate/contract* | Interface transition method, not a database engine guarantee |
| E04 | [Confluent Schema Registry Schema Evolution](https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html), *compatibility types and transitive checks* | Format- and version-specific evolution semantics, not global end-to-end compatibility |
| E05 | [PostgreSQL 17 ALTER TABLE](https://www.postgresql.org/docs/17/sql-altertable.html), *description/lock mode subforms* | PostgreSQL DDL constraints, not measurements of a Tycho example |

This chapter owns the conceptual migration and verification model. The original deployment incident and all numbers are hypothetical. No real schema alteration, compatibility matrix execution, external event replay, production rollback, source-code inspection or independent expert review has been claimed.
