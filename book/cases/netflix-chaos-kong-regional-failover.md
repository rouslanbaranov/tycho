---
metadata_version: 1
id: "tycho.page.b256d263efff488c8cf549e116be9683"
kind: "page"
parent_id: "tycho.landing.43b3f0c107e34e5a800d6c1de65069e8"
canonical_path: "book/cases/netflix-chaos-kong-regional-failover.md"
title: "Netflix — Chaos Kong: testing application-level regional failure, not shutting down AWS"
topic_ids:
  - "architecture-case-studies"
perspectives:
  - "architecture"
  - "migration"
summary: "Reader entry for Netflix — Chaos Kong: testing application-level regional failure, not shutting down AWS. Scope includes Pressure: a green single-service test can miss regional dependencies; Architecture states and test boundary; Historical result versus experiment design."
route_hints:
  questions:
    - "What are the scope, mechanisms and limits of Netflix — Chaos Kong: testing application-level regional failure, not shutting down AWS?"
  prerequisites: []
  related_ids: []
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Netflix"
    - "Chaos"
    - "Kong"
    - "testing"
    - "application-level"
    - "regional"
    - "failure"
    - "not"
    - "shutting"
    - "down"
    - "AWS"
evidence_scope:
  source_ids:
    - "src.m9-n15"
  claim_ids: []
  status: "unknown"
  notes: "Global source IDs resolve directly through sources/register.json. Evidence-row identities use their own namespaced IDs; source URLs and evidence payloads are preserved. Identity registration does not imply source access, claim-level verification, reproduction rights or independent content acceptance; consult the dated case ledgers."
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

# Netflix — Chaos Kong: testing application-level regional failure, not shutting down AWS

**Case ID:** `case.netflix.chaos-kong-regional-failover` | **M9:** E16-04 #117 | **Status:** historical first-party evidence draft; independent review pending.  
**Source:** src.m9-n15, Ali Basiri, Lorin Hochstein, Abhijit Thosar, Casey Rosenthal (Netflix Chaos Team), [Chaos Engineering Upgraded](https://medium.com/netflix-techblog/chaos-engineering-upgraded-878d341f15fa), **2015-09-25**, sections "Chaos Kong", incident context and original footnote. Secondary provenance checkpoint: [Wave 06 Netflix historical platform source ledger](../../sources/REAL_WORLD_CASES_NETFLIX_PLATFORM_HISTORY_LEDGER.md). Original publisher URL may intermittently time out; this case does not mirror its content or pictures.

## Pressure: a green single-service test can miss regional dependencies

Netflix's multi-zone and multi-region architecture created a real question: whether customer playback and the supporting control plane would continue when infrastructure serving a whole AWS region became unavailable. Terminating one EC2 instance or availability-zone component exercises a different dependency graph from losing an entire region: DNS, discovery, external managed services, authentication, control-plane writes, caching and replay behavior may fail together.

The company distinguished **Chaos Monkey**, historically terminating an instance, from **Chaos Kong**, exercising a *regional outage simulation* at the application/traffic control level. **Crucial negative fact:** the Netflix article's footnote makes clear that Chaos Kong does **not actually switch off a region or all AWS infrastructure**. The resulting observation applies to the simulated failure envelope, not every infrastructure failure mode.

## Architecture states and test boundary

```mermaid
flowchart TD
  C[Customers / regional routing] --> A[Region A services]
  C --> B[Region B services]
  A --> D[Service dependencies and state in Region A]
  B --> E[Service dependencies and state in Region B]
  T[Chaos Kong failure simulation] -.-> X{Pretend Region A unavailable}
  X -.-> C
  X -.-> A
  V[Observability: end-user requests / latency / errors] --> C
  V --> B
```

**Text alternative:** the experiment makes one region behave as though it were unavailable for the chosen service/routing test while observers monitor whether requests move to another region and users remain served. This is an original conceptual sketch, **not** a copy of Netflix's diagram or claim that Netflix had only two regions.

## Historical result versus experiment design

The first-party 2015 discussion describes a regional disruption on **2015-09-20**, when AWS DynamoDB in US-EAST-1 had service issues. Netflix reports it had practiced with regional failure simulations and consequently avoided a major sustained customer-visible outage apart from a brief availability dip. The existence of the simulation and company incident narrative is independently readable historical evidence, **not a scientifically controlled before/after reliability study**. The article does not demonstrate that the same failover would succeed for all later Netflix systems or different AWS failure modes.

| Decision or observation | Evidence boundary | What must not be inferred |
|---|---|---|
| A single-instance failure game and a region simulation test different scopes | src.m9-n15, "Chaos Kong" | That every Netflix service participated in identical tests |
| Chaos Kong simulates region loss rather than physically destroying AWS region resources | src.m9-n15, explanatory footnote | That real provider-side metadata/storage/control-plane failures were necessarily reproduced |
| Engineers linked the preparation to handling the 2015-09-20 DynamoDB disruption | src.m9-n15 incident section | Causal attribution of all improvements or guaranteed future availability |
| End-user resilience rather than only green EC2 status is the metric | src.m9-n15 test intent | Quantified worldwide SLO or independent uptime audit |

## Bounded legacy-to-target migration design for another organization

Suppose a legacy platform runs primarily in Region A and maintains secondary replicated read state in Region B. Begin by mapping consistency and session guarantees, read/write regional authority and system services that cannot survive Region A loss. Adopt multi-region topology *only when* business recovery objectives, data loss tolerance and staffing justify it; otherwise improved backups and single-region multi-AZ failover may be superior.

A safe, independently designed adoption sequence is:

1. Define RTO/RPO targets, read-after-write semantics and failure dependencies. Decide which data may legitimately be stale.
2. Observe a synthetic region-unavailable event in staging, beginning with read-only traffic routing while protecting write authority.
3. Verify identity/signing, DNS/cache TTL, load balancer target changes, cross-region service discovery and data-source availability.
4. Add chaos tests in production only with isolation bounds, a kill switch, preplanned rollback and incident commander; never assume a test cannot itself cause outage.
5. Measure *user outcomes* (successful playable sessions/orders, p99, retry storms), not just resource counts.
6. Test failures outside the original simulation envelope—cross-region networking, correlated credential outage, dependency API quota, data corruption and replay races.

These six steps are **Tycho's synthetic transfer controls**, not a report of Netflix's exact operational runbook.

## Failure injection has a defined envelope, not unlimited coverage

A regional exercise is meaningful only if its **fault boundary is explicit**. The src.m9-n15 narrative dates Netflix's Chaos Kong work to 2015 and describes an application-level regional-loss simulation; it expressly does not shut down the physical AWS region. Thus a passing result concerns **traffic and dependencies that were actually redirected or suppressed**, not hypothetical failures of globally shared identity, cross-region control planes or every durable datastore.

For another system, the decision should be written as a statement of exactly what is disrupted: *which clients lose which region? which reads are allowed to become stale? which region owns writes? which shared services remain healthy?* Without that scope, success can mask the very global dependency a multi-region design is intended to eliminate.

| Candidate test envelope (Tycho synthetic) | What it proves if measured successfully | Significant blind spot |
|---|---|---|
| Route new client traffic away from region A | Traffic controller and receiving region accept eligible requests | Existing sessions, in-flight writes and global dependencies |
| Make region-A service calls fail | Callers correctly time out, retry or degrade for those endpoints | A real whole-region outage may also remove identity or discovery |
| Delay or partition inter-region replication | Secondary catches up or obeys bounded-staleness contract | Simultaneous promotion can create conflicting writes |
| Fail shared regional control-plane APIs | Application can continue or explicitly refuse operations without them | Provider-level DNS, external credentials and unrelated managed services |
| Disable the entire simulated region during live traffic | Selected end-to-end user journeys maintain agreed RTO/RPO and SLO | Does not prove all provider infrastructure was really unavailable |

The table is an **original test model**, not five reported experiments Netflix necessarily performed. It makes the distinction between *simulation fidelity* and *observed user benefit* independently reviewable.

## Write authority and the recovery contradiction

A secondary region can serve read-only degraded traffic before it can safely become a writer. Promoting writers requires a policy for **in-flight acknowledgments**, replica lag, ordering, globally unique identifiers, replay idempotency and a recovery model when the former primary returns. An active-active system further requires conflict rules that match domain semantics; last-write-wins may be unacceptable for some mutable state.

A fictitious acceptance exercise should stage two adversarial states: a write acknowledged in A but not visible in B when the failover begins, and a stale client still sending mutations to A after B has been promoted. Define whether to reject, forward, compensate or reconcile those writes, with **measured loss/recovery windows**, not a guessed “zero RPO.” The src.m9-n15 post does not publish Netflix's complete write-ownership mechanics or a cryptographic proof of no lost writes.

## Original engineering decision and staged verification

Before investing in multi-region complexity, a different platform should compare a cheaper **single-region multi-AZ** deployment and practiced backup restoration. If the requirement truly demands regional continuity, first implement dependency discovery and runbooks, then shadow routing of read-only cohorts, then controlled region unavailable tests within bounded blast radius, and only later tests of write promotion, replication lag and regional return. Every stage has a stop switch and an incident owner.

Metrics include completed end-user journeys, abandoned session count, p99 at failover, RTO, recovery point, retry amplification, authentication failures, routing convergence, and restoration correctness. If an experiment uses a prepared simulated region switch, report **the injection method and unaffected services** with the result.

**Do not conclude:** “Chaos Kong proves an AWS region outage cannot affect customers.” The reported September 2015 DynamoDB incident is supporting historical context, not a controlled guarantee for all future faults. The independent source-review gate remains open, especially because the src.m9-n15 original has intermittent access and its precise version is not pinned.

## Alternatives, counterexamples, and failure criteria

| Choice | Correct when | Risk |
|---|---|---|
| Multi-AZ inside one region | RTO/RPO are modest and whole-region event is tolerable | Still subject to region-wide services |
| Multi-region active/passive | Regional recovery required, moderate operational complexity | Cold failover, promotion correctness and staleness |
| Multi-region active/active | Need regional continuity and workloads permit split ownership | Cross-region consistency, split brain, billing/storage expense |
| Chaos Kong-like simulation | Want to verify selected failover routing/dependencies | Does **not** reproduce physically all provider failure modes |

**Decision reversal:** When failover shows dependent services retaining stale primary endpoints or a secondary database lacking current writes, do not declare production multi-region readiness; restore normal routing and close the gap first.

**Unknowns:** exact fault-injection API, full run manifest, source-code revision, all regions participating, per-service latency/recovery distributions and independent incident analysis. Case remains **draft** until #121 technical review; src.m9-n15 source is admitted only as a dated narrative, not a universal availability benchmark.