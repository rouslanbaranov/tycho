# Independent read-only delta review — V12 isolated volume remediation

## Review identity and pin

| Field | Value |
|---|---|
| Reviewer harness | OpenAI Codex |
| Vendor | OpenAI |
| Model | GPT-5-based Codex; exact serving version not exposed |
| Session identifier | Not exposed |
| Review timestamp | 2026-10-29T12:43:48Z |
| Repository | `/Users/rbaranov/Projects/tycho-v12` |
| Branch | `feature/TYCHO-587-v12-architecture-modeling-simulation-decision-validation-isolated-volume` |
| HEAD / content commit | `bb10d96c2149cf4e03332c599e69d0a4af173f7a` |
| Prior reviewed commit | `7e002cd2f0e2e7f4cf99ed84841ffd0259516e95` |
| Correction range | `7e002cd2f0e2e7f4cf99ed84841ffd0259516e95..bb10d96c2149cf4e03332c599e69d0a4af173f7a` |
| Author relationship | Independent reviewer; no authorship or prior involvement |
| Working tree | Clean at review start and end |
| Sufficiency claim | `sufficient: 0` |

## Verdict

**Reject.**

The correction makes substantial progress: correlations are now sampled, all ten run records
bind the current engine source, stored hashes are internally consistent, costs use the
measurement window, invariants are preserved in run and decision artifacts, schemas require
the result hash, source labels are bounded more honestly, and stale verification names were
corrected.

However, the retry correction introduces or leaves a blocking attempt-lifecycle defect. Queue
wait is no longer included in the documented per-attempt deadline, and a timeout while queued
does not consume the retry budget. The regenerated A/B/C results and checkout recommendation
therefore do not implement the declared model.

The correlated sensitivity screen also reports first-order and total-order variance shares
using formulas that omit covariance terms, although its inputs are explicitly correlated.

## Prior-finding dispositions

| ID | Disposition | Evidence |
|---|---|---|
| B1 | Resolved, with a new related high finding | `scripts/v12_engine.py:664-735` constructs a correlation matrix, applies Cholesky correlation, and transforms marginal draws. Correlated runs were regenerated. The sensitivity decomposition remains invalid for dependent inputs; see N2. |
| B2 | Resolved by static inspection | `scripts/v12_engine.py:847-856` binds `engine_sha256` into provenance and the input hash; `:896-912` checks it during replay. All 10 run engine, model, scenario, input and result hashes recomputed correctly. Replay was not executed. |
| B3 | Partially resolved | Completion and timeout events now carry attempt tokens, and stale completions are rejected at `scripts/v12_engine.py:303-305`. The same lifecycle resets the deadline on dispatch and fails to count queued timeouts as attempts; see N1. |
| H1 | Resolved | Checkout cost uses `duration - warmup` at `scripts/v12_engine.py:368-398`; regenerated A/B/C costs and prose use the corrected window. |
| H2 | Resolved, with stale prose | All 10 runs contain passing `invariants` records; both decisions contain explicit constraint evaluations. The checkout decision still says “all nine stored runs”; see N4. |
| M1 | Resolved | `schemas/v12/run-result.v1.schema.json:7-22` requires `result_sha256` and `invariants`. |
| M2 | Resolved | The two partial units now use a bounded register label, and the Owen unit names Appendix A.6 consistently. |
| M3 | Resolved for the listed gaps; tests not executed | Correlation, stale-completion, cost-window and committed-run replay tests exist, and all 10 model verification references name existing methods. The new queue-wait lifecycle defect is not tested. |
| L1 | Partially resolved | The protected set now contains five records, including `sufficient-rereview-packets.v1.json`. The baseline captures that file only after the initial V12 commit edited its route-index binding, so it does not prove the record was unchanged by V12. |

## New findings

### Blocking

#### N1 — Queue-inclusive deadlines and bounded attempts are not implemented

The canonical lifecycle says a deadline begins when a request enters the system or begins a
retry:

- `event-ordering-and-timeouts.md:82-94` defines arrival/retry time plus the timeout.
- Its worked case at `:104-108` requires a request that waits 0.9 seconds and then receives
  0.4 seconds of service to time out at 1.0 seconds.

The engine behaves differently:

1. Arrival schedules a timeout with attempt token zero at
   `scripts/v12_engine.py:327-340`.
2. Dispatch increments the attempt token and schedules another full timeout from service
   start at `:257-274`.
3. The original queue-inclusive timeout is then ignored by the token guard at `:276-278`.

A request dispatched after queueing therefore receives `queue wait + timeout`, rather than
the declared per-attempt timeout.

There is a second defect in the same lifecycle. `attempts` is incremented only when service
starts at `:265`, but a queued timeout checks that counter at `:291`. A request that repeatedly
times out while queued retains `attempts == 0`, so even `max_attempts == 1` can schedule
unbounded queue-timeout retries until the horizon.

This invalidates the documented timeout and retry semantics, retry-amplification meaning, the
regenerated checkout runs, and the quantitative evidence behind
`edition/v12/decisions/checkout-candidate.json`.

### High

#### N2 — Correlated inputs are passed to an independent-input variance decomposition

`edition/v12/scenarios/checkout-sensitivity.json:53-58` declares correlation `0.3`. The
sensitivity implementation correctly obtains correlated rows through `sample_row` at
`scripts/v12_engine.py:967-972`.

It then computes:

- `var_main_1 = b1² + 2b11²`;
- `var_main_2 = b2² + 2b22²`;
- `var_interaction = b12²`;

at `scripts/v12_engine.py:998-1015`.

Those terms are not a variance partition for correlated standardized predictors: covariance
and mixed quadratic terms do not vanish. No dependent-input sensitivity definition,
orthogonalization, or covariance terms are implemented. The reported `0.345/0.522` and
`0.478/0.655` values therefore cannot be interpreted as the claimed first-order and
total-order shares.

The bounds-only test at `tests/test_tycho_v12_engine.py:265-281` cannot detect this error.
This contradicts the statistical gate claimed at
`book/.../c07-validation-and-limits/validation-gates.md:99-106`.

### Medium

#### N3 — `rollback_seconds` silently excludes 18 failed rollback replications

The aggregation at `scripts/v12_engine.py:801-816` drops every `None` value. The fallback to
the horizon is used only when no replication has a value.

Consequently, `edition/v12/runs/modernization-staged.json` records:

- provenance replications: 20 at lines 153-162;
- `rollback_completed = 0.1` over 20 replications at lines 103-109;
- `rollback_seconds = 0.0` over only 2 replications at lines 111-117.

The latter is a conditional duration for the two successful rollbacks, but neither the metric
nor its limitations says so. It can be mistaken for a zero-second run-level rollback result.
The current decision uses `rollback_completed`, so this does not reverse its
insufficient-evidence outcome.

#### N4 — Correction and review metadata contain stale or unsupported statements

Several correction records conflict with the corrected artifacts:

- `authoring/V12-IMPLEMENTATION-2026-10-29.md:68-70` says the sensitivity run is
  `insufficient-sample`; its stored status is `converged`.
- The same file at `:64-66` says rollback does not complete, while the run and decision say
  it completes in 10% of replications.
- `edition/v12/decisions/checkout-candidate.json:190-195` says all nine stored runs preserve
  conservation; there are now ten.
- `authoring/V12-IMPLEMENTATION-2026-10-29.md:131` and
  `authoring/ai-reviews/README.md:100` name a specific prior-review model, while the raw report
  at `authoring/ai-reviews/2026-10-29-v12-isolated-volume-codex.md:7-10` says the exact serving
  version was not exposed.
- `authoring/V12-IMPLEMENTATION-2026-10-29.md:107` says no promotion record was edited, while
  `:112-116` records that an existing re-review packet binding was refreshed.

These are evidence and provenance records, so the contradictions should not be treated as
cosmetic.

### Low

No additional low-severity finding beyond the partially resolved L1 baseline issue.

## Static checks and derived counts

No repository validator, test, simulation, or replay command was run.

| Derived item | Count/result |
|---|---:|
| V12 Markdown documents | 31 |
| Volume landings | 1 |
| Chapter landings | 7 |
| Technical pages | 23 |
| Models | 3 |
| Scenarios | 10 |
| Runs | 10 |
| Decisions | 2 |
| Registry artifacts | 25 |
| Converged runs | 9 |
| Insufficient-sample runs | 1 |
| Correlated-input runs | 3 |
| Reading-ledger records | 10 |
| Newly registered sources | 9 |
| Reused source units | 1 |
| Source-plan topics / references | 8 / 16 |
| Unique source units | 10 |
| Generated V12 index entries | 56 |
| Protected pages / records | 449 / 5 |
| Manifest document hashes matching | 31/31 |
| Registry artifact hashes matching | 25/25 |
| Run result hashes matching | 10/10 |
| Model/scenario/engine/input provenance hashes matching | 10/10 each |
| Stored invariant records reporting pass | 10/10 |
| Unique manifest IDs and paths | 31/31 |
| Unique registry artifact IDs | 25/25 |
| Normalized A/B/C comparison digest | `447b1002806da92fe0f85805afcd5f64b755e40ea1dcecc08855dec865dc58ee` |

## Independently computed principal artifact hashes

These are file-byte SHA-256 values, not the embedded semantic result hashes.

| Artifact | SHA-256 |
|---|---|
| `scripts/v12_engine.py` | `9a91f9086cc9a9cbdb04b1bb25930a1d7ba2e42387c558056a802f6f3209611c` |
| `schemas/v12/run-result.v1.schema.json` | `38ced2b298589d2ffbbcd54ec50b1ea7de54dfc172ecb97a379dc7f0111c146b` |
| `schemas/v12/decision-record.v1.schema.json` | `9fa9e5e4b190d5d194cb017b66401b63b2f4252a19fbf86c991b5c7b39ca44fb` |
| `edition/v12/manifest.json` | `4c1cfea98627dfa44a715d606a897571b82570649c97ba93e28b1c26bfc20be3` |
| `edition/v12/registry.json` | `c502faef95df9621154c3bbed2baea19f1228336d0811f58880977f3d1011427` |
| `edition/v12/protected-baseline.json` | `9ba1457db211ca955e298ff61a8a681cd5c98a97af5bec1b8bcf10315d17b160` |
| `edition/v12/reading-ledger.v1.json` | `8f020d8beeed785a60b72b86c177c45a1abf2c79d6dcd38b13e00bbb80929abf` |
| `edition/v12/source-plan.v1.json` | `ed6e7b0ee447f2f7b663a47408d391fa42472f0d9ffa84d47970e36fb87c03a5` |
| `edition/v12/models/checkout-des.json` | `e20e16717a225e714709b5931e7fccc425303462c82c6fa058ee3059804254db` |
| `edition/v12/scenarios/checkout-sensitivity.json` | `70ea1f6bb103ace15c4561799b7720af843b16c10ca9d135efb02072558d4274` |
| `edition/v12/scenarios/checkout-convergence-stress.json` | `0801f149f9448140624388d8ae31b59cdff52509be8b7ee4c63b001f9218fff5` |
| `edition/v12/scenarios/modernization-staged.json` | `8cb384c7f6d29a230299bda8b1fe6c88689871f96c433e68f2872964617acd59` |
| `edition/v12/runs/checkout-a-synchronous.json` | `0000191a342fb185433c8b4ab70243dec8d4469872ec8da16d75b8dbc174a130` |
| `edition/v12/runs/checkout-b-queue.json` | `403adb6c54ecb8eab1da792ff7515e4ec80f597580bb5fc787a0c190f7bf0d9b` |
| `edition/v12/runs/checkout-c-partitioned.json` | `c5b7774a13739103ce6bab4228244ec24e6d5b37c4dd6696624772b8d8db9b95` |
| `edition/v12/runs/checkout-sensitivity.json` | `85e0311a3509109df03ef23333e9c9df357aeda7f9622f421aec73510b1b6abc` |
| `edition/v12/runs/checkout-convergence-stress.json` | `2ddcc0128160a13980ebfceb3473faed19026fe435a48c0fd54b7d7f5b729f14` |
| `edition/v12/runs/modernization-staged.json` | `4b8a6626ff6e40d7f1b732eda1c060e9b7ed509fecb5e047b4ccaa024f97de46` |
| `edition/v12/decisions/checkout-candidate.json` | `a714ead93d48f1c2de578ba398ec4b2d59e1cf15f4c6d19ed02335fc22ab5048` |
| `edition/v12/decisions/modernization-cutover.json` | `d4d9945a72ed04a4253f669f36f7db51117669307fe59734f707535d71dc8272` |
| `tests/test_tycho_v12_engine.py` | `c0f39279d8d8a0efac976febe9be23894e5452d0c0c0a4be7b27275aa236308f` |
| `tests/test_tycho_v12_experiments.py` | `05d3ea82a008074fb2a9ed6363b2345f682060bffce0681b6178bd29a93efc63` |
| `sources/register.json` | `650b949babc50ddbd4db0ab6ba7bf1ddf0e14de7b863536eb424feea5d2623db` |
| `event-ordering-and-timeouts.md` | `fb7138923ffc7b1b1248b0de87cf4a4debe05a2e609a085048d897542f41c6d8` |
| `uncertainty-and-sensitivity.md` | `457d822397674c0f2017449368f162b6c6e71cf6738604252cd7befe877e3b2a` |
| `authoring/V12-IMPLEMENTATION-2026-10-29.md` | `d5088b253da91ea8fc352425dbe4ff4bccff147311266291bac4fde1bebe660d` |
| Prior raw review | `0c23513867c8921c66e648857aa561559abfed168e28445d58f4e73991f903db` |
| `edition/patterns/sufficient-rereview-packets.v1.json` | `dfda3349f7131d9fbc494f60a7fa46bca9ad9371a665f98ac0afa30331211336` |
| `generated/v12-index.v1.json` | `723d5e1e0e8d1f4d281a5c762073bc803367fc9b3dcacda0e9e31c6d7c4f77a9` |

## Limits and unresolved questions

- I did not run tests, repository validators, simulations, replay commands, index builders, or
  source-retrieval commands.
- Public sources were not fetched or re-read. Source admission metadata and bounded reading
  records were inspected locally.
- Hash consistency establishes artifact integrity, not model correctness.
- The A/B/C recommendation may remain unchanged after correcting deadline and retry semantics,
  but that cannot be assumed; the runs and decision evidence require regeneration.
- A valid dependent-input sensitivity definition or an explicitly independent sensitivity
  scenario is still required before interpreting the recorded indices.
- The intended treatment of failed rollback durations—censoring, horizon substitution, or a
  conditional metric—remains unspecified.
- The checkout retry budget needs a declared answer to whether queue waiting consumes an
  attempt. The current canonical prose says it does; the engine does not.
- No repository content was written or modified during this review.

This review is not owner acceptance, CI, sufficient coverage, pattern promotion, permission to
merge, or evidence that any test or validator executed successfully.