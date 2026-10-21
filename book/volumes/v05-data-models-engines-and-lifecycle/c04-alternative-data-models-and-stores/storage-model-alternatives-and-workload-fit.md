---
metadata_version: 1
id: "tycho.page.c75a11f9786442a5b5456f11c2412df4"
kind: "page"
parent_id: "tycho.chapter.4a127ad6ab514ede9ff74394e5174f9c"
canonical_path: "book/volumes/v05-data-models-engines-and-lifecycle/c04-alternative-data-models-and-stores/storage-model-alternatives-and-workload-fit.md"
title: "Storage model alternatives: embedded SQL, distributed SQL, document, wide-column, OLAP, graph and time series"
topic_ids:
  - "data-architecture"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Alternative data models and stores. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "When are document, wide-column, KV, distributed SQL or analytical stores useful?"
  prerequisites: []
  related_ids:
    - "tycho.page.9176c39f97f544f884666e291ae38b90"
    - "tycho.page.ddeff7f1556f44f18c67659b73e6e15f"
    - "tycho.page.ace968ab1de8409383c6a9b22a00d006"
    - "tycho.page.7beb6ba382a1458dbfba5800ff1b53af"
    - "tycho.page.7b980e671a324f769064bc5233761c62"
    - "tycho.page.ee2dd008d4f445eaa9b20998f855a786"
    - "tycho.page.06363f8c9c8244aaa2bbc12abee16fa4"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Storage"
    - "model"
    - "alternatives"
    - "embedded"
    - "SQL"
    - "distributed"
    - "document"
    - "wide-column"
    - "OLAP"
    - "graph"
    - "and"
    - "time"
evidence_scope:
  source_ids:
    - "src.sqlite"
  claim_ids: []
  status: "source-linked"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-18"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.c75a11f9786442a5b5456f11c2412df4:-1 -->

# Storage model alternatives: embedded SQL, distributed SQL, document, wide-column, OLAP, graph and time series

> Tycho Issue [#83](https://github.com/rouslanbaranov/tycho/issues/83). Independent official public documentation inspected on 2026-10-19, versions recorded below. This is a **bounded comparative architecture primer**, not a vendor ranking, empirical TCO calculation or claim of testing production databases.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.c75a11f9786442a5b5456f11c2412df4:0 -->
## Purpose and mission

Storage engines optimize for different **transaction boundaries, access patterns, data layout, query expressiveness, operational footprints and recovery behavior**. "SQL versus NoSQL" is too crude to select one. The first decision should identify the authoritative invariants and representative read/write queries; next, decide whether one data model can serve them or a separately maintained derived view is worthwhile.

**Primary question:** What model trade-offs and operational prerequisites distinguish relational/server, embedded SQL, distributed transactional key-value/SQL, document, wide-column, analytical columnar, graph and time-series data designs?

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.c75a11f9786442a5b5456f11c2412df4:10 -->
## Engineering walkthrough — Four storage choices with disqualifying gates

**Original synthetic workload:** a reservation service must atomically prevent two confirmed allocations for the same physical unit and time interval, expose relational staff joins, support a 24-hour offline export and handle bursts against a few hot resources. The team knows PostgreSQL operations but has no 24/7 expertise for an additional distributed datastore.

| Candidate | Best possible rationale | Gate / disposition |
|---|---|---|
| Single relational authority | Constraints, transactional joins and understood operations | **Conditional fit**; verify scale, hot keys and restore |
| Document store | Flexible nested catalogue descriptions | **Hard fail as replacement** until equivalent cross-booking exclusivity and join/authority plan is proven; viable read projection |
| Wide-column / partitioned KV | High-key-volume access with predicted partition shape | **Not justified** for one extremely hot exclusive key or unmodeled cross-key transaction |
| Distributed SQL | Horizontal SQL with stronger global transaction potential | **Conditional but infeasible under stated ops staffing**, plus test contention/cost |

Separate "a useful additional read model" from "a second authoritative writer". A search index or document projection may accelerate public descriptions while booking correctness stays relational. Moving only query presentation is fundamentally different from moving business mutations to a new engine.

**Failure sequence:** a migration writes a booking to old SQL and attempts the same update in a new store; the second write times out. Neither a success count nor matching row totals can establish atomic cross-store identity. Use one fenced writer plus a versioned projection/reconciliation path, or reject the change. If the relational authority demonstrably cannot meet a hard availability/isolation requirement and sufficient operational support exists, reconsider distributed SQL under measured constraints. The existing official storage references define mechanisms; this shortlist and all capacity assumptions are **synthetic**; no database comparison was executed.


**Verification status:** The preceding original example and its predicted outcomes are synthetic. No implementation experiment, benchmark or independent technical review was executed for this example.
<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.c75a11f9786442a5b5456f11c2412df4:11 -->
## Applied M9 evidence: what transfers and what does not

These examples connect the chapter's conditional mechanism to published experiences or synthetic decision exercises. A historical company report is **first-party, time-scoped evidence**, not a controlled Tycho benchmark; an M9 decision playbook is **original synthetic analysis**, not a company decision.

**Case lens — [Uber — MyRocks](../../../cases/uber-mysql-to-myrocks.md)**. **Relevant mechanism or architectural contrast:** Storage-engine choice must include operational write amplification, workload shape and production rollout gates. **Not established by this report/playbook:** Company-reported MyRocks savings do not transfer to arbitrary datasets, hardware, version or query patterns.

**Case lens — [Discord — Cassandra to ScyllaDB](../../../cases/discord-cassandra-scylladb-messages.md)**. **Relevant mechanism or architectural contrast:** Combining data engine migration with request coalescing addresses hot partitions and latency feedback. **Not established by this report/playbook:** Publisher-reported results cannot isolate the new engine as sole cause or compare equal server resources without adjustment.

**Transfer test:** before applying the lesson to another legacy system, identify the exact workload, source date, relevant runtime/protocol versions, state authority, failure/recovery gate and the new observation that would reverse the choice. Follow the case's public evidence ledger rather than treating its link as independent proof.
<!-- /tycho-question-source -->

## Integrated decision and reading route

Choose a storage model from access patterns, invariant scope and operating constraints, keeping migration costs visible.

Replacing an engine does not remove a hot logical key or a cross-owner transaction requirement.

The detailed pages separate the mechanisms that make this decision conditional:

- [Relational, embedded and transactional key-value models](transactional-models.md) — Which transaction and locality requirements distinguish these storage choices?
- [Document, wide-column and analytical access](specialized-models.md) — Which access pattern justifies specialized modeling and what is lost?
- [Cross-model comparison and synchronization](multi-store-selection.md) — Which extra authority and recovery obligations appear when stores are combined?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
