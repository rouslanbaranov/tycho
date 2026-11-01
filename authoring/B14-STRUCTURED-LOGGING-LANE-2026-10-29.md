# B14 — Structured Logging invariant and failure/recovery lane

Status: lane-local book edit, self-checked on 2026-10-29. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry remains unpromoted; the preflight pass below depends on the integrator
applying the metadata patch.

## Lane coordinates

- Parent HEAD: `0b2752f87efa36d1844e9b94c04cd2f637e8d407`.
- Branch: `b14-structured-logging`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b14-structured-logging`.
- Scope: V11/C11 `structured-logging.md` and the V09/C04
  `logs-audit-and-data-lineage.md` owner section `### Structured Logging`
  only.
- This is a single-entry lane; no other entry, shared owner page, promotion or
  generated file is changed.

## Source binding

- Primary source: `src.owasp-asvs`, OWASP Application Security Verification
  Standard 5.0.0, pinned PDF.
- Ledger record: `read.batch6-asvs.2026-10-21`; section
  "V16 Security Logging and Error Handling"; requirements 16.2.4, 16.2.5,
  16.4.2 and 16.4.3.
- Revision: `a2fa1bbe38f12cac86d3a0f0023327e9772201f65a7f741f282f5e785d268fc5`.
  Downloaded the pinned URL on 2026-10-29; the PDF bytes hash to this value,
  matching the ledger `content_sha256`.
- Exact public quote for the invariant binding (requirement 16.2.5,
  Description cell):

      Verify that when logging sensitive data, the application enforces logging
      based on the data’s protection level. For example, it may not be allowed
      to log certain data, such as credentials or payment details. Other data,
      such as session tokens, may only be logged by being hashed or masked,
      either in full or partially.

  The `pdftotext -layout` representation places the table's Level column
  between the first and second physical lines; the quote is the continuous
  Description cell, verified by extracting that column. The character
  `data’s` uses U+2019 as in the PDF.
- Exact public quote for the failure/recovery binding (V16 control objective):

      Logs should not include sensitive personal data unless legally required,
      and any logged data must be protected as a high‑value asset. Logging
      must not compromise privacy or system security.

  `high‑value` uses U+2011 as in the PDF.
- Supporting quotes:
  - 16.2.4: "Verify that logs can be read and correlated by the log processor
    that is in use, preferably by using a common logging format."
  - 16.4.2: "Verify that logs are protected from unauthorized access and
    cannot be modified."
  - 16.4.3: "Verify that logs are securely transmitted to a logically separate
    system for analysis, detection, alerting, and escalation. The aim is to
    ensure that if the application is breached, the logs are not compromised."
- The mechanism, alternative and stable-schema context remain bound to
  `src.otel`, ledger record `read.batch6-otel-logs.2026-10-21`, revision
  `c9e3b0c7ae0ba7e58fbc14898159199a683edbfbc5474fd43e2fc1b07e2d98bb`;
  no new OTel fetch or unit is claimed. The supporting OTel statements are
  "A structured log is a log with a defined, consistent schema or typed fields
  that downstream systems can reliably parse and interpret." and
  "Semistructured logs include machine-readable key/value pairs or delimited
  fields but do not guarantee a stable schema across emitters."
- Limit: ASVS is a verification standard. It requires protection-level
  enforcement and log protection but does not define a schema-version or
  compatibility-window policy, a build-failing redaction test, or a
  purge/rotation/notification procedure. Those remain Tycho synthesis and are
  labelled as such in both book files.

## Book edits

- V11/C11 card `structured-logging.md`: the route question is completed with
  `?` so the preflight sees a full question. **Good-fit conditions** now
  state the schema, protection-level and correlation conditions. **Failure and
  recovery** states the ASVS-bound failure and protection/escalation response
  and labels stop/rotate/purge/notify as Tycho guidance. **Sources** adds
  `src.owasp-asvs`, the V16 requirements and the pinned revision; the
  frontmatter `evidence_scope.source_ids` adds `src.owasp-asvs`, and
  `updated_at`, `source_inspection_date` and
  `content_review.reviewed_at` advance to 2026-10-29.
- V09/C04 owner `logs-audit-and-data-lineage.md#structured-logging`: the
  **Invariant** paragraph now binds requirement 16.2.5 and the stable-schema /
  correlation supporting claim. The **Failure and recovery** paragraph binds
  the V16 control objective, 16.4.3 and the schema-variation clause, and labels
  purge/rotation/notification as Tycho guidance. A **Source boundary**
  paragraph records both sources, the ASVS revision and the unsupported
  synthesis. Frontmatter `updated_at` and `source_inspection_date` advance
  to 2026-10-29; the section keeps the existing alternative sentence verbatim
  so the supported alternative binding still preflights.
- The owner heading remains at line 113; `### Audit Trail` moves from 136 to
  157, so the integrator patch updates both owner-unit line fields.
- No other book file, edition JSON, promotion or generated file is changed.

## Promotion and enrichment baseline check

- `edition/patterns/sufficient-promotions.v1.json` contains 27 promotions.
  Neither edited file's SHA-256 matches any `card_sha256` or
  `owner_page_sha256`, and no promotion names
  `tycho.pattern.structured-logging`. The entry is unpromoted. This lane adds
  no promotion.
- The edited owner page is a retained baseline document
  (`tycho.page.436c2b22dc9e47acaaca7d18fadb511c` is in
  `retained_document_ids`), not a new or modified enrichment document in
  `edition/enrichment-manifest.json`. `python3 scripts/validate_enrichment.py`
  passes on the lane worktree.
- The frozen search pre-enrichment snapshot
  (`edition/patterns/search-pre-enrichment.v1.json`) hashes the edited owner
  page and will be stale; it is a derived search snapshot, not the enrichment
  conservation baseline. The integrator must regenerate it with the other
  derived artifacts. No promotion or enrichment baseline is invalidated.

## Preflight

At the parent HEAD the baseline fails on the unbound dimensions and the card
question:

    FAIL: tycho.pattern.structured-logging
      - invariant: state 'partial', not supported
      - failure_recovery: state 'partial', not supported
      - route_hints.questions missing or not a full question
    0/1 entries preflight clean

After the two book edits, lane HEAD fails only because
`edition/patterns/owner-units.v1.json` is integrator-owned and still says
`invariant: partial` and `failure_recovery: partial`:

    FAIL: tycho.pattern.structured-logging
      - invariant: state 'partial', not supported
      - failure_recovery: state 'partial', not supported
    0/1 entries preflight clean

A detached scratch worktree at parent HEAD with the two book files copied and
the metadata patch below applied runs:

    PASS: tycho.pattern.structured-logging
    1/1 entries preflight clean

The same scratch tree also passes:

- `python3 scripts/validate_pattern_owner_units.py` — PASS: owner units 145
  entries, 145 units, 30 shared pages.
- `python3 scripts/validate_pattern_sources.py` — PASS: source plan 145
  entries; 168 read; 138 ledger records.
- `python3 scripts/validate_pattern_registry.py` — PASS: pattern registry 145
  entries, 11 families.
- `python3 scripts/validate_pattern_cards.py` — PASS: pattern cards 11
  batch(es), 145 entries.
- `python3 scripts/check_markdown_line_length.py` — PASS: V11 prose <=100;
  145 exact owner-link exceptions.
- `python3 scripts/check_boundary.py` — PASS: configured lexical boundary
  checks; independent-origin review still required.
- `python3 scripts/validate_enrichment.py` — PASS: explicit membership and
  byte conservation.

`python3 scripts/validate_pattern_atlas.py` still fails at
`atlas-document-sha` until the integrator refreshes the atlas manifest and the
other derived artifacts. This is a derived-artifact refresh, not a content
failure. The lane intentionally does not touch generated files.

## Metadata patch (integrator)

Run this from the repository root. It edits only shared metadata; the two book
files are already in the lane commit. It reuses the admitted
`read.batch6-asvs.2026-10-21` ledger record and `src.owasp-asvs`; no ledger
or source-register change is required.

```python
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(".").resolve()
PATTERN = "tycho.pattern.structured-logging"
ASVS_SOURCE = "src.owasp-asvs"
ASVS_RECORD = "read.batch6-asvs.2026-10-21"
ASVS_SECTION = "V16 Security Logging and Error Handling"
ASVS_REVISION = (
    "a2fa1bbe38f12cac86d3a0f0023327e9772201f65a7f741f282f5e785d268fc5"
)
OWNER = (
    "book/volumes/v09-observability-security-and-operations/"
    "c04-logging-audit-and-lineage/logs-audit-and-data-lineage.md"
)
CARD = (
    "book/volumes/v11-pattern-atlas/c11-security-operations/"
    "structured-logging.md"
)

INV = (
    "When sensitive data is logged, the application enforces the data's protection "
    "level: data that may not be logged is excluded, and allowed sensitive values are "
    "hashed or masked, in full or partially. Events also follow a consistent, "
    "machine-readable schema so the log processor can read and correlate them."
)
FR = (
    "Logging sensitive personal data without a legal basis, or failing to protect logs "
    "as a high-value asset, can compromise privacy or system security; a schema that "
    "varies across emitters also needs normalization before reliable analysis. Protect "
    "logs from unauthorized access and modification, and transmit them securely to a "
    "separate system for analysis, detection, alerting and escalation."
)
Q_16_2_4 = (
    "Verify that logs can be read and correlated by the log processor that is in use, "
    "preferably by using a common logging format."
)
Q_16_2_5 = (
    "Verify that when logging sensitive data, the application enforces logging based on "
    "the data’s protection level. For example, it may not be allowed to log certain "
    "data, such as credentials or payment details. Other data, such as session tokens, "
    "may only be logged by being hashed or masked, either in full or partially."
)
Q_16_4_2 = (
    "Verify that logs are protected from unauthorized access and cannot be modified."
)
Q_16_4_3 = (
    "Verify that logs are securely transmitted to a logically separate system for "
    "analysis, detection, alerting, and escalation. The aim is to ensure that if the "
    "application is breached, the logs are not compromised."
)
Q_CONTROL = (
    "Logs should not include sensitive personal data unless legally required, and any "
    "logged data must be protected as a high\u2011value asset. Logging must not "
    "compromise privacy or system security."
)
Q_OTEL_STRUCTURED = (
    "A structured log is a log with a defined, consistent schema or typed fields that "
    "downstream systems can reliably parse and interpret."
)
Q_OTEL_SEMI = (
    "Semistructured logs include machine-readable key/value pairs or delimited fields "
    "but do not guarantee a stable schema across emitters."
)


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def save(path, data):
    (ROOT / path).write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def squash(value):
    return re.sub(r"\s+", " ", value).strip()


def binding(source_id, record, section, quote, revision):
    return {
        "source_id": source_id,
        "ledger_record": record,
        "section": section,
        "quote": quote,
        "revision": revision,
    }


# Owner units
path = "edition/patterns/owner-units.v1.json"
units = load(path)
entry = next(e for e in units["entries"] if e["pattern_id"] == PATTERN)
owner_text = (ROOT / entry["owner"]["path"]).read_text(encoding="utf-8")
assert entry["owner"]["path"] == OWNER
owner_body = owner_text[owner_text.index("### Structured Logging"):
                        owner_text.index("### Audit Trail")]
assert squash(INV) in squash(owner_body), "invariant quote not verbatim"
assert squash(FR) in squash(owner_body), "failure quote not verbatim"

inv = entry["technical_evidence"]["invariant"]
inv["state"] = "supported"
inv["quote"] = INV
inv["reason"] = (
    "Binds ASVS 5.0.0 requirement 16.2.5: when sensitive data is logged, the "
    "application enforces the data's protection level, excluding data that may not be "
    "logged and hashing or masking allowed sensitive values. Requirement 16.2.4 and the "
    "OpenTelemetry Logs page support the common-format/correlation and stable-schema "
    "clauses. ASVS defines no schema-version or compatibility-window rule; those are "
    "Tycho design guidance."
)
inv["binding"] = binding(
    ASVS_SOURCE, ASVS_RECORD, ASVS_SECTION, Q_16_2_5, ASVS_REVISION
)
inv["supporting_bindings"] = [
    binding(ASVS_SOURCE, ASVS_RECORD, ASVS_SECTION, Q_16_2_4, ASVS_REVISION),
    binding(
        "src.otel",
        "read.batch6-otel-logs.2026-10-21",
        "Structured logs",
        Q_OTEL_STRUCTURED,
        "c9e3b0c7ae0ba7e58fbc14898159199a683edbfbc5474fd43e2fc1b07e2d98bb",
    ),
]

fr = entry["technical_evidence"]["failure_recovery"]
fr["state"] = "supported"
fr["quote"] = FR
fr["reason"] = (
    "Binds the ASVS V16 control objective: logs must not include sensitive personal "
    "data unless legally required and must be protected as a high-value asset; "
    "requirements 16.4.2 and 16.4.3 require protection from unauthorized access or "
    "modification and secure transmission to a separate system for analysis, detection, "
    "alerting and escalation. The OpenTelemetry Logs page supports the schema-variation "
    "clause. ASVS prescribes no purge, credential-rotation or notification procedure; "
    "those are Tycho recovery guidance."
)
fr["binding"] = binding(
    ASVS_SOURCE, ASVS_RECORD, ASVS_SECTION, Q_CONTROL, ASVS_REVISION
)
fr["supporting_bindings"] = [
    binding(ASVS_SOURCE, ASVS_RECORD, ASVS_SECTION, Q_16_4_2, ASVS_REVISION),
    binding(ASVS_SOURCE, ASVS_RECORD, ASVS_SECTION, Q_16_4_3, ASVS_REVISION),
    binding(
        "src.otel",
        "read.batch6-otel-logs.2026-10-21",
        "Semistructured logs",
        Q_OTEL_SEMI,
        "c9e3b0c7ae0ba7e58fbc14898159199a683edbfbc5474fd43e2fc1b07e2d98bb",
    ),
]

support = entry["source_support"]
support["auxiliary"] = [
    {
        "source_id": ASVS_SOURCE,
        "ledger_record": ASVS_RECORD,
        "revision": ASVS_REVISION,
    }
]
entry["technical_coverage"] = "partial-bounded"
entry["notes"] = (
    "Invariant and failure/recovery bound 2026-10-29 to ASVS 5.0.0 V16 requirements "
    "16.2.4, 16.2.5, 16.4.2 and 16.4.3, with the OTel logs page retained for the "
    "mechanism, alternative and stable-schema context; all four dimensions supported, "
    "technical coverage partial-bounded, no promotion; schema versioning and incident "
    "purge/rotation/notification remain Tycho synthesis."
)
entry["owner"]["line"] = next(
    number for number, line in enumerate(owner_text.splitlines(), 1)
    if line == "### " + entry["owner"]["heading"]
)
audit = next(e for e in units["entries"] if e["pattern_id"] == "tycho.pattern.audit-trail")
audit["owner"]["line"] = next(
    number for number, line in enumerate(owner_text.splitlines(), 1)
    if line == "### " + audit["owner"]["heading"]
)
units["summary"]["invariant_supported"] += 1
units["summary"]["failure_recovery_supported"] += 1
units["summary"]["technical_partial_bounded"] += 1
units["summary"]["technical_partial"] -= 1
for page in units["shared_pages"]:
    if page["path"] == OWNER:
        page["bounded_entries"] = sum(
            1 for item in units["entries"]
            if item["owner"]["path"] == OWNER
            and item["technical_coverage"] == "partial-bounded"
        )
save(path, units)

# Registry
path = "edition/patterns/registry.v1.json"
registry = load(path)
pattern = next(p for p in registry["patterns"] if p["id"] == PATTERN)
pattern["technical_owner"]["state"] = "partial-bounded"
pattern["coverage"]["technical"] = "partial-bounded"
pattern["coverage"]["overall"] = "partial-bounded"
ledger = load("edition/patterns/reading-ledger.v1.json")
record = next(r for r in ledger["records"] if r["id"] == ASVS_RECORD)
assert record["content_sha256"] == ASVS_REVISION
assert not any(u["source_id"] == ASVS_SOURCE for u in pattern["source_units"])
pattern["source_units"].append({
    "source_id": ASVS_SOURCE,
    "unit": record["unit_label"],
    "status": "read",
})
pattern["notes"] = (
    "Invariant and failure/recovery bound 2026-10-29 to ASVS 5.0.0 V16; all four "
    "dimensions supported, technical coverage partial-bounded, no promotion; schema "
    "versioning and incident purge/rotation/notification remain Tycho synthesis."
)
save(path, registry)

# Source plan
path = "edition/patterns/source-plan.v1.json"
plan = load(path)
entry = next(e for e in plan["entries"] if e["pattern_id"] == PATTERN)
assert not any(u["source_id"] == ASVS_SOURCE for u in entry["required_units"])
entry["required_units"].append({
    "source_id": record["source_id"],
    "unit": record["unit_label"],
    "unit_type": record["unit_type"],
    "url": record["unit_url"],
    "sections": record["sections_read"],
    "status": "read",
    "read_record_id": record["id"],
    "blocked_reason": None,
})
plan["summary"]["required_units"] += 1
plan["summary"]["read_units"] += 1
entry["notes"] = (
    "Batch 6 public unit read; Health checks reuse the batch 4 Kubernetes probe "
    "record; ASVS V16 supplies the structured-logging invariant and failure/recovery "
    "evidence."
)
plan["updated"] = "2026-10-29"
plan["registry_sha256"] = hashlib.sha256(
    (ROOT / "edition/patterns/registry.v1.json").read_bytes()
).hexdigest()
save(path, plan)
print("metadata patch applied")

```

The patch:

- sets `invariant.state` and `failure_recovery.state` to `supported`,
  adds the owner claims, primary bindings to ASVS V16 and supporting bindings
  to ASVS 16.2.4/16.4.2/16.4.3 and the OTel stable/semistructured schema text;
- adds the ASVS auxiliary source declaration;
- moves `technical_coverage` and the registry technical/overall coverage to
  `partial-bounded` (the owner-units derivation requires this once the
  invariant is supported), updates the registry technical-owner state and the
  shared-page bounded count from 0 to 1;
- updates the owner-unit line fields for Structured Logging (113) and Audit
  Trail (157);
- increments `invariant_supported` 60→61, `failure_recovery_supported`
  48→49, `technical_partial_bounded` 28→29 and decrements
  `technical_partial` 90→89;
- adds the ASVS unit to the registry and source plan, increments the plan
  summary required/read units, and recomputes `registry_sha256`;
- leaves `decision_coverage` (`partial-bounded`), `review_state`,
  promotion and owner acceptance unchanged.

## Remaining metadata and review needs

- Refresh derived artifacts after the patch: atlas manifest, inventory,
  content revisions, page census, route index, coverage/reverse maps,
  semantic audit, candidate and review packets, delivery evidence, search
  pre-enrichment snapshot and search indexes.
- Request a fresh external review under the book/atlas gate. The historical
  logging review record at `b83f90e1...` predates this text; its page hash is
  stale. This lane is self-checked only.
- The owner page frontmatter `evidence_scope.source_ids` remains empty,
  although the body now carries an ASVS-bound claim. The card and owner-unit
  source declarations carry `src.otel` and `src.owasp-asvs`; the integrator
  may choose to normalize the owner-page scope.
- Owner acceptance, promotion, CI and merge permission are not claimed.
- No runtime logging, redaction, emitter-validation or incident-response test
  was executed.

## Limits

The binding covers one pinned ASVS 5.0.0 revision and four V16 requirements.
ASVS states what applications must verify; it does not establish that any
particular logging library enforces a schema, that a redaction canary exists,
or that incident response will purge or rotate within a bounded time. The
schema-version, compatibility-window, build-gate, purge, rotation and
notification steps are Tycho synthesis, not source claims. Coverage remains
`partial-bounded`; no promotion or owner acceptance is claimed.
