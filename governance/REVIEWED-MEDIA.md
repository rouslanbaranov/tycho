# Reviewed binary media

Status: mandatory for binary files admitted to the repository.
Effective: 2026-11-01.

## Why this exists

`check_boundary.py` is a lexical guard for text. It cannot read JPEG, PNG, PDF,
or other binary media, so it fails closed. The reviewed-media manifest records an
explicit origin review and pins the exact bytes that were reviewed.

A manifest entry is not a waiver of source admission, independent review, owner
acceptance, or legal review. It does not make a file independently sourced.

## Admission

A file may be listed only when:

- it is public, project-supplied, or otherwise reusable under the project's terms;
- it contains no restricted employer-specific material;
- a human has visually reviewed the exact file;
- its SHA-256, review date, reviewer role, origin, and rights limits are recorded.

The manifest is `governance/reviewed-media.json`. Paths are repository-relative
POSIX paths. The manifest is intentionally small and reviewed like prose.

## How the check uses it

- Only files that cannot be decoded as UTF-8 are eligible for the skip.
- The file's current SHA-256 must equal the manifest value.
- A missing, duplicate, malformed, or stale entry fails the check.
- Text files remain fully scanned even if they appear in the manifest.
- Symlinks remain rejected; this mechanism covers regular binary files only.
- A hash match records an origin review, not a content scan.

## Updating

Replace a file only together with its manifest hash. Run:

```text
python3 scripts/check_boundary.py
python3 -m unittest tests.test_tycho_reviewed_media -v
```

Do not add a manifest entry to silence a finding in scanned text.
