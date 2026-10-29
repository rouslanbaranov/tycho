# Independent read-only delta review 2 — V12 isolated volume remediation

## Review identity and pin

| Field | Value |
|---|---|
| Reviewer harness | OpenAI Codex |
| Vendor | OpenAI |
| Model | GPT-5-based Codex; exact serving version not exposed |
| Session identifier | Not exposed |
| Review timestamp | 2026-10-29T12:55:43Z |
| Repository | `/Users/rbaranov/Projects/tycho-v12` |
| Branch | `feature/TYCHO-587-v12-architecture-modeling-simulation-decision-validation-isolated-volume` |
| HEAD | `06d4722c9a1b333b7e4bc1e32eb4fbec328629e9` |
| Prior reviewed commit | `bb10d96c2149cf4e03332c599e69d0a4af173f7a` |
| Correction range | `bb10d96c2149cf4e03332c599e69d0a4af173f7a..06d4722c9a1b333b7e4bc1e32eb4fbec328629e9` |
| Author relationship | Fresh independent reviewer; no authorship or prior involvement |
| Working tree | Clean at review start and end |
| Sufficiency claim | `sufficient: 0` |

## Verdict

**Pass-with-findings.**

N1 and N2 are resolved by implementation, not merely by the presence of tests. N3 is only
partially resolved: failed rollback replications are no longer omitted, but their censored
duration uses the full scenario duration instead of elapsed time since the rollback trigger.
N4 is partially resolved because several primary metadata statements were corrected, while
corrected prose still contains stale numerical and method descriptions.

There are no remaining blocking or high-severity findings. The rollback defect does not change
the recorded `insufficient-evidence` decision, but the affected metric, decision rationale and
prose are quantitatively wrong.

## Prior finding dispositions

| Prior ID | Disposition | Evidence |
|---|---|---|
| N1 | Resolved | `scripts/v12_engine.py:318-336` starts attempt 1 at arrival and schedules its deadline before enqueueing. Dispatch at `:257-268` does not reset the deadline. Retry at `:349-360` increments both attempt counters and schedules one new deadline. `_timeout` applies the bounded budget at `:270-295`. This matches `event-ordering-and-timeouts.md:82-108`. |
| N2 | Resolved | `edition/v12/scenarios/checkout-sensitivity.json:36-54` now declares no correlations. `scripts/v12_engine.py:953-957` rejects a correlated response-surface screen. The stored sensitivity run reports `correlated_inputs: false` at `edition/v12/runs/checkout-sensitivity.json:159-164`. Correlated uncertainty remains represented by separate propagation runs. |
| N3 | Partially resolved | All 20 rollback replications now contribute to `rollback_seconds`, but `scripts/v12_engine.py:573-574` substitutes `duration` for a non-completion. The scenario duration is 2,400 seconds and rollback starts at 1,200 seconds, so the elapsed censoring limit is 1,200 seconds, not 2,400. |
| N4 | Partially resolved | The sensitivity status, ten-run count, exposed model description and main rollback-completion statement were corrected. Residual contradictions remain in corrected prose and the engine description; see D2-M2. |

## New findings

### Medium — D2-M1: rollback censoring uses the wrong time origin

`scripts/v12_engine.py:573-574` returns the following for an unfinished rollback:

```text
duration
```

Successful rollback durations use:

```text
rollback_end - rollback_at
```

The two cases therefore use different time origins. In
`edition/v12/scenarios/modernization-staged.json:8-10,40`, the horizon is 2,400 seconds and
rollback begins at 1,200 seconds. A rollback still incomplete at the horizon has an observed
elapsed duration of 1,200 seconds.

The stored run reports:

- 20 replications;
- completion ratio 0.1, meaning 2 completed and 18 censored;
- stored mean `rollback_seconds` of 2,160 seconds.

The stored mean is exactly the result of substituting 2,400 seconds for the 18 failures:

```text
(18 × 2400 + 2 × 0) / 20 = 2160
```

Using elapsed censoring produces:

```text
(18 × (2400 - 1200) + 2 × 0) / 20 = 1080
```

Affected artifacts include:

- `scripts/v12_engine.py:573-574`
- `edition/v12/runs/modernization-staged.json:104-118`
- `edition/v12/decisions/modernization-cutover.json:96-99`
- `book/.../c06-migration-simulation/coexistence-and-rollback.md:101-125`
- `book/.../c06-migration-simulation/modernization-path-experiment.md:78-87`

The decision remains `insufficient-evidence`, so this does not reverse its outcome.

### Medium — D2-M2: corrected prose retains contradictory descriptions

Two material contradictions remain:

1. `retries-and-backpressure.md:107-115` lists the corrected overload values as rejection
   `0.0005` and timeout `0.3495`, then immediately says rejection is 16.6% and timeout is
   27.9%. Those trailing percentages are stale.

2. `scripts/v12_engine.py:11-13` describes the engine as providing pick-freeze sensitivity
   estimates. The implementation at `:943-1026` and the stored artifacts use a quadratic
   response-surface screen, not pick-freeze.

The failure-mode bullets in
`modernization-path-experiment.md:151-154` also describe independent draws and zero-second
non-completions without clearly marking them as hypothetical failure cases. They now read as
contradictions of the implemented correlated sampling and censoring behavior.

### Low — D2-L1: regression tests do not directly discriminate all corrected defects

`tests/test_tycho_v12_engine.py:175-187` is named
`test_queued_timeout_consumes_attempt_budget`, but it asserts only zero success, a timeout
rate above 0.5 and conservation. Those assertions could also hold under the previous
unbounded queued-retry behavior. It does not assert the attempt count, retry amplification,
terminal-failure count or absence of retries when `max_attempts == 1`.

The modernization tests at `tests/test_tycho_v12_engine.py:221-255` cover a successful
rollback only. No test checks that an unfinished rollback is censored at
`duration - rollback_at`; this gap permitted D2-M1.

No test directly exercises the new rejection of correlated sensitivity inputs at
`scripts/v12_engine.py:956-957`.

## Derived counts

No repository test, validator, simulation or replay command was run.

| Derived item | Count/result |
|---|---:|
| Files changed in correction range | 36 |
| Changed Markdown files | 14 |
| Changed run records | 10 |
| Changed decision records | 2 |
| Changed test files | 3 |
| Changed schemas | 0 |
| Changed source register | 0 |
| V12 documents | 31 |
| Volume / chapter / technical pages | 1 / 7 / 23 |
| Models / scenarios / runs / decisions | 3 / 10 / 10 / 2 |
| Registry artifacts | 25 |
| Converged / insufficient-sample runs | 9 / 1 |
| Correlated-input runs | 2 |
| Sensitivity runs | 1 |
| Reading-ledger records | 10 |
| Full / partial scoped readings | 7 / 3 |
| Source-plan topics / units | 8 / 16 |
| Relevant registered source units | 10 |
| Manifest hashes matching | 31/31 |
| Registry artifact hashes matching | 25/25 |
| Run result hashes matching | 10/10 |
| Run engine/model/scenario hashes matching | 10/10 each |
| Stored invariant records reporting pass | 10/10 |
| Staged rollback completed / censored replications | 2 / 18 |
| Stored / elapsed-censor rollback mean | 2,160 / 1,080 seconds |

The relevant source-register entries remain present with public-access, revision, access-date,
licensing and bounded verification metadata. Neither the source register nor the V12 schemas
changed in this correction range.

## Independently computed artifact hashes

### Engine, validator, tests and schemas

```text
01e9b190ecef273f259431a5a7d3b2d73fea936894a2f8302d3abc280d38f2a0
scripts/v12_engine.py

7e36cb5db6ace5166c286f391e08c2cc587899759988f9053eafa14759db097a
scripts/validate_v12.py

a21571c8bea7ea288c8378e85c4e4b2d14909e637e19feffd822f3a49b89178a
tests/test_tycho_v12_engine.py

d3dc04f6564048d6d584c5c2f64d097735d43980601d25de33eaaa0b82574805
tests/test_tycho_v12_experiments.py

38ced2b298589d2ffbbcd54ec50b1ea7de54dfc172ecb97a379dc7f0111c146b
schemas/v12/run-result.v1.schema.json

3a2da685a263a89e00ac5bada13270d439bc902a3ed0863c92de81c3294510ee
schemas/v12/scenario-specification.v1.schema.json

9fa9e5e4b190d5d194cb017b66401b63b2f4252a19fbf86c991b5c7b39ca44fb
schemas/v12/decision-record.v1.schema.json
```

### Scenarios, runs and decisions

```text
e8eb755cf569de49b64f8dd1fd132a7d77d7aa0c1dab0bad5f93da8bba327ad7
edition/v12/scenarios/checkout-sensitivity.json

830be5726c1bc1c4de6c737fea93ecb7caef455227758273f5cbf91529cad6b4
edition/v12/runs/checkout-sensitivity.json

3bb2ad7bd19cc406aef1f2f7077010b5cc88f17427b4c28cc2777e16150f5d0a
edition/v12/runs/checkout-overload.json

735a8e38e3600d9f0019804ecabd00c103d6ddf3d802cd1e9c353218c0011073
edition/v12/runs/modernization-staged.json

b02aaff9096234bac17be1128e1742231639d2dca6cbc3923f31dec9e17ff0c8
edition/v12/decisions/checkout-candidate.json

ec68b0fdad9c4a1ba506bc9bde82146ad2a742d5606fc07718effd1df033e0e0
edition/v12/decisions/modernization-cutover.json
```

### Registry, sources and review metadata

```text
6615a4722a5183d19a2776160b8f45e4c438a2bafb893750d24234c0960a2987
edition/v12/manifest.json

55f4f5a277dfa26bad4dc0d558da0aae8534c89b4c7dcc0d3ae6b3d03f43305b
edition/v12/registry.json

650b949babc50ddbd4db0ab6ba7bf1ddf0e14de7b863536eb424feea5d2623db
sources/register.json

8f020d8beeed785a60b72b86c177c45a1abf2c79d6dcd38b13e00bbb80929abf
edition/v12/reading-ledger.v1.json

0c103655907740c40ca1af8a2b69129a8ef232339495366782fc5d8a0414e20d
authoring/V12-IMPLEMENTATION-2026-10-29.md

f1c4ce40d6dbfe916adf0d0fddc6e41a415733bc041951c6cffd041bb551d106
authoring/ai-reviews/2026-10-29-v12-isolated-volume-delta-codex.md

b41fa492b9b2ef7ed5486e940d8558a37fe2c51860233aa80896a305a3d2158b
authoring/ai-reviews/README.md
```

### Principal corrected prose

```text
fb7138923ffc7b1b1248b0de87cf4a4debe05a2e609a085048d897542f41c6d8
event-ordering-and-timeouts.md

5473db704e784fea734823307d57405fa57a02a9d6d7902cc510a9fe0a1a8143
retries-and-backpressure.md

3f42cf3880d297bcacffcc5a68f9fb42dda874026ef067ac8375a0ae09d1223d
uncertainty-and-sensitivity.md

2588d45af68b6488b73abdb07adb4a8194a3df544c660720f15f01892c59a7f8
coexistence-and-rollback.md

2c3e0bdd224caa7c6354ee72eda1a6c944d9351e5d3b07aa278e0a9b606e6ac0
modernization-path-experiment.md
```

## Limits and unresolved questions

- No tests, repository validators, simulations, replay commands or index builders were run.
- Public sources were not fetched or independently re-read.
- Schema and hash consistency establish structure and integrity, not model validity.
- The author-reported local test results were not independently verified.
- The intended rollback metric must choose and document either elapsed censoring,
  absolute event time or another survival-analysis representation. The current record mixes
  elapsed and absolute time.
- The affected run, decision and prose require regeneration or correction after that choice.
- The added N1 test should assert the actual attempt budget rather than indirect outcomes.
- No repository content was written or modified during this review.

This review is not owner acceptance, CI, sufficient coverage, pattern promotion, permission to
merge or evidence that any test or validator executed successfully.