---
metadata_version: 1
id: "tycho.page.b7913b53d5ea439697bc5236f902d76e"
kind: "page"
parent_id: "tycho.chapter.94b4b6d9e2e1490abd0055a5265141ff"
canonical_path: "book/volumes/v08-delivery-deployment-and-recovery/c03-vms-containers-orchestration-and-serverless/static-stability.md"
title: "Control planes, placement and reversibility"
topic_ids:
  - "deployment-architecture"
perspectives:
  - "architecture"
  - "operations"
summary: "What work can continue when orchestration or placement control is unavailable?"
route_hints:
  questions:
    - "What work can continue when orchestration or placement control is unavailable?"
  prerequisites:
    - "tycho.page.5d5dd1d008b848a39dfae29a147da6d0"
  related_ids:
    - "tycho.chapter.94b4b6d9e2e1490abd0055a5265141ff"
    - "tycho.page.ea94649bfd8c4be183f9114618d7ccaa"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "static"
    - "stability"
evidence_scope:
  source_ids:
    - "src.aws-static-stability"
  claim_ids: []
  status: "source-linked"
  notes: "Bounded question from tycho.page.ea94649bfd8c4be183f9114618d7ccaa; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
# Control planes, placement and reversibility

**Owning question:** What work can continue when orchestration or placement control is unavailable?

This page belongs to [V08/C03 — VMs, containers, orchestration and serverless](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.ea94649bfd8c4be183f9114618d7ccaa:2 -->
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

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [Immutable Infrastructure](../../v11-pattern-atlas/c10-deployment-modernization/README.md#immutable-infrastructure) — decision conditions and contraindications.

> **Pattern atlas:** [Sidecar](../../v11-pattern-atlas/c01-application-boundaries/README.md#sidecar) — decision conditions and contraindications.
> [Ambassador](../../v11-pattern-atlas/c01-application-boundaries/README.md#ambassador) — decision conditions and contraindications.
<!-- tycho-question-source:tycho.page.ea94649bfd8c4be183f9114618d7ccaa:3 -->
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

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.ea94649bfd8c4be183f9114618d7ccaa:4 -->
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

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](compute-models.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](runtime-placement-and-control-plane.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

## Bounded pattern ownership notes

These notes define the decision boundary for atlas cards whose mechanism is
not the main subject of this page. They are synthetic design guidance, not
measured evidence, and they do not create a new source claim.

### Ambassador

An ambassador is a proxy or sidecar that brokers a service outbound calls. It can own
discovery, TLS identity, retries, timeouts and telemetry away from the application. It
needs a clear data-plane owner, a configuration path and a failure policy for the proxy
itself. Use it when many clients need the same remote-access contract. Do not use it when
a client library is simpler or when the proxy would become an unobserved single point of
failure.

The failure path is a stale proxy configuration or a proxy that outlives its control
plane; test configuration rollback and keep a direct-path recovery. A shared gateway is
the alternative when the concern is ingress rather than per-client egress.

**Limits.** An ambassador cannot grant authority the remote peer does not recognize, and
it adds a data-plane hop whose latency and outage must be budgeted.

### Sidecar

A sidecar runs as a helper process or container beside each service instance and supplies
networking, policy or telemetry behaviour without changing the application image. The sidecar's
failure policy must be explicit, and its lifecycle and configuration must be coupled to the instance
it serves.

A missing or misconfigured sidecar silently removes a control or opens a bypass; readiness must
include it, and the fail-open or fail-closed choice must be tested. A shared proxy or an in-process
library provides the same control without per-instance overhead; choose a sidecar when per-instance
isolation or independent upgrade matters.

**Limits.** A sidecar cannot isolate a compromised shared kernel, replace host-level policy or
remove the per-instance resource and upgrade cost. Its failure mode must include
control-plane unavailability.

### Immutable Infrastructure

Immutable infrastructure replaces instances from a versioned image or definition instead of mutating
running hosts, so each instance is reproducible from a recorded artifact. Every running instance
must be reproducible from a recorded artifact digest, and drift must be detected rather than
tolerated.

A rebuilt image that no longer matches the deployed artifact turns replacement into an uncontrolled
change; record digests and test the rebuild path. Configuration management on long-lived hosts is
cheaper when state locality dominates; choose immutable replacement when reproducibility and
rollback speed matter.

**Limits.** Immutable replacement is not a backup: data, secrets and external effects still need
lifecycle ownership, toolchain and base-image provenance must be reproducible, and a rollback
restores an artifact, not necessarily compatible data. Rebuild time and image size are
operational costs, not proofs of reproducibility.
