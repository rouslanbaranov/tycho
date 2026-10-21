---
metadata_version: 1
id: "tycho.page.76244dbe2bd44035b7154f821191f6f2"
kind: "page"
parent_id: "tycho.chapter.bbfd14751d274868b152ba431dc904c9"
canonical_path: "book/volumes/v01-requirements-and-architecture/c06-capacity-operational-constraints-and-total-cost/operational-constraints-and-total-cost-gates.md"
title: "Capacity, operational constraints and total-cost hard gates"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Capacity, operational constraints and total cost. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "Which hard gates and team/budget limits invalidate otherwise appealing options?"
  prerequisites: []
  related_ids:
    - "tycho.page.5ae9f2c4b45842c7975fd32c252dc4d8"
    - "tycho.page.49d9df04c0b4488e936b02e580a62271"
    - "tycho.page.c5d20ae7ef6445e5b23dd5fbac625060"
    - "tycho.page.868027aee4884210bea1d8a6542fbfb0"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.be90d29e1bc04524b2ea41ee9beaab0f"
    - "tycho.page.4318e542ac7e445b9e8b3150effd2cff"
    - "tycho.page.06b70cb83d4f490ea9ef698a025e7684"
    - "tycho.page.fdb4ef7f69154f8c8c433591f71494f9"
    - "tycho.page.f05854fcc406435bbf38a192bc7ab2f1"
    - "tycho.page.8284605817fc48dba499425b0d908df0"
    - "tycho.page.b8d02f9b40c44c729e2b99e01a8b0dbf"
    - "tycho.page.f3b4041502a7403bbc63bb2611eb5c0f"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Capacity"
    - "operational"
    - "constraints"
    - "and"
    - "total-cost"
    - "hard"
    - "gates"
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
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.76244dbe2bd44035b7154f821191f6f2:-1 -->

# Capacity, operational constraints and total-cost hard gates

> **Tycho book draft V01/C06, 2026-10-19.** Independent conceptual treatment of constraints that architecture proposals must pass. Public arc42 constraints and AWS cost design guidance consulted; original fictional scenarios only. No operational team, workload, budget, price, or independent approval was examined.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.76244dbe2bd44035b7154f821191f6f2:0 -->
## Purpose and mission

An architecture can satisfy a theoretical throughput target while being **unfit to operate**. It may require expertise unavailable to the owner, untested disaster recovery, dependencies with incompatible support windows, unrealistic permission boundaries, or costs that exceed an explicit ceiling. These are not optional concerns to apply *after* design selection. They can be **hard architectural gates**.

This foundational chapter answers which organizational, lifecycle, cost and recovery constraints must be established before ranking designs. The [capacity planning and cost/performance chapter](../../v07-performance-scale-and-resilience/c07-capacity-planning-and-cost-performance-trade-offs/capacity-planning-and-cost-performance.md) owns quantitative resource sensitivity. Here the goal is translating operating constraints into explicit decision eligibility.

[arc42 Constraints §2](https://docs.arc42.org/section-2/) treats technical and organizational limits as real inputs to architectural freedom. [AWS Well-Architected Cost Optimization design principles](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html) emphasize attributing costs and measuring outcomes rather than assuming low infrastructure prices imply a lower total burden.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.76244dbe2bd44035b7154f821191f6f2:8 -->
## Engineering walkthrough — Hard constraints before weighted cost scoring

**Original sensitivity calculation, not market prices.** A fictional small team can support one database on-call rotation, 90-day audit retention, and at most one additional operationally critical service. Suppose option A (retain/optimize) uses 60 engineer-days of change and 10 on-call hours per month; B (extract two services) uses 140 engineer-days, 25 on-call hours per month and separate trace/log retention. These are **invented staffing inputs**, not CHF or cloud quotes.

A three-year model should separately carry implementation person-days, recurring operational time, storage/egress/telemetry units, incident/restore drills, migration coexistence, and potential forward repair after incompatible writes. A simplified staffing subtotal might be `A: 60 + 36×10/8 = 105 engineer-days` versus `B: 140 + 36×25/8 = 252.5 engineer-days`, assuming eight-hour days and no escalation overhead. These are lower-bound educational arithmetic, **not total TCO**, which also depends on external cost inputs and availability outcomes.

| Gate | A | B |
|---|---|---|
| Exactly one authoritative booking writer during change | Can preserve | Requires fenced ownership transfer |
| One additional critical service maximum | Pass | Fail if two independently critical services are introduced |
| Audit retention and reproducible restore | Must validate | Must validate in each store/trace domain |
| Expected release autonomy | Lower | Potentially higher, but unmeasured |

**Decision:** exclude B on the stated operational constraint *before* weighted scoring; better potential deployment autonomy cannot erase that gate. If staffing expands or one service replaces a retired critical dependency, re-evaluate with real cost/incident data. Under another requirement set the decision may reverse. No financial estimate, observed labor or vendor offer is claimed.


**Verification status:** The preceding original example and its predicted outcomes are synthetic. No implementation experiment, benchmark or independent technical review was executed for this example.
### Sensitivity across retention, coexistence and no-return recovery (original synthetic units)

The earlier staffing totals are a **lower-bound component** of lifecycle effort, not vendor TCO. Hold a 36-month horizon and an illustrative audit payload of **1 GiB/day** constant. Assume **one logical retained copy** for this toy comparison, no compression, identical user outcomes and no real cloud price:

| Dimension | A: retain and optimize | B: extract two services | Interpretation |
|---|---:|---:|---|
| Initial work + 36-month on-call | 105 engineer-days | 252.5 engineer-days | The preceding arithmetic, not money |
| 90-day audit rolling window | 90 GiB | 270 GiB, if three independent 1-GiB/day audit streams are needed | **Inventory assumption**, not an inherent property of service extraction |
| Temporary coexistence for 45 days | 0 extra GiB assumed | 45 extra GiB at 1 GiB/day if an additional shadow copy is retained | Temporary capacity, not perpetual retained volume |
| Recovery after an incompatible persisted write | 0–10 engineer-days if the original representation remains readable | 20–80 engineer-days in a hypothetical forced forward-repair | A *risk range*, not expected effort or guaranteed outcome |

All storage numbers are *invented, logical GiB*, not price quotes or physical volume provisioned; real retention may require backups, replicas, compression, and legal deletion. At **365-day** rather than 90-day retention, the illustrative storage windows become **365 GiB A** versus **1,095 GiB B** before replication. If a storage-specific rate is later supplied, use **GiB-month × authorized price per GiB-month** with the same replication/retention policy, rather than pretending GiB equals CHF. A steady-state rolling window approaches those quantities after its retention horizon; the exact integral over 36 months depends on ramp-up, deletion and coexistence dates.

**Sensitivity and reversal:** in the initially stated small-team scenario, B already **fails the hard limit on additional critical services**, irrespective of its autonomy score or a cheap storage quote; the **correct disposition is infeasible**, not “B loses by 147.5 engineer-days.” If owners raise that cap and *require genuinely independent deployment and credential isolation*, B becomes eligible **conditionally** after testing business authority, restore paths and operations. If retention rises to 365 days or repair risk widens, B's relative resource burden grows under this model; if independently deployable components replace existing systems and reduce duplicated streams, B's assumed tripled audit volume ceases to be valid and must be recalculated. This is a falsifiable sensitivity exercise, not a forecast or a performed incident repair.

**Gate:** request real workload, data growth, audit semantics, legal retention, owner-approved staffing rates, reconciliation method, replication/backup policy and restore drill before converting this table into a financial decision. Quantitative unit-cost optimization across throughput/capacity belongs to [V07/C07](../../v07-performance-scale-and-resilience/c07-capacity-planning-and-cost-performance-trade-offs/capacity-planning-and-cost-performance.md), not to this hard-constraint decision.

<!-- /tycho-question-source -->

## Integrated decision and reading route

Reject candidates that exceed an explicit operating, recovery, staffing or total-cost constraint before ranking attractive features.

A low instance price can conceal migration, dual-running and rollback costs; uncertain inputs must remain uncertain instead of becoming precise forecasts.

The detailed pages separate the mechanisms that make this decision conditional:

- [Feasibility before preference scoring](feasibility-gates.md) — Which hard constraint makes a candidate inadmissible regardless of its score?
- [Lifecycle cost and sensitivity](lifecycle-cost.md) — Which migration, dual-running and rollback costs can reverse a cost comparison?
- [Operating capability and readiness](operating-capacity.md) — Which capacity, ownership and recovery constraints must be demonstrated before adoption?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
