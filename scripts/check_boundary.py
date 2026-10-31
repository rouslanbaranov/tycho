#!/usr/bin/env python3
"""Limited lexical guard; independent-origin review is still mandatory.

Git-ignored artifacts are not committed content and are skipped. Tracked files and
untracked non-ignored files remain scanned.

Binary media cannot be read as text. It is admitted only through
governance/reviewed-media.json, which pins the exact SHA-256 of a manually
reviewed file. A matching hash authorizes a skip for that exact byte sequence;
it is not a content scan, independent review or owner acceptance.
"""
from datetime import date
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PRIVATE_LINK = re.compile(r"(?i)(?:file:/{2}|https?://(?:localhost|127\.0\.0\.1)(?=[:/\s]|$))")
MEDIA_MANIFEST = Path("governance/reviewed-media.json")
MEDIA_FIELDS = {
    "path",
    "sha256",
    "reviewed_at",
    "reviewed_by",
    "origin",
    "rights",
}
MEDIA_OPTIONAL = {"review_note"}
MEDIA_ALLOWED = MEDIA_FIELDS | MEDIA_OPTIONAL
SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")

# Construct restricted terminology from short pieces so the guard and its
# fixtures comply with the repository's own publication rules.
INDUSTRY_WORD_STEMS = ("ba" + "nk", "ба" + "нк")
INDUSTRY_WORD = re.compile(
    r"(?iu)\b(?:" + "|".join(re.escape(term) for term in INDUSTRY_WORD_STEMS)
    + r")[\w-]*"
)


def violations(relative, content):
    result = []
    if PRIVATE_LINK.search(content):
        result.append("non-self-contained local link")
    if INDUSTRY_WORD.search(content):
        result.append("industry-specific terminology is prohibited")
    return result


def _nonempty_text(value):
    return isinstance(value, str) and bool(value.strip())


def load_reviewed_media(root):
    """Return (path -> entry, error). Fail closed on malformed manifests."""
    manifest = root / MEDIA_MANIFEST
    if not manifest.is_file():
        return {}, None
    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return {}, "reviewed-media manifest is not readable JSON"
    if not isinstance(data, dict) or data.get("version") != 1:
        return {}, "reviewed-media manifest has an unsupported schema"
    entries = data.get("media")
    if not isinstance(entries, list):
        return {}, "reviewed-media manifest has no media list"

    reviewed = {}
    for item in entries:
        if not isinstance(item, dict):
            return {}, "reviewed-media entry is not an object"
        if not MEDIA_FIELDS.issubset(item) or set(item) - MEDIA_ALLOWED:
            return {}, "reviewed-media entry has missing or unknown fields"
        if not all(_nonempty_text(item.get(field)) for field in MEDIA_FIELDS):
            return {}, "reviewed-media entry has an empty required field"
        raw_path = item["path"]
        if "\\" in raw_path or raw_path.startswith("/"):
            return {}, "reviewed-media path is not repository-relative"
        relative = Path(raw_path).as_posix()
        if relative in {"", "."} or ".." in Path(relative).parts:
            return {}, "reviewed-media path is not repository-relative"
        if relative in reviewed:
            return {}, "reviewed-media manifest has a duplicate path"
        if not SHA256_PATTERN.fullmatch(item["sha256"]):
            return {}, "reviewed-media entry has an invalid SHA-256"
        try:
            date.fromisoformat(item["reviewed_at"])
        except ValueError:
            return {}, "reviewed-media entry has an invalid review date"
        if "review_note" in item and not isinstance(item["review_note"], str):
            return {}, "reviewed-media note is not text"
        reviewed[relative] = item
    return reviewed, None


def git_ignored():
    try:
        result = subprocess.run(
            ["git", "ls-files", "--others", "--ignored", "--exclude-standard", "-z"],
            cwd=ROOT, capture_output=True, check=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return frozenset()
    return frozenset(
        part for part in result.stdout.decode("utf-8", "surrogateescape").split("\0")
        if part
    )


def file_sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    errors = []
    reviewed, manifest_error = load_reviewed_media(ROOT)
    if manifest_error:
        errors.append((MEDIA_MANIFEST.as_posix(), manifest_error))
    reviewed_count = 0
    used_media = set()
    ignored = git_ignored()

    for path in sorted(ROOT.rglob("*")):
        rel = path.relative_to(ROOT).as_posix()
        if any(p in {".git", ".venv", "__pycache__"}
               for p in path.relative_to(ROOT).parts):
            continue
        if rel in ignored:
            continue
        if INDUSTRY_WORD.search(rel):
            errors.append((rel, "industry-specific path name is prohibited"))
        if path.is_symlink():
            errors.append((rel, "symlinks require explicit origin review"))
            continue
        if not path.is_file():
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (UnicodeError, OSError):
            entry = reviewed.get(rel)
            if entry is None:
                errors.append((rel, "unscannable file requires explicit origin review"))
                continue
            used_media.add(rel)
            try:
                digest = file_sha256(path)
            except OSError:
                errors.append((rel, "reviewed media cannot be read"))
                continue
            if digest != entry["sha256"]:
                errors.append((rel, "reviewed media hash mismatch"))
                continue
            reviewed_count += 1
            continue
        errors.extend((rel, reason) for reason in violations(rel, content))

    for rel in sorted(set(reviewed) - used_media):
        errors.append((rel, "stale reviewed-media entry"))

    for rel, reason in errors:
        safe_path = INDUSTRY_WORD.sub("[restricted]", rel)
        print(f"FAIL {safe_path}: {reason}")  # Never reproduce restricted terms or source content.
    if errors:
        return 1
    suffix = ""
    if reviewed_count:
        suffix = f"; {reviewed_count} hash-pinned reviewed media file(s) skipped"
    print("PASS: configured lexical boundary checks" + suffix
          + "; independent-origin review still required.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
