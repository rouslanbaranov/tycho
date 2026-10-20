---
metadata_version: 1
id: "tycho.page.ea94649bfd8c4be183f9114618d7ccaa"
kind: "page"
parent_id: "tycho.landing.6f58e5c00dea4f4086963169a2590bf5"
canonical_path: "book/deployment/runtime-placement-and-control-plane.md"
title: "Deployment topology and control-plane independence"
topic_ids:
  - "deployment-architecture"
perspectives:
  - "architecture"
  - "operations"
summary: "Reader entry for Deployment topology and control-plane independence. Scope includes Decision question and scope; Compute models and their real trade-offs; Control plane, data plane and static stability."
route_hints:
  questions:
    - "What are the scope, mechanisms and limits of Deployment topology and control-plane independence?"
  prerequisites: []
  related_ids:
    - "tycho.page.2536d18422944e27abe4ea8549beb9ab"
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
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---

# Deployment topology and control-plane independence

> Original Tycho technical chapter for [E14-09 / issue #87](https://github.com/rouslanbaranov/tycho/issues/87), research scope inspected 2026-10-19. Explains design trade-offs; NOT a deployment recipe or performance benchmark. The examples are synthetic, no employer/private architecture is used.

## Decision question and scope

Given a required user journey, workload, failure class, operational team and data-residency constraints, **which runtime boundary, placement arrangement and control-plane dependencies can preserve the stated behavior?** The deployment unit alone—bare metal, VM, container or function—cannot answer that question. A container in one failure zone is not automatically more available than a VM with proven restore; a service mesh adds configuration and a data plane but does not make application state consistent.

Record separately: state writer, ingress, runtime instance, scheduler/control service, deployment mechanism, network path, secrets/identity service, availability zone/host/region and operator responsibility.

## Compute models and their real trade-offs

| Model | Isolation and ownership boundary | Relative advantages when conditions fit | Constraints, failure questions and disqualifiers |
|---|---|---|---|
| **Bare metal / dedicated host** | Physical machine and its firmware/storage/network plus chosen OS | Direct device control, predictable specialized capacity, hardware/locality requirements | Provision and repair time, host loss, replacement inventory, OS patching, storage replication, team operation burden |
| **Virtual machine** | Guest OS with hypervisor and virtualized devices; placement is still physical | Established OS/kernel isolation and explicit runtime image lifecycle; can host legacy services | Host and zone fault domains, VM boot/restore, hypervisor dependency, attached volume recovery, deployment velocity |
| **Container on shared host/orchestrator** | Namespaced processes and images; kernel may be shared; scheduler/node placement matter | Repeatable image artifact and selected scheduling/rescheduling policy, if node/registry/control services are healthy | Container is NOT its own kernel or zone; image registry, cluster control plane, network overlay, storage/secret fetch and autoscaler delay can block recovery |
| **Managed function/serverless** | Provider-managed execution and scaling, with invocation/event/timeout boundaries | Scale-to-demand and reduced direct host operations when workload execution model matches | Runtime quotas/concurrency, start delay, state externalization, connection spikes, event retry/delivery and vendor control-plane/region dependencies |
| **Managed platform service** | Provider-defined database/broker/queue/cache failure domain | Reduces operational ownership for versioned service features | Actual failover and consistency semantics require exact provider/region/version evidence; not a universal RPO/RTO guarantee |

Comparisons require the **same observable outcome, admitted/offered load, logical data correctness and named outage**, plus staffing, steady-state cost and restore test. Package type does not imply a number of safe replicas. A migration to containers may be contraindicated by a hard device driver/kernel dependency, unsupported legacy licensing, or an immutable on-disk contract; those are evidence questions, not stereotypes.

## Control plane, data plane and static stability

A **control plane** changes placement, configuration, membership, policy or resource count. A **data plane** serves the already-defined requests or processes previously admitted work. A functionally correct data plane can still depend on control-plane services for bootstrapping credentials, routing, discovery, certificate renewal, replacement instances or configuration fetches. Those dependencies must be measured under loss of the control plane, not waved away.

The AWS Builders' Library article *Static stability using Availability Zones*, **Static stability** and **Static stability patterns**, describes designing a service that retains enough pre-existing capacity and locally available state to continue serving during a zone/control-plane impairment; it contrasts this with depending on immediate provisioning during the incident. This is a reported AWS design approach, NOT a promise that any arbitrary orchestration stack shares its guarantees.

### Original illustrative topology

~~~mermaid
flowchart TD
  Client["User or upstream request"] --> Edge["Ingress / routing data plane"]
  Edge --> A["Worker pool: zone A"]
  Edge --> B["Worker pool: zone B"]
  Edge --> C["Worker pool: zone C"]
  A --> State["Authoritative state boundary"]
  B --> State
  C --> State
  Manager["Scheduler / deployment control plane"] -.-> A
  Manager -.-> B
  Manager -.-> C
  IaC["Versioned infrastructure definition"] -.-> Manager
  Secrets["Secrets and identity dependency"] -.-> A
  Secrets -.-> B
  Secrets -.-> C
~~~

Text alternative: an ingress routes requests to workers already spread across three distinct zones and a separately identified authoritative state owner. A scheduler and IaC control plane configure or replace workers; secrets/identity may remain a shared runtime dependency. The dashed edges indicate management/configuration, not guaranteed availability. Every arrow is **conceptual**, not an observed installation.

### Synthetic capacity thought experiment, not a recommendation

Assume three zones, each can demonstrably serve 60 *identical invented* units/s at the specified operation mix, with no shared downstream saturation. Normal demand is 100 units/s. Total nominal capacity is 180, but failure of one zone leaves 120: only 20 units/s of nominal headroom (relative to the demand of 100) and **not** a guarantee of satisfying p99 or correctness. A shared database limited to 80 units/s invalidates the premise; likewise if traffic cannot be steered, authentication unavailable or concurrency surges. For a real design, test loss of zone and control-plane concurrently, offered versus completed logical operations, queue, network ingress and downstream behavior.

## Placement and topology constraints

### Bare-metal/VM/container placement

State locality and failure domains may span process, host, rack, network switch, power zone, availability zone and region. A scheduler can distribute pods across topology domains only to the extent they are represented by supported labels and available nodes; a topology policy cannot conjure healthy hardware or storage replicas.

Kubernetes **Pod topology spread constraints** uses topology domains and constraints to influence pod placement. Specify topology key, scheduling condition, skew and what happens when a zone lacks capacity. Review the precise Kubernetes version and scheduler configuration; the documentation does **not** prove any given cluster has achieved a desired AZ distribution. Node architecture docs separately describe kubelet/control-plane and node status, not application correctness.

Record distinct properties: (a) failure-domain diversity, (b) network locality, (c) state quorum or leader placement, (d) capacity remaining after failure, (e) legal/data residency, and (f) operational ability to recover. Multi-zone replicas that write to one unreplicated external database may still share one fatal failure domain.

### Service mesh and traffic intermediaries

A service mesh often has an API/control plane that distributes route and policy configuration and a data plane of proxies or library-level equivalents. For an **Envoy-based example**, xDS supplies dynamic resources for cluster/endpoints/listeners/routes. Distinguish the plane that **configures** the proxy from the proxy's live behavior. Introduce actual tests for stale configuration and rollback, TLS identity/certificate renewal, outlier detection, retry storms and health checks.

A mesh is appropriate only when those operational controls solve a measured cross-service need. In a simple monolith, introducing sidecars, certificates, policy versioning and debugging layers may be cost without benefit. A mesh cannot make an application transaction cross databases atomically; it may actually amplify load if retries are configured without a budget.

### Infrastructure as code and drift

Infrastructure as code (IaC) is a *versioned desired declaration plus a change mechanism*, not an availability mechanism by itself. Separate the source commit, reviewed plan, resulting state, external drift and an actually tested restore. Terraform's state documentation explains the mapping of configured resources to real objects and the need to retain state securely; a stored HCL file alone is not proof that production matches it. Before planning disaster recovery, verify state storage/access, backend/credential availability during a region loss, recovery-account separation and immutable deployment artifacts.

An IaC change that removes a database or rewrites a routing rule is operationally consequential. Require independent change authorization for destructive plans, deterministic versioned inputs, an exit/rollback test and explicit handling of drift; don't infer a safe rollback from the ability to revert a text file.

## Failure matrix and reversibility

| Disruption | Potential control/data path outcome | Gate/measurement before declaring recovery |
|---|---|---|
| One instance or VM dies | Healthy sibling may serve traffic; stateful leader might be lost | Confirm enough warmed capacity, correct routing, persisted state and duplicate-safe replay |
| One host/rack/zone unavailable | Rescheduling may need impaired shared management or full node scale-up | Exercise outage without provisioning any new instance for the required initial window |
| Deployment API/control plane stops | Existing data plane may or may not continue (secrets, certificates, stale membership matter) | Fault-inject loss, measure existing requests and new-route changes separately |
| Mesh configuration push wrong | Incorrect routing, authorization or retries may hit all services | Canary config, policy validation, scoped rollback and log/correlation evidence |
| Image registry or secret service unreachable | Cold/replacement nodes cannot start even if running replicas are fine | Test a recovery path with required artifacts/certificates already available |
| State owner unavailable | All stateless frontends can become ineffective | Verify database/broker quorum, RPO, leader fencing and correct user outcomes |
| IaC state lost/compromised | Restoration may not reconstruct original ownership safely | Test actual state recovery, drift handling and protected credentials |

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

## Source-to-claim ledger — inspected primary scope

| Ref | Exact publicly inspected material (2026-10-19) | Supports and exclusions |
|---|---|---|
| D87-01 | [AWS Builders' Library: Static stability using Availability Zones](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/), *Static stability*, *Static stability patterns* and *Control/Data plane* explanation | Failure readiness/preprovisioned capacity in AWS examples; does **not** establish an exact generic overprovisioning ratio or a service's SLA |
| D87-02 | [Kubernetes: Pod Topology Spread Constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/), *Spread constraints for Pods* and scheduler behavior | Versioned topology scheduling parameters; not a proof of actual placement or healthy nodes |
| D87-03 | [Kubernetes: Nodes](https://kubernetes.io/docs/concepts/architecture/nodes/), node components and status documentation | Control/worker relationships and node lifecycle; not application failover |
| D87-04 | [Envoy: xDS configuration API overview](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/operations/dynamic_configuration), *xDS overview*, living latest documentation inspected 2026-10-19 | Control configuration of Envoy proxies; cannot assert mesh behavior for every vendor/version or independent data-plane consistency |
| D87-05 | [HashiCorp Terraform: State](https://developer.hashicorp.com/terraform/language/state/purpose), *State purpose*, documentation inspected 2026-10-19 | Declared-resource ↔ real-resource mapping and state importance; no claim that a disaster-recovery runbook exists |
| D87-06 | [AWS DR Whitepaper: Disaster recovery options](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), *Backup and restore* and *Pilot light* | Need to restore infrastructure/configuration and exercise DR; not a universal recovery duration |

### Open source and version gaps

No single inspected umbrella reference in this issue establishes comparable isolation/latency/cold-start guarantees for **all bare-metal, VM, container and serverless vendors**. A dedicated primary-source packet must be added before a vendor-specific selection or quantitative cost ranking: exact container runtime and kernel isolation docs, hypervisor/security policy, selected FaaS concurrency/start limits, actual mesh version and provider quotas. A future benchmark must include equipment, region, topology and time window. Until then, the table is a **conditional mechanism comparison**, not a measured product ranking.

## Architecture-selection outcome

Return **insufficient evidence** if the dominant failure class, transaction owner, placement domain, control-plane availability, workload shape or measured RPO/RTO is unknown. A simpler single-region, well-restorable design may be more defensible than two regions with untested conflict semantics. The companion [disaster-recovery chapter](multi-region-disaster-recovery-contracts.md) owns state recovery and cross-region policy; no assumption that its design has been deployed is made.
