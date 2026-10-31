# B47 Consistent Hashing — bounded evidence packet

Status: prepared for one bounded read-only independent AI review. It is not a review,
promotion, sufficient-coverage claim or owner acceptance. The reviewer fills the verdict;
the author does not.

## Review coordinates

| Item | Value |
|---|---|
| Issue | #540 |
| Branch | wip/b47-consistent-hashing-integration |
| Content commit | 19739a73 |
| Review HEAD | Record `git rev-parse HEAD` at review start |
| Entry | `tycho.pattern.consistent-hashing` |
| Policy | `governance/SUFFICIENT-COVERAGE.md` |
| Owner units | `edition/patterns/owner-units.v1.json` |
| Registry | `edition/patterns/registry.v1.json` |
| Source plan | `edition/patterns/source-plan.v1.json` |
| Reading ledger | `edition/patterns/reading-ledger.v1.json` |
| Source register | `sources/register.json` |

## Artifact scope

Owner page (concatenate the two lines):

    book/volumes/v05-data-models-engines-and-lifecycle/
    c05-partitioning-sharding-and-rebalancing/resharding-transition.md

- Owner heading: `### Consistent Hashing` (level 3, line 132).
- Owner page raw SHA-256:

      3ebcff9969062507cb594e4344c0ec143cf7e6fb5940983942e7028f61362453

- Dedicated card:
  `book/volumes/v11-pattern-atlas/c06-database-storage/consistent-hashing.md`.
- Card raw SHA-256:

      ea2ce0bc8e2c70f7930f8d6806ba39697ce0df0e1a80e2d785be52cd4efca8de

- Chapter landing (keeps the section anchor and card pointer):
  `book/volumes/v11-pattern-atlas/c06-database-storage/README.md`.
- Chapter landing raw SHA-256:

      74a283fc42fe468cada73d4ce1ad4c82d4cfa4a973849d7baf1da1e0c090378b

## Bound sources and records

- `src.karger` — Karger et al., STOC '97 paper; record
  `read.karger-consistent-hashing.2026-10-31`; sections Abstract, 1, 4.1 and 4.2.
- `src.dynamo` — Dynamo SOSP 2007 paper; record
  `read.dynamo-consistent-hashing.2026-10-31`; sections 4.2, 4.3, 4.6, 4.7 and 4.9.
- `src.cassandra` — Cassandra 5.0 "Dynamo"; record
  `read.cassandra-dynamo-consistent-hashing.2026-10-31`; three named sections.
- `src.riak` — Riak KV 2.2.3; records `read.riak-vnodes.2026-10-31`,
  `read.riak-clusters.2026-10-31` and `read.riak-adding-removing-nodes.2026-10-31`.
- The retained `read.batch3-cassandra-arch.2026-10-21` record is a scope limit, not
  support: it explicitly excludes the token ring.

## Recorded state at this HEAD

- Owner units: all four dimensions `supported`; `technical_coverage` and
  `decision_coverage` remain `partial-bounded`; no promotion.
- Registry: technical and atlas owner states `partial-bounded`; coverage
  `partial-bounded`; seven read source units.
- Candidate: `candidate-for-independent-review`; blocker `independent-review`.
- Historical agent pass: 2026-10-23, for an earlier 147-word owner section with pinned
  page hash `20fad2cfe4434e75abac7d4a17774040f44cd4a0ba6955b0e360a0fdb40b6509`.
  The current section is 844 words, so that pass does not cover these bytes; the
  rereview packet reports `page-changed-since-review`.

## Required checks

1. Confirm each of the four owner quotes is verbatim in the owner section, and each
   binding quote is within the named ledger record's `claims_supported`.
2. Check every material source claim against the public source scope, revision and
   limits in the register and ledger; flag stretched or unsupported claims.
3. Check that owner section, dedicated card and the four owner-unit bindings agree.
4. Confirm Tycho-labelled synthesis is not presented as source support: ownership
   epoch, measured moved share, token-cost rule, range/rendezvous comparison and the
   choice rule.
5. Confirm no benchmark, production observation, cluster experiment, owner acceptance
   or current external review is claimed.
6. Derive counts from artifacts; do not accept numbers stated in this packet.
7. Return `pass`, `pass-with-findings` or `reject` with findings by severity and
   exact paths. A blocking or major finding means no promotion.

## Verdict schema

```json
{
  "reviewer": null,
  "vendor": null,
  "model": null,
  "session": null,
  "reviewed_at": null,
  "head": null,
  "content_commit": "19739a73",
  "owner_sha256": "3ebcff9969062507cb594e4344c0ec143cf7e6fb5940983942e7028f61362453",
  "card_sha256": "ea2ce0bc8e2c70f7930f8d6806ba39697ce0df0e1a80e2d785be52cd4efca8de",
  "checks": {
    "mechanism": null,
    "invariant": null,
    "failure_recovery": null,
    "alternative": null,
    "card_owner_agreement": null,
    "source_support": null,
    "limits": null
  },
  "verdict": null,
  "findings": [],
  "limits": null,
  "sufficient": 0
}
```

## Exact reviewer prompt

```text
You are an independent AI reviewer from a different harness and session than the
DeepSeek Harness authoring agent. Perform one bounded read-only review of the B47
Consistent Hashing entry for promotion from partial-bounded to sufficient. Do not
edit, commit, open a PR, change configuration or run the test suite.

Repository: /Users/rbaranov/Projects/tycho
Checkout: current branch HEAD; record `git rev-parse HEAD`.
Content commit: 19739a73.
Packet: authoring/B47-CONSISTENT-HASHING-REVIEW-PACKET-2026-10-31.md
Policy: governance/SUFFICIENT-COVERAGE.md
Entry: tycho.pattern.consistent-hashing
Owner page: book/volumes/v05-data-models-engines-and-lifecycle/c05-partitioning-sharding-and-rebalancing/resharding-transition.md
Card: book/volumes/v11-pattern-atlas/c06-database-storage/consistent-hashing.md

Read the owner section, the dedicated card, the owner-unit entry, the registry source
units, the source-plan units and every cited ledger record. Verify the four dimensions
independently: mechanism, invariant, failure/recovery and alternative. Check quoted
passages against the cited public source scope; the public URLs and revisions are in
the ledger records and source register. Use public sources only.

Historical note: the 2026-10-23 agent pass covered an earlier 147-word section, not
the current 844-word section. It is not current evidence.

Return one Markdown report with: reviewer harness/vendor, model/version when exposed,
session id, timestamp, repository path, review HEAD, content commit, artifact hashes,
per-check results, verdict (pass, pass-with-findings or reject), findings by severity
with exact paths and evidence, limits, and `sufficient: 0`. Do not claim owner
acceptance, CI or merge permission.
```

## Limits

- The packet contains no verdict and does not prove sufficiency.
- The reviewer must be read-only and must not run tests.
- The sources are public papers and documentation, not local experiments.
- Owner acceptance remains a separate batched owner decision.
