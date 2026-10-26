# Independent AI review hand-off — full-unit reading and removed-claim verification

Status: prepared for independent AI review. This document is not a review, a reviewer sign-off,
`sufficient` coverage, owner acceptance or CI evidence.

- Issue: #535
- Branch: `feature/TYCHO-535-read-the-155-pattern-source-plan-units-in-full`
- Evidence HEAD: `180597e52403e3dabb71c50eb92a5b991d6803b8`
- Hand-off/policy commit: `5afae41a`
- Base dependency: the branch is based on the unmerged #532 work because the 155-unit
  plan and the newest records are not on `main`.
- Pull request: #536 is a draft. #534 is also draft and unmerged. Nothing is merged.

## 1. What was done

Two bounded passes were completed.

1. **B1 reading**: all 155 source-plan units were addressed. 143 were read in full or
   matched an exact prior revision/scope; 1 is partial; 11 are blocked and accepted.
2. **Removed-claim verification**: all 23 claims removed as unconfirmed were reassigned a
   final disposition after reading the complete available source, not only the cited page
   or chapter. The final set contains no pending claim.

## 2. Final counts

### Units

| Disposition | Count |
|---|---:|
| `full-read` | 129 |
| `full-read-exact-reuse` | 14 |
| `partial-read` | 1 |
| `blocked-current` | 11 |
| **Total** | **155** |

- 143 units were read fully or with exact reuse.
- 1 partial: PostgreSQL `Failover / Failback`; §26.3 was read, but the PostgreSQL 18
  manual contains no failback procedure. Accepted.
- 11 blocked: 10 EIP Chapter 4+ units and 1 DDIA unit. Accepted as source-unavailable.

### Removed claims

| Disposition | Count |
|---|---:|
| `unconfirmed` (accepted) | 17 |
| `contradicted` | 3 |
| `partially-supported` | 2 |
| `resolved` | 1 |
| **Total** | **23** |

- 17 unconfirmed: 11 EIP Chapter 4+, 5 public-web claims absent from fully read pages,
  and 1 SRE Workbook claim absent from the complete book.
- 3 contradicted: Cassandra overview consistent hashing; KEDA landing page mechanics;
  EIP per-stage buffering/ordering/failure.
- 2 partially supported: ASVS 5.0.0; EIP Routing Slip.
- 1 resolved: OpenID Federation revocation process versus revocation status data.

## 3. Scope for the AI reviewer

Do not re-read all 155 units from scratch. The high-value review is targeted.

### Mandatory checks

1. **ASVS FS-22** — confirm that ASVS 5.0.0 supports levels, least privilege,
   authorization and tenant isolation, and that `trust boundary` is absent. The claim is
   accepted only as partially supported.
2. **OpenID FS-23** — confirm §11.4 says the specification does not define a revocation
   process, and that the resolution separates process from key/trust-mark status data.
3. **EIP FS-10** — confirm the contradiction using the official Chapter 3 PDF, printed
   pp.72, 74 and 77. This is the strongest negative finding.
4. **EIP Chapter 4+ acceptance** — challenge whether any of the 11 accepted-unconfirmed
   claims can be supported by the public pattern pages or Chapter 3. If yes, the
   acceptance is too broad.
5. **DDIA block** — confirm that no full text was used and that `blocked-current` is
   honest.
6. **Five public claims** — spot-check FS-01, FS-02, FS-03, FS-19 and FS-20 against the
   complete pages and the PostgreSQL 18 manual search.
7. **SRE Workbook FS-21** — spot-check that the complete 34-page book never defines
   synthetic monitoring.

### Sampling

Read at least one cited passage for each of the 23 claims. For the 143 full units, sample
at least 15 units across batches 1-21, including every batch with a corrected heading
list or a contradicted claim.

## 4. Known limits and accepted gaps

- 10 EIP units are accepted `source-unavailable`. Only Chapter 3 is author-hosted; the
  Internet Archive controlled-lending copy was located but not borrowed.
- DDIA is accepted `blocked-current`. Only a controlled-lending copy was located.
- PostgreSQL failback is accepted `partial`; the 18 A4 manual has zero occurrences of
  `failback`, `RPO`, `RTO`, `restore drill` and `restore verification`.
- Five public claims are accepted `unconfirmed` because the complete public pages do not
  state them.
- FS-21 is accepted `unconfirmed` after reading the complete SRE Workbook.
- No independent AI review, CI, owner acceptance or `sufficient` coverage is
  claimed anywhere in this hand-off.

## 5. Evidence index

- Reading plan and counts: `edition/patterns/full-unit-reading-plan.v1.json`
- Reading ledger: `edition/patterns/reading-ledger.v1.json`
- Source plan: `edition/patterns/source-plan.v1.json`
- Crosswalk: `authoring/FULL-UNIT-READING-CROSSWALK.md`
- Reading contract: `authoring/FULL-UNIT-READING-CONTRACT-2026-10-26.md`
- Batch records: `research/full-unit-reading-535/batch-01.json` … `batch-21.json`
- Claim registry: `research/full-source-confirmation/claims.v1.json`
- Claim results: `research/full-source-confirmation/results.v1.json`
- Alternatives: `research/full-source-confirmation/ALTERNATIVES.md`
- Accepted gaps: `research/full-source-confirmation/ACCEPTED.md`
- Owner resolutions: `research/full-source-confirmation/RESOLUTIONS.md`
- Prior #225 audit: `research/source-audit-225/readings.json`

Key commits, oldest first:

- `fd9c1004` — finish B1 batch 21
- `3570118d` — start full-source verification
- `7c0ef1d5` — complete SRE Workbook
- `9b66bea3` — OpenID resolution applied
- `545ad654` — EIP per-stage buffering contradicted
- `d02c3451` — alternative official sources
- `50ef9856` — accept DDIA and PostgreSQL failback
- `9b31daef` — accept five public claims and FS-21
- `18449574` — EIP controlled-lending copy recorded
- `180597e5` — accept EIP Chapter 4+ as source-unavailable

## 6. Reproduction checks

From the worktree root:

```bash
python3 - <<'PY'
import collections, json
p = 'edition/patterns/full-unit-reading-plan.v1.json'
d = json.load(open(p))
print(collections.Counter(x['disposition'] for x in d['entries']))
c = json.load(open('research/full-source-confirmation/claims.v1.json'))
print(collections.Counter(x['status'] for x in c['claims']))
PY

for s in validate_sources validate_pattern_sources validate_pattern_cards \
  validate_pattern_owner_units validate_pattern_semantic_audit \
  validate_pattern_atlas validate_delivery_evidence; do
  python3 scripts/$s.py
done
python3 scripts/validate_edition.py
```

Expected: 129 full + 14 exact + 1 partial + 11 blocked; claims 17 unconfirmed + 3
contradicted + 2 partially supported + 1 resolved. `validate_edition.py` writes an
inventory and exits zero.

## 7. Out of scope

- Do not edit canonical pages, cards, ledger, plan, schemas or generated indexes.
- Do not mark any unit `sufficient` on the basis of this hand-off.
- Do not infer EIP Chapter 4+ text from the abridged public pages or from a pirated copy.
- Do not claim CI ran; GitHub Actions is not triggered by push or PR in this repository.
- Do not treat a validator pass as content review.

## 8. Reviewer decision

| Field | Value |
|---|---|
| Reviewer harness / vendor | |
| Model / version | |
| Session / run id | |
| Date | |
| Scope reviewed | |
| Verdict | pass / pass-with-findings / reject |
| Blocking findings | |
| Non-blocking findings | |
| Accepted gaps challenged | |
| `ai_review` | not-performed until signed above |
| `sufficient` | 0 |

A pass here is a review of this evidence package only. It is not sufficient coverage,
owner acceptance of the Pattern Atlas, or permission to merge.


## 9. Exact prompt for the external reviewer

Copy the block below into a fresh ChatGPT or Claude Code session. Do not pass this
conversation or any author conclusion as context.

```text
You are an independent AI reviewer from a different vendor and harness than the
DeepSeek Harness authoring agent. Review Tycho issue #535 read-only. Do not edit,
commit, open a PR or change configuration.

Repository: /Users/rbaranov/Projects/tycho
Review checkout: current branch HEAD (record git rev-parse HEAD). B1 data is
unchanged from 180597e5.
B1 evidence HEAD: 180597e52403e3dabb71c50eb92a5b991d6803b8
Hand-off: authoring/AI-REVIEW-HANDOFF_2026-10-26.md
Claims: research/full-source-confirmation/claims.v1.json
Results: research/full-source-confirmation/results.v1.json

Read the hand-off completely. Derive every count from the artifacts, not from this
prompt. Do not trust the author's conclusions; test them against the evidence and
public sources. Use public sources only. Never use restricted or private material.

Verify at minimum:
1. Unit counts: 129 full, 14 exact reuse, 1 partial, 11 blocked, total 155.
2. Claim counts: 17 unconfirmed, 3 contradicted, 2 partially supported, 1 resolved,
   total 23.
3. ASVS FS-22: trust-boundary term is absent from ASVS 5.0.0; three other elements
   are present.
4. OpenID FS-23: Section 11.4 says the specification does not define a revocation
   process; key and trust-mark status data are separate.
5. EIP FS-10: official Chapter 3 PDF contradicts per-stage buffering, ordering and
   failure behavior at printed pp.72, 74 and 77.
6. EIP Chapter 4+ acceptance: check whether any of the 11 accepted-unconfirmed claims
   is actually supported by the public pages or Chapter 3. If yes, say so.
7. DDIA block: confirm no full text was used.
8. Five public claims and FS-21: confirm they are absent from the complete public
   sources and the complete SRE Workbook.

Run the reproduction commands in the hand-off. You may sample at least one cited
passage per claim and at least 15 of the 143 full units, including every batch with a
corrected heading list or a contradicted claim. Do not re-read all 155 units.

Return one Markdown report with: reviewer harness/vendor, model/version, session id,
timestamp, repository path, review checkout, B1 evidence HEAD, exact scope, verdict
(pass / pass-with-findings / reject), findings by severity with exact paths and
evidence, limits, and the statement `ai_review: performed` only if you actually ran
the checks. State `sufficient: 0`. Do not claim owner acceptance, CI or merge
permission.
```
