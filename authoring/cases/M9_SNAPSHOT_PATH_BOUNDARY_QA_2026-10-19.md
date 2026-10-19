# M9 E16-08 — Snapshot-Bound Case Links and Symlink Guard

**2026-10-19 · Review state:** implemented guard and added regression tests, but full GitHub checkout suite still awaiting actual execution.

## Reason for change

The M9 case/index checker formerly resolved relative Markdown links and merely asked whether the resulting file **existed**. A link such as `../../../private.md` from `book/cases/` could resolve to a file **outside the selected repository snapshot** and still count as valid when that file existed. Likewise, a symlink in `book/cases/` could point outside its intended collection while appearing to be an indexed `.md` file.

The validator now resolves index paths and referenced Markdown targets and enforces:

- README-indexed case and decision files must stay under the selected `book/cases` collection, even through symlinks.
- Every relative Markdown link inside those pages must resolve **within the selected root**, which may include shared `sources/` and `authoring/` files under that same checkout.
- Internal relative link targets must exist. Remote HTTPS URLs are not locally dereferenced and still require separate real source/permission checks.
- A valid link inside the root must not be rejected simply because it points to a shared `sources/` document outside the case subdirectory.

## Regression coverage added

`tests/test_m9_validator_root_and_status.py` now constructs synthetic 20-case collections and checks: valid in-snapshot source references, an existing relative path escaping the selected root, and a case index symlink to a real outside file.

## Actually executed isolated logic probe

A standalone Python 3.13.5 local probe reproduced the changed `read_case_catalog` path-normalization guards against a **synthetic temporary checkout**, and observed:

| Probe | Observed |
|---|---|
| 20 synthetic case files with valid `../../sources/public.md` link | PASS: accepted |
| Existing `../../../private.md` outside selected root | PASS: rejected |
| Indexed `alias.md` symlink resolving outside the case collection | PASS: rejected |

**Boundary:** this is a real run of independently reconstructed guard logic, **not** execution of the full, byte-verified `scripts/validate_m9_cases.py` file from a GitHub checkout. Tests committed to the repository must still be run and their actual exit code recorded before #121 can use them as complete validation evidence.

Suggested pinned-checkout commands:

```bash
python3 -m unittest discover -s tests -p 'test_m9_validator*.py' -v
python3 scripts/validate_m9_cases.py --self-test --root .
python3 scripts/validate_m9_cases.py --root .
```

This rejects only dangerous **filesystem path relationships**; it cannot validate a publisher's copyright license, DNS resolution, source author's claim, or whether an external page is trustworthy. Tycho still needs independent source and case review before M9 acceptance.
