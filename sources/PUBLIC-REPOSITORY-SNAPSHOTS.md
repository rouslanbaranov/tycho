# Public pinned repository snapshots — operator guide

> Implementation for [E03-02 issue #28](https://github.com/rouslanbaranov/tycho/issues/28). Status: bounded public Git snapshot tooling, **not** a general-purpose network sandbox or a licence grant. Local disposable Git tests passed on 2026-10-19. Real GitHub clone integration remains unverified.

## Contract

- Canonical manifest: [public-repositories.lock.json](public-repositories.lock.json). Currently two approved *public* examples (CloudEvents and HdrHistogram), pinned to full 40-character Git commit IDs observed on GitHub 2026-10-19. Neither revision is a branch/tag alias or a statement that the commit's technical content was inspected.
- Generated human navigation: [PUBLIC-REPOSITORIES.md](PUBLIC-REPOSITORIES.md). Reproduce with the `catalogue` command; `check` detects drift. The manifest is authoritative, not the Markdown rendering.
- Interpreter/tool: Python 3.10+ and system Git, no third-party Python packages. `validate`, `check`, `catalogue` and local `verify` perform **no network access**.
- Only canonical HTTPS `github.com/owner/repo.git` origins are admitted; no local-path, SSH, token-bearing URL, arbitrary host, HEAD/tag/ref or mutable version. Every submodule gitlink must be explicitly pinned as `relative/path → full SHA`. No recursive submodule checkout.
- A previously existing destination is NEVER reset, fetched, force-updated, silently overwritten or re-cloned. It must already be clean, detached, remote-free and at the exact commit with matching gitlink inventory. Otherwise the command fails.
- New checkouts use a temporary staging directory and then one final rename. The tool removes the origin remote, writes local pre-commit/pre-push refusing hooks and clears write bits on normal working files. **Best-effort accidental-write protection**: a user can change permissions or bypass hooks; this is not an OS security boundary, tamper proofing or remote server access control.
- No `git submodule update`, untrusted repository scripts, arbitrary commit checkout, shell string evaluation or push command is used.

## Operator invocation

~~~sh
python3 scripts/public_repo_snapshots.py check
python3 scripts/public_repo_snapshots.py catalogue
python3 -m unittest discover -s tests -p 'test_tycho_public_repo_snapshots.py' -v

# Optional, explicitly networked and using a fresh *dedicated* directory:
mkdir -p source-checkouts
python3 scripts/public_repo_snapshots.py checkout --root source-checkouts
python3 scripts/public_repo_snapshots.py verify --root source-checkouts
~~~

The checkout root must already exist and be a normal non-symlink directory. Use an isolated unprivileged filesystem/container in environments that have one. Do **not** pass a directory that contains someone else's working tree. Network operations require explicit permission and may fail because of GitHub availability, auth/policy, access, rate limits or missing commit history.

### Failure cases that must stop work

| Observed condition | Required response |
|---|---|
| Source ID, URL, full revision or submodule path invalid | Reject manifest before contacting network |
| Missing pinned commit in an existing checkout | Report mismatch; do **not** reset or fetch behind user's back |
| Existing repo has uncommitted/untracked changes, branch HEAD or remote | Fail and preserve all files |
| Existing checkout has unlisted gitlinks or SHA mismatch | Fail until reviewed and explicitly locked |
| Clone fails or pinned commit isn't retrievable | Remove only the freshly created temporary staging tree, leave destination absent |
| Catalogue does not match normalized manifest | Regenerate via explicit `catalogue` action after reviewing source-lock changes |
| External license, source access or repository revision uncertain | Defer reuse; being public or cloneable does not authorize mirroring/republishing |

The tool does not generate source-level claims or authorize quotation, asset copying or re-distribution. Consult [access and licensing decisions](ACCESS-LICENSING-RESOLUTION.md) and the original source's exact revision licence before wider use.

## Reproducibility evidence and limits

The `tests/test_tycho_public_repo_snapshots.py` suite creates disposable local Git fixtures to test exact revision, clean detached state, wrong SHA, missing checkout, untracked/dirty state, gitlink mismatch, invalid origin and whole checkout→verify path without a remote GitHub request. Tests were run in a local isolated copy of the **same code bytes** as the GitHub branch on 2026-10-19; test content itself was never run on a Github Actions push/PR workflow (milestone-close policy).

Not established: availability of upstream commits in a real public clone, global inability to edit cloned files, GitHub redirection behavior, submodule object traversal and all platform/security-threat environments. The lock's two records are demonstration coverage, NOT a complete mirror of all public repository candidates in `register.json`. Expand only through deliberate source admission and exact revision inspection.
