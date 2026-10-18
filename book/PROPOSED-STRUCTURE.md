# Tycho — proposed question-driven book structure

Status: **proposal for Issue #23**, 2026-10-18. This is an authoring/navigation plan, **not** completed chapters, reviewed technical claims, approved JSON metadata IDs, or a commitment to replicate another book's numbering. Existing `book/README.md` remains the current canonical entry until a structure is accepted.

## Audience and use cases

- **Engineers and architects:** trace how mechanisms operate, where guarantees stop, how to validate behavior and what fails at load.
- **Engineers modernizing systems:** compare observable baseline constraints and migration options without treating distributed architectures as automatic upgrades.
- **SRE/platform/data/security engineers:** find operational prerequisites, failure/recovery modes, cost and observability consequences.
- **External AI agents:** retrieve a bounded canonical explanation, follow stable links to evidence and understand unknowns without downloading a whole volume.

The essential questions are: *What problem does this mechanism solve? Under which workload and failure assumptions? What alternatives exist? What evidence substantiates the claimed behavior? What changes for deployment, recovery and maintenance?* No chapter is an unconditional product recommendation.

## Structure rules for this draft

1. The hierarchy is **Book → Volume → Chapter → bounded section/page**. Only create pages when a real research contract has sufficiently narrow scope; do not manufacture a fixed chapter/page count or empty files.
2. Each volume has a **Purpose and Mission** landing page. Each chapter owns one canonical mechanism or tightly coupled decision question. Other chapters refer to it, adding only local consequences.
3. Proposed IDs (`V01/C01`, etc.) are **planning locators, not finalized persistent document IDs**. The eventual metadata/identity design is issue #32.
4. Pages will progress from **Orientation → Architecture → Evidence**, including assumptions, normal/failure/recovery, invariants and counterexamples when material. The detailed editorial templates are owned by #24.
5. Public specification, versioned implementation documentation, reproducible test and model-derived inference must remain separate types of evidence. All technical chapter claims are **pending research** until exact sources are inspected.
6. The proposed architecture-decision volume comes **after** the technical and operational chapters in research dependency order. Cross-book question routes are entry points, not replacements for canonical material.

## Proposed volumes and chapter ownership

### V01 — Requirements, quality attributes and architecture fundamentals

**Mission:** translate a problem into observable behavior, constraints and competing qualities without naming a solution prematurely.

| Draft chapter | Canonical question |
|---|---|
| C01 — Problem framing and system boundaries | Which actors, outcomes, interfaces and external failure dependencies define the system? |
| C02 — Workload and demand models | How do active users, offered arrivals, concurrency, operation mix and skew differ? |
| C03 — Quality attributes and trade-offs | How are performance, availability, consistency, cost, security and changeability made measurable? |
| C04 — Evidence, hypotheses and architecture experiments | What do sources, estimates, simulations and measurements actually prove? |
| C05 — Architecture descriptions and decision records | What belongs in diagrams, views, assumptions, ADRs and source-linked evidence? |
| C06 — Capacity, operational constraints and total cost | Which hard gates and team/budget limits invalidate otherwise appealing options? |

### V02 — Application boundaries and interaction contracts

**Mission:** decide responsibilities and system boundaries before distributing them.

| Draft chapter | Canonical question |
|---|---|
| C01 — Layered, modular and ports-and-adapters design | How are dependencies directed and replaceable? |
| C02 — Domain boundaries, data ownership and contracts | When should business capabilities form module or service boundaries? |
| C03 — Modular monolith and internal events | Which coupling and deployment constraints fit an in-process architecture? |
| C04 — SOA, microservices and distributed boundaries | When is independent deployment justified by measured coordination cost? |
| C05 — Public APIs, HTTP/RPC and compatibility | How do deadlines, versioning, retries and API contracts evolve? |
| C06 — Integration adapters and anti-corruption boundaries | How can incompatible domains and legacy contracts coexist? |
| C07 — Authorization boundaries and multitenancy | What must be isolated between clients, organizations and data owners? |

### V03 — Execution models, concurrency and flow control

**Mission:** explain the execution and resource budgets behind a request.

| Draft chapter | Canonical question |
|---|---|
| C01 — Threads, tasks and coordination | What creates concurrency and which shared state creates contention? |
| C02 — Java execution and virtual threads | What improves concurrency without creating downstream capacity? |
| C03 — Reactive streams, demand and cancellation | How do backpressure, scheduling and blocking boundaries affect execution? |
| C04 — Asynchronous APIs and streaming | Which flow and cancellation semantics are required across protocols? |
| C05 — Thread, connection and buffer pools | How do pool sizes, queues and timeouts compose across layers? |
| C06 — Memory, GC, CPU and blocking diagnostics | How should bottleneck observations constrain execution-model choice? |

### V04 — Distributed coordination and event integration

**Mission:** describe what can and cannot be guaranteed across failure-prone boundaries.

| Draft chapter | Canonical question |
|---|---|
| C01 — Time, causality and ordering | Which ordering can a distributed system observe or guarantee? |
| C02 — Replication, consensus and leader changes | Which failure assumptions sustain agreement or availability? |
| C03 — Consistency and distributed transactions | Which invariants need coordination, isolation or reconciliation? |
| C04 — Retries, idempotency and duplicate effects | Which side effects survive retries and ambiguous acknowledgements? |
| C05 — Outbox, inbox, sagas and durable workflows | How are state changes coordinated without claiming global atomicity? |
| C06 — Messaging families and delivery contracts | What are the consequences of acknowledgement, retention and consumer state? |
| C07 — Kafka logs, partitions and transactions | What do producer/consumer guarantees cover and what stays at application level? |
| C08 — Stateful/event-time stream processing | How do replay, watermarks, state stores and recovery shape correctness? |

### V05 — Data models, engines and lifecycle

**Mission:** connect data integrity, workload, engine internals and deployment costs.

| Draft chapter | Canonical question |
|---|---|
| C01 — Relational modeling and transaction isolation | Which invariants and anomalies are relevant to the data contract? |
| C02 — PostgreSQL MVCC, WAL and recovery | What are the consequences of durability, vacuum and replication mechanisms? |
| C03 — Query planning, indexes and access paths | Which read/write trade-offs explain an observed query plan? |
| C04 — Alternative data models and stores | When are document, wide-column, KV, distributed SQL or analytical stores useful? |
| C05 — Partitioning, sharding and rebalancing | How do hot keys, routing, joins and ownership affect scale? |
| C06 — Schema evolution, data migration and retention | What compatibility windows and irreversibility constraints exist? |
| C07 — Replication, backups and restore drills | How do consistency, lag, RPO/RTO and restore evidence connect? |

### V06 — Caching, indexing and information retrieval

**Mission:** show why different acceleration and search mechanisms solve different problems.

| Draft chapter | Canonical question |
|---|---|
| C01 — Local and distributed caching | How do authority, freshness, eviction and invalidation differ? |
| C02 — Hot keys, cache stampedes and read amplification | When does adding a cache worsen recovery or contention? |
| C03 — Lexical full-text indexing and ranking | Which queries need tokenization, inverted indexes, BM25 or filtering? |
| C04 — Vector embeddings and nearest-neighbor retrieval | What are exact versus approximate search and recall trade-offs? |
| C05 — Hybrid retrieval and reranking | When do fusion and metadata filters improve measured relevance? |
| C06 — Graph relationships and traversal | When is explicit typed connectivity preferable to lexical or vector similarity? |
| C07 — Retrieval evaluation and index lifecycle | How are index freshness, reproducibility, latency and result quality measured? |

### V07 — Performance, scale and resilience under load

**Mission:** connect load and failure conditions to observed limits, avoiding universal thresholds.

| Draft chapter | Canonical question |
|---|---|
| C01 — Queueing, Little's Law and measurement boundaries | What do arrival, throughput, mean response and in-flight counts imply? |
| C02 — Contention, saturation and scaling laws | When does coordination dominate additional capacity? |
| C03 — Load-test methods and benchmark validity | How do open/closed arrivals, warmup and coordinated omission bias conclusions? |
| C04 — Tail latency, fan-out and time budgets | Why can p99 degrade despite adequate mean capacity? |
| C05 — Overload protection and graceful degradation | How should admissions, queues, retries and shedding be bounded? |
| C06 — Horizontal/vertical scaling and autoscaling delay | Which headroom, statefulness and failure assumptions shape capacity? |
| C07 — Capacity planning and cost/performance trade-offs | What experiments can confirm or falsify a scaling hypothesis? |

### V08 — Delivery, deployment and disaster recovery

**Mission:** distinguish producing deployable software from safely releasing and operating it.

| Draft chapter | Canonical question |
|---|---|
| C01 — CI/CD architecture and artifact provenance | Which boundaries separate build, test, publication and production deployment? |
| C02 — Supply chain and release verification | How are reproducibility, signatures and promotion controls established? |
| C03 — VMs, containers, orchestration and serverless | Which topology suits operational and workload requirements? |
| C04 — GitOps, rollout and progressive delivery | How do rolling, blue/green, canary, rollback and analysis gates differ? |
| C05 — Backward-compatible database change | What permits old and new binaries/data schemas to coexist? |
| C06 — High availability and failure-domain placement | What survives machine, zone, dependency or region loss? |
| C07 — Multi-region recovery and data reconciliation | How are RPO/RTO, split brain, recovery routes and failback validated? |

### V09 — Observability, security and operational architecture

**Mission:** make system behavior measurable, operable and bounded by explicit security constraints.

| Draft chapter | Canonical question |
|---|---|
| C01 — SLIs, SLOs and error budgets | Which user outcomes are measured and how do budgets guide changes? |
| C02 — Metrics ingestion, cardinality and time-series storage | How do scrape/push, temporality, labels, retention and scale interact? |
| C03 — Distributed tracing and propagation | Which context, sampling and async boundaries determine trace usefulness? |
| C04 — Logging, audit and lineage | How do security audit, event lineage and operational logs differ? |
| C05 — Identity, authorization and threat modeling | Where do trust boundaries and permission checks have to sit? |
| C06 — Incident response and operational change | What evidence distinguishes recovery, mitigation and restored guarantees? |
| C07 — Safety, isolation and privacy in agent-accessible services | What can remote readers infer or retrieve under bounded permissions? |

### V10 — Decision support and modernization playbooks

**Mission:** apply validated knowledge to constrained choices while allowing “measure first”, “retain design” and “insufficient evidence” outcomes.

| Draft chapter | Canonical question |
|---|---|
| C01 — Architecture requirement and workload profiles | What inputs are required before comparing candidate patterns? |
| C02 — Baseline analysis for existing software | Which observed limitations justify changing the architecture? |
| C03 — Pattern applicability and contraindications | Which evidence, preconditions and failures bound a pattern's usefulness? |
| C04 — Alternatives, experiments and ADRs | Which hypotheses distinguish feasible options under hard constraints? |
| C05 — Target architecture versus transition states | What is safe during coexistence, migration, rollback and recovery? |
| C06 — Search and question routes for architecture agents | How can requirements, symptoms and evidence guide selective reading? |
| C07 — Cross-domain worked comparisons and unresolved cases | How does a decision stay falsifiable and attributable to its sources? |

## Proposed first page-level research slices

These are **three real authoring targets**, not placeholders to commit until the relevant primary sources have been read. Chapters own the following bounded pages initially:

| Pilot chapter owner | First bounded page | Second bounded page | Third bounded page |
|---|---|---|---|
| V07/C01, queueing and demand | Arrival and completion boundary definitions, with distributions and units | Little's Law applicability and finite-window caveats | Capacity diagnosis, overload counterexamples and experiments |
| V04/C04–C05, cross-system events | Local transaction, outbox and publication timeline | Delivery/replay/consumer idempotency and duplicate effects | Failure matrix, recovery and alternative mechanisms |
| V08/C04–C07, rollback and recovery | Rollout/compatibility timeline, target versus transition | Failure-domain, backup and recovery checks | Go/no-go, observability, irreversibility and unresolved evidence |

Each page will contain orientation, a bounded mechanism or failure scenario, and exact public provenance. Do not assume three pages are sufficient; split only to maintain bounded context and precise ownership. This **does not replace** the editorial standards of #24, research contracts of #26 or evidence controls of #27–#37.

## Mandatory research-track ownership

Each track below has one primary home; multiple chapters may link to it without copying its core explanation.

| Required track | Primary owner | Secondary context |
|---|---|---|
| Kafka, ordering and transactions | V04/C07 | V04/C04–C06; V05/C06 |
| Reactive Java / backpressure | V03/C03 | V03/C04–C06 |
| Java virtual threads / concurrency | V03/C01–C02 | V03/C05–C06 |
| PostgreSQL/MVCC/WAL | V05/C01–C03 | V05/C06–C07 |
| Sharding and rebalancing | V05/C05 | V07/C02/C06 |
| Connection and thread pooling | V03/C05 | V07/C05 |
| Local/distributed caching | V06/C01–C02 | V05/C03 |
| Full-text / vector / hybrid / graph search | V06/C03–C07 | V09/C02 |
| Load, queues, high throughput and tail latency | V07/C01–C05 | V03/C05 |
| Autoscaling and capacity | V07/C06–C07 | V08/C03/C06 |
| CI/CD and supply chain | V08/C01–C02 | V08/C04 |
| Deployment patterns, GitOps and migrations | V08/C03–C05 | V05/C06 |
| Multi-region resilience, disaster recovery | V08/C06–C07 | V05/C07 |
| Metric pipelines, traces, audit, lineage | V09/C01–C04 | V06/C07 |
| Architecture comparisons and modernization | V10/C01–C07 | V01/C01–C06 |
| Security, isolation and data protection | V09/C05/C07 | V02/C07; V08/C02 |

## Reader / agent routes (provisional, question-first)

| Incoming question | Load first | Expand as required |
|---|---|---|
| “How many RPS is N users?” | V01/C02; V07/C01 | V07/C03, specific measured system constraints |
| “Monolith or microservices for these requirements?” | V01/C03; V02/C03–C04 | V10/C03–C04 when evidence cards exist |
| “Could a database pool or Kafka partition be overloaded?” | V03/C05; V04/C07 | V05/C03/C05; V07/C02/C05 |
| “How to avoid duplicates after timeout and retry?” | V04/C04–C05 | V04/C07; V05/C01; V08/C05 |
| “Should search use Lucene, vectors, or graph?” | V06/C03–C07 | V07/C03; V01/C03 |
| “How to deploy with no irreversible data loss?” | V08/C04–C07 | V05/C06–C07; V10/C05 |
| “Why did metrics/storage costs explode?” | V09/C02 | V07/C07; V03/C05 |
| “How to modernize an existing application safely?” | V10/C02 | V01/C01–C04; V08/C04–C07 |

These are **future routes**. There is no generated index, working route CLI, populated chapter content or evidence graph yet. Do not present navigation links as live until the corresponding chapters exist.

## First real content, not further meta-design

Once #24–#26 provide **minimal** authoring/research contracts, initiate three bounded, evidence-backed chapters:

1. **Mechanism pilot — V07/C01**: queueing, arrival rate, throughput and Little's Law with exact primary/public reading, conditional derivations and load-measurement limitations (#38).
2. **End-to-end pilot — V04/C04–C05**: independent transactional state change, idempotency, outbox/event publication, duplicate/recovery boundaries (#39).
3. **Recovery pilot — V08/C04–C07**: one synthetic failed deployment/failure domain with recovery checks and explicit unknowns (#40).

The research topics are now selected as **bounded proposed contracts** by [#26](../authoring/PILOT-WAVE-01.md), with independent source-reading and chapter acceptance still pending. The structure itself remains a proposed table of contents. The pilot creates actual technical pages and evidence. The comprehensive decision-pattern corpus (#18/#19) is deliberately not a prerequisite for the first material: refine it from researched case studies rather than filling generic applicability cards first.

## Gaps and acceptance limits

This is a navigation and scope proposal grounded in the [coverage map](../sources/COVERAGE.md), [implementation families](../sources/IMPLEMENTATIONS.md) and [reading plan](../sources/READING-PLAN.md), all of which are **discovery-stage inventories**. No books, papers, source repositories or implementations were fully researched for this issue. Technology coverage does not mean technology behavior is established.

The proposed chapter count is intentionally revisable. Topics such as accessibility/HCI, regulatory controls, specialized ML serving and geographical data may warrant deeper treatment as independent public sources are admitted. Resolve disputed canonical ownership through a bounded research contract, not title duplication. Detailed metadata/schema and complete title/page hierarchy will follow evidence and issue #32; this table is not a published book catalogue.
