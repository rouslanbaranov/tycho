# Delivery, deployment and disaster recovery

Status: first bounded research chapter; the full proposed delivery/recovery volume is **not** complete.

## Purpose and mission

Explain how CI, rollout, compatibility, health signals, state ownership, failure domains and recovery objectives fit together. A deployment controller's successful transition must not be mistaken for proven user-level correctness or restored recoverable data.

## Reading map

```mermaid
flowchart LR
    Build["Release artifact"] --> Deploy["Rolling, canary or blue-green"]
    Deploy --> Compatibility["Mixed-version contract"]
    Compatibility --> Monitor["User outcomes and data invariants"]
    Monitor --> Recover["Rollback or forward recovery"]
    Recover --> Evidence["Recovery evidence and next decisions"]
```

Text alternative: prepare versioned artifacts, select a rollout strategy, validate old/new compatibility, observe users and data, then carry out a tested recovery/repair path with recorded evidence. The map shows **research responsibilities**, not a real deployment.

## Existing research

- [Safe rollout, compatibility and recovery under partial failure](safe-rollout-and-recovery.md) — original synthetic transition and failure diagrams, Kubernetes/Argo deployment semantics, rollback limits and an insufficient-evidence RPO/RTO scenario.

## Unwritten questions

CI/CD architecture, supply chain provenance, VM/container/serverless choices, database evolution, zone/multi-region placement and independent recovery tests are planned but remain separate unresearched chapter areas. See the [proposed structure](../PROPOSED-STRUCTURE.md).
