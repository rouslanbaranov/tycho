---
metadata_version: 1
id: "tycho.page.1810c1f1f11648bdba66aafa5da60d33"
kind: "page"
parent_id: "tycho.chapter.691463ecbf6f44af84274ab3ff798b3d"
canonical_path: "book/volumes/v09-observability-security-and-operations/c06-incident-response-and-operational-change/incident-practice.md"
title: "Practice and recovery readiness"
topic_ids:
  - "observability"
perspectives:
  - "architecture"
  - "operations"
summary: "What must an incident exercise demonstrate before the runbook is trusted?"
route_hints:
  questions:
    - "What must an incident exercise demonstrate before the runbook is trusted?"
  prerequisites:
    - "tycho.page.ddc98233f12643a287ccd6bd0b92b4d6"
  related_ids:
    - "tycho.chapter.691463ecbf6f44af84274ab3ff798b3d"
    - "tycho.page.d87f9ba3852b49ee8188d150bb679716"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "incident"
    - "practice"
evidence_scope:
  source_ids:
    - "src.sre-workbook-incident-response"
  claim_ids: []
  status: "source-linked"
  notes: "Bounded question from tycho.page.d87f9ba3852b49ee8188d150bb679716; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: "2026-10-20"
content_verified_at: null
---
# Practice and recovery readiness

**Owning question:** What must an incident exercise demonstrate before the runbook is trusted?

This page belongs to [V09/C06 — Incident response and operational change](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.d87f9ba3852b49ee8188d150bb679716:6 -->
## 7. Practice response before production failure

The architecture should be exercised with bounded **failure drills**, preferably in a safe isolated environment first: change a response to error, pause a synthetic consumer, kill a nonauthoritative replica, simulate unavailable backup, corrupt a generated *test* index. Check not only recovery speed but whether metrics detect it, responder permissions are sufficient, instructions are unambiguous, and business invariants survive.

A complete rehearsal is explicit about:
- Which user journey/failure classes were exercised and which were not.
- What signal triggered response, including false-positive/false-negative boundaries.
- Actual detection, decision, mitigation, restored correctness and communication times from a declared clock.
- Whether restoring code, authoritative state and derived data required different actions.
- Which intervention would be unsafe under untested production conditions.
- Which corrective action can be verified later through tests, drills or changed failure exposure.

An uncontrolled real failure is not an acceptable experiment merely to validate a book diagram. Production exercises need independent risk approval, safe rollback and safeguards; Tycho's fictional exercises cannot provide it.

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [Health, Readiness and Liveness Checks](../../v11-pattern-atlas/c11-security-operations/health-readiness-and-liveness-checks.md#health-readiness-and-liveness-checks) — decision conditions and contraindications.


## Original tabletop exercise — recovery must have an oracle

Prepare a fictional incident in which catalogue search is stale while the authoritative item store remains correct. Give participants a visible symptom, a current permission boundary and several plausible explanations. Do not give them a secret instruction to select a predetermined remedy. The exercise should reveal how they distinguish observations, hypotheses and authorized changes.

One person coordinates the response and assigns work; another owns a proposed operational action; a communication owner records what users currently experience. Before performing a hypothetical restart or traffic move, ask which invariant could be harmed, what evidence permits the action and what would trigger its reversal. An observer records when authority or ownership becomes ambiguous.

The success condition is not that participants eventually name the planted explanation. Require a bounded impact assessment, a durable decision chronology, a safe mitigation and an explicit check of user-visible correctness after mitigation. Include an action that restores process health without repairing stale state, so the team must distinguish a green deployment from a recovered service.

The [SRE Workbook incident-response chapter](https://sre.google/workbook/incident-response/) supports defining response roles, shared coordination and practice before an incident. The catalogue scenario, evaluation oracle and failure injection above are original educational proposals. No exercise was run and no recovery time was measured; a tabletop also does not demonstrate the target deployment's real failover or restore behavior.

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](incident-evidence.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](incident-response-and-operational-change.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

## Bounded pattern ownership notes

These notes define the decision boundary for atlas cards whose mechanism is
not the main subject of this page. They are synthetic design guidance unless a
sentence attributes a claim to a cited public source; otherwise no source claim is made.

### Health, Readiness and Liveness Checks

Health checks answer different questions: liveness asks whether the process should be
restarted, readiness asks whether it should receive traffic, and startup asks whether
initialization has completed. Each needs its own endpoint, timeout and failure action. Use
them when the runtime can separate process health from dependency readiness. Do not use a
liveness check to test a shared dependency, because a dependency outage would restart
healthy workers and amplify the failure.

The failure path is a false restart or traffic sent to an unready instance; bound probe
timeouts, require consecutive failures and keep shared-dependency checks out of liveness.
External journey monitoring is the alternative when process-local probes cannot observe
the user-visible contract. It observes the journey but does not by itself establish process
health or readiness. For process or host liveness, a dedicated application endpoint is
also not the only route. The public Health Endpoint Monitoring pattern states in its
"When to use this pattern" section: "A platform-managed transport-level probe can be
sufficient when there's no application-specific logic, dependency chain, or functional
behavior to verify." Where a compatible health interface is unavailable, it also recommends
"platform-level metrics, log-based alerts, or internal heartbeat mechanisms instead."
Those are the alternatives for process or host liveness; reverse the choice when
application-specific logic, a dependency chain or functional behavior must be verified.

**Source boundary.** The transport-level and telemetry alternative is bound to Microsoft's
public Azure Architecture Center, "Health Endpoint Monitoring pattern",
<https://learn.microsoft.com/en-us/azure/architecture/patterns/health-endpoint-monitoring>,
page updated 2026-09-26, accessed 2026-10-29; canonical text SHA-256
`b5b302585c4e60a5d696b128b6a03d21c9629848e9fa2be23e6e1bc1751d1d61`. The Kubernetes
documentation remains the source for the liveness, readiness and startup probe semantics.
The transport-level probe does not establish readiness or startup behavior; the
telemetry alternatives detect only what their signals cover.

**Limits.** Probe frequency, false positives and dependency coupling are costs; a green probe
does not prove a correct user journey.
