# B12 — Least Privilege alternative lane

Status: lane-local book edit, self-checked on 2026-10-29. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry stays `partial-bounded`; the preflight pass below depends on the
integrator applying the owner-unit patch.

## Lane coordinates

- Parent HEAD: `77bf3b8a0946d24fd7aabd84a74acf93fc9ffd10`.
- Branch: `b12-least-privilege`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b12-least-privilege`.
- Scope: V11/C11 `least-privilege.md` and the V09/C05
  `authorization-policy-and-least-privilege.md` owner section
  `## Least Privilege` only.

## Source binding

- Source: `src.owasp-asvs`, OWASP Application Security Verification Standard
  5.0.0, pinned PDF; the exact URL is recorded in
  `edition/patterns/reading-ledger.v1.json` under
  `read.batch6-asvs.2026-10-21`.
- Ledger record: `read.batch6-asvs.2026-10-21`; section
  `V2 Validation and Business Logic`; requirement 2.3.5, Level 3.
- Exact public quote, verbatim in the plain `pdftotext` extraction of the
  pinned PDF (the code block uses U+2011 non-breaking hyphens in
  `high‑value` and `multi‑user`, matching the PDF text layer):

      Verify that high‑value business logic flows require multi‑user approval to prevent
      unauthorized or accidental actions. This could include but is not limited to large
      monetary transfers, contract approvals, access to classified information, or safety
      overrides in manufacturing.

- Revision: `a2fa1bbe38f12cac86d3a0f0023327e9772201f65a7f741f282f5e785d268fc5`.
  Downloaded the pinned URL on 2026-10-29; the PDF bytes hash to this value,
  matching the ledger `content_sha256`, and the plain-text extraction contains
  the quote.
- The quote supports multi-user approval as a Level 3 control for high-value
  business logic flows and its examples. It does not compare that control with
  least privilege, does not define approver independence, and does not define
  approval evidence. The card and owner section label the substitution as a
  Tycho decision inference.

## Book edits

- `least-privilege.md`: the Competing alternative now states dual control with
  multi-user approval, the reversal conditions and the inference limit. Sources
  record requirement 2.3.5 and the pinned PDF SHA-256. The frontmatter route
  question is completed with `?` because the preflight requires a full question;
  `updated_at`, `source_inspection_date` and `content_review.reviewed_at`
  advance to 2026-10-29.
- `authorization-policy-and-least-privilege.md#least-privilege`: the owner
  section replaces the unsupported coarse-role sentence with the dual-control
  alternative, the exact requirement quote and a **Source boundary** paragraph.
  Frontmatter `updated_at` and `content_review.reviewed_at` advance to
  2026-10-29. The section heading remains at line 92 and no later owner-unit
  `line` on that page changes.
- No other book file, edition JSON, promotion or generated file is changed.

## Promotion check

No entry in `edition/patterns/sufficient-promotions.v1.json` binds either
edited file: all 26 promotions were checked against the current file SHA-256
values and against the least-privilege pattern ID; none matches. Least Privilege
remains unpromoted and this lane adds no promotion.

## Preflight

At the parent HEAD the baseline fails on the unbound alternative and on the
frontmatter question:

    FAIL: tycho.pattern.least-privilege
      - alternative: state 'partial', not supported
      - route_hints.questions missing or not a full question
    0/1 entries preflight clean

After the card edit, lane HEAD fails only because
`edition/patterns/owner-units.v1.json` is integrator-owned and still says
`alternative: partial`:

    FAIL: tycho.pattern.least-privilege
      - alternative: state 'partial', not supported
    0/1 entries preflight clean

A detached scratch worktree at the parent HEAD with the two book files copied
and the owner-unit patch below applied runs:

    python3 scripts/preflight_sufficient.py --pattern tycho.pattern.least-privilege
    PASS: tycho.pattern.least-privilege
    1/1 entries preflight clean

`python3 scripts/validate_pattern_owner_units.py` also passes there:
`PASS: owner units 145 entries, 145 units, 30 shared pages`.

`python3 scripts/check_boundary.py` and
`python3 scripts/check_markdown_line_length.py` pass on the lane worktree.

## Owner-unit metadata patch (integrator)

The only shared metadata needed is this patch. It reuses the admitted
`read.batch6-asvs.2026-10-21` ledger record and `src.owasp-asvs`; no ledger,
source-plan, registry or source-register change is required.

```python
import json
import re
from pathlib import Path

root = Path(".").resolve()
units = root / "edition/patterns/owner-units.v1.json"
data = json.loads(units.read_text(encoding="utf-8"))
entry = next(e for e in data["entries"]
             if e["pattern_id"] == "tycho.pattern.least-privilege")

batches = json.loads(
    (root / "edition/patterns/card-batches.v1.json").read_text(encoding="utf-8"))
card_path = next(item["card_path"]
                 for batch in batches["batches"]
                 for item in batch["entries"]
                 if item["pattern_id"] == "tycho.pattern.least-privilege")
card_text = (root / card_path).read_text(encoding="utf-8")
match = re.search(r"\*\*Competing alternative\.\*\*\s*(.+?)(?:\n\n|\Z)",
                  card_text, re.S)
assert match, "card alternative field missing"

owner_text = (root / entry["owner"]["path"]).read_text(encoding="utf-8")
squash = lambda value: " ".join(value.split())
owner_quote = ("When no narrow role can express the task, keep a task-capable "
               "identity and require independent approval by more than one "
               "principal before a high-value action executes, instead of "
               "splitting the entitlement.")
assert squash(owner_quote) in squash(owner_text), "owner quote not verbatim"

alt = entry["technical_evidence"]["alternative"]
alt["state"] = "supported"
alt["quote"] = owner_quote
alt["reason"] = (
    "Binds ASVS 5.0.0 requirement 2.3.5: high-value business logic flows "
    "require multi-user approval to prevent unauthorized or accidental "
    "actions. Using approval in place of narrower entitlements is a Tycho "
    "decision inference; ASVS does not compare the controls or define "
    "approver independence or approval evidence."
)
alt["binding"] = {
    "source_id": "src.owasp-asvs",
    "ledger_record": "read.batch6-asvs.2026-10-21",
    "section": "V2 Validation and Business Logic",
    "quote": ("Verify that high\u2011value business logic flows require "
              "multi\u2011user approval to prevent unauthorized or accidental "
              "actions. This could include but is not limited to large "
              "monetary transfers, contract approvals, access to classified "
              "information, or safety overrides in manufacturing."),
    "revision": "a2fa1bbe38f12cac86d3a0f0023327e9772201f65a7f741f282f5e785d268fc5",
}
entry["decision_evidence"]["competing_alternative"] = squash(match.group(1))
entry["notes"] = (
    "Alternative bound 2026-10-29 to ASVS 5.0.0 requirement 2.3.5; all four "
    "dimensions supported, coverage partial-bounded, no promotion; approver "
    "independence and approval evidence remain outside the source."
)
data["summary"]["alternative_supported"] += 1
units.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
print("owner-units patch applied")
```

The patch sets `alternative.state` to `supported`, adds the owner quote and
the binding to requirement 2.3.5, rewrites
`decision_evidence.competing_alternative` to match the card field, rewrites
the entry note, and increments `summary.alternative_supported` from 60 to 61.
It does not change `technical_coverage` (`partial-bounded`),
`decision_coverage` (`partial-bounded`) or `review_state`.

## Remaining metadata and review needs

- Refresh derived artifacts after applying the patch: page hashes and content
  revisions, inventory, atlas manifest, card batches, source-plan snapshot,
  section evidence, coverage/reverse maps, candidates, packets, semantic audit
  and other generated indexes. The lane intentionally does not touch them.
- The owner page frontmatter `evidence_scope.source_ids` lists only
  `src.owasp-rest-enrichment`, although the page now carries an ASVS-bound
  claim and already carried ASVS-bound pattern-atlas links. The lane leaves
  that pre-existing metadata for the integrator; the card and owner-unit
  source declarations carry `src.owasp-asvs`.
- Request a fresh external review under the book/atlas gate. The historical
  B18 binding audit is the finding this lane addresses, not a review of this
  text; this lane is self-checked only.
- Owner acceptance, promotion, CI and merge permission are not claimed.
- No runtime authorization, approval workflow or failure test was executed.

## Limits

The binding covers one Level 3 requirement in one pinned PDF revision. It does
not establish that multi-user approval bounds a credential's scope, that
approvers are independent, that approval evidence is retained, or that approval
remains practical under time pressure. The alternative is a decision
substitution, not an ASVS comparison, and coverage remains `partial-bounded`.
