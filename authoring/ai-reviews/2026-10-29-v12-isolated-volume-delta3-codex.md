# Independent read-only delta review 3 — V12 final remediation

## Review identity and pin

| Field | Value |
|---|---|
| Reviewer harness | OpenAI Codex |
| Vendor | OpenAI |
| Model | GPT-5-based Codex; exact serving version not exposed |
| Session identifier | Not exposed |
| Timestamp | 2026-10-29T13:07:56Z |
| Repository | `/Users/rbaranov/Projects/tycho-v12` |
| Branch | `feature/TYCHO-587-v12-architecture-modeling-simulation-decision-validation-isolated-volume` |
| HEAD | `fbde63d214f18fb9b18d9957ad335145bb868787` |
| Prior commit | `06d4722c9a1b333b7e4bc1e32eb4fbec328629e9` |
| Correction range | `06d4722c9a1b333b7e4bc1e32eb4fbec328629e9..fbde63d214f18fb9b18d9957ad335145bb868787` |
| Author relationship | Fresh independent reviewer; no authorship or prior involvement |
| Working tree | Clean at review start and end |
| Sufficiency claim | `sufficient: 0` |

## Verdict

**Pass-with-findings.**

N3, N4 and D2-L1 are resolved. Static inspection found no remaining defect in the requested
rollback censoring, corrected descriptions, or direct regression assertions.

One new low-severity editorial finding remains: the newly added AI-review index row violates
the mandatory Markdown line-length policy. It does not affect the technical remediation.

## Prior finding dispositions

| Prior ID | Disposition | Evidence |
|---|---|---|
| N3 | Resolved | Engine, staged run, decision and three pages use elapsed censoring. |
| N4 | Resolved | Stale rates and engine description are corrected; failure text is qualified. |
| D2-L1 | Resolved | Tests assert the attempt budget, elapsed censoring and rejection behavior. |

### N3 evidence

`scripts/v12_engine.py:572-574` now assigns an unfinished rollback:

```text
max(0.0, duration - rollback_at)
```

The staged scenario declares a 2,400-second horizon and a trigger at 1,200 seconds. Therefore,
the elapsed censoring limit is 1,200 seconds.

`edition/v12/runs/modernization-staged.json:104-119` records:

- 20 replications;
- completion ratio 0.1, hence 2 completed and 18 censored;
- mean censored duration 1,080 seconds;
- standard error 82.58966419340223;
- interval 918.1272326856744–1,241.8727673143258.

The stored values are internally consistent:

```text
(18 × 1200 + 2 × 0) / 20 = 1080 seconds
```

The decision rationale and constraint evidence at
`edition/v12/decisions/modernization-cutover.json:98,146` use the same censoring basis.
The implementation record and three affected book pages also report 1,080 seconds.

### N4 evidence

- `retries-and-backpressure.md:107-115` now reports rejection as 0.05% and timeout as 35.0%,
  consistent with stored values 0.0005 and 0.3495.
- `scripts/v12_engine.py:11-13` describes a quadratic response-surface screen.
- `scripts/v12_engine.py:945-957` documents the approximation and rejects correlated inputs.
- The sensitivity run records `quadratic-response-surface`.
- Remaining references to pick-freeze either describe the public method, explicitly contrast
  it with the V12 approximation, or are generic schema alternatives.
- `modernization-path-experiment.md:151-154` makes correlation omission conditional and
  describes censoring as a limit rather than an observed completion.

Searches found no remaining positive current-behavior claims using the stale percentages or
the old 2,160-second rollback mean.

### D2-L1 evidence

`tests/test_tycho_v12_engine.py` now includes:

- `:175-188`: with `max_attempts == 1`, retry amplification must equal 1.0;
- `:252-259`: an unfinished rollback triggered at 100 seconds in a 400-second scenario must
  produce 300 seconds and `rollback_completed == 0.0`;
- `:268-278`: a correlated response-surface screen must raise `EngineError`.

These are direct assertions of the three requested behaviors. No tests were executed.

## New findings

### Low — D3-L1: newly added review-index row exceeds 100 characters

`authoring/ai-reviews/README.md:102` is a newly added 253-character Markdown table row.

The repository instructions require every new or edited Markdown line to remain at or below
100 characters and require redesigning tables that cannot satisfy the limit. This is an
editorial defect in the correction range, not a modeling or evidence defect.

## Derived counts

| Derived item | Count/result |
|---|---:|
| Files changed in correction range | 25 |
| Changed Markdown files | 7 |
| Changed run records | 10 |
| Changed decision records | 1 |
| Changed schema files | 0 |
| New engine test methods | 2 |
| Existing test strengthened with a direct assertion | 1 |
| Current V12 engine test methods | 21 |
| V12 documents | 31 |
| Models / scenarios / runs / decisions | 3 / 10 / 10 / 2 |
| Registry artifacts | 25 |
| Manifest hashes matching files | 31/31 |
| Registry hashes matching files | 25/25 |
| Canonical run-result hashes matching | 10/10 |
| Run input hashes matching | 10/10 |
| Engine / model / scenario provenance hashes matching | 10/10 each |
| Stored invariant records reporting pass | 10/10 |
| Converged / insufficient-sample runs | 9 / 1 |
| Correlated-input runs | 2 |
| Sensitivity runs | 1 |
| Staged completed / censored replications | 2 / 18 |
| Elapsed censoring limit | 1,200 seconds |
| Mean censored rollback duration | 1,080 seconds |
| Newly introduced Markdown line-length violations | 1 |

Canonical result, input and provenance hashes were recomputed from stored artifacts. This was
static hash calculation, not engine replay.

## Independently computed artifact hashes

`BOOK` below denotes:

```text
book/volumes/v12-modeling-simulation-and-decision-validation
```

### Engine, tests and schemas

```text
659bdb5e60bf13af0dafe7eea5ff0c5214f349f719f49db468088217b4875df1
scripts/v12_engine.py

3f945d6494af793334f6db8627c34a3dcd99367afa9dea31765caf8fc910729a
tests/test_tycho_v12_engine.py

90ddf79ad9ce04b808592c839f9886db1a0bf0ee0c676852a034125daaa17dd4
tests/test_tycho_ai_reviews.py

38ced2b298589d2ffbbcd54ec50b1ea7de54dfc172ecb97a379dc7f0111c146b
schemas/v12/run-result.v1.schema.json

3a2da685a263a89e00ac5bada13270d439bc902a3ed0863c92de81c3294510ee
schemas/v12/scenario-specification.v1.schema.json

9fa9e5e4b190d5d194cb017b66401b63b2f4252a19fbf86c991b5c7b39ca44fb
schemas/v12/decision-record.v1.schema.json
```

### Principal scenarios, decision and run records

```text
8cb384c7f6d29a230299bda8b1fe6c88689871f96c433e68f2872964617acd59
edition/v12/scenarios/modernization-staged.json

669eae2165c77c36e277b95e9478221c14314bea249d6ecc659112d91e768c5e
edition/v12/scenarios/checkout-overload.json

e8eb755cf569de49b64f8dd1fd132a7d77d7aa0c1dab0bad5f93da8bba327ad7
edition/v12/scenarios/checkout-sensitivity.json

f99ec73f50ba33e28dd3f0579558d0edb2391333687027988f05a299187e0bdd
edition/v12/runs/modernization-staged.json

3dd59f600e271f05ac876c8efab5c4ca91265961affff0bc7df27bf8ba9a3816
edition/v12/runs/modernization-no-cutover.json

82c1851bcbaafebbc76c123c27ecc9465efd0595bf84605d60ca08dec17a3ad1
edition/v12/runs/checkout-overload.json

af8e57093ca7b48fdd877abebb56789949cbc501293bbc039f92e6d8ce292202
edition/v12/runs/checkout-sensitivity.json

182a8700dbc3b05757f44aa657c0609b3dd8c5803e31a3fab82287ac2952d3d0
edition/v12/decisions/modernization-cutover.json
```

### Other run records used in static consistency counts

```text
3d3bcbfeeedef548988d44eb24be52306b6fe4cb79fa2d25cc04279c464b1391
edition/v12/runs/checkout-a-synchronous.json

353cdfbc2f8545707a584b646b1437c1bdfd0f9b19ca62af098695bc1bcee731
edition/v12/runs/checkout-b-queue.json

d1ad74a065e6b978364ef42fb4204c0a7be77805f853b6bececd514d7ca7cb31
edition/v12/runs/checkout-c-partitioned.json

c21531be35a387234298d62661726e5841930cb265c63eb662fe1d592a4e465e
edition/v12/runs/checkout-convergence-stress.json

fd2035326dd1dca6456c31288e15e98787d5054724be431caa901c6f2a7dbfe5
edition/v12/runs/order-intake-baseline.json

664e7b3c5eb51dec61d9ff2c68dba986f22da48959276730e71db245e3641d9d
edition/v12/runs/order-intake-saturation.json
```

### Manifests and review records

```text
f4c5d6a7ab08fe80dfc341e36c9963266d01db9dfe6eecc824b1aefb527a0fbb
edition/v12/manifest.json

4c5020e697d13ac1e0e8c39d48eec7a1a30adb84f3baf8bd4d7daa107b3f1438
edition/v12/registry.json

71092e5e5372e7ae31f253eb71074fd65127fc9c2fcc084bc4469ab533dcba6a
edition/inventory.json

37109829b0d5a81b7d484653c5f8220ebd1ae3774e74925f2278cb8cdc4df00a
generated/route-index.v1.json

c00d27def132641c102c59b0b6e4b1c5a1585bf4af1894c74aa3c630a63e8413
authoring/V12-IMPLEMENTATION-2026-10-29.md

b03e32f9e3eea1b2615291d8c263929589de0873cfbc0210a8973fcb811e6754
authoring/ai-reviews/2026-10-29-v12-isolated-volume-delta2-codex.md

906688db285aac597f5f7bde6d46cf67176b06160d0a2c296900499813fd5ba9
authoring/ai-reviews/README.md
```

### Corrected prose

```text
8387b01584ce878f9ffd09059314e96c12118359af03decbd87bba96a7b9216f
$BOOK/c03-deterministic-and-des/retries-and-backpressure.md

3f42cf3880d297bcacffcc5a68f9fb42dda874026ef067ac8375a0ae09d1223d
$BOOK/c04-monte-carlo/uncertainty-and-sensitivity.md

0a9f75616bb19e96b06661b1c25d5fef079dc3ba37ca023274802efd730bd9b7
$BOOK/c05-decision-integration/insufficient-evidence-outcomes.md

befd3caabc83c917cb9028510d6cfc5d6b2270b8af385a29b28e603d78f11613
$BOOK/c06-migration-simulation/coexistence-and-rollback.md

52f3dfac6d06cac673bdec2ce22f246c1df74a4a7cee6b71620c57c5f2652e3b
$BOOK/c06-migration-simulation/modernization-path-experiment.md
```

## Limits and unresolved questions

- No test suite, validator, simulation, replay, index builder or model command was executed.
- The author-reported 629-test result was not independently verified.
- Public sources were not fetched or independently re-read.
- Stored platform and Python provenance were inspected but not reproduced.
- The rollback mean treats right-censored limits as numeric observations. It is accurately
  labeled as a censored mean, but it is not an estimated mean completion time.
- Schema and hash consistency establish structural integrity, not model validity.
- The new line-length finding remains unresolved.
- No repository content was written or modified during this review.

This review is not owner acceptance, CI, sufficient coverage, pattern promotion, permission
to merge, or evidence that any test or validator executed successfully.