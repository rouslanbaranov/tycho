# Independent re-review instructions — current HEAD

> **Superseded 2026-10-26.** This instruction set describes the retired same-harness review
> model. New reviews must use an external AI harness from a different vendor under
> [the AI review policy](../governance/AI-INDEPENDENT-REVIEW.md). This file is historical.

> Issue [#330](https://github.com/rouslanbaranov/tycho/issues/330), child of #228.
> This is an instruction set, not a review, promotion or acceptance. The auditor must
> produce a separate report; the owner decides whether to apply it.

## 1. Purpose

Run a new independent re-review of the sufficient-candidate pattern records at the current
HEAD. The previous audit is historical: its page hashes are pinned to `7be12e0` and owner
pages have changed since then. Do not reuse those hashes or verdicts.

## 2. Hand-off snapshot

Record the actual HEAD in the report. The baseline observed when this document was written:

| Item | Value |
|---|---|
| Hand-off baseline HEAD | `49df510296ceadf8fa2ff1293133c57450f639a4` |
| Delivery content commit | `40cded2c4fdd68c198e957e537a0f5075aa0e75f` |
| Records | 145 |
| Verdicts | 37 pass / 105 pass-with-findings / 3 reject |
| Previously audited | 52: 33 pass / 16 PWF / 3 reject |
| Not previously audited | 93: 4 initial pass / 83 needs remediation / 6 remediated |
| Re-reviews with separate report | 52 |
| Re-reviews without report | 0 |
| Route snapshot | `f5921b364492bdba3240db244cf35d9527b938dbaf1feb9d0efd2fe62d359046` |
| Section snapshot | `65faf4fe8566...` |
| Qrels snapshot | `f5921b364492bdba3240db244cf35d9527b938dbaf1feb9d0efd2fe62d359046` |

The qrels baseline is page hit@5 0.758, chapter hit@5 0.884, nDCG@10 0.5577 over 95
answerable items. These metrics are retrieval evidence, not content review.

### Scope manifest

The [scope manifest][scope-json] lists the 52 Phase A and 93 Phase B entries with current
page hashes, owner/card bindings, prior verdicts/findings and read source units. It is an
index snapshot at content commit `40cded2`, not a review.

Check it read-only before starting:

```bash
.venv/bin/python scripts/build_rereview_scope.py --check
```

If the check reports drift, record the actual hand-off HEAD and recompute every page hash;
do not edit the manifest. `--write` is prohibited for the auditor.

## 3. Scope

Phase A is mandatory: all 52 previously audited entries at the handed-off HEAD. This
includes the 3 reject entries, the 16 audited PWF entries and the 33 audited pass entries.
Re-check the pass entries too; a card or owner page may have changed.

Phase B is required before any global claim: the 93 not previously audited entries. If the
owner commissions Phase A only, say so explicitly; do not imply that 145 entries were
reviewed.

Phase C is out of scope for the auditor: human per-page review and owner acceptance. Do not
perform, invent or imply either.

Use this read-only command to print the exact scope lists:

```bash
.venv/bin/python - <<'PY'
import json
from pathlib import Path
r = json.loads(Path("edition/patterns/sufficient-review-records.v1.json").read_text())
a = json.loads(Path(
    "edition/patterns/independent-agent-rereview-2026-10-22.v1.json").read_text())
audited = {p["pattern_id"] for p in a["packets"]}
for rec in r["records"]:
    if rec["pattern_id"] in audited:
        print("A", rec["verdict"], rec["pattern_id"])
for rec in r["records"]:
    if rec["pattern_id"] not in audited:
        print("B", rec["verdict"], rec["remediated"], rec["re_reviewed"],
              rec["pattern_id"])
PY
```

## 4. Independence and authority

- Do not author, remediate or edit any canonical record, page, card, schema or artifact.
- Do not accept the prior audit, this document or a validator pass as proof of content.
- Read public sources only. Do not use private, restricted or conversation-derived corpora.
- If a source is inaccessible, do not infer its content; mark the entry `reject` with a
  blocking `source-unavailable` finding.
- Never claim human review, independent human review, owner acceptance, CI or `sufficient`.
- You may create only the report files described in section 8. If the owner asks you to add
  them to the repository, use a separate issue-specific branch and do not touch canonical
  artifacts.

### Read-only access

Read-only repository access is sufficient; no canonical write access is required.

- A fresh clone does not contain `.venv`. Use a prepared environment or install the
  validation dependencies; do not write into the checkout.
- `generated/sections-fts-v3.sqlite` is git-ignored. `section_fts_index.py check` and
  `section_search.py` need it; if absent, skip the check and record that limitation.
- Set `PYTHONDONTWRITEBYTECODE=1` and use a writable scratch directory outside the checkout.
- Deliver the report files to the owner. The `authoring/...` names are delivery conventions;
  the owner commits them. If you need to open a PR, use your own fork; upstream can stay
  read-only.

## 5. Read-only checks

Run from the repository root with the project virtual environment:

```bash
git rev-parse HEAD
git status --short
.venv/bin/python scripts/check_boundary.py
.venv/bin/python scripts/validate_pattern_sources.py
.venv/bin/python scripts/validate_pattern_cards.py
.venv/bin/python scripts/validate_pattern_owner_units.py
.venv/bin/python scripts/validate_delivery_evidence.py --json
.venv/bin/python scripts/validate_corpus_qrels.py
.venv/bin/python scripts/route_index.py check
.venv/bin/python scripts/section_fts_index.py check
.venv/bin/python scripts/build_rereview_scope.py --check
```

Do **not** run `reconcile_sufficient_reviews.py`, `build_rereview_packets.py`,
`sufficient_candidates.py --write`, `phase4_audit.py`, `pattern_census.py --write`,
`route_index.py build`, `section_fts_index.py build` or any command that rewrites tracked
artifacts. A validator pass is structural evidence only.

`section_fts_index.py check` requires the git-ignored generated index. If it is absent,
skip it and record the limitation; it is not required for content review.

## 6. Per-entry procedure

For every entry in scope:

1. Read the record: `pattern_id`, verdict, findings, `re_review`, `report_path`.
2. Read the registry: catalog name, owner path, anchor, source units, coverage state.
3. Read the owner section in full, not only the heading or the card.
4. Read the card decision question, conditions, contraindications, alternative, failure and
   recovery, sources and decision state.
5. Recompute the page SHA-256 and record it. Do not reuse the old packet hash.
6. Read the source-plan unit and the reading-ledger record. Verify source ID, URL, unit
   label, sections read, access date and content hash.
7. Check the source register: admission, access, version and verification scope. Pin a
   version when the source is rolling.
8. Verify each material card/owner claim against the exact source text or the owner's
   original design boundary. Quote the supporting or contradicting line.
9. Check link anchors, line lengths, `evidence_scope`, review labels and reciprocal links.
10. Check the F-001-F-022 remediation table in section 7 against the current files. A
    previous fix is not evidence that the current file still has it.
11. Assign one verdict and findings. Do not skip an entry because it is hard or the source
    is unavailable.

## 7. Prior findings to verify

These were resolved or remediated before this hand-off. Verify each in current files:

| Finding | Status to verify |
|---|---|
| F-001 | Every re-review has a separate report path, reviewer, page hash and findings. |
| F-002 | Original findings counts match the cited report sections. |
| F-003 | Cell-Based cites a dedicated cell source, not Deployment Stamps. |
| F-004 | CDC cites a general log-based source, not only the outbox router. |
| F-005 | Materialized View cites PostgreSQL 18 refresh semantics, not projector cursors. |
| F-006 | Protocol records three reject-level entries, not zero. |
| F-007 | Delivery evidence counts, source commit and review labels match current files. |
| F-008 | Read Replicas states its lag/routing boundary, not a multi-leader protocol. |
| F-009 | Expand-and-Contract has only owner-supported conditions/alternative. |
| F-010 | Event Sourcing has no assumed idempotent-projector requirement. |
| F-011 | Cache-Aside uses the owner-supported alternative. |
| F-012 | Negative Caching uses bypass/per-principal-key/short-TTL. |
| F-013 | Process Manager states the routing-slip source boundary. |
| F-014 | Circuit Breaker has an explicit fallback/fail-fast condition. |
| F-015 | Five owner sections no longer repeat earlier-page sentences. |
| F-016 | Slash-heading backlinks use double-hyphen anchors. |
| F-017 | Correlation/Request-Reply labels describe their targets. |
| F-018 | The cited workflow-failure lines are within 100 characters. |
| F-019 | Deadline citation label matches "Addressing Cascading Failures". |
| F-020 | Static Content Hosting records retained-version/edge-copy cost. |
| F-021 | Shuffle Sharding records containment and recovery. |
| F-022 | The 11 owner pages have non-empty evidence scope. |

A remediation may be present but still wrong. Report a new finding if it is.

## 8. Verdicts and findings

Allowed verdicts: `pass`, `pass-with-findings`, `reject`.

- `pass`: no findings; card, owner, source and links are coherent; no unsupported claim.
- `pass-with-findings`: only non-blocking findings; the decision remains usable.
- `reject`: at least one blocking finding; do not promote until remediated and re-reviewed.

Severity: `blocking` for an unsupported claim, source mismatch, missing owner or
unavailable source; `major` for a stale source/version, wrong alternative or broken
evidence chain; `minor` for wording, anchors, line length or metadata.

Finding schema:

```yaml
- id: G-001
  severity: blocking | major | minor
  pattern_id: tycho.pattern.example
  path: book/.../page.md
  line: 42
  quote: "exact text"
  issue: "what is wrong and why it matters"
  remediation: "what must change"
  evidence: "source/owner line or rule"
```

Do not report a finding without an exact location and evidence. Do not duplicate one issue
across entries without saying so.

## 9. Report format

Deliver:

- `authoring/INDEPENDENT-AGENT-REREVIEW-<YYYY-MM-DD>-v2.md` (English, at most 100 chars/line);
- `authoring/INDEPENDENT-AGENT-REREVIEW-<YYYY-MM-DD>-v2.json` (machine-readable).

With read-only access, send the two files to the owner; the owner commits them. The paths
are delivery conventions, not write permission.

The Markdown must contain: reviewer identity and relationship, review date, actual HEAD,
scope (Phase A and whether Phase B), summary counts, one row per entry, findings, limits and
nonclaims. The JSON must contain: metadata, summary, `packets` with `pattern_id`,
`catalog_name`, `verdict`, `page_sha256`, `finding_ids`, and a `findings` array using
the schema above.

The report is an audit record. It does not update the canonical records.

## 10. Acceptance

- Phase A: 52/52 entries have a current page hash and verdict.
- Every F-001-F-022 item is checked against current files, not the old report.
- No verdict is promoted without this report; no `sufficient`; no human/owner claim.
- No canonical file, record, page or artifact is edited.
- If any entry is inaccessible, it is `reject` with a blocking finding, not skipped.

## 11. Known traps

- Old page hashes are from `7be12e0`; current owner pages have changed.
- The scope manifest is a snapshot; verify its hashes at the actual HEAD.
- 16 PWF and 3 reject entries are still unpromoted; do not copy their old verdict as proof.
- The 4 initial passes and the 83/6 backlog were not in the 52-packet audit.
- The semantic audit and validators are self-checked structural evidence, not independent
  content review.
- Retrieval metrics do not establish claim support.
- A source title or abstract is not a read; check the ledger sections and content hash.
- Do not use internal, private or employer-specific material, even as an example.

## 12. Hand-off checklist

- [ ] Confirm HEAD and clean working tree.
- [ ] Print the Phase A and Phase B lists.
- [ ] Run the read-only checks.
- [ ] Recompute page hashes.
- [ ] Complete every entry in the commissioned phase.
- [ ] Write the Markdown and JSON reports.
- [ ] State limits and nonclaims.
- [ ] Deliver to the owner; do not edit canonical records.

[scope-json]: ../edition/patterns/independent-rereview-scope-2026-10-22.v2.json
