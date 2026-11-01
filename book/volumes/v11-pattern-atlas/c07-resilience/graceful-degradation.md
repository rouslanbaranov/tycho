---
metadata_version: 1
id: "tycho.page.f13601692470d89f22c2549bdbb3cd5b"
kind: "page"
parent_id: "tycho.chapter.69085752a11c69305aa2a369b8ec9d29"
canonical_path: "book/volumes/v11-pattern-atlas/c07-resilience/graceful-degradation.md"
title: "Graceful Degradation"
topic_ids:
  - "performance-engineering"
  - "distributed-systems"
perspectives:
  - "architecture"
  - "operations"
summary: "Decision card for Graceful Degradation with bounded owner evidence."
route_hints:
  questions:
    - "Should non-essential capabilities be reduced to protect essential work under stress?"
  prerequisites:
    - "tycho.chapter.69085752a11c69305aa2a369b8ec9d29"
  related_ids:
    - "tycho.chapter.69085752a11c69305aa2a369b8ec9d29"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved card."
  keywords:
    - "pattern atlas"
    - "graceful degradation"
    - "resilience"
evidence_scope:
  source_ids:
    - "src.sre-cascading"
    - "src.sre-overload"
    - "src.aws-load-shedding"
    - "src.sre-best-practices"
    - "src.kubernetes"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.batch4-sre-cascading.2026-10-21,
    read.sre-overload.2026-10-21 and the 2026-10-30 Google SRE best-practices,
    AWS load-shedding and Kubernetes HPA records; owner section and limits are
    bounded.
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-30"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-30"
updated_at: "2026-10-30"
source_inspection_date: "2026-10-30"
content_verified_at: null
---
# Graceful Degradation

**Identity.** Graceful Degradation; family Resilience and fault tolerance; kind
resilience-pattern; priority core.

**Decision question.** Should non-essential capabilities be reduced to protect essential
work under stress?

**Good-fit conditions.** Essential and optional work are distinguishable; a degraded
response is explicitly less accurate or contains less data; the reduced outcome and the
caller-visible state are declared; recovery and hysteresis are defined and exercised.

**Hard contraindications.** Reject when every capability is essential, when degradation
cannot be communicated, when it silently changes correctness, or when no degraded response
can be computed and an explicit error is the remaining option.

**Competing alternative.** An explicit outage or added capacity. Reverse the choice when no
safe degraded response exists, when no reduced result preserves the correctness contract,
or when capacity can be added faster than a degraded mode can be made safe. The choice rule
is Tycho guidance.

**Failure and recovery.** A degraded mode is a rarely exercised path. Google SRE warns that
the unused code path often does not work, that complexity can trip a server into a degraded
mode unintentionally or create feedback cycles, and that operators need monitoring and a way
to disable or tune the mode. AWS treats rejection as a visible availability reduction and
instruments it. Tycho adds that silent loss of correctness is worse than an explicit
failure: each mode needs an entry condition, a visible status, an owner and an audited
override. Recovery needs hysteresis; Kubernetes compares flapping to hysteresis and uses a
stabilization window. Applying that window to a degraded mode is Tycho composition.

**Technical owner.** [Graceful Degradation](../../v07-performance-scale-and-resilience/c05-overload-protection-and-graceful-degradation/overload-admission-control-and-graceful-degradation.md#graceful-degradation) — graceful degradation is bounded to the overload path, not a complete capacity plan.

**Sources.** [src.sre-cascading](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-sre-cascading.2026-10-21. The dimensions also cite Google SRE
"Handling Overload" (read.sre-overload.2026-10-21) and "A Collection of Best Practices for
Production Services" (read.sre-best-practices-overload.2026-10-30), AWS "Using load shedding
to avoid overload" (read.aws-load-shedding.2026-10-30) and Kubernetes "Horizontal Pod
Autoscaling" (read.k8s-hpa.2026-10-30). The last three are recorded in the ledger. These are
public pattern/documentation units, not benchmarks.

**Decision state.** applicable-under-conditions.

**Related entries.** Fallback; Load Shedding; Throttling; Rate Limiting.
