# Bounded evidence and decision-reference resolution

> Issue [#51](https://github.com/rouslanbaranov/tycho/issues/51), M4. **Status 2026-10-22:**
> read-only resolver over the existing claim ledger and source register. It is not yet wired
> into the search response or MCP adapter, and it is not a knowledge graph.

## Scope and inputs

[section_evidence.py](../scripts/section_evidence.py) resolves registered IDs against:

- [claim-references.json](../sources/claim-references.json): three typed claims with
  support, qualification, contradiction and unavailable-source relations;
- [register.json](../sources/register.json): 269 admitted or discovery-only source records;
- [public-repositories.lock.json](../sources/public-repositories.lock.json): pinned code
  revisions;
- [route-index.v1.json](../generated/route-index.v1.json): canonical book documents and
  their frontmatter evidence scope.

The resolver runs the existing claim-ledger validator before serving any record. A malformed
or inconsistent ledger fails closed as `not-available`; the resolver does not attempt to
repair it.

It never fetches a URL, copies source text, reads a repository, invents inspection, traverses
a graph or writes metadata. Source content remains outside the returned payload; only the
registered citation metadata, relation, verification declaration and location are returned.

## Operations

~~~sh
python3 scripts/section_evidence.py claim --id claim.same-intent-retry
python3 scripts/section_evidence.py source --id src.http-semantics
python3 scripts/section_evidence.py document \
  --id tycho.page.ace968ab1de8409383c6a9b22a00d006
python3 scripts/section_evidence.py decision \
  --id tycho.decision.054f312b9e744575ac80632f4acf72fa
~~~

| Action | Returns |
|---|---|
| `claim` | Claim statement, status, applicability, typed evidence, source summaries, relations, contradictions, unavailable entries and the owner document when it is in the book index. |
| `source` | Source metadata, admission/access/verification scope and every registered claim that references it. |
| `document` | Book metadata, frontmatter claim/source IDs, ledger claims owning that page and resolved source summaries. |
| `decision` | Decision metadata and its direct related/prerequisite documents only. No traversal beyond those direct references. |

Each result carries `status`, `snapshot`, `route_snapshot` and `warnings`. Warnings are
findings, not failures: for example, an owner page that does not declare its ledger claim in
frontmatter, or a source that is not admitted for research evidence.

## Snapshot semantics

The evidence snapshot is a SHA-256 over the route snapshot and the exact bytes of the claim
ledger, source register and repository lock:

~~~text
sha256({
  "route_snapshot": route-index.snapshot_sha256,
  "claims_sha256": sha256(claim-references.json),
  "register_sha256": sha256(register.json),
  "lock_sha256": sha256(public-repositories.lock.json)
})
~~~

A caller may pass `--expected-snapshot`. If the ledger, register, lock or book route
changed, the resolver returns `snapshot-mismatch` instead of silently serving newer
evidence. The snapshot is an identity aid, not a signature or an access-control token.

## Current findings

The resolver exposes, without changing the records:

- `claim.same-intent-retry` is `evidence-linked` with one `supports` and one `qualifies`
  relation. Its owner page does not list the claim in frontmatter `claim_ids`, so the
  result warns about that inconsistency.
- `claim.http-idempotence-is-not-global-exactly-once` is `contested` and contains one
  `contradicts` relation. The contradiction is against a broad interpretation, not
  necessarily against another source.
- `claim.jep491-full-text-unavailable` is `insufficient-evidence`: the source is
  `pending-content-access`, the relation is `unavailable`, the location is null and the
  owner page is outside the book route index.
- The decision lookup returns only direct related/prerequisite documents and says so in a
  warning.

## Statuses

| Status | Meaning |
|---|---|
| `ok` | The ID resolved and the ledger passed validation. |
| `not-found` | The requested claim, source, document or decision is absent. |
| `invalid-request` | Empty ID, wrong document kind or malformed input. |
| `not-available` | The ledger, register, lock or route index is missing or invalid. |
| `snapshot-mismatch` | The caller expected a different evidence snapshot. |

## Verification boundary

[Nine offline tests](../tests/test_tycho_evidence.py) cover supported, contested and
unavailable claims, source relations, document/frontmatter mismatch, decision references,
snapshot refusal, unknown IDs, wrong kind and an invalid ledger. They do not verify URL
reachability, source text, claim truth, reviewer approval or legal reuse rights. They do not
prove that a returned source actually supports the claim; the claim ledger records that
judgement separately.

The resolver is document-level. Section-level evidence lookup requires the section index and
is a later integration step. Only three claims are registered today, so coverage is
deliberately small.

## Integration and next gates

The retrieval contract's `evidence` operation can use these functions directly. Wiring it
into the search/API response should happen after #50 lands, and the MCP adapter (#57+)
should expose the same bounded fields rather than a new graph method. Next steps:

1. Wire `evidence` into the search/read flow with the same snapshot check.
2. Add section-level document/section evidence resolution when the section index is present.
3. Expand the claim ledger only through the existing admission and validation workflow.
