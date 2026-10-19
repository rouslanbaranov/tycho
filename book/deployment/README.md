# Deployment topology, availability and disaster recovery

## Purpose and mission

This part of Tycho answers two questions before naming a deployment product: **where does a system run, and which failure can it survive without violating its business invariants?** Runtime form, service placement, control-plane availability, recoverable business state and operators' actual restore ability are separate architectural responsibilities.

## Canonical chapters

1. [Deployment topology and control-plane independence](runtime-placement-and-control-plane.md) — bare metal, VMs, containers, managed functions, cluster placement, service mesh, data/control planes, IaC state and failure isolation. Use this first when a runtime or placement recommendation is requested.
2. [Availability zones, placement and failure domains](availability-zones-placement-and-failure-domains.md) — **V08/C06** replicas, gateway/state dependencies, quorum placement and zonal failure acceptance.
3. [Disaster recovery, RTO/RPO and state reconciliation](disaster-recovery-and-recovery-objectives.md) — **V08/C07** disaster-class recovery, fencing, acknowledged-state reconciliation and synthetic restore drills.
4. [Earlier multi-zone/multi-region research](multi-region-disaster-recovery-contracts.md) — preserved combined source for provenance mapping; no longer shared primary owner.

## Boundaries and reading routes

| Question | Start | Expand when needed |
|---|---|---|
| Containers, VMs or serverless for this workload? | [Runtime/placement](runtime-placement-and-control-plane.md) | [Workload shape and capacity experiments](../performance/workload-profiles-and-capacity-experiments.md) |
| How can traffic survive one zone failure? | [Failure-domain placement](availability-zones-placement-and-failure-domains.md) | [Recovery](disaster-recovery-and-recovery-objectives.md) and [safe rollout](../delivery/safe-rollout-and-recovery.md) |
| Does multi-region deployment mean RPO=0? | [Recovery](multi-region-disaster-recovery-contracts.md) | [PostgreSQL WAL and recovery](../data/postgresql-wal-replication-and-recovery.md) |
| Is an application image rollback also a data rollback? | [Safe rollout](../delivery/safe-rollout-and-recovery.md) | [Recovery](multi-region-disaster-recovery-contracts.md) |
| Can the system safely operate while orchestration services are impaired? | [Runtime/placement](runtime-placement-and-control-plane.md) | [Recovery](multi-region-disaster-recovery-contracts.md) |

A topological diagram is not evidence of RPO/RTO compliance, even where it shows multiple regions. Each decision needs the relevant business operation, data owner, client-visible SLI, exact failure injection, successful restore and a named reviewer.

## Research and completion status

These topic chapters are original, source-linked technical drafts for [E14-09 #87](https://github.com/rouslanbaranov/tycho/issues/87). The failure timelines and comparative examples are **synthetic**; no cloud account, disaster exercise, VM/container benchmark or independent human review is claimed. Their evidence-ledger passages distinguish official publisher mechanisms from unknown provider and workload-specific outcomes.

Other topics in V08 (CI/CD, GitOps and data schema evolution) are owned by subsequent E14-10 work and should not be declared covered by this landing page.
