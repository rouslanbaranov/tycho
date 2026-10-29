# Independent read-only review — V12 isolated volume

## Review identity and pin

| Field | Value |
|---|---|
| Reviewer harness | OpenAI Codex |
| Vendor | OpenAI |
| Model | GPT-5-based Codex; exact serving version not exposed |
| Session identifier | Not exposed |
| Review timestamp | 2026-10-29T12:12:10Z |
| Repository | `/Users/rbaranov/Projects/tycho-v12` |
| Branch | `feature/TYCHO-587-v12-architecture-modeling-simulation-decision-validation-isolated-volume` |
| HEAD | `7e002cd2f0e2e7f4cf99ed84841ffd0259516e95` |
| Content commit | `7e002cd2f0e2e7f4cf99ed84841ffd0259516e95` |
| Author relationship | Independent reviewer; no prior authorship |

All line references below refer to the pinned HEAD.

## Verdict

**Reject.**

The document and registry structure is largely coherent, the protected baseline is unchanged,
and the A/B/C scenario comparison uses an identical workload, warmup, duration, metrics,
replication count, and seed scheme. However, three blocking engine/provenance defects invalidate
the claimed simulation semantics and reproducibility.

## Findings

### Blocking

1. **Declared input correlations are not applied.**

   [v12_engine.py](/Users/rbaranov/Projects/tycho-v12/scripts/v12_engine.py) lines 651–657
   independently call `sample_draw` for each parameter and never read the scenario’s
   `correlations` array. Lines 765–768 nevertheless label any such run as
   `gaussian-copula` with `correlated_inputs: true`.

   This contradicts:

   - [modernization-staged.json](/Users/rbaranov/Projects/tycho-v12/edition/v12/scenarios/modernization-staged.json:57),
     which declares a −0.4 correlation;
   - [modernization-staged run](/Users/rbaranov/Projects/tycho-v12/edition/v12/runs/modernization-staged.json:157),
     which records a Gaussian copula;
   - [uncertainty-and-sensitivity.md](/Users/rbaranov/Projects/tycho-v12/book/volumes/v12-modeling-simulation-and-decision-validation/c04-monte-carlo/uncertainty-and-sensitivity.md:88),
     which explicitly says the engine applies the correlation.

   The modernization intervals and checkout sensitivity results were therefore generated from
   independently sampled inputs while being presented as correlated-input evidence.

2. **Stored B and C runs cannot be reproduced by the pinned engine.**

   At pinned HEAD, `retry_amplification` is assigned unit `ratio` at
   `scripts/v12_engine.py:681–693`; lines 729–730 clamp every ratio confidence interval to a
   maximum of 1.0. The stored runs instead contain:

   - B: `ci_high = 1.004276039321762`;
   - C: `ci_high = 1.067660650336653`.

   Thus the pinned engine would produce different run records and different result hashes.
   Stored result hashes are internally correct for the stored JSON, but that only proves file
   integrity—not that HEAD produced the files.

   The input hash binds only model, scenario, and the string engine version `1.0.0`
   (`scripts/v12_engine.py:752–758`); it does not bind the engine source hash. Changed engine
   semantics can therefore retain the same provenance version.

3. **A stale completion event can complete a later retry attempt.**

   `scripts/v12_engine.py:262–263` schedules completion with only a request ID. After timeout,
   the same request object and ID are reused for a retry at lines 280–286 and 341–347.
   When the earlier completion fires, lines 332–335 resolve the current in-service request by
   that ID and can complete the newer attempt prematurely.

   Candidates B and C use retries, so their latency, success, timeout, and retry metrics are
   not trustworthy until events carry and validate an attempt identifier.

### High

1. **Cost uses inconsistent measurement windows.**

   Post-warmup requests alone contribute to `completed`, while
   `cost_per_1k_success` charges the full 1,800-second duration
   (`scripts/v12_engine.py:355–385`). The measured window is 1,500 seconds.

   Consequently the checkout costs are overstated by 20%. Using the same counts with the
   measurement duration gives approximately A `1.810`, B `1.335`, and C `3.570`, rather than
   `2.171`, `1.602`, and `4.284`. This does not reverse C4 or the recommendation, but the
   decision’s hard-constraint evidence and reported values are wrong.

2. **Hard constraints C1 and C2 are not preserved in stored run evidence.**

   The engine checks `conservation_ok` while generating replications
   (`scripts/v12_engine.py:700–713`) but drops the flag and accounting totals from the
   aggregated run record. The stored runs therefore cannot demonstrate conservation or
   absence of silent loss.

   [comparative-decision-worked-example.md](/Users/rbaranov/Projects/tycho-v12/book/volumes/v12-modeling-simulation-and-decision-validation/c05-decision-integration/comparative-decision-worked-example.md:88)
   says the model “reports a conservation flag,” but no stored run contains it. A
   `decision-supported` record should carry an explicit constraint evaluation or invariant
   evidence for each candidate.

### Medium

1. **The strict run schema does not require the result hash.**

   [run-result.v1.schema.json](/Users/rbaranov/Projects/tycho-v12/schemas/v12/run-result.v1.schema.json:7)
   omits `result_sha256` from `required`, even though the property is defined at line 260 and
   the book describes it as mandatory. A run without a result hash can therefore satisfy the
   schema.

2. **Source-register reading labels conflict with the bounded ledger.**

   `sources/register.json` labels the new W3C and JCGM units
   `full-public-page-inspected`, while the ledger records coverage `0.55` and `0.45` with
   status `partial-scoped-text-read`:

   - [register:6910](/Users/rbaranov/Projects/tycho-v12/sources/register.json:6910) versus
     [ledger:248](/Users/rbaranov/Projects/tycho-v12/edition/v12/reading-ledger.v1.json:248);
   - [register:7010](/Users/rbaranov/Projects/tycho-v12/sources/register.json:7010) versus
     [ledger:437](/Users/rbaranov/Projects/tycho-v12/edition/v12/reading-ledger.v1.json:437).

   The detailed scope text is honest, but the summary label conflates retrieval of the full
   representation with reading only selected sections. The Monte Carlo registration also
   says “Appendix A inspected” while the ledger bounds the unit to Appendix A.6.

3. **Test evidence does not cover the blocking paths, and seven recorded test names are stale.**

   The tests do not exercise correlated sampling, stale completion events across retries,
   warmup-adjusted cost, or replay of committed runs. The experiment tests primarily assert
   values already stored in JSON.

   Seven model verification records name test methods that do not exist, including
   `test_des_deterministic_replay`, `test_stock_flow_capacity`, and
   `test_modernization_zero_lag`; see
   [checkout-des.json](/Users/rbaranov/Projects/tycho-v12/edition/v12/models/checkout-des.json:172),
   [order-intake.json](/Users/rbaranov/Projects/tycho-v12/edition/v12/models/order-intake.json:127),
   and
   [modernization-path.json](/Users/rbaranov/Projects/tycho-v12/edition/v12/models/modernization-path.json:158).

### Low

1. **The protected promotion-record set is narrower than the stated iron rule.**

   The protected baseline contains four promotion-related records, but
   `edition/patterns/sufficient-rereview-packets.v1.json` was also modified on the branch and
   is not protected. Its current change is explicitly scoped to V1–V11 and contains no direct
   V12 reference, so this is not a demonstrated current leak. It is a coverage gap in the
   mechanical gate.

## Checks that passed

- All 449 protected Markdown files and four protected records match their baseline SHA-256.
- No V12-specific reference was found in those 453 protected artifacts.
- No existing page, card, owner page, frontmatter, protected promotion record, or atlas
  manifest changed.
- The three A/B/C scenarios have identical non-configuration content after removing identity,
  title, purpose, configuration, and run ID; normalized digest:
  `14422c71809f6036434bf765105232eaa9c95af804fb4e78654895c693b68ae9`.
- Manifest and registry identifiers are unique.
- Model, scenario, run, decision, pattern-owner, and source-plan references resolve.
- Registry artifact hashes and all nine stored result hashes are internally consistent.
- The standalone reverse index matches the registry and is derivable from artifact pattern IDs.
- All model parameters are explicitly `assumed`; all three models are `uncalibrated`.
- The modernization decision clearly returns `none`, explains why evidence is insufficient,
  and identifies measurements and rollback evidence that could change the outcome.
- Nine new public sources plus one reused source have reading-ledger records. Source-plan
  record IDs, units, source IDs, and `used_by` paths resolve.

## Derived counts

| Artifact | Count |
|---|---:|
| V12 Markdown documents | 31 |
| Volume landings | 1 |
| Chapter landings | 7 |
| Technical pages | 23 |
| Models | 3 |
| Scenarios | 9 |
| Runs | 9 |
| Decisions | 2 |
| Source reading records | 10 |
| Newly registered sources | 9 |
| Reused source units | 1 |
| Source-plan topics | 8 |
| Source-plan references | 16 |
| Unique source units | 10 |
| Reverse-index patterns | 9 |
| Generated V12 index entries | 54 |
| Protected Markdown files | 449 |
| Protected promotion-related records | 4 |

## Principal pinned artifact hashes

| Artifact | SHA-256 |
|---|---|
| `edition/v12/protected-baseline.json` | `2a55424ad1b5de5e423bc0a55d90a38a4b108328c047b556b78ebfd496fbf112` |
| `edition/v12/manifest.json` | `6097d5a1ae516c942593b56bc98194325a3e6709d3259733be6f9e966a791ff7` |
| `edition/v12/registry.json` | `ea488331c6f864b32e6b79e400f3034d22edb2ed46ebf4e93626aa79c90961be` |
| `edition/v12/reverse-index.v1.json` | `cce1a30c66423e1ce47c56a8084a6d6d23d1d660d5ce6b2a0ee6afa716831e7d` |
| `edition/v12/reading-ledger.v1.json` | `8f020d8beeed785a60b72b86c177c45a1abf2c79d6dcd38b13e00bbb80929abf` |
| `edition/v12/source-plan.v1.json` | `ed6e7b0ee447f2f7b663a47408d391fa42472f0d9ffa84d47970e36fb87c03a5` |
| `scripts/v12_engine.py` | `74f779f5ba5b01f80be937aef55583e396cae0827bdbbce2a3010e84f1a3ddd6` |
| `scripts/validate_v12.py` | `c474f9e8477e2c56c0fe7274a07676ccfd34a2c1540af67bc897cce36c5ed383` |
| `schemas/v12/run-result.v1.schema.json` | `f722733f1aa47f1504f74916cd2d8ef3e892fad4df79fc5f9b86e9d997007a48` |
| `edition/v12/decisions/checkout-candidate.json` | `f8d95ca1d72323feaebf922029e6b8671ddb9eda7f8aab5776f6f8f9523fd810` |
| `edition/v12/runs/checkout-a-synchronous.json` | `34f74502ce3ebb451cd72b511f84bf05a0a59c2ac96273b786af166b56b3bfc7` |
| `edition/v12/runs/checkout-b-queue.json` | `296aff4b4e3b6bd452c0520fa856b4cdbfeb9541e9a61ab063c3d742688e82c8` |
| `edition/v12/runs/checkout-c-partitioned.json` | `0527d7abfe08f2069ca8cce039003b5f33c702ad5d28aa53ffb28db42dfa4109` |
| `edition/v12/decisions/modernization-cutover.json` | `24158f7c63cf0220855b37fe86d60d5d28d3ac5a5d7f7d1331c6e4a0032b357a` |
| `edition/v12/runs/modernization-staged.json` | `bee56fb9aa55c2572963b1ffe7aab3b181904f55871019bebb5c1bbdb33e6dd8` |
| `tests/test_tycho_v12_engine.py` | `372c9cc40db34bb7681334465e1cab3bb4574044fa810540d8b36cef7c68d941` |
| `tests/test_tycho_v12_experiments.py` | `29a7fa3b469e75022eb3197fb8311c0b1deb11d45e621847862b79d17ad002f4` |
| `generated/v12-index.v1.json` | `fac09fb341d8c740c07677265b06722f08b9534d6ec9955c70cd47adccbcdfa1` |
| `sources/register.json` | `70d7b89ad83accdda7adb715a0ddf3b09234b2cf596f69a4c8239c2166564dce` |

## Limits and unresolved questions

- No test suite, repository validator, simulation, or replay command was run.
- Public sources were not fetched. Source admission metadata, ledger coverage, links, and
  internal hashes were inspected, but representation hashes were not independently re-derived.
- The engine defects were established through static control-flow and artifact inspection.
- Four uncommitted changes appeared during the review in `scripts/v12_engine.py`,
  `edition/v12/runs/checkout-sensitivity.json`, `edition/v12/registry.json`, and
  `edition/inventory.json`. The checkout was clean at the start; the reviewer did not create
  these changes. They were excluded by reading the pinned Git objects directly.
- Whether corrected runs change the recommendation remains unresolved until the correlation,
  retry-event, cost-window, and provenance defects are fixed and the experiments are rerun.

This review is not owner acceptance, CI, sufficient coverage, pattern promotion, permission to
merge, or evidence that any test executed successfully.