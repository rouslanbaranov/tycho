---
metadata_version: 1
id: "tycho.page.02238832b395417bae63939cd96b9134"
kind: "page"
parent_id: "tycho.chapter.d5b789c9cd7e4cb693c22943423531c2"
canonical_path: "book/volumes/v03-execution-concurrency-and-flow-control/c02-java-execution-and-virtual-threads/platform-threads-executors-and-virtual-threads.md"
title: "Platform-thread executors and virtual-thread capacity"
topic_ids:
  - "execution-models"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Java execution and virtual threads. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "What improves concurrency without creating downstream capacity?"
  prerequisites: []
  related_ids:
    - "tycho.page.a9a28aaa4d1e4e9cb0accd2fc2c5ba9b"
    - "tycho.page.ace968ab1de8409383c6a9b22a00d006"
    - "tycho.page.c33e9e4b605a4aa3b073a9f91437fc26"
    - "tycho.page.c880ba1a0a594ad38d6713d198e46436"
    - "tycho.page.f5efc4fa96e242b59ddcd80a48c54af4"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Platform-thread"
    - "executors"
    - "and"
    - "virtual-thread"
    - "capacity"
evidence_scope:
  source_ids:
    - "src.jep444"
    - "src.jep491"
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
<!-- tycho-question-source:tycho.page.02238832b395417bae63939cd96b9134:-1 -->

# Platform-thread executors and virtual-thread capacity

> **Tycho #82, public research inspected 2026-10-18.** Scope: OpenJDK JEP 444 (JDK 21), OpenJDK JEP 491 implementation discussion (JDK 24), Spring Boot 3.3.13. Original design reasoning and synthetic examples; no Java code was executed, no load test or independent human review occurred.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.02238832b395417bae63939cd96b9134:7 -->
## Applied M9 evidence: what transfers and what does not

These examples connect the chapter's conditional mechanism to published experiences or synthetic decision exercises. A historical company report is **first-party, time-scoped evidence**, not a controlled Tycho benchmark; an M9 decision playbook is **original synthetic analysis**, not a company decision.

**Case lens — [Netflix — Java platform convergence][platform].** **Relevant mechanism or
architectural contrast:** Separate GraphQL
composition and Java platform modernization; staged compatibility changes coordination
ownership. **Not established by this report/playbook:** The historical talk and later abstract
do not establish a universal RxJava-versus-Spring performance ranking or identical fleet
versions.

**Case lens — [Netflix — Java 21 virtual-thread pinning][pinning].** **Relevant mechanism or
architectural contrast:** JDK 21 monitor pinning
makes synchronization and tracing part of concurrency acceptance. **Not established by this
report/playbook:** The JEP mechanism is not a failure rate and must not be extrapolated
unchanged to later JDKs.

**Transfer test:** before applying the lesson to another legacy system, identify the exact workload, source date, relevant runtime/protocol versions, state authority, failure/recovery gate and the new observation that would reverse the choice. Follow the case's public evidence ledger rather than treating its link as independent proof.
<!-- /tycho-question-source -->

## Integrated decision and reading route

Choose execution resources with explicit downstream permits and release-specific blocking assumptions.

Cheaper waiting can increase demand on a saturated connection pool; replacing platform threads with virtual threads does not create database capacity.

The detailed pages separate the mechanisms that make this decision conditional:

- [Platform executors and queue budgets](platform-pools.md) — Which queue, deadline and resource assumptions govern a platform-thread executor?
- [Virtual threads and release-specific pinning](virtual-threads.md) — What changes with virtual threads and which downstream limits stay finite?
- [Context, cancellation and framework integration](context-cancellation.md) — How do execution choices propagate context and handle effects after a caller stops waiting?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.

[platform]: ../../../cases/netflix-java-platform-convergence.md
[pinning]: ../../../cases/netflix-java21-virtual-thread-pinning.md
