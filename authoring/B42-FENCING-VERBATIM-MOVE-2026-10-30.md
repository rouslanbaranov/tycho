# Fencing Tokens promotion protection — verbatim card move

Status: completed format-only promotion rebind, 2026-10-30. The V11/C08
Fencing Tokens card moved verbatim from the shared chapter page to a dedicated
page. No card text, frontmatter source binding, owner section or review report
changed. The existing sufficient promotion is rebound to the new page by the
proof below; this is not a new content review.

## Why this move precedes B42

The B42 Causal Ordering lane edits the V11/C08 chapter page. That page carried
the `tycho.pattern.fencing-tokens` promotion card hash, so any C08 edit would
invalidate the promotion. Splitting the Fencing Tokens card first isolates it
from the shared page; the B42 Causal card is then split separately.

## Baseline

- Parent HEAD: `3cebce623e6efe3a3fd4b166372172d28edf3c1d`.
- Shared page:
  `book/volumes/v11-pattern-atlas/c08-coordination/README.md`.
- Fencing section: `### Fencing Tokens`, old lines 213-248; the next heading
  was `### Quorum Coordination` at old line 249.
- Old README raw SHA-256:
  `3c25d9b5eaf1dec34bfe43a44a583a5769e6f6e8caac83829112f40c1b63702c`.
- Promotion record: `edition/patterns/sufficient-promotions.v1.json`,
  reviewed 2026-10-29 at `103db2257ee637f99ec9ddb307586881a38796ce`,
  report `authoring/ai-reviews/2026-10-29-fencing-final-deepseek.md`
  (SHA-256 `9eb50d90c52438ad690c56810d30061ae683b761b355ccd9f593fa857d1597bc`).
- Owner page (concatenate):

      book/volumes/v04-distributed-coordination-and-events/
      c02-replication-consensus-and-leader-changes/leader-recovery.md

  Unchanged SHA-256
  `6123ac21f7f777c03c92f0dc20106fcc17534281500f6ed1561d94c3182e746f`.

## Verbatim-move proof

- Dedicated page:
  `book/volumes/v11-pattern-atlas/c08-coordination/fencing-tokens.md`.
- The page consists of new page frontmatter, the H1 `# Fencing Tokens`, and
  the old section body. The frontmatter records the same source id
  (`src.kleppmann-distributed-locking`), the same owner link and the same
  self-checked status; it does not alter the card.
- Old section body SHA-256, normalized to one trailing newline:
  `536becf7e06d6d890f9c1ff7371886424b24f25d35d18590bd54d17fac883cb2`
  (1,810 bytes).
- New page card body SHA-256, normalized to one trailing newline:
  `536becf7e06d6d890f9c1ff7371886424b24f25d35d18590bd54d17fac883cb2`
  (1,810 bytes).
- Canonical text SHA-256 (whitespace-joined):
  `d50932705d7cb36f44626ba6cc5fbb8d5c12afa91720d47d351a9f67e5694df0`.
- New page raw SHA-256:
  `39b75daf58966aa8586d6bd76c9a96af3601f209d5391521c1899705d4aaec0a`.
- Split README raw SHA-256:
  `d2eed35ca8d4678a752974467c03fe8a8e33221f756ebb2f23100b4a7efc1d87`.
- New page historical-view SHA-256:
  `e19f905020eb224a0df1a55f353f26b2171133eedf4007598df0134c02585b65`.

Reproduction commands, run from the repository root:

    tmp=$(mktemp -d)
    git show HEAD:book/volumes/v11-pattern-atlas/c08-coordination/README.md \
      > "$tmp/old-readme.md"
    python3 - "$tmp" <<'PY'
    import hashlib, sys
    from pathlib import Path

    tmp = Path(sys.argv[1])
    old = (tmp / "old-readme.md").read_text()
    lines = old.splitlines(keepends=True)
    start = next(i for i, line in enumerate(lines)
                 if line.rstrip("\n") == "### Fencing Tokens")
    end = next(i for i in range(start + 1, len(lines))
               if lines[i].startswith("### "))
    body = "".join(lines[start + 1:end]).rstrip("\n") + "\n"
    (tmp / "old-body.md").write_text(body)

    page = Path("book/volumes/v11-pattern-atlas/"
                "c08-coordination/fencing-tokens.md").read_text()
    after = page.split("---\n", 2)[2]
    new = after.split("# Fencing Tokens\n", 1)[1].lstrip("\n")
    new = "\n" + new if new else ""
    new = new.rstrip("\n") + "\n"
    (tmp / "new-body.md").write_text(new)
    print("old", hashlib.sha256(body.encode()).hexdigest())
    print("new", hashlib.sha256(new.encode()).hexdigest())
    PY
    diff -u "$tmp/old-body.md" "$tmp/new-body.md"
    git diff -w --no-index --exit-code "$tmp/old-body.md" "$tmp/new-body.md"

Observed results on 2026-10-30:

    old body bytes 1810; new body bytes 1810
    diff -u: no output, exit 0
    git diff -w --no-index --exit-code: exit 0
    both body files: 536becf7e06d6d890f9c1ff7371886424b24f25d35d18590bd54d17fac883cb2

Second read-only verification used a separate POSIX `awk`/`perl`
extraction, not the Python extractor: both normalized bodies hashed to
`536becf7...` and `cmp` exited 0. The proof is mechanically reproducible
from the parent HEAD and the new page.

## Promotion update

- `card_sha256`:
  `3c25d9b5eaf1dec34bfe43a44a583a5769e6f6e8caac83829112f40c1b63702c`
  -> `39b75daf58966aa8586d6bd76c9a96af3601f209d5391521c1899705d4aaec0a`.
- `owner_page_sha256` is unchanged
  (`6123ac21f7f777c03c92f0dc20106fcc17534281500f6ed1561d94c3182e746f`).
- `reviewed_at`, `reviewed_head`, `reviewer`, `report_path` and
  `report_sha256` are unchanged. The reviewed card text is the same text;
  only its containing file changed.
- `edition/patterns/card-batches.v1.json` now points the Fencing entry at the
  dedicated page. The README keeps the stable `### Fencing Tokens` anchor and
  links onward to the card.
- No promotion, owner acceptance, test result or independent content review is
  newly claimed.

## Limits

- The move is format-only for the card body; it does not add evidence or
  rewrite the Fencing decision.
- The second verification is a separate read-only tool process, not an
  external AI content review.
- The B42 Causal Ordering lane remains partial-bounded and unpromoted.
