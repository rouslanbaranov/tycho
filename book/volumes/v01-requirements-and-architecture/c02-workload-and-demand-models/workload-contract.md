---
metadata_version: 1
id: "tycho.page.59682af71a9f435680917ae5ece63088"
kind: "page"
parent_id: "tycho.chapter.316b50ac3db440ae82c0986b896ff468"
canonical_path: "book/volumes/v01-requirements-and-architecture/c02-workload-and-demand-models/workload-contract.md"
title: "Workload contracts for architecture choices"
topic_ids:
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "What must a workload contract state before it can reject or support an option?"
route_hints:
  questions:
    - "What must a workload contract state before it can reject or support an option?"
  prerequisites:
    - "tycho.page.f66686aeabca4f5b8f550696bf37e557"
  related_ids:
    - "tycho.chapter.316b50ac3db440ae82c0986b896ff468"
    - "tycho.page.fdb4ef7f69154f8c8c433591f71494f9"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "workload"
    - "contract"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.fdb4ef7f69154f8c8c433591f71494f9; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Workload contracts for architecture choices

**Owning question:** What must a workload contract state before it can reject or support an option?

This page belongs to [V01/C02 — Workload and demand models](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.fdb4ef7f69154f8c8c433591f71494f9:6 -->
## 6. Workload state and unknowns: a usable input contract

A workload record could include the following fields as a **methodological table**, not a claimed final machine-readable schema:

| Field | Value example | Evidence status |
|---|---|---|
| User journey | Reservation final-decision command | Proposed synthetic scope |
| Window | 15 seconds during a publication event | Assumed, not observed |
| Operation mix | Reads 70%, writes 30% | Hypothetical |
| Offered arrival schedule | Timestamped independent intents, duplicates separately tagged | Requires source trace |
| Data model/skew | Top five keys account for 60% of writes | Hypothetical and decision-changing |
| Resource ceilings | CPU quota, pool limit, DB write lock, external call rate | Unknown until instrumented |
| Outcome SLO | Final correct result within specified time and population | Requirement, not achieved result |
| Security and cost constraints | Authorization checks, operating budget, retention | Requires owner and exact acceptance |
| Validation plan | Replay workload at low/peak/degraded rates | Future experiment, not run |

The values and constraints must be revisited when client behavior or schema changes. A workload profile is a versioned hypothesis, not a permanent truth about a product.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.fdb4ef7f69154f8c8c433591f71494f9:7 -->
## 7. Architecture implications are conditional

| Evidence | Candidate action | Why a premature action may be wrong |
|---|---|---|
| CPU hot path dominates under valid representative load | Reduce CPU cost or increase CPU capacity | Pool/thread changes may only worsen contention |
| Database connection acquisition dominates | Bound concurrency and inspect total pool budget | More connections can saturate the DB |
| One key dominates writes | Reconsider state/lock policy and key ownership | Sharding does not split one indivisible invariant |
| Synchronous user deadline too short for actual durable work | Re-negotiate outcome; consider accepted/pending semantics where allowed | Async acceptance is not a completed synchronous command |
| Cacheable public reads dominate | Evaluate cache with freshness and miss cost | Cache adds invalidation risk and may not fix writes |
| Short unpredictable burst exceeds warm capacity | Admission control or pre-warm under explicit cost/SLO | Autoscaling may arrive after the burst |

This table does **not** choose an architecture. It identifies what to measure and when a mechanism could become applicable. [Pattern applicability](../../v10-decision-support-and-modernization/c03-pattern-applicability-and-contraindications/pattern-applicability-and-contraindications.md) is the later choice layer.


### Worked example: lost offered load versus server rejection

In an **original hypothetical** ten-second burst, a test schedules 1,200 iterations, starts 800, observes 500 correct completions, 100 explicit rejections and 200 timeouts, while dropping 400 iterations before starting them. These invented counts distinguish scheduled load from actual attempts and correct business effects. The server cannot be blamed for 400 attempts that never reached it. The 200 timeouts might conceal durable commits and require operation-ID reconciliation.

The [k6 open/closed workload contract](https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/open-vs-closed/) explains why clients that wait for prior responses may hide overload by reducing their own arrival rate. Its [dropped-iterations reference](https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/dropped-iterations/) identifies both generator sizing and system slowdown as possible reasons for drops; a drop counter alone cannot distinguish them. Actual ingress observations and generator resource measurements are necessary.

**Proposed, not executed:** rerun the same planned arrival schedule with sufficient generator headroom, then compare ingress attempts, admission, correct durable outcomes and post-burst backlog. Do not treat 50 correct completions per second as a tested maximum capacity or equate timeout with non-commit. The [queueing chapter](../../v07-performance-scale-and-resilience/c01-queueing-littles-law-and-measurement-boundaries/queueing-littles-law.md) owns finite-window conservation; [benchmark validity](../../v07-performance-scale-and-resilience/c03-load-test-methods-and-benchmark-validity/load-testing-and-benchmark-validity.md) owns workload-generator bias.

### Paired arrival traces under the same constrained service (original synthetic calculation)

The following **matched six-second comparison is arithmetic, not a k6 run**. The backend can execute two operations concurrently; each admitted operation occupies its slot for exactly two seconds. Service is FIFO, no retries or failures occur, and there is no think time after a completed closed-loop operation. Both generators have access to the same logical catalogue and identical server capacity. Only the *client arrival contract* changes; this is deliberate, not a measured estimate of a population.

- **Closed generator:** two users each submit a new intent immediately after their previous two-second request finishes. Starting at `t=0`, arrivals are two at 0, 2 and 4 seconds.
- **Open generator:** an external schedule presents **two new independent intents every second**, even when older operations are unfinished. It is not throttled by the server's response time. Twelve intents arrive at 0–5 seconds.

| Second `[t,t+1)` | Closed arrivals | Open scheduled/started arrivals | Cumulative correct completions by `t+1`: closed / open | Open outstanding by `t+1` |
|---|---:|---:|---:|---:|
| 0 | 2 | 2 | 0 / 0 | 2 |
| 1 | 0 | 2 | 2 / 2 | 2 |
| 2 | 2 | 2 | 2 / 2 | 4 |
| 3 | 0 | 2 | 4 / 4 | 4 |
| 4 | 2 | 2 | 4 / 4 | 6 |
| 5 | 0 | 2 | 6 / 6 | 6 |

**Clock convention and reconciliation:** a pair of occupied slots finishes at the exact boundaries `t=2`, `t=4`, and `t=6`, freeing two slots for queued work. Thus, by `t=6`, the closed model offers and completes six intents and has no remaining work. The open model offers twelve, completes six, and has **six outstanding** (two running, four queued). Those totals exclude repeated attempts, timeouts and scheduled-generator drops by construction. With a real load generator, scheduled iterations, started iterations, backend ingress, admitted operations, and correct completions must be recorded separately. The shared two-user population is *two logical client identities*: the open scheduler is allowed to issue concurrent independent intents for them, while the closed scheduler waits for a response before each identity issues its next intent. This difference is the comparison's variable, not an observed user behavior claim.

**Architectural consequence:** sizing from *completed requests per second alone* cannot distinguish the two cases. The open model requires bounded admission, queue/deadline policy and possibly pre-warm for a sustained offered rate above one correct completion per second. The closed generator silently slows its offered arrival rate as requests take longer. If the same six-second population is instead scheduled at a lower open rate, the backlog conclusion must be recomputed from that offered trace. The [k6 generator documentation](https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/open-vs-closed/) provides the modeling distinction; it does **not** establish the invented two-second service time or that the live backend can sustain it. **Not run or benchmarked.**

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](demand-skew.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](workload-demand-and-arrival-models.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
