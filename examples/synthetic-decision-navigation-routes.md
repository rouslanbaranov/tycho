# Four synthetic decision routes and negative results

> Companion to [Tycho's navigation contract](../authoring/models/decision-navigation.md), issue #22. All events, counts, systems and outcomes are fictional. This is NOT a tested search provider, approved modernization plan or evidence that a specific pattern performs better.

The same fictional workshop-registration journey is used to make route results comparable. Consult the [requirements model](../authoring/models/requirements-workload-profile.md), [legacy baseline](../authoring/models/legacy-modernization-profile.md), [pattern applicability](../authoring/models/pattern-applicability-card.md), [ADR method](../authoring/models/candidate-comparison-adr.md) and [transition model](../authoring/models/target-transition-architecture.md). None is a source of observed production metrics.

## R1: Begin from a requirement

**Input:** “Can the registration journey handle a surge of 200 offered commands per second?” No operation mix, peak duration, request amplification, current service capacity, business deadlines or data size are supplied.

**Canonical navigation:** requirements workload dimensions → [queueing and arrival boundaries](../book/volumes/v07-performance-scale-and-resilience/c01-queueing-littles-law-and-measurement-boundaries/queueing-littles-law.md) → [conditional admission applicability](synthetic-admission-control-card.md) → ADR comparison.

**Missing evidence:** offered/admitted/completed logical operations by tenant and command, p95/p99 and errors, queue/resource bottleneck, cost and duration of burst, preserved no-double-seat allocation invariant. The value 200 is **an invented query input, not a measured threshold**.

**Output:** `MEASURE_FIRST`, not “deploy queue”, “use microservices” or “scale to N replicas”. Record the accepted user-level SLI and run both open and closed load models as appropriate. A proven minimal improvement may retain the deployment.

## R2: Begin from a symptom

**Input:** “p99 sometimes increases during registration.” Neither time window, client measurement point, independent offered rate nor suspected downstream bottleneck is specified.

**Competing hypotheses:** (H1) bounded DB pool wait, (H2) slow external dependency, (H3) serial lock hotspot on a workshop key, (H4) suppressed client arrivals causing a misleading load-test sample.

**Canonical navigation:** [legacy observation/hypothesis register](../authoring/models/legacy-modernization-profile.md) → queueing chapter and existing [pool/sharding chapter](../book/volumes/v03-execution-concurrency-and-flow-control/c05-thread-connection-and-buffer-pools/connection-pools-hikaricp-pgbouncer.md) → conditionally viable patterns → ADR only after distinguishing causes.

**Output:** `INSUFFICIENT_EVIDENCE`. Instrument pool acquisition, transaction/lock waits, dependency spans, offered vs actual generation and per-route p99, with comparable high/low load windows. An untested hypothesis is not a diagnosis and does not authorize decomposition.

## R3: Begin from a legacy constraint

**Input:** “Some third-party callers cannot upgrade concurrently with the server.” Existing old/new request schema compatibility and the time horizon of callers are unknown.

**Canonical navigation:** [legacy integration and version boundary](../authoring/models/legacy-modernization-profile.md) → [target and transition](../authoring/models/target-transition-architecture.md) → current [ADR](synthetic-workshop-adr.md).

**Exclusion:** a breaking change that requires all clients to update atomically violates the stated compatibility requirement unless a version-negotiation/coexistence mechanism is validated.

**Output:** `CONTRAINDICATED` for the breaking-in-place candidate, plus `INSUFFICIENT_EVIDENCE` for any proposed target that lacks old-client/new-server and new-client/old-server tests. A backward-compatible change in the existing deployment remains a candidate. No external system is described.

## R4: Begin from a modernization objective

**Input:** “Reduce the operational risk of a poorly supported runtime without disrupting existing client behavior.” The actual runtime version, advisory, module coupling and test coverage have not been provided.

**Canonical navigation:** [requirements outcomes](../authoring/models/requirements-workload-profile.md) → [legacy support/version snapshot](../authoring/models/legacy-modernization-profile.md) → [candidate comparison](../authoring/models/candidate-comparison-adr.md) → [transition gates](../authoring/models/target-transition-architecture.md).

**Plausible options:** (A) supported runtime upgrade in the same deployment; (B) branch by abstraction if internal calls can be intercepted; (C) independent service extraction only if a corresponding bounded requirement and data-interface ownership are established. None is approved.

**Output:** `RETAIN` existing architecture *as topology* while investigating a compatible runtime upgrade; `MEASURE_FIRST` for all unknown version/coupling/rollback constraints. A supported-version advisory is required; guessing “legacy means obsolete” is forbidden.

## Route contract fixture table

| Route | Input uncertainty | Diagnostic target | Candidate exclusion | Legitimate outcome |
|---|---|---|---|---|
| R1 requirement | Burst mix/deadlines/limits missing | Arrival, resource, correctness and SLO profile | Universal scale-out threshold | MEASURE_FIRST |
| R2 symptom | Causal location unknown | Pool, dependency, lock and generator telemetry | Premature service split | INSUFFICIENT_EVIDENCE |
| R3 legacy | Old/new clients cannot be assumed compatible | Supported API matrix and irreversible writes | Atomic breaking deployment | CONTRAINDICATED + INSUFFICIENT_EVIDENCE |
| R4 objective | Runtime advisories and data unknown | Version inventory and coexistence tests | “All legacy must be microservices” | RETAIN + MEASURE_FIRST |

**Review boundary:** Every route points to actually existing, distinct canonical pages; none relies on a planned MCP endpoint, graph edge or made-up source ID. Route responses need the live facts required by a future user, not this fixture's invented outcomes. The examples exercise the contract's negative/retain paths only; no agent retrieval benchmark or independent expert review was performed.
