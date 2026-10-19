# Target architecture design template

> For the [Tycho target/transition model](../authoring/models/target-transition-architecture.md), issue #21. A target is a **candidate** unless evidence and actual decision-owner approval establish otherwise.

## Identity, decision authority, and boundaries

- Target ID / revision / status / observation date:
- Linked [requirements/workload](../authoring/models/requirements-workload-profile.md), [legacy baseline](../authoring/models/legacy-modernization-profile.md), and [ADR](evidence-backed-adr.md):
- Business capability and affected journey:
- Included and excluded state, infrastructure, external dependencies and consumer versions:
- Approval, review and evidence state (pending is acceptable):

## Desired design without pretending the migration happened

| Responsibility / owner | Components and interfaces | State and transactional invariants | Security and trust boundary | Exact source / unknown |
|---|---|---|---|---|
| | | | | |

### Interaction, runtime, data, and fault domains

- User-facing request/event normal path and partial-failure path:
- State owner, durability, idempotency, ordering and consistency:
- Queues/pools/fan-out, throughput and latency hypothesis, dependency budgets:
- Deployment placement and zones, supported software/contract versions:
- AuthN/AuthZ, tenancy, secrets, audit and exposure boundaries:
- Observability, runbook, operational owner, alerting and restoration:

Add an original, bounded Mermaid view **only** when the intended boundaries are clear. Provide a textual alternative, version assumptions and synthetic/proposed status.

## Measurable satisfaction and negative cases

| Requirement / invariant | Target outcome | Measurement, version and scenario | Hard gate and failure counterexample | Evidence / gap |
|---|---|---|---|---|
| | | | | |

- Cost, skill, operational and release commitments:
- Alternative that remains viable (including improved current design):
- Claim owner and exact cited public sections:
- What observation or new requirement would invalidate the target:
- Independent review / actual sign-off:
- Validation never performed (if any):

**Transition is deliberately external:** provide a link to a separate filled [transition architecture](transition-architecture.md) when one is designed. This target template does not authorize a cutover, shared-database ownership reassignment, or irreversible migration.
