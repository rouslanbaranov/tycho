---
metadata_version: 1
id: "tycho.page.ea94649bfd8c4be183f9114618d7ccaa"
kind: "page"
parent_id: "tycho.chapter.94b4b6d9e2e1490abd0055a5265141ff"
canonical_path: "book/volumes/v08-delivery-deployment-and-recovery/c03-vms-containers-orchestration-and-serverless/runtime-placement-and-control-plane.md"
title: "Deployment topology and control-plane independence"
topic_ids:
  - "deployment-architecture"
perspectives:
  - "architecture"
  - "operations"
summary: "Integrated question, original scenario and transfer limits for VMs, containers, orchestration and serverless. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "Which topology suits operational and workload requirements?"
  prerequisites: []
  related_ids:
    - "tycho.page.2536d18422944e27abe4ea8549beb9ab"
    - "tycho.page.5d5dd1d008b848a39dfae29a147da6d0"
    - "tycho.page.b7913b53d5ea439697bc5236f902d76e"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Deployment"
    - "topology"
    - "and"
    - "control-plane"
    - "independence"
evidence_scope:
  source_ids:
    - "src.aws-static-stability"
  claim_ids: []
  status: "source-linked"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-10-21"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.ea94649bfd8c4be183f9114618d7ccaa:-1 -->

# Deployment topology and control-plane independence

> Original Tycho technical chapter for [E14-09 / issue #87](https://github.com/rouslanbaranov/tycho/issues/87), research scope inspected 2026-10-19. Explains design trade-offs; NOT a deployment recipe or performance benchmark. The examples are synthetic, no employer/private architecture is used.
>
> The content_review field retains the decomposition-era draft state; no independent
> acceptance is asserted.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.ea94649bfd8c4be183f9114618d7ccaa:5 -->
## Engineering walkthrough — Control-plane outage and continued data-plane work

**Original fictional service:** request-serving pods are already running in a zone when the orchestration control plane becomes unreachable. Some existing client requests can continue through existing routes and working data-plane components. New deployment, rescheduling or configuration changes may not proceed, and losing nodes can degrade capacity over time. The observable service contract must distinguish *existing steady-state survival* from *ability to create/recover resources*.

| Hosting choice | Control and state owner | Failure condition to model |
|---|---|---|
| VM processes | OS/process/operator provision, external state service | Host dies; replacement and placement may depend on unavailable management API |
| Container orchestrator | Scheduler/controllers for placement; applications own domain state | Control plane down, running instances alive; node loss cannot be promptly repaired |
| Managed runtime/serverless | Provider-owned lifecycle/scale admission | Cold starts, service limits, provider-region/control dependencies |
| Self-managed on premises | Organization owns hardware, recovery and capacity | Network/power/operator failure may be more correlated than expected |

A container is not by itself an availability zone, a managed service is not a business-state correctness proof, and serverless autoscaling cannot create authoritative consistency. Changing hosting model may introduce new irreversible state/network contracts while leaving the original domain bottleneck untouched.

**Proposed test (not run):** isolate orchestrator/API access while keeping running workers and database reachable; issue existing reads/writes, then kill one node and measure degradation/recovery. Repeat under a real downstream outage. Reject a topology if its data-plane ability to serve a correct user journey depends on immediate control-plane participation that cannot meet the declared outage duration. The existing static-stability and orchestration references support the failure-model method, not results from this fictional deployment.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.ea94649bfd8c4be183f9114618d7ccaa:7 -->
## Architecture-selection outcome

Return **insufficient evidence** if the dominant failure class, transaction owner, placement domain, control-plane availability, workload shape or measured RPO/RTO is unknown. A simpler single-region, well-restorable design may be more defensible than two regions with untested conflict semantics. The companion [disaster-recovery chapter](../../../deployment/multi-region-disaster-recovery-contracts.md) owns state recovery and cross-region policy; no assumption that its design has been deployed is made.
<!-- /tycho-question-source -->

## Integrated decision and reading route

Compare runtime topologies against the same outcome, failure model, resource needs and operating capability.

A container or orchestration label does not establish fault isolation, useful spare capacity or recoverable state.

The detailed pages separate the mechanisms that make this decision conditional:

- [Compute models and operating constraints](compute-models.md) — Which workload, isolation and operating constraints make a runtime topology viable?
- [Control planes, placement and reversibility](static-stability.md) — What work can continue when orchestration or placement control is unavailable?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
