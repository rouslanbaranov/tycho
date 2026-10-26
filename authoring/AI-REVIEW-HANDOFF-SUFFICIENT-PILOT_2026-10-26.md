# Independent AI review hand-off — sufficient pilot

Status: prepared for an independent external AI review of six sufficient-ready entries.
This is not a review, promotion, owner acceptance or sufficient-coverage claim.

- Issue: #540
- Pilot baseline: `974de23d`
- Policy: [governance/SUFFICIENT-COVERAGE.md](../governance/SUFFICIENT-COVERAGE.md)
- Manifest: `research/sufficient-pilot-540/manifest.json`
- Owner units: `edition/patterns/owner-units.v1.json`
- Registry: `edition/patterns/registry.v1.json`
- Source plan: `edition/patterns/source-plan.v1.json`
- Ledger: `edition/patterns/reading-ledger.v1.json`
- Cards: `book/volumes/v11-pattern-atlas/c10-deployment-modernization/README.md`
  and `book/volumes/v11-pattern-atlas/c11-security-operations/README.md`

## Scope

1. Workload Identity / mTLS
2. Dark Launching / Shadow Traffic
3. RBAC/ABAC
4. Federated Identity
5. Controlled Cutover
6. Parallel Run

For each entry decide whether **technical sufficiency** and **decision sufficiency**
under the policy are met. `sufficient-ready` is not accepted as evidence.

## Required checks

1. Recompute the owner-page and card hashes in the manifest.
2. Read the owner heading and card section; verify mechanism, invariant, failure/recovery,
   alternative, decision question, fit conditions, contraindications and competing
   alternative.
3. Verify the ledger record is `read`, has the stated source and limitations, and supports
   the quoted passages.
4. Verify the source plan unit and revision/hash.
5. Identify any synthetic-only claim that is presented as source support.
6. Decide pass / pass-with-findings / reject per entry, for technical and decision.
7. Record exact findings, paths, line/heading and evidence.

## Exact prompt

```text
You are an independent AI reviewer from a different vendor and harness than the
DeepSeek Harness authoring agent. Review six Tycho pattern entries for promotion from
sufficient-ready to sufficient. Work read-only; do not edit, commit, open a PR or change
configuration.

Repository: /Users/rbaranov/Projects/tycho
Checkout: current branch HEAD; record `git rev-parse HEAD`.
Pilot baseline: 974de23d.
Policy: governance/SUFFICIENT-COVERAGE.md
Manifest: research/sufficient-pilot-540/manifest.json
Owner units: edition/patterns/owner-units.v1.json
Registry: edition/patterns/registry.v1.json
Source plan: edition/patterns/source-plan.v1.json
Ledger: edition/patterns/reading-ledger.v1.json

Entries:
1. tycho.pattern.workload-identity-mtls
2. tycho.pattern.dark-launching-shadow-traffic
3. tycho.pattern.rbac-abac
4. tycho.pattern.federated-identity
5. tycho.pattern.controlled-cutover
6. tycho.pattern.parallel-run

Do not accept sufficient-ready as evidence. For each entry, apply the policy and
decide technical sufficiency and decision sufficiency independently. Verify the owner
page hash and card hash from the manifest, read the owner heading and card section, and
verify the ledger/source binding and quoted passages. Use public sources only.

Return one Markdown report with: reviewer harness/vendor, model/version, session id,
timestamp, repository path, review HEAD, pilot baseline, per-entry table
(technical pass/PWF/reject, decision pass/PWF/reject), findings by severity with
exact paths and evidence, synthetic-only claims, limits, and `sufficient: 0` until an
entry is actually promoted. Do not claim owner acceptance, CI or merge permission.
```

The author saves the returned report verbatim under `authoring/ai-reviews/` and records
its SHA-256 in the index. Promotion waits for a separate commit that adds the matching
promotion records.
