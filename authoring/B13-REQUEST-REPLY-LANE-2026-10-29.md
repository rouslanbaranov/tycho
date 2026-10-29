# B13 — Request-Reply Messaging alternative lane

Status: lane-local book edit, self-checked on 2026-10-29. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry stays `partial-bounded`; the preflight pass below depends on the
integrator applying the metadata patch.

## Lane coordinates

- Parent HEAD: `7f5f23aaffa3054901737a6aabad3c025ad25615`.
- Branch: `b13-request-reply`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b13-request-reply`.
- Scope: V11/C03 `request-reply-messaging.md` and the V04/C06
  `request-reply-messaging.md` owner section `# Request-Reply Messaging` only.
- This is a single-entry lane; no other entry, shared owner page or promotion is
  changed.

## Source binding

- Primary source remains `src.enterprise-integration`, Request-Reply — pattern
  page, ledger record `read.batch2-request-reply.2026-10-21`. Its mechanism,
  invariant and failure/recovery bindings are unchanged.
- Alternative source: `src.microservices-patterns`, Messaging — pattern page,
  `https://microservices.io/patterns/communication-style/messaging.html`,
  retrieved 2026-10-29.
- New ledger record: `read.microservices-communication-messaging.2026-10-29`;
  sections read: Context, Forces, Problem, Solution, Examples, Resulting
  context, Related patterns, See also.
- Exact public quote, verbatim in the canonical visible text of the served page:

  > The RPI pattern is an alternative pattern

  The served list item has no terminal period; the period in the owner text is
  outside the quotation.
- Supporting exact quotes, all from `Resulting context`:

  > Loose runtime coupling since it decouples the message sender from the consumer

  > Improved availability since the message broker buffers messages until the
  > consumer is able to process them

  > Additional complexity of message broker, which must be highly available

  > Request/reply-style communication is more complex

- Revision: `491719296be7ab61e96cf8c59c35dab87a8d9a6d0f4d5d8641f235e61bf5369d`.
  The canonical visible text hashes to this value. The page was fetched twice on
  2026-10-29 and both runs produced the same hash. The extraction is
  `python3 scripts/source_content_hash.py` over the served HTML.
- The new unit is a public source page from an already admitted source
  (`src.microservices-patterns` is in `sources/register.json`). Under AGENTS rule
  28, this new public unit is authorized once the existing source registration
  and the ledger, source-plan and registry unit records are in place. The lane
  does not edit those shared JSON files; the metadata patch below supplies them.
- Limit: the page names RPI as an alternative and records messaging's benefits
  and costs. It does not state a request-budget, blocking or latency rule. The
  selection conditions are Tycho synthesis. Its examples were not executed, and
  the RPI page was not read.

## Book edits

- V11/C03 card `request-reply-messaging.md`: the **Competing alternative** field
  now binds the microservices.io Messaging page, states its explicit alternative
  label and its four Resulting-context trade-offs, and labels the request-budget
  selection as Tycho synthesis. The **Sources** field adds the new record, URL,
  revision and the page's limits. `evidence_scope.source_ids` adds
  `src.microservices-patterns`. `source_inspection_date` advances to
  2026-10-29; `content_review.reviewed_at` and `updated_at` were already
  2026-10-29.
- V04/C06 owner `request-reply-messaging.md#request-reply-messaging`: the
  **Alternative** paragraph carries the same bound claims and exact quotes; the
  **Limits** paragraph separates the primary page's blocking comparison from the
  new page's alternative label and trade-offs; a **Sources** paragraph records
  both records, URLs and revisions. The invariant sentence is now a separate
  sentence beginning with the source's capital `The request thread awaiting…`,
  so the existing binding is verbatim again. `evidence_scope.source_ids` adds
  `src.microservices-patterns`; `source_inspection_date` advances to
  2026-10-29; `content_review.reviewed_at` and `updated_at` were already
  2026-10-29.
- The owner heading remains at line 46; the owner-unit `line` field must move
  from 45 to 46 because one source-id line was added to the frontmatter. No
  later owner-unit line on this dedicated page is affected.
- No other book file, edition JSON, promotion or generated file is changed by
  this lane.

## Promotion check

`edition/patterns/sufficient-promotions.v1.json` contains 27 promotions. Neither
edited file's SHA-256 matches any `card_sha256` or `owner_page_sha256`, and no
promotion names `tycho.pattern.request-reply-messaging`. The entry was already
suspended on 2026-10-29 when the owner note moved to a dedicated page. This lane
does not invalidate, rebind or add a promotion.

Lane file hashes:

- Card: `20eae2431da8143d56d483ac664ad8279f9e6a6261d67bbaff31372bed224210`
- Owner: `f8a2fa968e597b7225092700ebfa854999f599b8a38a76b997b329662da3db7c`

## Preflight

At parent HEAD the baseline fails on the invariant quote and on the unbound
alternative:

    FAIL: tycho.pattern.request-reply-messaging
      - invariant: owner quote not verbatim in owner section
      - alternative: state 'partial', not supported
    0/1 entries preflight clean

After the two book edits, the lane worktree fails only because
`edition/patterns/owner-units.v1.json` is integrator-owned and still says
`alternative: partial`:

    FAIL: tycho.pattern.request-reply-messaging
      - alternative: state 'partial', not supported
    0/1 entries preflight clean

A detached scratch worktree at parent HEAD with the two book files copied and
the metadata patch below applied runs:

    PASS: tycho.pattern.request-reply-messaging
    1/1 entries preflight clean

The same scratch tree also passes:

- `python3 scripts/validate_pattern_owner_units.py` — PASS: owner units 145
  entries, 145 units, 30 shared pages.
- `python3 scripts/validate_pattern_sources.py` — PASS: source plan 145 entries;
  168 read; 139 ledger records.
- `python3 scripts/check_boundary.py` — PASS: configured lexical boundary
  checks; independent-origin review still required.
- `python3 scripts/check_markdown_line_length.py` — PASS: V11 prose <=100; 145
  exact owner-link exceptions.
- `python3 scripts/validate_pattern_cards.py` — PASS: pattern cards 11 batch(es),
  145 entries.
- `python3 scripts/validate_claim_references.py` — PASS: traceable claims,
  inventory IDs, evidence status and pinned references.

`python3 scripts/validate_pattern_atlas.py` still fails at
`atlas-registry-hash` until the integrator refreshes the atlas manifest and the
other derived artifacts. This is a derived-artifact refresh, not a content
failure. The lane intentionally does not touch generated files.

## Metadata patch (integrator)

Run this from the repository root. It edits only shared metadata; the two book
files are already in the lane commit.

~~~python
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(".").resolve()
RECORD_ID = "read.microservices-communication-messaging.2026-10-29"
SOURCE_ID = "src.microservices-patterns"
REVISION = "491719296be7ab61e96cf8c59c35dab87a8d9a6d0f4d5d8641f235e61bf5369d"
UNIT = "Messaging — pattern page"
URL = "https://microservices.io/patterns/communication-style/messaging.html"
SECTIONS = [
    "Context",
    "Forces",
    "Problem",
    "Solution",
    "Examples",
    "Resulting context",
    "Related patterns",
    "See also",
]
CARD = ("book/volumes/v11-pattern-atlas/c03-messaging-integration/"
        "request-reply-messaging.md")
PATTERN = "tycho.pattern.request-reply-messaging"


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def save(path, data):
    (ROOT / path).write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def squash(value):
    return " ".join(value.split())


# Owner units
path = "edition/patterns/owner-units.v1.json"
units = load(path)
entry = next(e for e in units["entries"] if e["pattern_id"] == PATTERN)
alt = entry["technical_evidence"]["alternative"]
card_text = (ROOT / CARD).read_text(encoding="utf-8")
match = re.search(r"\*\*Competing alternative\.\*\*\s*(.+?)(?:\n\n|\Z)",
                  card_text, re.S)
assert match, "card alternative field missing"
alternative = squash(match.group(1))
alt["state"] = "supported"
alt["quote"] = (
    "The bound Messaging page names the RPI pattern as an alternative and "
    "records messaging's loose runtime coupling and buffered availability "
    "against the added broker complexity and more complex request/reply "
    "communication."
)
alt["reason"] = (
    "Binds the Messaging page's Related patterns sentence that names RPI as an "
    "alternative, plus its Resulting context record of loose runtime coupling, "
    "buffered availability, broker complexity and more complex request/reply "
    "communication. The page states no request-budget or blocking rule; "
    "preferring direct RPI under a request budget is Tycho synthesis."
)
alt["binding"] = {
    "source_id": SOURCE_ID,
    "ledger_record": RECORD_ID,
    "section": "Related patterns",
    "quote": "The RPI pattern is an alternative pattern",
    "revision": REVISION,
}
alt["supporting_bindings"] = [
    {
        "source_id": SOURCE_ID,
        "ledger_record": RECORD_ID,
        "section": "Resulting context",
        "quote": "Loose runtime coupling since it decouples the message sender "
                 "from the consumer",
        "revision": REVISION,
    },
    {
        "source_id": SOURCE_ID,
        "ledger_record": RECORD_ID,
        "section": "Resulting context",
        "quote": "Improved availability since the message broker buffers "
                 "messages until the consumer is able to process them",
        "revision": REVISION,
    },
    {
        "source_id": SOURCE_ID,
        "ledger_record": RECORD_ID,
        "section": "Resulting context",
        "quote": "Additional complexity of message broker, which must be highly "
                 "available",
        "revision": REVISION,
    },
    {
        "source_id": SOURCE_ID,
        "ledger_record": RECORD_ID,
        "section": "Resulting context",
        "quote": "Request/reply-style communication is more complex",
        "revision": REVISION,
    },
]
owner_text = (ROOT / entry["owner"]["path"]).read_text(encoding="utf-8")
entry["owner"]["line"] = next(
    number for number, line in enumerate(owner_text.splitlines(), 1)
    if line == "# " + entry["owner"]["heading"]
)
entry["decision_evidence"]["competing_alternative"] = alternative
entry["source_support"]["auxiliary"] = [
    {
        "source_id": SOURCE_ID,
        "ledger_record": RECORD_ID,
        "revision": REVISION,
    }
]
entry["notes"] = (
    "Alternative bound 2026-10-29 to the microservices.io Messaging page, "
    "which names RPI as an alternative and records messaging's loose runtime "
    "coupling and buffered availability against broker complexity and more "
    "complex request/reply communication; all four dimensions supported, "
    "coverage partial-bounded, no promotion; request-budget and blocking "
    "selection remain Tycho synthesis."
)
units["summary"]["alternative_supported"] += 1
save(path, units)

# Reading ledger
path = "edition/patterns/reading-ledger.v1.json"
ledger = load(path)
assert not any(r["id"] == RECORD_ID for r in ledger["records"])
ledger["records"].append({
    "id": RECORD_ID,
    "source_id": SOURCE_ID,
    "unit_url": URL,
    "unit_label": UNIT,
    "unit_type": "pattern-page",
    "access_date": "2026-10-29",
    "access_method": "public HTTP fetch; served text/html inspected",
    "sections_read": SECTIONS,
    "sections_not_read": [
        "linked child pages",
        "navigation and unrelated chrome",
        "code examples not reproduced",
    ],
    "tables_figures": [
        "no tables or figures in the inspected sections",
    ],
    "license_notes": (
        "Public page; cite short excerpts and paraphrase; do not mirror."
    ),
    "claims_supported": [
        "The RPI pattern is an alternative pattern.",
        "Messaging provides loose runtime coupling and buffered availability "
        "at the cost of broker complexity and more complex request/reply "
        "communication.",
    ],
    "claims_not_supported": [
        "linked pages",
        "implementation behavior",
        "independent reproduction or benchmark",
    ],
    "limitations": (
        "One pattern page; examples were not executed; the RPI page was not "
        "read."
    ),
    "content_sha256": REVISION,
    "read_scope": (
        "complete publicly served page as returned by fetch, excluding "
        "navigation and linked pages"
    ),
    "reviewer": "Automated authoring agent",
    "status": "read",
})
ledger["updated"] = "2026-10-29"
save(path, ledger)

# Registry
path = "edition/patterns/registry.v1.json"
registry = load(path)
pattern = next(p for p in registry["patterns"] if p["id"] == PATTERN)
assert not any(u["source_id"] == SOURCE_ID for u in pattern["source_units"])
pattern["source_units"].append({
    "source_id": SOURCE_ID,
    "unit": UNIT,
    "status": "read",
})
pattern["notes"] = (
    "Promotion and owner acceptance suspended 2026-10-29 because the "
    "Request-Reply Messaging owner note moved to a dedicated page and the card "
    "backlink changed; all four technical dimensions remain supported and "
    "review-ready; the alternative is bound to the microservices.io Messaging "
    "page; coverage partial-bounded; a fresh external review must pass before "
    "restoration."
)
save(path, registry)

# Source plan
path = "edition/patterns/source-plan.v1.json"
plan = load(path)
entry = next(e for e in plan["entries"] if e["pattern_id"] == PATTERN)
assert not any(u["source_id"] == SOURCE_ID for u in entry["required_units"])
entry["required_units"].append({
    "source_id": SOURCE_ID,
    "unit": UNIT,
    "unit_type": "pattern-page",
    "url": URL,
    "sections": SECTIONS,
    "status": "read",
    "read_record_id": RECORD_ID,
    "blocked_reason": None,
})
plan["summary"]["required_units"] += 1
plan["summary"]["read_units"] += 1
plan["summary"]["ledger_records"] += 1
plan["registry_sha256"] = hashlib.sha256(
    (ROOT / "edition/patterns/registry.v1.json").read_bytes()
).hexdigest()
plan["updated"] = "2026-10-29"
save(path, plan)
print("metadata patch applied")
~~~

The patch:

- sets `alternative.state` to `supported`, adds the owner claim, the binding to
  `Related patterns` and four supporting bindings at `Resulting context`;
- updates the owner-unit `line` to 46 and rewrites
  `decision_evidence.competing_alternative` from the card field;
- adds the auxiliary source declaration;
- increments `summary.alternative_supported` from 61 to 62;
- adds the new ledger record, registry source unit and source-plan unit;
- increments the source-plan summary counts and recomputes
  `registry_sha256`;
- leaves `technical_coverage`, `decision_coverage`, `review_state`, promotion
  and owner acceptance unchanged.

## Remaining metadata and review needs

- Refresh derived artifacts after the patch: atlas manifest, inventory, content
  revisions, page census, route index, coverage/reverse maps, semantic audit,
  candidate and review packets, delivery evidence and search indexes. The lane
  intentionally does not touch them.
- The ledger record, source-plan unit and registry unit must be applied
  together: `validate_pattern_sources.py` requires registry `source_units` to
  equal the source-plan units and the plan's `registry_sha256` to match the
  registry file.
- Request a fresh external review under the book/atlas gate. The historical
  Request-Reply reviews predate this alternative text; this lane is
  self-checked only.
- Owner acceptance, promotion, CI and merge permission are not claimed.
- No runtime request-reply, broker, timeout or failure test was executed.

## Limits

The binding covers one served Messaging page at one pinned revision. Its
"alternative pattern" sentence is a related-pattern label, not a selection rule.
The request-budget, blocking, availability and broker-complexity comparison in
the card is Tycho synthesis from that label and the page's Resulting-context
trade-offs. The page is a rolling public page; the revision pins the 2026-10-29
representation, not future edits. Coverage remains `partial-bounded`.
