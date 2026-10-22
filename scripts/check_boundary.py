"""Limited lexical guard; independent-origin review is still mandatory.

Git-ignored artifacts are not committed content and are skipped. Tracked files and
untracked non-ignored files remain scanned.
"""
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PRIVATE_LINK = re.compile(r"(?i)(?:file:/{2}|https?://(?:localhost|127\.0\.0\.1)(?=[:/\s]|$))")

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


def main():
    errors = []
    ignored = git_ignored()
    for path in sorted(ROOT.rglob("*")):
        rel = path.relative_to(ROOT).as_posix()
        if any(p in {".git", ".venv", "__pycache__"} for p in path.relative_to(ROOT).parts):
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
            errors.append((rel, "unscannable file requires explicit origin review"))
            continue
        errors.extend((rel, reason) for reason in violations(rel, content))
    for rel, reason in errors:
        safe_path = INDUSTRY_WORD.sub("[restricted]", rel)
        print(f"FAIL {safe_path}: {reason}")  # Never reproduce restricted terms or source content.
    if errors:
        return 1
    print("PASS: configured lexical boundary checks; independent-origin review still required.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
