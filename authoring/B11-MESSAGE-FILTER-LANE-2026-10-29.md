# B11 — Message Filter failure/recovery lane

Status: lane-local book edit, self-checked on 2026-10-29. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry stays `partial-bounded`; the preflight pass below depends on the
integrator applying the owner-unit patch.

## Lane coordinates

- Parent HEAD: `77abedb9c3d1444c6f8e02d041dcff16edf7ffb5`.
- Branch: `b11-message-filter`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b11-message-filter`.
- Scope: V11/C03 `message-filter.md` and the V04/C06 `message-selection.md`
  owner section `### Message Filter` only.

## Source binding

- Source: `src.enterprise-integration`, public page
  https://www.enterpriseintegrationpatterns.com/patterns/messaging/Filter.html.
- Ledger record: `read.batch2-filter.2026-10-21`; sections read:
  `Message Filter` and `Example: RabbitMQ Bindings`.
- Exact public quote, verbatim in the served page:

      If the message content does not match the criteria, the message is discarded.

- Revision: `899fcd8bbb8d91b9a0985314998a4707c1b4e0b34aa79a2821149c861d53db2c`.
  A served-page representation with this SHA-256 contains the quote; the
  recorded ledger `content_sha256` is the same value.
- The quote supports the discard outcome only. The lane does not assert a
  recovery, audit, retention or dead-letter behavior from this source.

## Book edits

- `message-filter.md`: the failure/recovery field now quotes the discard
  sentence, states the absent disposition/audit/retention/recovery, labels the
  recovery design as Tycho synthesis, records the revision in Sources, and
  advances `updated_at`, `source_inspection_date` and
  `content_review.reviewed_at` to 2026-10-29.
- `message-selection.md#message-filter`: the owner section carries the same
  bounded claim and revision. It keeps exactly 11 body lines, so every later
  owner-unit `line` on that page remains valid.
- No other book file, edition JSON, promotion or generated file is changed.

## Promotion check

No entry in `edition/patterns/sufficient-promotions.v1.json` binds either
edited file or the shared owner page: all 25 promotions were checked against
the owner-unit owner paths and card paths. Message Filter remains suspended and
unpromoted. This lane adds no promotion.

## Preflight

Lane HEAD alone fails because `edition/patterns/owner-units.v1.json` is
integrator-owned and still says `failure_recovery: partial`:

    FAIL: tycho.pattern.message-filter
      - failure_recovery: state 'partial', not supported

A detached scratch worktree at the same HEAD, with the two book files copied
and the owner-unit patch below applied, runs:

    python3 scripts/preflight_sufficient.py --pattern tycho.pattern.message-filter
    PASS: tycho.pattern.message-filter
    1/1 entries preflight clean

`python3 scripts/validate_pattern_owner_units.py` also passes there:
`PASS: owner units 145 entries, 145 units, 30 shared pages`.

## Owner-unit metadata patch (integrator)

The only shared metadata needed is this patch. It reuses the admitted
`read.batch2-filter.2026-10-21` ledger record and `src.enterprise-integration`;
no ledger, source-plan, registry or source-register change is required.

```python
import json
from pathlib import Path

path = Path("edition/patterns/owner-units.v1.json")
data = json.loads(path.read_text(encoding="utf-8"))
entry = next(e for e in data["entries"]
             if e["pattern_id"] == "tycho.pattern.message-filter")
fr = entry["technical_evidence"]["failure_recovery"]
fr["state"] = "supported"
fr["quote"] = ("If content does not match, the message is discarded and "
               "produces no downstream output.")
fr["reason"] = (
    "Binds the served page's discard outcome. The page states no "
    "rejected-message disposition, audit record, retention or recovery "
    "path; the claim is limited to the discard consequence and the "
    "absence of a stated recovery, and no recovery mechanism is asserted."
)
fr["binding"] = {
    "source_id": "src.enterprise-integration",
    "ledger_record": "read.batch2-filter.2026-10-21",
    "section": "Message Filter",
    "quote": ("If the message content does not match the criteria, "
              "the message is discarded."),
    "revision": ("899fcd8bbb8d91b9a0985314998a4707c1b4e0b34aa79a2821"
                 "149c861d53db2c"),
}
entry["notes"] = (
    "Failure/recovery binding to the served Message Filter discard "
    "sentence added 2026-10-29; all four dimensions supported, coverage "
    "partial-bounded, no promotion; recovery remains unstated and out of "
    "scope."
)
data["summary"]["failure_recovery_supported"] += 1
path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
```

The patch sets `failure_recovery.state` to `supported`, adds the binding to
the discard sentence, rewrites the entry note, and increments
`summary.failure_recovery_supported` from 47 to 48. It does not change
`technical_coverage` (`partial-bounded`), `decision_coverage`
(`partial-bounded`) or `review_state`.

## Remaining metadata and review needs

- Refresh derived artifacts after applying the patch: page hashes, inventory,
  atlas manifest, card batches, candidates, packets, semantic audit and other
  generated indexes. The lane intentionally does not touch them.
- Request a fresh external review under the book/atlas gate. The historical
  Message Filter reviews predate this text; this lane is self-checked only.
- Owner acceptance, promotion, CI and merge permission are not claimed.
- No runtime filter, deployment or failure test was executed. The recovery
  paragraph is explicitly labelled Tycho synthesis.

## Limits

The binding covers one served page at one recorded revision. It does not
recover the publisher-withheld book text, does not establish a dead-letter or
retention contract, and does not turn the filter's absent recovery into a
supported recovery mechanism. Coverage remains `partial-bounded`.
