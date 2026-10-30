---
metadata_version: 1
id: "tycho.page.4cd5af48018f47f7b30ace45acf4e220"
kind: "page"
parent_id: "tycho.chapter.69085752a11c69305aa2a369b8ec9d29"
canonical_path: "book/volumes/v11-pattern-atlas/c07-resilience/health-endpoint-monitoring.md"
title: "Health Endpoint Monitoring"
topic_ids:
  - "performance-engineering"
  - "distributed-systems"
perspectives:
  - "architecture"
  - "operations"
summary: "Decision card for Health Endpoint Monitoring with bounded owner evidence."
route_hints:
  questions:
    - "Should an external monitor distinguish liveness, readiness and startup health?"
  prerequisites:
    - "tycho.chapter.69085752a11c69305aa2a369b8ec9d29"
  related_ids:
    - "tycho.chapter.69085752a11c69305aa2a369b8ec9d29"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved card."
  keywords:
    - "pattern atlas"
    - "health endpoint monitoring"
    - "resilience"
evidence_scope:
  source_ids:
    - "src.kubernetes"
    - "src.sre-cascading"
    - "src.sre-frontend-enrichment"
    - "src.aws-elastic-load-balancing"
    - "src.aws-cloudwatch-synthetics"
    - "src.sre-workbook"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.batch4-k8s-probes.2026-10-21, the 2026-10-30 AWS ELB,
    AWS Synthetics, Google SRE cascading/frontend and SRE Workbook records;
    owner section and limits are bounded.
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
# Health Endpoint Monitoring

**Identity.** Health Endpoint Monitoring; family Resilience and fault tolerance; kind
operations-pattern; priority core.

**Decision question.** Should an external monitor distinguish liveness, readiness and
startup health?

**Good-fit conditions.** Startup, readiness and liveness are separate probes; probe
semantics match the failure; restart and traffic removal are distinct; an external journey
check is independent of the dependency it observes.

**Hard contraindications.** Reject when a liveness probe would restart a healthy process
because a shared dependency is down, when one probe is used for every failure, or when the
external check shares the dependency under test.

**Competing alternative.** Process liveness plus an external journey check (a synthetic
canary) or SLO-based alerting on customer experience. Reverse the choice when probe complexity
causes false restarts or the external check reuses the failing dependency. The choice rule is
Tycho guidance.

**Failure and recovery.** Shared-dependency failures can fail every probe and cause mass
restart/ejection; cached or missing health can keep routing to a draining instance. Kubernetes
binds readiness to traffic removal and liveness to restart; Google SRE records that health
checking itself can make a service unhealthy; AWS removes a target after bounded consecutive
failures and fails open when all targets fail. The shared-dependency composition and DNS-cache
staleness are Tycho. Define no-response behavior, keep probes on an independent path, and
bound frequency and exposure.

**Technical owner.** [Request routing and health signals](../../v08-delivery-deployment-and-recovery/c08-network-request-paths-routing-and-edge-delivery/routing-and-health.md#health-endpoint-monitoring) — readiness/health is bounded, not a full monitoring product.

**Sources.** [src.kubernetes](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-k8s-probes.2026-10-21: all fifteen served headings read.
The failure and alternative dimensions also cite Google SRE "Addressing Cascading Failures"
(read.batch4-sre-cascading.2026-10-21) and "Load Balancing at the Frontend"
(read.batch5-sre-frontend.2026-10-21), AWS "Health checks for Application Load Balancer
target groups" (read.aws-elb-health-checks.2026-10-30), AWS "Synthetic monitoring
(canaries)" (read.aws-synthetics-canaries.2026-10-30) and Google SRE Workbook "Alerting on
SLOs" (read.sre-workbook-slos.2026-10-30). The last three are recorded in the ledger. These
are public pattern/documentation units, not benchmarks.

**Decision state.** applicable-under-conditions.

**Related entries.** Health, Readiness and Liveness Checks; Failover/Failback; Synthetic
Monitoring; Circuit Breaker.
