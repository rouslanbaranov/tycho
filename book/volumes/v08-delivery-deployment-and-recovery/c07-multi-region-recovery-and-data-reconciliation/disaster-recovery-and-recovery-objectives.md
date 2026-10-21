---
metadata_version: 1
id: "tycho.page.2f6602f8e20b4f80a22e0ef85a6d1765"
kind: "page"
parent_id: "tycho.chapter.30e63461f024419ab87cd012b140c600"
canonical_path: "book/volumes/v08-delivery-deployment-and-recovery/c07-multi-region-recovery-and-data-reconciliation/disaster-recovery-and-recovery-objectives.md"
title: "Disaster recovery: measured RTO, RPO, fencing and state reconciliation"
topic_ids:
  - "deployment-architecture"
perspectives:
  - "architecture"
  - "operations"
summary: "Integrated question, original scenario and transfer limits for Multi-region recovery and data reconciliation. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "How are RPO/RTO, split brain, recovery routes and failback validated?"
  prerequisites: []
  related_ids:
    - "tycho.page.2536d18422944e27abe4ea8549beb9ab"
    - "tycho.page.6b3725950fad4c0db82417b3d0225d32"
    - "tycho.page.81efb7e6d72349768b6f202845cbe35e"
    - "tycho.landing.6f58e5c00dea4f4086963169a2590bf5"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.page.1e89567050974052b13ba62b3b44484f"
    - "tycho.page.4b654b81026f4d8b8909563bcffc01e4"
    - "tycho.page.aeedcc93ea554edc9059b8f9ddefa292"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Disaster"
    - "recovery"
    - "measured"
    - "RTO"
    - "RPO"
    - "fencing"
    - "and"
    - "state"
    - "reconciliation"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-10-21"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.2f6602f8e20b4f80a22e0ef85a6d1765:-1 -->

# Disaster recovery: measured RTO, RPO, fencing and state reconciliation

> **Tycho V08/C07 book manuscript**, 2026-10-19. Versioned PostgreSQL 17 PITR and public
> Well-Architected recovery-strategy guidance were reviewed. The failure chronology, tables and
> drills are original fictional material. No failover, region loss, backup restore, replication test
> or independent human review was executed. Earlier [regional/DR
> research](../../../deployment/multi-region-disaster-recovery-contracts.md) is preserved.
>
> The content_review field retains the decomposition-era draft state; no independent
> acceptance is asserted.

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [Geode](../../v11-pattern-atlas/c09-scalability/README.md#geode) — decision conditions and contraindications.

<!-- tycho-question-source:tycho.page.2f6602f8e20b4f80a22e0ef85a6d1765:0 -->
## Purpose and mission

Disaster recovery is not “run a copy somewhere else.” Its engineering deliverable is the ability to **restore a correct user-visible capability** after a specified disruptive failure within owner-approved loss and time budgets.

A regional failover can recover a process and still fail its business obligations: an asynchronous secondary may lack a recently accepted write, old clients may repeat an operation, and two primaries may accept divergent state. Recovery requires an explicit **failure class, authority transfer, acceptable data loss, reconciliation and verified restart of user journeys**.

[Availability placement](../c06-high-availability-and-failure-domain-placement/availability-zones-placement-and-failure-domains.md) owns topology and zonal isolation. [PostgreSQL backup/PITR](../../v05-data-models-engines-and-lifecycle/c07-replication-backups-and-restore-drills/backup-restore-pitr-and-recovery-drills.md) owns concrete source backup mechanics.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.2f6602f8e20b4f80a22e0ef85a6d1765:8 -->
## Applied M9 evidence: what transfers and what does not

These examples connect the chapter's conditional mechanism to published experiences or synthetic decision exercises. A historical company report is **first-party, time-scoped evidence**, not a controlled Tycho benchmark; an M9 decision playbook is **original synthetic analysis**, not a company decision.

**Case lens — [Netflix — Chaos Kong regional simulation](../../../cases/netflix-chaos-kong-regional-failover.md)**. **Relevant mechanism or architectural contrast:** Application-level regional fault simulation can expose cross-service failover dependencies and missing readiness. **Not established by this report/playbook:** Chaos Kong does not simulate provider-wide physical outage or prove universal multi-region data integrity.

**Transfer test:** before applying the lesson to another legacy system, identify the exact workload, source date, relevant runtime/protocol versions, state authority, failure/recovery gate and the new observation that would reverse the choice. Follow the case's public evidence ledger rather than treating its link as independent proof.
<!-- /tycho-question-source -->

## Integrated decision and reading route

Fence the former writer, define acceptable loss and reconcile state before directing recovered traffic to a new authority.

Promoting a second region without exclusive authority can create divergent accepted effects; failback is another transition to validate.

The detailed pages separate the mechanisms that make this decision conditional:

- [Recovery clocks, historical state and alternatives](objectives-strategies.md) — Which failure and data-loss contract distinguishes recovery strategies?
- [Recovery state machines, fencing and failback](authority-failback.md) — Which steps prevent two writers and demonstrate recovered user journeys?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.

## Bounded pattern ownership notes

These notes define the decision boundary for atlas cards whose mechanism is
not the main subject of this page. They are synthetic design guidance, not
measured evidence, and they do not create a new source claim.

### Geode

Geode places identical regional nodes behind a global routing layer so clients can use a
nearby healthy region. It needs a data replication and consistency contract, a regional
health signal, a routing rule and an explicit failover authority. Use it when locality or
regional survival is material and the data model can reconcile cross-region state. Do not
use it when a single region meets the objective or when routing would hide divergent
state.

The failure path is a route to a stale or isolated region; the router must use an
authoritative health and data-freshness signal, and failover must fence the old writer.
Active-passive recovery is the alternative when cross-region consistency is not worth the
routing complexity.
