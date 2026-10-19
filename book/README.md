# Tycho — System Design

## Purpose and mission

Help readers and AI agents reason about system design: identify constraints, compare alternatives, state assumptions, explain trade-offs, analyze failure, and choose verifiable next steps.

The book should develop engineering judgment rather than prescribe universal architectures. Explain the conditions under which a design works, when it fails, and what evidence could change the recommendation.

## Reading contract

A reader can understand each chapter using the explanations and local links in this repository. Public citations support further verification. No private system knowledge or companion corpus is required.

A [question-driven draft table of contents](PROPOSED-STRUCTURE.md) defines 10 planned volumes and 69 chapter questions. The active [content-completeness matrix](../authoring/BOOK_COMPLETENESS_AUDIT.md) compares them with the existing researched prose; the feature-branch assessment is **69 directly addressed questions, 0 partially addressed questions and 0 without any focused book treatment**, after a series of independently sourced chapter drafts. This is **topical coverage only**: many original research pages span multiple planned chapters, and **69 final, independently validated chapter units do not yet exist**. The corpus remains grouped in topical folders rather than final Volume → Chapter → Page directories. [Issue #213](https://github.com/rouslanbaranov/tycho/issues/213) owns full content completion, followed by [Issue #214](https://github.com/rouslanbaranov/tycho/issues/214) for edition assembly, authoritative navigation and release. The [editorial contract](../authoring/EDITORIAL-CONTRACT.md) and [research workflow](../authoring/RESEARCH-WORKFLOW.md) continue to govern bounded original prose, sources, diagrams and validation.

## Available researched entry points

- [Application architecture, evidence and quality foundations](application/README.md) — context and views, hypothesis/evidence discipline, domain/module boundaries, SOA/microservices, ports/adapters and safe modernization.
- [Performance, workload and queueing](performance/README.md) — arrival models, queueing, scaling laws, cost/capacity, tail latency, load-test validity and overload contracts.
- [Distributed coordination](distributed/README.md) — causal ordering, quorum and leader-change failure modes, transactions, sagas, outbox, CQRS and projections.
- [Search and retrieval architecture](search/README.md) — inverted indices, SQL FTS, vector/ANN, hybrid ranking, graph data models as educational material, and retrieval evaluation.
- [Scaling mechanisms](scaling/README.md) — sharding, connection pooling, cache freshness and overload controls.
- [Data storage and database engines](data/README.md) — PostgreSQL 17 transactions, WAL, replication, query/index choices and comparison of alternative storage models.
- [Messaging and stream processing](integration/README.md) — Kafka, RabbitMQ, Pulsar, NATS, stateful stream processing and CDC, with versioned evidence.
- [Java concurrency and execution](execution/README.md) — platform and virtual threads, Reactor/WebFlux/R2DBC, Netty/Vert.x/Quarkus/Mutiny/RxJava.
- [Deployment and recovery](delivery/README.md) — rollout, compatibility and restoration constraints.
- [Runtime topology and disaster recovery](deployment/README.md) — control-plane/data-plane limits, failure domains and region recovery decisions.
- [Observability and incident response](observability/README.md) — SLOs, metrics, traces, lineage, audit and original incident response model.
- [Security and safe agent-accessible knowledge](security/README.md) — identity, object authorization, untrusted source boundaries and data privacy as System Design topics.
- [Architecture decision and modernization guidance](decisions/README.md) — source-grounded requirements, legacy baseline, pattern applicability and progressive evidence-first question routes.

These are **draft research areas**, not 10 finalized volumes or a published 69-chapter edition. The [69-chapter completeness audit](../authoring/BOOK_COMPLETENESS_AUDIT.md) records what remains partial and unreviewed. Source reading, content validation, planned metadata/index/search and independent review are tracked separately.

## Machine-readable knowledge product

The book is also the canonical content for a planned read-only MCP knowledge service. External agents will discover its structure through onboarding, retrieve ranked sections, verify source-to-claim provenance and browse typed metadata/navigation using versioned snapshots. A shared Rocinante integration package will carry the operating guidance. These are required roadmap outcomes; see the [knowledge-platform plan](../authoring/knowledge-platform-and-mcp-plan.md). The hosted service and full evaluation are not implemented; foundational schemas and some deterministic routing/validation tooling already exist, with current coverage and test limits recorded separately. A manually curated concept graph is not in Tycho's delivery scope. The book remains self-contained and locally navigable without MCP.
