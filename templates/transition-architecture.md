# Transition architecture and safe modernization template

> Use with a specific filled [target design](target-architecture.md) and the [Tycho target/transition model](../authoring/models/target-transition-architecture.md). A sequence of deployment commands is not a safety argument. All gates require real evidence.

## Scope and baseline

- Transition ID/revision, current and target versions, named decision owner:
- Current [legacy profile](../authoring/models/legacy-modernization-profile.md), linked approved/proposed [ADR](evidence-backed-adr.md):
- Target capabilities and alternatives (including retain/tune):
- User and runtime boundary, data writer, consumers and external side effects:
- Downtime budget, RPO/RTO, support hours and recovery permissions (or **unknown**):
- Fixed versions/source revisions and expected delivery artifacts:

## State-by-state coexistence map

| State ID | Live old/new topology and routing | Supported clients and schemas | Data writer/readers, backfill and replay | Entry gate | Exit/no-go gate | Rollback vs forward recovery |
|---|---|---|---|---|---|---|
| Baseline | | | | | | |
| Expanded | | | | | | |
| Coexistence | | | | | | |
| Backfill and reconcile | | | | | | |
| Cutover | | | | | | |
| Retired old paths | | | | | | |

## Mixed-version contract matrix

| Client or consumer | Old producer/server | New producer/server | Test version/fixture and outcome | Blocker |
|---|---|---|---|---|
| Old | | | | |
| New | | | | |

Do not infer backwards compatibility from unchanged field names. Check semantic constraints, events in flight, delayed consumers and persisted records, not just HTTP status codes.

## Data and invariant migration

- Key ownership; authoritative source at each state:
- Schema ID/version, optional/default semantics, read/write duality and old-reader compatibility:
- Backfill identity and stable cursor/checkpoint; retry and deduplication:
- Reconciliation by business key and semantic hash/meaning, not only row count:
- Change capture, lag horizon, out-of-order writes, error/dead-letter reporting:
- Point after which an old binary can no longer interpret newly committed state:
- Backup provenance, restore exercise and permissible data-loss bounds:

## Go/no-go check and abort authority

| Stage | Required invariant/SLI | Actual tool and reproducible scenario | Minimum acceptable result | Owner/signoff | Observed evidence or unknown |
|---|---|---|---|---|---|
| Before first new write | | | | | |
| Before routing expansion | | | | | |
| Before old path removal | | | | | |
| During fault/recovery | | | | | |

If any required field is unknown, pause at the current reversible state. Never claim success from a merely planned test.

## Recovery and irreversibility

- What can be reverted by routing/code alone? Exact until-when condition:
- What old/new data cannot safely be read in both directions?
- Under which observable event do we STOP rollback and run **forward recovery** instead?
- Failed deploy, mid-backfill crash, duplicate event, out-of-order update, retention loss and restore drill:
- Idempotent resume/reconciliation procedure; evidence to declare repaired:
- Safety owner, incident command, budget and rollback decision rights:

## Outcome and review

- Approved original hypothesis/decision and validation status:
- Captured actual test results vs proposed experiments:
- Residual unknowns, operational debt and decommission preconditions:
- Link the immutable artifacts, configuration and exact public/vendor docs:
- Named independent reviewer (if obtained) and revisit triggers:
- Text alternative for any original architecture/state diagram:

If old readers cannot process new data, **a code rollback is not automatically safe**. Treat irreversible migration as a distinct stage with an explicit no-return gate and tested forward-recovery plan.
