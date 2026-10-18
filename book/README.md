# Tycho — System Design

## Purpose and mission

Help readers and AI agents reason about system design: identify constraints, compare alternatives, state assumptions, explain trade-offs, analyze failure, and choose verifiable next steps.

The book should develop engineering judgment rather than prescribe universal architectures. Explain the conditions under which a design works, when it fails, and what evidence could change the recommendation.

## Reading contract

A reader can understand each chapter using the explanations and local links in this repository. Public citations support further verification. No private system knowledge or companion corpus is required.

A [question-driven draft table of contents](PROPOSED-STRUCTURE.md) now maps the research coverage into proposed volume/chapter owners and the first three bounded pilot page slices. The [editorial contract](../authoring/EDITORIAL-CONTRACT.md) and [Pilot wave 01](../authoring/PILOT-WAVE-01.md) govern future bounded pages, source reading and the first three real technical research slices. **The outline is still a proposal, not an approved table of contents.** The first [source-grounded performance chapter](performance/queueing-littles-law.md) and an [outbox/duplicate-effects technical chapter](distributed/transactional-outbox-and-idempotency.md) are written as independently source-grounded drafts; a [safe rollout and recovery chapter](delivery/safe-rollout-and-recovery.md) now extends the first pilot wave; no complete volume, empirical benchmark or independent human review is claimed.

## Available researched entry points

- [Application architecture and quality foundations](application/README.md) — three original evidence-linked pages on quality drivers, modular monoliths, DDD boundaries, SOA/microservices, ports/adapters and safe modernization.
- [Performance and queueing](performance/README.md) — first researched mechanism and measurement boundary.
- [Distributed coordination](distributed/README.md) — causal ordering, consensus, transactions, sagas, outbox, CQRS and projections.
- [Search and retrieval architecture](search/README.md) — inverted indices, SQL FTS, vector/ANN, hybrid ranking and graph-backed evidence.
- [Scaling mechanisms](scaling/README.md) — sharding, connection pooling, cache freshness and overload controls.
- [Data storage and database engines](data/README.md) — PostgreSQL 17 transactions, WAL, replication, query/index choices and comparison of alternative storage models.
- [Messaging and stream processing](integration/README.md) — Kafka, RabbitMQ, Pulsar, NATS, stateful stream processing and CDC, with versioned evidence.
- [Java concurrency and execution](execution/README.md) — platform and virtual threads, Reactor/WebFlux/R2DBC, Netty/Vert.x/Quarkus/Mutiny/RxJava.
- [Deployment and recovery](delivery/README.md) — rollout, compatibility and restoration constraints.

These are **partial topic areas**, not completed volumes or comprehensive architecture recommendations. Source reading, content validation, planned metadata/index/search and independent review are tracked separately.

## Machine-readable knowledge product

The book is also the canonical content for a planned read-only MCP knowledge service. External agents will discover its structure through onboarding, retrieve ranked sections, traverse evidence-backed graphs and verify provenance using versioned snapshots. A shared Rocinante integration package will carry the operating guidance. These are required roadmap outcomes; see the [knowledge-platform plan](../authoring/knowledge-platform-and-mcp-plan.md). They are not implemented yet. The book remains self-contained and locally navigable without MCP.
