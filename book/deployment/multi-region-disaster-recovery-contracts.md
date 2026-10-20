---
metadata_version: 1
id: "tycho.page.2536d18422944e27abe4ea8549beb9ab"
kind: "page"
parent_id: "tycho.landing.6f58e5c00dea4f4086963169a2590bf5"
canonical_path: "book/deployment/multi-region-disaster-recovery-contracts.md"
title: "Multi-zone availability, multi-region disaster recovery and restore contracts"
topic_ids:
  - "deployment-architecture"
perspectives:
  - "architecture"
  - "operations"
summary: "Reader entry for Multi-zone availability, multi-region disaster recovery and restore contracts. Scope includes The question: what survives which loss?; RTO, RPO and their measurement boundaries; DR strategies with different operational dependencies."
route_hints:
  questions:
    - "What are the scope, mechanisms and limits of Multi-zone availability, multi-region disaster recovery and restore contracts?"
  prerequisites: []
  related_ids:
    - "tycho.page.ea94649bfd8c4be183f9114618d7ccaa"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Multi-zone"
    - "availability"
    - "multi-region"
    - "disaster"
    - "recovery"
    - "and"
    - "restore"
    - "contracts"
evidence_scope:
  source_ids:
    - "src.aws-static-stability"
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

# Multi-zone availability, multi-region disaster recovery and restore contracts

> Original Tycho E14-09 technical chapter, 2026-10-19, linked to [issue #87](https://github.com/rouslanbaranov/tycho/issues/87). The plans, tables and example timeline are **fictional and proposed**, not an operated disaster recovery system or evidence of a successful restore.

## The question: what survives which loss?

A service can survive a failed container yet lose all user state when its single database fails. It can span three availability zones yet be unavailable during a region-wide routing or identity outage. Conversely, a cross-region copy of an inconsistent state is not a valid recovery point merely because replication completed.

Define each required **failure class** and loss boundary before choosing any topology:

- single process/host/VM loss, rack/node-group loss, one zone unavailable, zonal network isolation;
- partial region-control-plane outage while data plane operates, regional data-plane outage, complete region loss;
- logical data corruption, destructive operator mistake, malicious deletion or compromised credentials;
- dependency/customer-identity service loss, missing deployment artifact, expired certificate, accidental schema incompatibility.

A *high-availability deployment* and a *disaster-recovery plan* solve different, sometimes overlapping, questions. A successful regional failover does not automatically protect against malicious data replication, old-client contract incompatibility or two simultaneous writers.

## RTO, RPO and their measurement boundaries

**RTO (Recovery Time Objective)**: the approved maximum period a named user capability can be unavailable for the declared disaster class. An operational measurement must say when the incident timer starts (user impact, confirmed failover decision or injection) and what verified user-visible state counts as restored. Do not start the timer only after the slow detection or approval phase.

**RPO (Recovery Point Objective)**: the maximum accepted loss of committed, relevant state relative to a chosen pre-failure boundary. Define the last known durable *correct* business event; asynchronous replicas can be behind, and continuous replication may faithfully propagate an accidental deletion. Zero RPO cannot be inferred from a replica or a vendor's generic marketing wording.

Recoverability is at least:

- **Recovering serving capability**: detection, authorized decision, routing, secrets/config, compute, state owner election, warm-up and client contract tests.
- **Recovering business truth**: backup/replica timeline, commit IDs, replay boundary, external side effects, event IDs, reconciliation and audit evidence.
- **Recovering safely**: avoid two active primaries, enforce write fencing and prevent stale clients from silently issuing duplicate business effects.

An RTO number or RPO number is a **target, not an observed result** until a performed and timed drill provides evidence of the declared failure scenario.

## DR strategies with different operational dependencies

| Approach | Passive region readiness | Strength and relative cost tendency | Critical outage-time dependency and evidence gap |
|---|---|---|---|
| Backup and restore | Durable data/config/artifacts protected; serving topology may be absent | Often least permanent active capacity, but restore may take substantial time | Recover identity/IaC credentials, compute/network and data restores; test reconstitution from offsite resources |
| Pilot light | Core state/replication present; most application serving capacity is not yet started | Lower standing application capacity with faster state readiness than bare restore | Must provision/scale application and recover artifacts during incident; control plane might be impaired |
| Warm standby | Reduced but already operating critical application and state footprint | Higher standing costs, fewer cold setup steps | Must scale/provision to declared normal load, switch writes safely and verify state/role promotion |
| Multi-site active/active | Multiple regions serve some user traffic before disaster | Potentially fast traffic continuity when workloads and state model allow | Distributed writes, conflict resolution, global identity, network partitions, cost, data residency and consistency—**not** generic zero RPO |

These patterns are categorized in the AWS *Disaster recovery options in the cloud* whitepaper, **Backup and restore**, **Pilot light**, **Warm standby** and **Multi-site active/active**. The AWS paper's comparative positions are source-specific architecture illustrations, **not universal prices, failover timings or availability guarantees**.

### The active/active misconception

Active traffic in two regions is not equal to multiple write masters with a safely reconciled business invariant. A fully active write topology must specify partition behavior and concurrency semantics. If both regions independently allocate the final workshop seat during isolation, a later conflict resolution cannot necessarily undo the user-visible double confirmation. Possible solutions include a single authoritative writer with remote reads, per-key single-writer partitioning, escrow/reservation protocols, or an application that deliberately tolerates merge conflicts. Each requires actual workload, correctness and failure tests; a globally replicated database alone does not choose the business policy.

Active/passive with one writer may be much simpler, but a promotion after ambiguous leader loss still needs fencing, epoch/lease or other source-backed role-control. A DNS switch is **not** a transaction or split-brain prevention protocol.

## Original proposed region recovery flow

~~~mermaid
sequenceDiagram
    participant U as Client
    participant A as Region A: original writer
    participant W as Region B: standby
    participant R as Recovery controller
    participant B as Backups / immutable checkpoints
    U->>A: Last acknowledged logical operation K
    A->>W: Asynchronous data replication
    Note over A,W: Region A becomes unreachable
    R->>R: Assess user impact, state lag, approval
    R->>A: Attempt fencing / exclusion of old writer
    R->>B: Identify latest correct recovery point
    R->>W: Restore/promote only after write-safety gate
    W->>B: Reconcile journal, request/event identity
    R->>U: Route to verified surviving endpoint
    U->>W: Repeat K after ambiguous response
    W-->>U: Recover same logical outcome if preserved
~~~

Text alternative: a client has an acknowledged or ambiguous request near a regional outage. State replication may lag; recovery must verify last correct state and prevent the original region from accepting conflicting writes before promoting a standby. Recovery compares immutable backups/events and deduplicates repeated logical requests; routing changes come **after** correctness and serving validation. Every step is a proposed test obligation, not an event that occurred.

## Failure matrix: detection through restored user journey

| Failure/drill | Recovery method hypothesis | Evidence needed before saying it meets RTO/RPO | Do-not-proceed condition |
|---|---|---|---|
| Single instance/zone | Pre-warmed healthy replicas route around failure | Load under loss, data owner/quorum, latency/error and correct completions | Remaining zones lack capacity or are dependent on failed management |
| Region A unavailable | Restore/promote Region B using tested role/fencing and recovery state | Incident start time, lag, write-role ownership, traffic switch and read/write checks | Original write authority cannot be fenced, business reconciliation unknown |
| Corruption replicated to secondary | Restore from immutable/versioned point in time | Verified good backup before corruption, independently readable checksums, semantic business recovery | Only a corrupted continuous replica exists |
| Lost IaC/identity control | Use pre-tested independent restoration credentials/config | Alternate-account/region access, artifact integrity, tested deployment state | Recovery relies exclusively on failed control plane |
| Application schema drift during outage | Reconcile mixed old/new records, select compatible binary or forward recovery | Verified compatibility matrix, stored schema/version, replay of old events | Old binary cannot read post-cutover data and rollback is assumed safe |
| Two active regions in network partition | Enforce one authoritative writer or a reviewed conflict contract | Split-brain injection, documented epoch/lease, invariant audits | Both sides may independently confirm mutually exclusive business actions |

## A bounded drill is not a disaster simulator

A safe **proposed experiment**, using a fictional workshop registration system, should identify:

1. **Design prerequisites:** source snapshot, two regions/zones and their actual services, writer and reader roles, allowed failure class, sample rate, backup version and authoritative event K/R identity.
2. **Invariant:** no double seat allocation for the same capacity unit; every acknowledged registration must be either visible in the declared recovered state or be accounted for as permitted RPO data loss with explicit compensating business handling.
3. **Baseline:** a stable known workload and time zone; offered/admitted/completed logical operations, p95/p99/error and replication lag measured separately. Include live resources, control-plane changes and secret/certificate dependencies.
4. **Injection:** disconnect one region in an **authorized non-production exercise**; separately simulate a data corruption or expired artifact. Start recovery clocks at the declared boundary and preserve timestamped evidence.
5. **Safety:** confirm no overlapping writer epoch, test retry ambiguity and consumer idempotence, authenticate redirected clients, reconcile events/rows by business keys—not just record counts.
6. **Recovery:** promote or restore only when gates are satisfied, observe actual time to valid user outcomes, RPO gap and failure budget; restore normal topology and exercise failback separately.
7. **Review:** repeat across different failure classes and recording windows; if evidence is missing, write **insufficient evidence / do not cut over**, not a green check.

A **synthetic arithmetic illustration**: with a business RTO target of 15 minutes, if detection consumes 4, operator decision 5, traffic reconfiguration 3 and validation 4 minutes, total is **16 minutes**, already beyond the target. These invented numbers illustrate the importance of measuring the whole sequence. They are not measurements, platform timings or recommended budgets. Parallel phases and retries require actual traces; simple addition is only valid for the stated serial hypothesis.

## Placement, IaC and operational contract

Cross-region deployment must reproduce more than code:

- network routing, DNS/certificates, identities/secrets, state/backup permissions and egress;
- source code/release artifacts and immutable provenance, database schema/CDC/event versions, retention and write roles;
- runbook owner, on-call/approval channel, maintenance access and control-plane unavailability fallback;
- tenant and personal-data residency rules with actual jurisdiction/version evidence, not assumed replication permission.

Infrastructure as code with source control reduces manual divergence only if the state backend, provider API, credentials and artifacts remain operable during the very failure class being tested. Recovery automation that needs the failed primary region to supply fresh credentials or images cannot be called resilient without a fallback.

An application with a single correct writer, good tested backups, reversible deployment and explicit RPO/RTO may prefer warm standby over multiwriter active/active. Conversely, an event workload with independently partitioned ownership could justify regional distribution when actual data locality and correctness gates permit it. The outcome depends on evidence, not on technology popularity.

## Exact source-to-claim ledger and coverage gaps

| Ref | Primary material actually inspected 2026-10-19 | Supported scope, not established |
|---|---|---|
| R87-01 | [AWS DR Whitepaper, Disaster recovery options in the cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), *Backup and restore*, *Pilot light*, *Warm standby*, *Multi-site active/active*, paper publication 2021-02-12 | Four recovery approaches, IaC/replication trade-offs and test necessity; no universal RTO, RPO, price or guaranteed failover duration |
| R87-02 | [AWS Builders' Library, Static stability using Availability Zones](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/), *Static stability* and *Static stability patterns* | Pre-provisioning/stable data plane and zone isolation in AWS examples; not evidence of the fictional system |
| R87-03 | [Terraform State purpose](https://developer.hashicorp.com/terraform/language/state/purpose), state-to-resource mapping and remote state discussion | IaC state matters for rebuild; not proof that a backup/restore procedure is in place |
| R87-04 | [Tycho target/transition model](../../authoring/models/target-transition-architecture.md) | Canonical original coexistence/rollback gates, no real migration or recovery evidence |

**Research gaps requiring separate primary documents before a deployed recommendation:** regional database-specific role promotion, write fencing and replica consistency; provider/API failure and DNS propagation, route cache, multi-region data residency and encryption-key recovery, immutable backup restoration proof, disaster simulation authorization and artifact availability. The AWS general umbrella is not a substitute for exact PostgreSQL/Aurora/Kafka or selected provider documentation. No RPO/RTO result is claimed from this manuscript.

## Reader decision route

From requirements, name the failure class, correctness contract and tolerable loss. From legacy baselines, identify current single writer, backup reality and old/new compatibility. From a symptom, first distinguish zonal failure from data corruption. Compare backup/restore, pilot, warm standby and active/active with the same workload, permissions and failure/restore exercise. Return an ADR with **measured or explicitly unknown** safety gates; never select an active/active data architecture purely because two regions appear in a topology chart.

Read the companion [deployment/control-plane chapter](../volumes/v08/c03/runtime-placement-and-control-plane.md) for instance placement, service mesh and IaC boundaries.
