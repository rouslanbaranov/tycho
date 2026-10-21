---
metadata_version: 1
id: "tycho.page.7ad835c06d5a4e3aabf6b14632f92c86"
kind: "page"
parent_id: "tycho.chapter.4cbc9e1582404965b696a63b79a66e93"
canonical_path: "book/volumes/v07-performance-scale-and-resilience/c02-contention-saturation-and-scaling-laws/contention-saturation-and-scaling-laws.md"
title: "Contention, saturation and scalability laws: distinguishing capacity limits"
topic_ids:
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Integrated question, original scenario and transfer limits for Contention, saturation and scaling laws. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "When does coordination dominate additional capacity?"
  prerequisites: []
  related_ids:
    - "tycho.page.a9a28aaa4d1e4e9cb0accd2fc2c5ba9b"
    - "tycho.page.fdb4ef7f69154f8c8c433591f71494f9"
    - "tycho.page.1cfb9cfdf1604fada0f508c123fe8b2e"
    - "tycho.page.0d34dd26886340b89fd4f1499d790a81"
    - "tycho.page.c5d20ae7ef6445e5b23dd5fbac625060"
    - "tycho.page.f784d6ef723c4c0e8836ff9085bf7dcc"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.b08f16ced4a142a785c37b43eb340260"
    - "tycho.page.dc2470904e004a4aa733abcdb25517ed"
    - "tycho.page.49d9df04c0b4488e936b02e580a62271"
    - "tycho.page.af6ce1d0b08a46bf908f851f77f7bb12"
    - "tycho.page.61c621bfa9a04a738e937416cec15e78"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Contention"
    - "saturation"
    - "and"
    - "scalability"
    - "laws"
    - "distinguishing"
    - "capacity"
    - "limits"
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
<!-- tycho-question-source:tycho.page.7ad835c06d5a4e3aabf6b14632f92c86:-1 -->

# Contention, saturation and scalability laws: distinguishing capacity limits

> **Tycho V07/C02 draft**, 2026-10-19. Original equations worked under explicit assumptions and invented load examples, not observed performance. Independently public queueing literature and Gunther's Universal Scalability Law paper are cited with narrow scope. No scaling experiment, fit or independently verified hardware benchmark was performed.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.7ad835c06d5a4e3aabf6b14632f92c86:0 -->
## Purpose and mission

An architecture can have many processors and still process work at almost a fixed rate. Some fraction of execution may serialize on a lock or data authority; more concurrent callers may contend for a shared connection, exhaust a quota or induce coherence overhead. The important question is not “Does horizontal scaling work?” but **which scarce resource sets the useful completion rate for this workload, and what measurable mechanism limits further growth?**

This chapter explains serial fractions, queue saturation, hot-key contention and the limited role of fitted scalability curves. [Queueing/Little's Law](../c01-queueing-littles-law-and-measurement-boundaries/queueing-littles-law.md) owns mean resident-work accounting, [workload profiles](../../v01-requirements-and-architecture/c02-workload-and-demand-models/workload-demand-and-arrival-models.md) owns demand/arrival semantics and [benchmark validity](../c03-load-test-methods-and-benchmark-validity/load-testing-and-benchmark-validity.md) owns generator and observation methods.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.7ad835c06d5a4e3aabf6b14632f92c86:10 -->
## Applied M9 evidence: what transfers and what does not

These examples connect the chapter's conditional mechanism to published experiences or synthetic decision exercises. A historical company report is **first-party, time-scoped evidence**, not a controlled Tycho benchmark; an M9 decision playbook is **original synthetic analysis**, not a company decision.

**Case lens — [Netflix — HotSpot sharing](../../../cases/netflix-hotspot-false-true-sharing.md)**. **Relevant mechanism or architectural contrast:** CPU scaling must test true/false sharing at representative offered load, not equal low-load canaries. **Not established by this report/playbook:** HotSpot behavior from the historical version is not evidence of the same bug in current JVMs or all low-CPU-scaling incidents.

**Transfer test:** before applying the lesson to another legacy system, identify the exact workload, source date, relevant runtime/protocol versions, state authority, failure/recovery gate and the new observation that would reverse the choice. Follow the case's public evidence ledger rather than treating its link as independent proof.
<!-- /tycho-question-source -->

## Integrated decision and reading route

Identify serial work, shared-state contention and resource saturation before extrapolating additional workers.

A scaling curve fitted outside the tested range can hide coordination cost; more workers may worsen useful throughput.

The detailed pages separate the mechanisms that make this decision conditional:

- [Parallelism, serial work and scaling models](scaling-models.md) — Which model assumptions bound useful throughput as concurrency grows?
- [Contended authority and discriminating scaling experiments](contention-response.md) — Which observation distinguishes resource saturation from coordination overhead?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
