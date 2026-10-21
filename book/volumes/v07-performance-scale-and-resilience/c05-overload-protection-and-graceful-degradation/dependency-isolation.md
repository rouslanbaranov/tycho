---
metadata_version: 1
id: "tycho.page.80ab784dafed47a7baf31722fce5eabc"
kind: "page"
parent_id: "tycho.chapter.0718556e0eb14d499adbbe67073327df"
canonical_path: "book/volumes/v07-performance-scale-and-resilience/c05-overload-protection-and-graceful-degradation/dependency-isolation.md"
title: "Bulkheads, retries and optional dependencies"
topic_ids:
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How can failure in optional work starve core work?"
route_hints:
  questions:
    - "How can failure in optional work starve core work?"
  prerequisites:
    - "tycho.page.d9abd43bb7394c04a6bf77d4014f870d"
  related_ids:
    - "tycho.chapter.0718556e0eb14d499adbbe67073327df"
    - "tycho.page.c5d20ae7ef6445e5b23dd5fbac625060"
    - "tycho.page.62ad1ae9e0d243d69b08be0ff32930a1"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "dependency"
    - "isolation"
evidence_scope:
  source_ids:
    - "src.aws-backoff"
    - "src.sre-overload"
  claim_ids: []
  status: "source-linked"
  notes: "Bounded question from tycho.page.c5d20ae7ef6445e5b23dd5fbac625060; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-21"
source_inspection_date: null
content_verified_at: null
---
# Bulkheads, retries and optional dependencies

**Owning question:** How can failure in optional work starve core work?

This page belongs to [V07/C05 — Overload protection and graceful degradation](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.c5d20ae7ef6445e5b23dd5fbac625060:4 -->
## 4. Bulkheads, circuit breakers and retries have different responsibilities

| Control | Primary purpose | Dangerous misuse |
|---|---|---|
| Admission/rate limit | Bound offered or admitted work before resource exhaustion | Hide rejected attempts from service-level outcomes |
| Queue limit/deadline | Bound waiting memory and usefulness | Queue accepted irreversible writes without durable tracking |
| Bulkhead | Reserve bounded workers/pools for independent classes/dependencies | Partition too tightly and waste capacity, or allow bypass |
| Circuit breaker | Avoid repeated costly calls to a failing dependency; probe recovery | Treat opening the breaker as permanent recovery or a substitute for backpressure |
| Retry budget + jitter | Spread bounded safe transient retries across time | Multiply load during outage or repeat non-idempotent effects |
| Load shedding | Discard lower-priority eligible work when explicitly permitted | Silently lose acknowledged business commands |
| Optional feature degradation | Preserve core outcome when nonessential enrichment fails | Present missing mandatory data as a complete result |

Across multiple layers, retries compound. If three independent layers make three attempts per incoming logical operation, a pathological path can create up to **27 downstream attempts** per logical intent (under a deliberately simplified fully nested retry model). No such amplification was observed here. [AWS Builders' Library retry and jitter discussion](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) explains why coordinated repeated retries can worsen overload. [Tycho's RPC and idempotency chapter](../../v02-application-boundaries-and-contracts/c05-public-apis-http-rpc-and-compatibility/http-rpc-contracts-and-compatibility.md) owns effect-safe retry identity.

The generic retry decision contract, including local-versus-broad overload and the
per-request, per-client and service-wide budgets, is owned by `V02/C05`
(`tycho.page.43414664520b4866929f7f006f27f59b`). This section owns the overload regime and
the isolation boundary; `V04/C04` (`tycho.page.33399db8d1574330951d9954801d6e71`) owns
effect identity and retention.

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [Circuit Breaker](../../v11-pattern-atlas/c07-resilience/README.md#circuit-breaker) — decision conditions and contraindications.
> [Bulkhead](../../v11-pattern-atlas/c07-resilience/README.md#bulkhead) — decision conditions and contraindications.

<!-- tycho-question-source:tycho.page.c5d20ae7ef6445e5b23dd5fbac625060:5 -->
## 5. Original synthetic failure: one optional dependency poisons core work

A fictional public trail guide serves a **required** trail description and an **optional** community photo suggestion. Both initially use one shared worker pool. During a picture-service slowdown, photo calls hold most workers; required trail descriptions fail their deadlines even though authoritative trail records remain healthy.

**Candidate A:** enlarge the shared pool. It might only increase calls to the failing photo dependency and thread/buffer use. **Candidate B:** give optional images a separate small concurrency budget, deadline and circuit breaker; serve core trail information without the optional image when its deadline expires. **Candidate C:** queue user operations for minutes waiting on the photo service—contradicts the intended interactive contract.

A bounded test (not executed) would keep offered arrival schedule and resource ceiling equal, inject image-service slowness and observe correct core responses, missing-photo labelling, queue age, retry attempts, errors and recovery. A result where A appears faster only because it drops unknown user attempts is invalid.

The optional nature of photos is a **fictional stated requirement**. If actual user safety depends on a recent trail-closure update from another service, substituting stale information would be unacceptable; the safe response might need a clearly denied/unknown result.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](admission-resource.md) |
| Next | [Continue the reasoning](overload-recovery.md) |
| Integrated question | [Original scenario and limits](overload-admission-control-and-graceful-degradation.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
