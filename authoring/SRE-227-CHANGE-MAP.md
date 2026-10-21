# SRE #227 source-to-Tycho change map

**Status:** implementation input for issue #227. P1 (overload, retries, caching and
recovery) is implemented and validated in PR #229; P2 (load balancing, consensus
placement, periodic work, launch demand and operational clarification) is implemented
and validated in the current #227 delivery branch. This document is not book prose,
an acceptance record, an independent review, or a completed comparison of the whole
SRE book.

**Baseline:** `main` at `6754bac` (tree `751d6e08650173d4655370b4989585e4c7ecdaea`), the frozen baseline used by #225. The #227 branch starts from that baseline; its governance commit `5c911e0` changes only `AGENTS.md` and `sources/README.md`. The comparison below targets the book content at `6754bac`.

**Source scope:** *Site Reliability Engineering* (2016), public HTML at the [publisher's table of contents](https://sre.google/sre-book/table-of-contents/). Selected sections of chapters 19–27 and 33 were re-inspected on 2026-10-21 for this map. Chapters 28–30 were checked at heading and #225 note level; appendix E is referenced only through #225's notes and is not treated as a current standard. #225 records the full-scope reading of all 48 public book units and remains the broader research owner. Linked publications, videos and code named by the book are separate sources and were not read for this map. The source is a 2016 operational account; its examples are contextual, not universal laws or current product documentation.

**Method:** for each candidate direction, locate the exact source section, then the
current Tycho owner (stable ID, path and section), then classify the comparison. A
**proposed change** is a proposal; except for the delivered P1/P2 rows, it has not been
authored, reviewed or executed. A **verification** is a question, counterexample or
failure scenario the eventual explanation must withstand, not a completed test.

**Outcome legend:**

- **already covered** — the current page states the mechanism with adequate qualifications; preserve it.
- **clarification** — the mechanism exists but a material distinction, condition or failure mode is missing or easy to misread.
- **deeper** — the mechanism is named but the causal chain, applicability limits or recovery conditions need a bounded expansion.
- **missing** — no current canonical owner addresses the owning question; a new page or a new section in an adjacent owner is proposed.

## Coverage summary

| Direction | Already covered | Clarification / deeper | Missing |
|---|---:|---:|---:|
| Load balancing | 1 | 1 | 2 |
| Overload and retries | 1 | 4 | 1 |
| Caching and recovery | 1 | 2 | 1 |
| Consensus | 2 | 1 | 0 |
| Schedulers and pipelines | 0 | 2 | 2 |
| Data integrity | 1 | 1 | 1 |
| Launches and change | 1 | 1 | 1 |
| Operational architecture | 2 | 1 | 0 |
| **Total** | **9** | **13** | **8** |

The counts are a navigation aid, not a target. Several rows are small clarifications;
the table must not be read as a demand to add ten pages. Rows CR-2/DI-1 and CR-3/DI-2
describe the same substantive change under two directions; implement each once in
`V05/C07`.

## Delivery status

- **P1 — implemented and validated:** overload rejection cost and criticality, retry
  layering and budgets, cache capacity versus latency, detection latency and selective
  restore, and multitenant fair re-admission. Delivered in PR #229.
- **P2 — implemented and validated:** resource/error/subsetting load-balancing
  guidance, quorum placement, a new periodic-work/leases/exactly-once page, launch
  demand and client behavior, recurring manual-work costs, and the collaboration
  project's ambiguous periodic reconciliation. The P2 changes are in the current
  #227 delivery branch.

## 1. Load balancing

| ID | Source section | Tycho owner (ID / path / section) | Outcome | Proposed change | Verification |
|---|---|---|---|---|---|
| LB-1 | Ch. 20, *Load Balancing Policies* → *Varying query costs* and *Weighted Round Robin* | `tycho.page.ad9c044731ff175a4d0bb6106fe2a0f7`; `book/volumes/v08-delivery-deployment-and-recovery/c08-network-request-paths-routing-and-edge-delivery/discovery-balancing.md`, *Original worked design: one connection is not one unit of work* | clarification | Compare connection-count, active-request-count and resource/utilization signals. Explain backend-reported utilization and error rates; note that active requests misrank I/O-bound work and that a request-cost cap may change the interface. | A two-backend synthetic case where one has twice the CPU and requests wait on I/O: which policy balances completed work rather than open requests? Does the choice reverse under CPU-bound load? |
| LB-2 | Ch. 20, *Least-Loaded Round Robin* (fast-error sinkhole) | `tycho.page.ad9c044731ff175a4d0bb6106fe2a0f7`; same page, *Failure and recovery* and *Original worked design* | missing | Add fast-error traffic attraction: a backend returning errors quickly looks lightly loaded, so a least-loaded or active-request selector can concentrate traffic on it. Add error/health weighting or an equivalent guard; distinguish this from a slow backend. | Inject a backend that returns errors in roughly 1 ms. Does least-loaded send it more traffic? Does the proposed signal divert new work while preserving recovery probes? |
| LB-3 | Ch. 20, *Limiting the Connections Pool with Subsetting* → *Picking the Right Subset*, *Random Subsetting*, *Deterministic Subsetting* | `tycho.page.ad9c044731ff175a4d0bb6106fe2a0f7`; same page, *The routing contract*; `connections-draining.md`, *A bounded drain procedure* | missing | Add bounded client–backend subsetting: connection and health-check cost, uniform assignment, churn on restart or resize, and the subset-size trade-off. Do not turn the source's example sizes into a universal default. | Restart one backend in a 100-backend fleet. Measure reconnect churn, per-backend load skew and recovery time with full membership versus a bounded subset. |
| LB-4 | Ch. 19, *Load Balancing Using DNS* and *Load Balancing at the Virtual IP Address* | `tycho.page.ad9c044731ff175a4d0bb6106fe2a0f7`; same page, *DNS and discovery have different update boundaries* and *Failure and recovery* | already covered | No prose change. Preserve the distinction between DNS TTL, resolver caching, established connections and a route update; cite the exact chapter sections in the page ledger if they are absent. | Resolver unavailable and a removed backend still cached. The existing text requires a bounded cached answer and explicit staleness; no new mechanism is needed. |

## 2. Overload and retries

| ID | Source section | Tycho owner (ID / path / section) | Outcome | Proposed change | Verification |
|---|---|---|---|---|---|
| OR-1 | Ch. 21, *Client-Side Throttling*; ch. 22, *Retries* | `tycho.page.d9abd43bb7394c04a6bf77d4014f870d`; `admission-resource.md`, §2 *Admission must precede the expensive operation* and §3 *Queues, limits and priority create new contracts* | missing | Add rejection-path cost: rejecting is cheaper only when the rejection path is actually cheap; a high rejection fraction can consume the remaining capacity. Require cheap validation, bounded rejection work, client-side self-throttling and separate offered/admitted/rejected/completed counts. | A service whose rejection path costs a large fraction of normal processing: at high offered load, does rejection itself consume the capacity needed for useful work? Compare with client-side throttling. |
| OR-2 | Ch. 21, *Handling Overload Errors* and *Deciding to Retry*; ch. 22, *Retries* (avoid multi-level retries) | `tycho.page.43414664520b4866929f7f006f27f59b`; `book/volumes/v02-application-boundaries-and-contracts/c05-public-apis-http-rpc-and-compatibility/deadlines-retries.md`, §3 *End-to-end deadlines, cancellation and retry budgets* (retry decision contract). Cross-link `V07/C05` `dependency-isolation.md` §4 and `V04/C04` `retry-retention.md` §6; do not duplicate the effect-identity rules. | deeper | Extend the retry decision contract with local imbalance versus broad overload. For a small overloaded subset, an immediate retry elsewhere may be appropriate; for broad overload, do not retry and let the failure surface. Retry only at the layer immediately above the failing layer, and propagate an “overloaded; do not retry” signal. The overload owner (`V07/C05`) decides which regime applies; `V02/C05` owns the generic contract. | A three-layer stack under 5% versus 80% backend overload: does the policy amplify attempts? Does a lower layer retry work that the layer above should have refused? Does intra-layer proxying create a cycle? |
| OR-3 | Ch. 21, *Deciding to Retry* (per-request and per-client budgets); ch. 22, *Retries* (server-wide retry budget) | `tycho.page.43414664520b4866929f7f006f27f59b`; `deadlines-retries.md`, §3; cross-link `V07/C05` `admission-resource.md` and `workload-profiles-and-capacity-experiments.md`, retry-amplification section | clarification | Distinguish a per-request attempt cap, a per-client retry ratio and a process/server-wide retry budget in the generic retry contract. Explain that a per-client ratio needs enough history and can misclassify sparse clients; count retries separately from original demand. `V07/C05` owns the overload policy that uses these budgets; `V04/C04` owns effect identity and retention. Do not import the source's numeric thresholds as defaults. | A high-volume client and a sparse client under the same partial failure: does the per-client ratio treat them appropriately? Does a server-wide budget cap amplification while preserving critical traffic? |
| OR-4 | Ch. 21, *Criticality* | `tycho.page.d9abd43bb7394c04a6bf77d4014f870d`; `admission-resource.md`, §3 *Fairness and priority*; `overload-admission-control-and-graceful-degradation.md` | clarification | Add authenticated criticality propagation to downstream calls; keep criticality separate from deadline and from a client-asserted class. State that a high-priority request must not become low-priority work at the next hop. | A critical request calls a shared dependency during overload. If criticality is not propagated, is the request shed? Does the dependency reject lower classes first? |
| OR-5 | Ch. 22, *Slow Startup and Cold Caching* | `tycho.page.f39fa61013ca41abbfba82ef48250f8f`; `cache-acceptance.md`, §5 *Failure/operation cost model* and §7 *Decision tests and recovery*; `stampede-protection.md`, §5 *Cache-loss and source-protection policy* | deeper | Classify cache dependence as a **latency cache** or a **capacity cache**. A capacity cache cannot be empty at expected load; adding one without source capacity creates a hard dependency. Add cold-start, broad-restart and slow-ramp tests; do not treat “fallback to the database” as automatically safe. | Empty the cache at peak. Does the source survive the full offered load? If not, the design has a capacity cache and needs either source capacity, admission during warm-up or a declared degraded contract. |
| OR-6 | Ch. 22, *Test Until Failure and Beyond* | `tycho.page.62ad1ae9e0d243d69b08be0ff32930a1`; `overload-recovery.md`, §7 *Experiments, acceptance criteria and costs* | already covered | Preserve the existing matrix. Add, if the owner agrees, rows for impulse versus gradual load and for exiting a degraded mode without human intervention. | The existing matrix already covers a short burst, dependency slowdown, ambiguous-command timeout and recovery after fault removal. The added observations would distinguish a capacity ramp from a step load. |

## 3. Caching and recovery

| ID | Source section | Tycho owner (ID / path / section) | Outcome | Proposed change | Verification |
|---|---|---|---|---|---|
| CR-1 | Ch. 22, *Slow Startup and Cold Caching* | `tycho.page.f39fa61013ca41abbfba82ef48250f8f`; `cache-acceptance.md`, §5 and §7; `tycho.page.edc267f2fa954e66891e006ddfbfb15f`; `stampede-protection.md`, §5 | deeper | Add the capacity-versus-latency classification and a recovery sequence: cold start, source admission, warm-up ramp, stale-service limits, and the condition that reverses the cache decision. | The OR-5 cold-cache test, plus a broad restart of every application replica. Does the recovery path stay within the source budget, and which user-visible result is degraded? |
| CR-2 | Ch. 26, *Types of Failures That Lead to Data Loss*, *Retention*, *Third Layer: Early Detection*, *Out-of-band data validation* | `tycho.page.60ffc845d47c44cba4af2760474d68c7`; `restore-drills.md`, §6 *Failure classes change the preferred architecture*; `recovery-objects.md`, §1 | deeper | Add corruption-detection latency: root cause, scope and rate of loss; creeping loss discovered late; out-of-band validation of a bounded invariant; the detection window and the retention window it implies. Treat validator cost, false positives and missing coverage as first-class limits. | A synthetic creeping corruption over several weeks: when would the validator detect it? Is the retained history long enough to restore before the corruption? Does a stricter validator reject legitimate changes? |
| CR-3 | Ch. 26, *Retention* and *Types of Failures That Lead to Data Loss* (narrow scope); *Knowing That Data Recovery Will Work* | `tycho.page.60ffc845d47c44cba4af2760474d68c7`; `restore-drills.md`, §3 *Original synthetic example* and §5 *Rehearse user-level recovery*; `tycho.page.8ff8bad016ba4b92ba968c18a9210020`; `recovery-objects.md`, §1–§2 | missing | Add selective restore: identify the affected tenant/record scope, restore into an isolated target, merge with current state under an authorized repair protocol, and verify referential integrity and external effects. A partial restore is not a smaller full restore. | Corrupt one tenant's records while other tenants continue writing. Can the team restore only that tenant without rolling back unrelated legitimate writes? Which invariants and approvals govern the merge? |
| CR-4 | Ch. 26, *Knowing That Data Recovery Will Work* (capacity, wall time, dependencies, monitoring) | `tycho.page.60ffc845d47c44cba4af2760474d68c7`; `restore-drills.md`, §5 table; `tycho.page.8ff8bad016ba4b92ba968c18a9210020`; `recovery-objects.md`, §4 | already covered | No prose change. The existing drill already requires sufficient storage, compatible runtime, archive access and a measured wall time. Optionally note concurrent restores if the recovery objective covers several datasets. | A single restore is covered. The open question is whether the team can restore several affected datasets concurrently within the same objective; record it as an unresolved capacity question rather than a new mechanism. |

## 4. Consensus

| ID | Source section | Tycho owner (ID / path / section) | Outcome | Proposed change | Verification |
|---|---|---|---|---|---|
| CO-1 | Ch. 23, *Deploying Distributed Consensus-Based Systems* → *Number of Replicas*, *Location of Replicas*, *Capacity and Load Balancing*, *Quorum composition* | `tycho.page.b93c892861fb4dd4afcfbdc2ced1af80`; `quorum-envelope.md`, §2 *Majority quorum arithmetic and the failure envelope*; `leader-recovery.md`, §5 *Reconfiguration and restoration are different actions* | deeper | Add quorum placement and failure-domain trade-offs: adding a replica can raise the quorum without increasing tolerated failures; co-locating replicas can remove redundancy; RTT and latency trade against failure-domain span; leader placement changes outbound network load and failover traffic. Cross-link `V08/C06` for the general placement model. | Five replicas across three zones with two in one zone: does loss of that zone remove quorum? Compare five and six replicas for tolerated failures and latency. What happens to quorum latency when the “link” replica is lost? |
| CO-2 | Ch. 23, *Motivating the Use of Consensus* and *How Distributed Consensus Works* | `quorum-envelope.md`, §1 and §3; `leader-recovery.md`, §4 and §6 | already covered | No prose change. The existing pages separate safety, liveness, durable state and client-visible unknown outcomes, and refuse to treat an overview as a correctness proof. | A minority partition must refuse unsafe writes/linearizable reads; a client timeout must remain an unknown outcome. The existing text already requires these checks. |
| CO-3 | Ch. 23, *Number of Replicas* (durable log, quorum loss, forced reconfiguration) | `leader-recovery.md`, §5 and §6 | already covered | No prose change. The existing page distinguishes membership reconfiguration from backup restore and records permanent quorum loss as a data-loss-bound recovery case. Optionally add the SRE chapter to the source ledger. | Permanent quorum loss and forced reconfiguration: the page already requires an explicit data-loss bound and does not claim automatic normal operation. |

## 5. Schedulers and pipelines

| ID | Source section | Tycho owner (ID / path / section) | Outcome | Proposed change | Verification |
|---|---|---|---|---|---|
| SC-1 | Ch. 24, *Cron Jobs and Idempotency*, *Tracking the State of Cron Jobs*, *Resolving partial failures* | No canonical owner. `V04/C05` (`tycho.chapter.18aa94285a164b6f94530cebcfd87b8b`) owns durable workflows, but `saga-workflows.md` §4–§5 covers multi-step compensation, not periodic launches. `V04/C08` owns stream processing, not cron. | missing | Add a page under `V04/C05`, owning the question “How does a periodic job recover when the launch outcome is unknown?” Cover skip versus double launch, stable launch identity including the scheduled time, idempotent external operations or authoritative outcome lookup, persisted state/snapshot, and the fail-closed trade-off. Link the new page from the C05 landing and from `V07/C05`. | The scheduler leader sends a launch RPC and dies before recording completion. The new leader must look up the precomputed job name plus scheduled time and launch only the missing names. Test both a double-launch and a skipped-launch variant; neither may be silently accepted. |
| SC-2 | Ch. 25, *Challenges with the Periodic Pipeline Pattern*, *Drawbacks of Periodic Pipelines in Distributed Environments*, *Workflow Correctness Guarantees* | No canonical owner. `V04/C08` covers stateful stream processing/checkpoints; `V04/C05` covers sagas/outbox. | missing | Add a bounded page or a substantial section under `V04/C05`: periodic pipelines, overlapping runs, lease validity, unique output names, task/config identity and the server/token identity. Distinguish exactly-once publication from exactly-once arbitrary external effects. | A configuration change lands while a work unit is in flight; an orphaned worker tries to commit; two workers hold overlapping leases; a different Task Master appears at the same address. Each case must fail closed. |
| SC-3 | Ch. 25, *Thundering Herd Problems* and *Moiré Load Pattern*; ch. 27, *Dealing with Abusive Client Behavior* | `tycho.page.62ad1ae9e0d243d69b08be0ff32930a1`; `overload-recovery.md`, §7; `tycho.page.edc267f2fa954e66891e006ddfbfb15f`; `stampede-protection.md`, §2 and §5; retry pages | clarification | Handle this inside the SC-1/SC-2 page with cross-links: synchronized periodic starts, overlapping pipeline cycles and shared-resource peaks. Recommend jitter/randomized schedules and measure aggregate demand; do not create a separate page. | Two periodic pipelines with occasionally overlapping cycles share a resource. Does randomized scheduling lower the aggregate peak without missing the declared completion window? |
| SC-4 | Ch. 25, *Workflow Correctness Guarantees* | `tycho.chapter.18aa94285a164b6f94530cebcfd87b8b`; `tycho.page.71aea7bc58a6411ba7baf8a2ff40ffbd`; `V04/C04` deduplication and `V04/C05` outbox/saga pages cover identity and publication, but not the lease/task/config/server-token tuple. | deeper | Add the four-boundary guarantee to the SC-2 page: valid lease at commit, immutable task/configuration identity, unique output names, and a validated coordinator identity. Explain which boundary fails open if one is omitted. | A stale worker with a valid old lease, a configuration change, and a misconfigured coordinator: each must be unable to publish. This is a proposed adversarial test, not an executed one. |

## 6. Data integrity

| ID | Source section | Tycho owner (ID / path / section) | Outcome | Proposed change | Verification |
|---|---|---|---|---|---|
| DI-1 | Ch. 26, *Types of Failures That Lead to Data Loss*, *Retention*, *Third Layer: Early Detection*, *Out-of-band data validation* | `tycho.page.60ffc845d47c44cba4af2760474d68c7`; `restore-drills.md`, §6 *Failure classes change the preferred architecture*; `tycho.page.8ff8bad016ba4b92ba968c18a9210020`; `recovery-objects.md`, §1 | deeper | Same substantive addition as CR-2, owned once in `V05/C07`. State the detection-latency and retention-window relationship; require validators to target invariants whose loss is catastrophic, not every invariant. | A creeping corruption over weeks; a validator that is too strict rejects a legitimate migration; a validator that is too narrow misses the corruption. The page must state which failure the chosen validator is expected to catch. |
| DI-2 | Ch. 26, *Retention* (merge restored data with current state); *Types of Failures* (narrow scope); *Knowing That Data Recovery Will Work* | `tycho.page.60ffc845d47c44cba4af2760474d68c7`; `restore-drills.md`, §3 and §5; `tycho.page.8ff8bad016ba4b92ba968c18a9210020`; `recovery-objects.md`, §1–§2 | missing | Same substantive addition as CR-3, owned once in `V05/C07`. Add the selective-restore protocol and its authorization/merge boundary. | One tenant's records are corrupted while others continue writing. A full restore would discard valid later writes; a selective restore must preserve them and prove referential integrity. |
| DI-3 | Ch. 26, *Knowing That Data Recovery Will Work* (resource capacity, wall time, dependencies) | `tycho.page.60ffc845d47c44cba4af2760474d68c7`; `restore-drills.md`, §5 table; `tycho.page.8ff8bad016ba4b92ba968c18a9210020`; `recovery-objects.md`, §4 | already covered | No prose change. Preserve the existing storage, runtime, archive-access and wall-time gates. Add a concurrent-restore question only if the objective covers multiple datasets. | The existing drill requires measured wall time and sufficient resources for one restore. The remaining unknown is concurrent restore capacity, not a missing single-restore mechanism. |

## 7. Launches and change

| ID | Source section | Tycho owner (ID / path / section) | Outcome | Proposed change | Verification |
|---|---|---|---|---|---|
| LA-1 | Ch. 27, *Capacity Planning*, *Client Behavior*, *Overload Behavior and Load Tests* | `tycho.page.3d13e39bb42a4458999803e40d7137cc`; `desired-state-exposure.md`, §4 *Release identity and evidence gates*; `tycho.page.21388c50717d4fa89384bedadcb0d3bd`; `canary-compatibility.md`, §3 and §5 | missing | Add launch demand as a distinct event: launch traffic may differ from steady state; client sync/retry behavior can multiply load; dependencies need provisioning before exposure; the stop condition must be concrete. Cross-link `V07/C05` and the retry owner rather than duplicating them. | A launch spike far above the steady-state estimate, with clients retrying on failure. Does the rollout stop condition trigger on user outcomes rather than pod health? Are the dependencies provisioned for the launch mix? |
| LA-2 | Ch. 27, *Rollout Planning*, *Gradual and Staged Rollouts*; appendix E | `tycho.page.3d13e39bb42a4458999803e40d7137cc`; `desired-state-exposure.md`, §2 *Release strategies and their limits* and §4; `tycho.page.21388c50717d4fa89384bedadcb0d3bd`; `canary-compatibility.md` | already covered | No prose change. Preserve staged exposure, stop/hold/abort controls and rollback/forward-recovery gates. Treat appendix E as an explicitly historical, abridged checklist, not a current exhaustive standard. | The existing page already requires exposure by cohort, a stop/abort authority and a rollback or forward-recovery plan. The proposed check is whether a launch-specific demand mix is included, not whether staged rollout exists. |
| LA-3 | Ch. 27, *Dealing with Abusive Client Behavior*; *Client Behavior* | `tycho.page.3d13e39bb42a4458999803e40d7137cc`; `desired-state-exposure.md`, §4; retry/overload pages | clarification | Add a cross-link, not a new mechanism: client-controlled sync intervals and retry behavior belong to the client/retry owners; the launch plan must test the actual client mix. | A client sync interval changes from ten minutes to one minute, multiplying load by ten. Does the launch plan test that mix, and does the client honor backoff/feature control? |

## 8. Operational architecture

| ID | Source section | Tycho owner (ID / path / section) | Outcome | Proposed change | Verification |
|---|---|---|---|---|---|
| OP-1 | Ch. 28, *Targeted Project Work, Not Menial Work*; ch. 29, *Managing Operational Load*; ch. 30, *Phase 1–3*; ch. 33, *Automating Away Repetitive Work and Operational Overhead* | `tycho.page.b8d02f9b40c44c729e2b99e01a8b0dbf`; `lifecycle-cost.md`, §4 *Operating cost is a lifecycle*; `operating-capacity.md`, §6 | clarification | Add recurring manual work as a capacity constraint: measure toil and its growth. Tycho inference, not a source claim: treat automation as a maintained system with its own failure, ownership and recovery cost. The source supports automation's benefits and the damage from incorrectly configured automation; it does not establish a universal automation policy. | A service whose manual reconciliation grows linearly with tenant count: at what scale does it exceed the team's capacity? Does the proposed automation have an owner, runbook and rollback? |
| OP-2 | Ch. 27, *Launch Coordination Engineering*; appendix E (historical/abridged) | `tycho.page.f3b4041502a7403bbc63bb2611eb5c0f`; `operating-capacity.md`, §6; `feasibility-gates.md` operations/staffing rows | already covered | No prose change. The existing readiness gate already requires owners, runbook/recovery evidence, access, version support, budget and revisit triggers. Avoid transplanting the source's checklist as a universal standard. | The readiness record names owners and recovery evidence. The source's staffing and checklist examples remain contextual; no universal numbers are added. |
| OP-3 | Ch. 15, *Postmortem Culture*; ch. 16, *Tracking Outages*; ch. 33, *Structured and Rational Decision Making* | `tycho.page.ddc98233f12643a287ccd6bd0b92b4d6`; `incident-evidence.md`, §7 *After-action analysis* | already covered | No new claim. Optionally add a cross-link from follow-up actions to the architecture decision record owner (`V10/C04`), so a prevention action can become a design change with an owner and acceptance test. | A postmortem action has an owner, acceptance test and residual-risk statement. The open question is whether the action is linked to a design decision when it changes architecture, not whether incident review exists. |

## Worked-project mapping

The three original projects in `V10/C07` already exercise several of these mechanisms. Stable IDs: catalogue `tycho.page.ae25f40712b658ecfb9d617ca977ad35`, collaboration `tycho.page.8743d09eab614132692f934fb22c5649`, multitenant `tycho.page.4856fd39b7e1bfa3b7430427192179fa`. Extend them only where the scenario actually composes the finding; do not duplicate the chapter walkthroughs.

| Project | Existing coverage | Proposed extension | Evidence state |
|---|---|---|---|
| `catalogue-project.md` | Object publication, outbox/search projection, retirement fences, restore and rebuild (`Retirement, crashes and recovery`; `Acceptance and conditions that reverse the decision`) | A metadata read cache is **not** part of the current design. If one is added to test CR-1/OR-5, it must be a declared latency cache with a cold-start and cache-loss test; otherwise leave the project unchanged. | Original synthetic design; no cache experiment executed. |
| `collaboration-project.md` | Durable edit admission, approval frontier, offline revocation, snapshot/log restore (`Failures, compaction and recovery`) | After SC-1 is implemented, add one periodic reconciliation job whose launch outcome is ambiguous. It must carry a stable job identity and an outcome-lookup path; the existing project does not test scheduler recovery. | Original synthetic design; no scheduler or reconciliation execution. |
| `multitenant-project.md` | Tenant burst, poison input, budget revision, cell outage, per-tenant budgets and cells (`Three failures and explicit recovery`) | Add fair re-admission after a shared overload episode: recovery hysteresis, per-tenant queues and a controlled ramp. This directly tests OR-1/OR-2/OR-5 composition without inventing a new project. | Original synthetic design; no load test executed. |

## P1 implementation package (delivered)

The first package remained bounded to the interacting mechanisms the issue recommends:
overload, retries, caching and recovery. It is implemented and validated in PR #229.

1. **Overload** — add rejection-path cost and criticality propagation to `admission-resource.md`; add the impulse/gradual and degraded-exit observations to `overload-recovery.md`.
2. **Retries** — add the generic retry decision contract (local-versus-broad overload, retry-layer ownership and the three budget scopes) to `V02/C05` `deadlines-retries.md`; put the overload-specific regime selection in `V07/C05`; cross-link `V04/C04` for effect identity and the existing retry-amplification arithmetic rather than duplicating it.
3. **Caching** — add the latency-versus-capacity classification and the cold-cache recovery sequence to `cache-acceptance.md` and `stampede-protection.md`.
4. **Recovery** — add detection latency and selective restore to `V05/C07`; update the multitenant project with fair re-admission.
5. **Provenance** — add exact SRE chapter/section rows to the affected page or chapter ledgers; use `src.sre` unless a specific chapter ID already exists. Do not invent a new source ID without an admission record.
6. **Indexes and validation** — rebuild the route index after any frontmatter change and run the repository gate ladder. No CI claim is implied.

The load-balancing, consensus, scheduler, launch and operational rows are implemented
in the P2 package. The scheduler rows received a separate canonical page and review
increment rather than a clarification-only bundle.

## P2 implementation package (delivered)

- **Load balancing:** selection signals, fast-error sinkhole and bounded subsets in
  `V08/C08` `discovery-balancing.md`.
- **Consensus:** quorum placement and failure-domain trade-offs in `V04/C02`
  `quorum-envelope.md`.
- **Schedulers and pipelines:** new `V04/C05` page on periodic launches, leases and
  exactly-once publication.
- **Launches:** launch demand, client behavior and dependency capacity in `V08/C04`
  `desired-state-exposure.md`.
- **Operations:** recurring manual-work capacity in `V01/C06` `lifecycle-cost.md` and
  an incident-to-design cross-link in `V09/C06`.
- **Projects:** periodic reconciliation with an ambiguous launch in the collaboration
  project.

## Review gate and unresolved questions

- P1 and P2 were authorized and implemented; this map is still an implementation input,
  not a reviewed finding set. Any further content change requires a new bounded package
  and a new content-revision entry.
- The SRE book is a 2016 operational account. Its numeric examples and organizational practices are contextual. The map does not convert them into universal thresholds, staffing rules or current product behavior.
- Protocol correctness for consensus, cron and pipeline leases must continue to rely on the existing protocol/implementation sources, not on the SRE overview alone. The map proposes operational conditions, not new protocol proofs.
- #225 remains the broader research owner. This map does not complete its source inventory, material-claim matrix or final deep synthesis, and it does not close #225 or PR #226.
- No experiment, load test, restore drill, scheduler failure or independent review was executed for this map. Every proposed verification remains a proposal.
