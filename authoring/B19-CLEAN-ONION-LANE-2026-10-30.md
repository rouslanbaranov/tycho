# B19 — Clean / Onion review-label lane

Status: lane-local book edit, self-checked on 2026-10-30. No shared edition metadata,
promotion, generated artifact or owner acceptance is included. The entry remains
`partial-bounded`; preflight still fails on the inline card path until the integrator
applies the metadata patch and splits the card. The lane commit edits only the two book
files listed below and this note.

## Lane coordinates

- Parent HEAD: `7f78402b02ae483112fba1faf4c74b77468b5cff` (`7f78402b`).
- Branch: `b19-clean`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b19-clean`.
- Scope: the V02/C01 owner section `### Clean-Onion Architecture` and the inline V11/C01
  card `### Clean / Onion Architecture` only.
- The card remains inline in the V11/C01 `README.md`; the integrator owns the split and
  the `card_path` registration.
- Single-entry lane; no other entry, shared owner page, promotion or generated file is
  changed.

## Findings and book edits

1. `failure_recovery` — the dependency-test and adapter remedy is now labeled Tycho
   guidance in both files. The owner sentence reads: "That dependency-test and adapter
   remedy is Tycho guidance, not a source claim; the source describes keeping outer data
   structures out of inner circles, not a specific test or adapter design." The card
   failure/recovery field reads: "Tycho guidance, not a source claim: recover with an
   enforceable dependency test and a deliberate adapter, not another layer name; the
   technical owner section states the remaining limits."
2. `invariant` — the automated build check is now labeled Tycho guidance in the owner
   section: "The automated build check is Tycho guidance, not a source claim: the source
   states the inward rule, not an enforcement mechanism."
3. `alternative` — the Fowler mapper/Hexagonal sentence is now quoted verbatim in the
   owner section and in the card's competing-alternative field. The card `Sources` field
   points to the quote and records the article's one-author limit.
4. Card contraindications — the first two conditions now match the owner Limits: mapping
   overhead dominating a small CRUD application, and ports with no genuinely different
   implementations. The remaining conditions are explicitly labeled "Tycho guidance, not
   a source claim."

## Source binding and exact quotes

Fowler quote, served page
https://martinfowler.com/bliki/PresentationDomainDataLayering.html, section
"Presentation Domain Data Layering":

> A common variation is to arrange things so that the domain does not depend on its data
> sources by introducing a mapper between the domain and data source layers. This approach
> is often referred to as a Hexagonal Architecture.

- Existing record: `read.fowler-layering.2026-10-21`, revision
  `bb249131feb914aa939976528d7d28ce4063e6413fc1038826d9e80bf12e0444`.
- The record covers the section. No new source, ledger record or source-plan unit is
  added.
- The quote was re-checked in the served page on 2026-10-30. The existing record and
  revision are retained; the lane makes no new source-completeness claim.

Clean Architecture binding quotes retained:

- Invariant: "Nothing in an inner circle can know anything at all about something in an
  outer circle." Section "The Dependency Rule"; record
  `read.clean-architecture.2026-10-21`; revision
  `ca86d5653333b894f0a525b2bc96e4a31e013138a8096d27742817296877554d`.
- Failure/recovery: "So when we pass data across a boundary, it is always in the form that
  is most convenient for the inner circle." Section "What data crosses the boundaries";
  same record and revision.
- Those source sentences support the inward rule and the inner-circle data form. They do
  not prescribe an automated build check, a dependency test or an adapter design; the
  labels above keep those prescriptions Tycho guidance.

## Hashes

Canonical SHA-256 (historical view used by `edition/content-revisions.json`):

- Owner before:
  `c4d89b0ae4be9cf3cac89d2b0c951066bde5704d626c5e7503446e801d949011`
- Owner after:
  `293dc996e1432c34d0601723a6f02e9f81571833fc50fed135557abfcc36dc67`
- Card before:
  `0c5c26415aaa4a9d7744579492125d53f10e844bc85e90a881674c28310fed3f`
- Card after:
  `73d194f07d191f2e9905a5cd837de6515262f92e78ddb0ce4f1e4be464766f18`

The before values are the `baseline_sha256` values in
`edition/directory-migration.json`, not the raw HEAD hashes.
`edition/content-revisions.json` authorization compares against those baselines.

## Preflight and validation

Lane worktree before the shared metadata patch:

    FAIL: tycho.pattern.clean-onion-architecture
      - alternative: source src.fowler-layering absent from source_support
      - card_path missing or absent
    0/1 entries preflight clean

`src.fowler-layering` is bound by the `alternative` dimension but absent from
`source_support`; the inline card has no `card_path`. The lane cannot fix either without
editing shared JSON or splitting the card.

A detached scratch worktree at parent HEAD with the two book files copied and the patch
below applied reports only:

    FAIL: tycho.pattern.clean-onion-architecture
      - card_path missing or absent
    0/1 entries preflight clean

The same scratch tree passes:

- `python3 scripts/validate_pattern_owner_units.py` — PASS.
- `python3 scripts/validate_pattern_cards.py` — PASS.
- `python3 scripts/validate_pattern_sources.py` — PASS.
- `python3 scripts/check_boundary.py` — PASS; independent-origin review still required.
- `python3 scripts/validate_claim_references.py` — PASS.
- `python3 scripts/validate_directory_migration.py` — PASS.

The lane worktree without the patch reports `owner-units-alternative` and
`directory-baseline-payload-drift`; both clear when the patch is applied.

`python3 scripts/check_markdown_line_length.py` still fails on
`book/volumes/v11-pattern-atlas/c03-messaging-integration/request-reply-messaging.md:86-87`
at parent HEAD; those lines are outside this lane. All added lines in the two book files
are at most 100 characters.

`python3 scripts/validate_pattern_atlas.py` fails at `atlas-document-sha` in the scratch
tree because the atlas manifest is derived and this lane does not regenerate it.

## Metadata needs (integrator)

### `edition/patterns/owner-units.v1.json`

Entry `tycho.pattern.clean-onion-architecture`:

- `technical_evidence.invariant.reason`: state that the source supports the inward rule
  and that the automated build check is Tycho guidance.
- `technical_evidence.failure_recovery.reason`: state that the source supports the
  inner-circle data form and that the dependency-test/adapter remedy is Tycho guidance.
- `technical_evidence.alternative.quote`: set to the Fowler mapper/Hexagonal quote
  above, which is now verbatim in the owner section.
- `technical_evidence.alternative.binding.quote`: top-to-bottom sentence plus the
  mapper/Hexagonal quote, both from the same Fowler section.
- `technical_evidence.alternative.reason`: mention the mapper/Hexagonal quote.
- `source_support.auxiliary`: add
  `{"source_id": "src.fowler-layering", "ledger_record":
  "read.fowler-layering.2026-10-21", "revision": "bb249..."}`.
- `notes`: record the 2026-10-30 label/quote change and retain `partial-bounded`.
- `decision_evidence.competing_alternative`: set to the card field verbatim. The tested
  patch extracts it with `card_field` to avoid transcription drift.
- `owner.line` remains 171; the patch recomputes it defensively.

### `edition/content-revisions.json`

Add one revision with `issue: 540`, `authorized_at: "2026-10-30"`, authorization
"B19 clean/onion review labels", and these `directory_documents`:

- Owner path, previous `c4d89...`, current `293dc...`.
- Card path, previous `0c5c2...`, current `73d19...`.

### `edition/patterns/card-batches.v1.json`

Split the inline card to a dedicated page, set `card_path`, and keep the V11/C01 anchor.
The lane does not split the card. After the split, rerun preflight; no `card_path` error
should remain.

### Derived artifacts

The integrator must regenerate the atlas manifest, inventory, route index and any other
derived artifact affected by the two book-file hashes. The lane does not edit
`edition/atlas-manifest.json`, `edition/inventory.json`,
`generated/route-index.v1.json` or promotions.

## Tested metadata patch

Run from the repository root after the lane commit. It edits only shared metadata.

```python
import json
import sys
from pathlib import Path

ROOT = Path(".").resolve()
sys.path.insert(0, str(ROOT / "scripts"))
from directory_paths import HistoricalView, sha as text_sha
from validate_pattern_owner_units import card_field, card_section_text

PATTERN = "tycho.pattern.clean-onion-architecture"
OWNER_REL = (
    "book/volumes/v02-application-boundaries-and-contracts/"
    "c01-layered-modular-and-ports-and-adapters-design/"
    "layered-hexagonal-ports-and-adapters.md"
)
CARD_REL = "book/volumes/v11-pattern-atlas/c01-application-boundaries/README.md"
OWNER = ROOT / OWNER_REL
CARD = ROOT / CARD_REL
OWNER_BASELINE = (
    "c4d89b0ae4be9cf3cac89d2b0c951066bde5704d626c5e7503446e801d949011"
)
CARD_BASELINE = (
    "0c5c26415aaa4a9d7744579492125d53f10e844bc85e90a881674c28310fed3f"
)
FOWLER_REVISION = (
    "bb249131feb914aa939976528d7d28ce4063e6413fc1038826d9e80bf12e0444"
)
MAPPER_QUOTE = (
    "A common variation is to arrange things so that the domain does not depend on its "
    "data sources by introducing a mapper between the domain and data source layers. "
    "This approach is often referred to as a Hexagonal Architecture."
)
TOP_DOWN = (
    "The dependencies generally run from top to bottom through the layer stack: "
    "presentation depends on the domain, which then depends on the data source."
)


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def save(path, data):
    text = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    path.write_text(text, encoding="utf-8")


units = load(ROOT / "edition/patterns/owner-units.v1.json")
entry = next(e for e in units["entries"] if e["pattern_id"] == PATTERN)
tech = entry["technical_evidence"]

tech["invariant"]["reason"] = (
    "Source states that inner circles must not know outer circles; the automated "
    "build check is Tycho guidance, not a source claim."
)
tech["failure_recovery"]["reason"] = (
    "Source supports keeping outer data structures out of inner circles; the "
    "dependency-test and adapter remedy is Tycho guidance, not a source claim."
)
tech["alternative"]["quote"] = MAPPER_QUOTE
tech["alternative"]["reason"] = (
    "Quotes the mapper variation between the domain and data source layers and its "
    "Hexagonal Architecture label; the top-to-bottom framing is in the same source "
    "section."
)
tech["alternative"]["binding"]["quote"] = TOP_DOWN + " " + MAPPER_QUOTE

entry["source_support"].setdefault("auxiliary", [])
if not any(a.get("source_id") == "src.fowler-layering"
           for a in entry["source_support"]["auxiliary"]):
    entry["source_support"]["auxiliary"].append({
        "source_id": "src.fowler-layering",
        "ledger_record": "read.fowler-layering.2026-10-21",
        "revision": FOWLER_REVISION,
    })
entry["notes"] = (
    "Alternative binding extended 2026-10-30 with the Fowler mapper/Hexagonal "
    "sentence. Invariant and failure/recovery reasons state that the automated build "
    "check and the dependency-test/adapter remedy are Tycho guidance. Coverage remains "
    "partial-bounded; no promotion."
)

card_text = card_section_text(
    CARD.read_text(encoding="utf-8"), "clean-onion-architecture"
)
entry["decision_evidence"]["competing_alternative"] = card_field(
    card_text, "Competing alternative"
)

owner_lines = OWNER.read_text(encoding="utf-8").splitlines()
for item in units["entries"]:
    if item["owner"]["path"] == OWNER_REL:
        heading = "### " + item["owner"]["heading"]
        item["owner"]["line"] = next(
            n for n, line in enumerate(owner_lines, 1) if line == heading
        )
save(ROOT / "edition/patterns/owner-units.v1.json", units)

view = HistoricalView(ROOT)
revisions = load(ROOT / "edition/content-revisions.json")
new_documents = []
for rel, previous in ((OWNER_REL, OWNER_BASELINE),
                      (CARD_REL, CARD_BASELINE)):
    current = text_sha(view.read_text(rel))
    for revision in revisions["revisions"]:
        for item in revision.get("directory_documents", []):
            if item.get("path") == rel and item.get("current_sha256") == current:
                raise SystemExit("revision already recorded: " + rel)
    new_documents.append({
        "path": rel,
        "previous_sha256": previous,
        "current_sha256": current,
    })
revisions["revisions"].append({
    "issue": 540,
    "authorized_at": "2026-10-30",
    "authorization": "B19 clean/onion review labels",
    "directory_documents": new_documents,
    "source_blocks": [],
    "enrichment_documents": [],
    "enrichment_additions": [],
    "enrichment_baselines": [],
})
save(ROOT / "edition/content-revisions.json", revisions)
print("patched clean/onion metadata")
```

## Commit scope

The lane commit contains this note and the two book files only:

- The V02/C01 owner file `layered-hexagonal-ports-and-adapters.md`.
- The V11/C01 inline card file `README.md`.

No shared JSON, promotion or generated file is in the lane commit.
