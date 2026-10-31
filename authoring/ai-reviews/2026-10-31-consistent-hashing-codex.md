# Independent AI Review — B47 Consistent Hashing

## Review identity

- Harness: OpenAI Codex
- Vendor: OpenAI
- Model: GPT-5 family; exact build/version not exposed
- Session: `01a19206-effa-7242-9576-bfad67fc85ed`
- Reviewed at: `2026-10-31T12:58:06Z`
- Review elapsed time: approximately 3 minutes 36 seconds
- Repository: `/Users/rbaranov/Projects/tycho`
- Branch: `wip/b47-consistent-hashing-integration`
- Review HEAD: `409c8ed6bc455218c0c1f1b4a9e5949fac0c941b`
- Content commit: `19739a7391025b5a731086365b8acdbeb8c706d5`

The reviewed B47 artifacts are unchanged between the content commit and review HEAD.

## Scope and verified hashes

- Owner:
  [resharding-transition.md](/Users/rbaranov/Projects/tycho/book/volumes/v05-data-models-engines-and-lifecycle/c05-partitioning-sharding-and-rebalancing/resharding-transition.md:132)
- Owner SHA-256:
  `3ebcff9969062507cb594e4344c0ec143cf7e6fb5940983942e7028f61362453`
- Card:
  [consistent-hashing.md](/Users/rbaranov/Projects/tycho/book/volumes/v11-pattern-atlas/c06-database-storage/consistent-hashing.md:59)
- Card SHA-256:
  `ea2ce0bc8e2c70f7930f8d6806ba39697ce0df0e1a80e2d785be52cd4efca8de`

The current owner section contains 844 words excluding its three-word heading, rather than
the earlier 147-word treatment. The historical 2026-10-23 review was not treated as current
evidence.

Derived from the artifacts:

- Source-plan units: 7
- Matching ledger records: 7
- Supporting units: 6
- Explicit scope-limit units: 1
- Distinct admitted source IDs: 4
- Primary and supporting dimension bindings: 16

The scope-limit record is
`read.batch3-cassandra-arch.2026-10-21`; it explicitly excludes consistent hashing and the
token ring.

## Per-check results

### Mechanism — pass

The owner explains the circular hash space, clockwise successor ownership, and multiple
tokens or virtual nodes. The mechanism owner-unit quote is verbatim in the owner section.

Its primary and supporting bindings all match a `read` ledger record, a listed section,
the recorded revision, and an exact `claims_supported` string. Public text corroborates the
ring and clockwise-walk mechanism in the
[2007 Dynamo paper](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf),
the token model in the
[Cassandra 5.0 documentation](https://cassandra.apache.org/doc/latest/cassandra/architecture/dynamo.html),
and vnode ownership in the
[Riak 2.2.3 vnode documentation](https://docs.riak.com/riak/kv/2.2.3/learn/concepts/vnodes/index.html).

### Invariant — pass with minor finding B47-M1

The evidence supports minimal or small movement when membership changes and supports the
balanced-node share premise. The owner quote is verbatim, and all four invariant bindings
match their ledger sections, revisions, and supported claims.

The public paper states that the expected moved fraction is the minimum needed for balanced
load; the current documentation states that only a small fraction moves and that a balanced
node normally owns a `1/N` ring share.
[Paper text](https://people.csail.mit.edu/karger/Papers/web.pdf),
[Cassandra documentation](https://cassandra.apache.org/doc/latest/cassandra/architecture/dynamo.html),
[Riak cluster documentation](https://docs.riak.com/riak/kv/2.2.3/learn/concepts/clusters/index.html).

The remaining precision issue is recorded under findings.

### Failure/recovery — pass

The dimension covers hotspots, uneven token ranges, temporary node loss, hinted handoff,
replica synchronization, permanent removal, token-count cost, and ownership fencing.

All five failure/recovery bindings match their ledger records, sections, revisions, and
supported claims. The public sources corroborate temporary handoff and subsequent delivery,
anti-entropy for persistent divergence, and increasing outage and repair cost with more
tokens.
[2007 paper](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf),
[Cassandra documentation](https://cassandra.apache.org/doc/latest/cassandra/architecture/dynamo.html).

The ownership epoch, fencing rule, monitoring runbook, and treatment of hinted handoff as
temporary protection are clearly labelled as Tycho synthesis rather than quoted source
behavior.

### Alternative — pass

The source-bound comparison is limited to modulo hashing and membership-change remapping.
Both alternative bindings match their ledger records, sections, revisions, and exact
supported claims.

Explicit ranges, rendezvous hashing, and the final choice rule are clearly labelled as
Tycho synthesis. They are not presented as findings from the bound sources.

### Card/owner agreement — pass

The card contains the required decision question, identity, fit conditions,
contraindications, alternatives, failure/recovery guidance, related entries, source note,
and conditional decision state.

The card, owner unit, registry, and source plan identify the same pattern, owner anchor, and
supporting records. Both technical and decision coverage remain `partial-bounded`; neither
artifact prematurely claims promotion, sufficiency, acceptance, benchmarks, or executed
cluster observations.

### Source support — pass with retrieval limits

Mechanical checks found:

- Four of four owner-unit quotes verbatim in the owner section.
- Sixteen of sixteen bindings attached to a `read` ledger record.
- Sixteen of sixteen binding sections present in `sections_read`.
- Sixteen of sixteen binding revisions equal to ledger `content_sha256`.
- Sixteen of sixteen binding quotations present exactly in `claims_supported`.
- All four source IDs present and admitted in `sources/register.json`.

No material benchmark, production observation, local experiment, or universal guarantee is
claimed.

## Findings

### Blocking

None.

### Major

None.

### Minor

#### B47-M1 — Membership-movement formula leaves `N` ambiguous

Paths:

- [resharding-transition.md:146](/Users/rbaranov/Projects/tycho/book/volumes/v05-data-models-engines-and-lifecycle/c05-partitioning-sharding-and-rebalancing/resharding-transition.md:146)
- [owner-units.v1.json:7289](/Users/rbaranov/Projects/tycho/edition/patterns/owner-units.v1.json:7289)

Evidence: the invariant uses approximately `K/N` for both adding and removing one node
without defining whether `N` is the pre-change or post-change node count. Removing one of
`N` balanced nodes moves approximately `K/N`; adding a node to an existing set of `N` moves
approximately `K/(N+1)` under ideal balance.

The surrounding qualification correctly calls the value an expectation rather than a
guarantee, so this does not invalidate the supported minimal-movement property. It should
be clarified by defining `N` separately for join and leave, or by stating that movement is
the joining node’s target share or the leaving node’s former share.

## Public-source retrieval and limits

Fetched successfully:

- The exact public URL for the 2007 Dynamo paper.
- The exact Cassandra 5.0 Dynamo documentation page.
- The exact Riak 2.2.3 Vnodes page.
- The exact Riak 2.2.3 Clusters page.
- The Cassandra overview page used only as a scope limit.
- An alternate public author copy of the Karger paper.

Not fetched at the exact recorded representation:

- The recorded Princeton-hosted Karger PDF returned unavailable through the web harness.
  The quotations were checked against an alternate public author copy, but the recorded
  Princeton PDF hash was not independently recomputed.
- The exact Riak 2.2.3 Adding/Removing Nodes URL and the commit-pinned raw Markdown could
  not be fetched. A publicly indexed current version contained the cited removal passage,
  but I did not infer that its bytes equal the pinned revision.
- Direct shell retrieval was unavailable because DNS resolution was blocked.

No source revision hash was inferred from an unavailable representation. No tests,
benchmarks, cluster execution, or CI were run. No files were written. Final repository
status still showed only the pre-existing untracked `deliverables/` directory.

This raw report was returned to the authoring harness and was not saved or indexed by the
reviewer.

## Verdict

**pass-with-findings**

The four evidence dimensions and the decision card are adequately supported. One minor
formula-precision finding remains; there are no blocking or major findings.

`sufficient: 0`

This review is not owner acceptance, CI evidence, a promotion record, merge permission, or
a sufficient-coverage claim by itself.