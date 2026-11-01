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
  source_ids: ["src.microsoft-cloud-patterns"]
  claim_ids: []
  status: "source-linked"
  notes: "Read source-plan units; page-level, not claim-mapped."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-11-01"
source_inspection_date: "2026-11-01"
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
nearby healthy region. Each geode is a self-contained regional deployment; Azure's page calls this
an active-active approach that "distributes request processing around the globe to improve
latency and increase availability" and says each geode uses a geo-replicated read-write service
to keep cross-geode data consistent
([Geode pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/geodes)).
Geodes "never exist in isolation", and any geode can take over after a regional outage. It
needs a data replication and consistency contract, a regional health signal, a routing rule
and an explicit failover authority.

**Failure and recovery (Tycho synthesis).** A route can remain stale or point at an isolated
region; use a reachability probe and a separate freshness gate, and fence the old writer before
failover. Azure Traffic Manager answers DNS queries, so a client keeps using a cached endpoint
"until the DNS cache expires"; the service cannot move existing connections, and geographic
routing "returns a response whether the endpoint is healthy or not"
([endpoint monitoring](https://learn.microsoft.com/en-us/azure/traffic-manager/traffic-manager-monitoring);
[routing methods](https://learn.microsoft.com/en-us/azure/traffic-manager/traffic-manager-routing-methods)).
When every eligible endpoint is degraded, Traffic Manager makes a "best effort" attempt and
answers as if they were online, so a probe bounds detection but not data freshness. Treat the
multi-location probe as the routing health signal: it is authoritative for reachability, not a
data-freshness signal. Add dependency checks such as database availability where possible; a
200 response does not prove the region's writes are current. Replication is asynchronous across
distant regions, so monitor lag and include it in the recovery design
([multi-region App Service guidance](https://learn.microsoft.com/en-us/azure/architecture/web-apps/guides/multi-region-app-service/multi-region-app-service)).
Before failover, fence the old writer; the sources delegate quorum to the replication backplane
and require conflict handling for bidirectional writes, but they do not prescribe fencing, so
that rule is Tycho guidance
([Geode pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/geodes);
[multiregion network design](https://learn.microsoft.com/en-us/azure/networking/design-guide/multi-region)).
The global router is a critical dependency, but not a proven single point of failure: Azure
Traffic Manager is "a single, global service" designed to be "resilient to a complete failure of
any Azure region" ([Traffic Manager FAQ](https://learn.microsoft.com/en-us/azure/traffic-manager/traffic-manager-faqs)).
The residual risks are stale DNS, long-lived connections and a health signal that does not
reflect data freshness.

**Alternative (Tycho comparison).** Active-passive recovery is the alternative when writes must
stay in one region, state cannot be replicated cheaply, cost prevents full active-active
capacity, or RTO tolerance allows activation time. It keeps one region primary and the other
ready but not serving traffic. The sources name "strict write-region requirements or can't
easily replicate state" and cost constraints, and warn that the passive path can drift
([multiregion network design](https://learn.microsoft.com/en-us/azure/networking/design-guide/multi-region)).
Active-active is justified when both regions can serve any request, the lowest RTO is required,
and conflict resolution and continuous bidirectional replication are affordable. Test failover
and failback, and reverse the choice when cross-region consistency, conflict handling and
routing complexity exceed the locality benefit.

**Limits.** Cross-region replication, conflict resolution and routing health are costs; a stale
route can defeat locality. This is a documentation-based comparison, not a failover, routing,
replication-lag or fencing test.
