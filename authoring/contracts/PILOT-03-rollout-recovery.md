# Pilot research 3 — safe rollout, compatibility and recovery

- **Contract ID:** TYCHO-PILOT-RECOVERY-v0.1
- **Issue / owner:** [#40](https://github.com/rouslanbaranov/tycho/issues/40); proposed canonical chapters V08/C04–C07.
- **Status:** bounded research plan, not a tested or approved deployment architecture.
- **Reader:** delivery, reliability and application architects comparing rollout, recovery and compatibility constraints for independently authored software.
- **Primary question:** How can a change be deployed and, if health or compatibility fails, traffic/software/data be safely recovered without confusing a successful deployment controller action with proof of user-level recovery or data correctness?

## Synthetic comparison and design routes

Use a fictional multi-instance workshop registration service with a separately evolving persistent schema and one hypothetical user flow. A **new design** route describes target deployment options. A **modernization** route assumes (for analysis only) that an older schema and a newly deployed binary must coexist temporarily.

Workload, support staffing, costs, dependency failure domains, and migration constraints are given as hypothetical inputs or marked unknown; no user infrastructure or production incident is represented.

**Target:** a service capable of serving the registered/booking workflow with stated quality/integrity. **Transition:** explicit interim routing, compatible schema versions, old/new binaries and reversible/irreversible actions; the existence of a target design never proves that its migration is safe.

## Public research sources and exact intended sections

Source IDs below resolve to the already curated public register. These are **targets for #40 reading**; chapter claims must cite material actually inspected and its documented version.

| Registered ID | Target version/page and sections | Evidence question and limitation |
|---|---|---|
| `src.k8s-deployments` | [Kubernetes Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/): **Updating a Deployment**, **Rolling Update Deployment**, **Rollover**, **Deployment status**, **Failed Deployment**. Record page's applicable K8s version and update timestamp. | What controller availability/progress conditions mean; why that does not prove user requests, state or database migrations are healthy. |
| `src.argo-rollouts` | [Argo Rollouts Concepts](https://argo-rollouts.readthedocs.io/en/stable/concepts/): **Canary**, **BlueGreen**, **Analysis**, **Progressive Delivery** where present; select a pinned release for claims of configuration/behavior. | Traffic progression, analysis and rollback controls; installation/runtime assertions need direct tests. |
| `src.aws-dr` | [Disaster Recovery of Workloads on AWS](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html): choose exact **RTO/RPO**, backup/restore or failover strategy subsections. | Recovery terminology and trade-offs; vendor-specific solutions are examples, not universal obligations. |
| `src.flyway` / `src.postgresql` | [Flyway reference](https://documentation.red-gate.com/flyway) and [version-pinned PostgreSQL documentation](https://www.postgresql.org/docs/current/); identify actual migration/DDL/locking sections before chapter-level claims | Whether a database change is backward-compatible, can be rolled back and remains safe while binaries coexist. |
| `src.sre-cascading` | [Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/), selected overload and recovery sections | Why failure load can rise during a rollout/recovery and why capacity assumptions must be challenged. |

The entire source tree of a product is never assumed to have been read. For differences among versions, locate actual release-specific sources; contradictions stay explicit.

## Required normal and failure timelines

1. Establish one original **synthetic** base request/data model and measurable acceptance checks: client success/latency/consistency, not only pod readiness.
2. Compare rolling replacement and another strategy (e.g., canary or blue/green) under declared cost/resource and traffic-control assumptions; note when the latter is unnecessary.
3. Define coexistence contract: old+new binary against N/N+1 schema, producer/consumer message formats, session/transaction boundaries, minimum rollback window.
4. Inject failure: new version times out under load or writes data the old version cannot read. Show what is **reversible**, what needs forward-fix, and what cannot safely be rolled back.
5. Include a second hypothetical failure of a zone/dependency and identify surviving headroom, health/readiness visibility, failover preconditions and possible recovery gaps.
6. Track decision gates: before launch, before widening traffic, after partial failure, before rollback/forward recovery and at final release acceptance.
7. Name what must be **measured first**: write/schema compatibility, data replication/restore evidence, p99 and error rate under degraded load, historical SLI/SLO definitions and team recovery capability.

## Explicitly unanswerable case

Given only "the deployment was successful" and no per-version user error data, schema compatibility tests, recovery drill, or dependency-state evidence, the responsible outcome is **insufficient evidence to assert safe rollout or RPO/RTO compliance**. Give a finite experiment plan; never claim safe migration based solely on readiness or a green CI build.

## Acceptance / stopping criteria

- Exact source passages and version applicability for each material mechanism; unknowns retained.
- At least one original target-vs-transition architecture diagram/table and a named compatibility/rollback contract.
- One normal, one failed rollout and one disaster-recovery path, including externally visible user behavior and integrity.
- A comparison of practical alternatives and the conditions that reverse preference.
- Measurable go/no-go acceptance checks, source-controlled release artifacts, monitoring, rollback versus forward recovery and irreversible-action boundaries.
- At least one deliberate **measure-first/insufficient-evidence** verdict rather than fictitious precision.
- Existing source/boundary/relative-link checks pass; record real CI, provenance and review limits.
- Do not claim a container cluster, restored database, load test or independent human review was exercised unless it actually happened.
