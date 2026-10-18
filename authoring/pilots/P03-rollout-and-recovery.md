# Pilot P03 — Safe rollout, compatibility and recoverability

**Status:** research contract ready; chapter research and writing **not performed**. **Execution owner:** [#40](https://github.com/rouslanbaranov/tycho/issues/40). **Draft book owner:** V08/C04–C07 (links to V05/C06–C07). **Pilot class:** failed deployment and recovery scenario, with explicitly synthetic legacy-modernization constraints.

## Decision question and bounded scenario

A fictional deployed registration platform changes its data contract and rolls an application version while registrations continue. An instance or deployment failure occurs halfway through. How can operators reason about **target architecture versus intermediate compatibility states**, safe rollback/forward recovery, acknowledged data and observable go/no-go checks?

The example must not embed real organization topology, internal systems, or data.

## Public evidence to read and pin

- `src.k8s-deployments`: [Kubernetes Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) — rolling update, progress/availability, rollback and limits; pin the documentation version and relevant subsections.
- `src.argo-rollouts`: [Argo Rollouts concepts](https://argo-rollouts.readthedocs.io/en/stable/concepts/) — canary, blue/green, analysis and controller operational constraints; pin a specific supported release when writing.
- `src.aws-dr`: [Disaster recovery workloads](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html) — use only as a *provider-specific public perspective* on RPO/RTO and recovery patterns; distinguish proposals from generally verified guarantees.
- `src.flyway`: [Flyway documentation](https://documentation.red-gate.com/flyway) — if needed, read exact migration behavior/version as a concrete implementation boundary, not as evidence that all schema rollouts are safe.

## Required steps and failure matrix

1. State a synthetic baseline: old application, current storage contract, mixed-version duration, client compatibility, tolerated downtime and a **proposed** RPO/RTO. All invented until independently verified.
2. Separate target-state architecture from at least two intermediate transition states (old+new binary, expanded schema with mixed readers/writers).
3. Describe one forced rollout failure and one loss-of-dependency case: user-visible effect, in-flight retry/duplicate, metrics and invariant checks, durable writes and ambiguous outcomes.
4. For every transition stage, identify prerequisites, rollout gate, abort gate, rollback or forward-only recovery, irreversible actions and reconciliation.
5. Compare simple rolling deployment with canary/blue-green using evidence and operational overhead; state when extra orchestration is unsupported by available evidence.
6. Include one **intentionally unanswerable** case: missing restore rehearsal or data-reconciliation proof prevents promising the RPO/RTO. Output "test restore first" rather than a fabricated guarantee.

**Exclusions:** deploying real infrastructure, claiming exact downtime/failover performance, writing migration SQL for a production system, equating healthy rollout status with user-outcome correctness.

## Acceptance

Bounded evidence-backed recovery pages with named versioned sources and exact sections, original state/failure timeline, explicit target and transition architectures, testable go/no-go and rollback/forward conditions, unresolved risks, possible counterexamples and one evidence-insufficient outcome. CI source-boundary and manual technical/source review are necessary; no live recovery exercise or human approval is assumed.
