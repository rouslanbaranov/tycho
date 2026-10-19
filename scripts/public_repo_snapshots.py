#!/usr/bin/env python3
"""Exact-revision, public-only Git checkouts; no implicit update/reset/push.

Tycho E03-02. Standard library + installed Git. No network calls from import,
validate, catalogue or inspect. Only 'checkout' contacts GitHub, exclusively
HTTPS URLs on the allowlisted host. Submodules are NEVER initialized here.
This is a best-effort accidental-write guard, not a security sandbox.
"""

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import stat
import subprocess
import tempfile
from urllib.parse import urlsplit

REV = re.compile(r"^[0-9a-f]{40}$")
SOURCE = re.compile(r"^src\.[a-z0-9]+(?:-[a-z0-9]+)*$")
COMPONENT = re.compile(r"^[A-Za-z0-9_.-]+$")
MANIFEST = Path(__file__).resolve().parents[1] / "sources" / "public-repositories.lock.json"
CATALOGUE = MANIFEST.with_name("PUBLIC-REPOSITORIES.md")


def validate(data):
    if not isinstance(data, dict) or set(data) != {"schema_version", "generated_from", "repositories"}:
        raise ValueError("Unexpected manifest fields")
    if type(data["schema_version"]) is not int or data["schema_version"] != 1:
        raise ValueError("Unsupported manifest schema version")
    if not isinstance(data["generated_from"], str) or not data["generated_from"].strip():
        raise ValueError("Missing provenance")
    if not isinstance(data["repositories"], list):
        raise ValueError("Repositories must be an array")
    used_id, used_url = set(), set()
    for r in data["repositories"]:
        if not isinstance(r, dict) or set(r) != {"id", "url", "revision", "submodules"}:
            raise ValueError("Unexpected repository fields")
        if not isinstance(r["id"], str) or not SOURCE.fullmatch(r["id"]):
            raise ValueError("Invalid public source ID")
        if r["id"] in used_id:
            raise ValueError("Duplicate source ID")
        used_id.add(r["id"])
        u = urlsplit(r["url"])
        parts = u.path.strip("/").split("/")
        if (u.scheme != "https" or u.netloc != "github.com" or u.username or u.password
                or u.query or u.fragment or len(parts) != 2
                or not all(COMPONENT.fullmatch(x) for x in parts)
                or not parts[0] or not parts[1] or parts[1] in {".git", ".."}):
            raise ValueError("Only canonical public GitHub HTTPS repository URLs are allowed")
        if r["url"] in used_url:
            raise ValueError("Duplicate canonical repository URL")
        used_url.add(r["url"])
        if not isinstance(r["revision"], str) or not REV.fullmatch(r["revision"]):
            raise ValueError("Revision must be a 40-character lowercase commit SHA")
        if not isinstance(r["submodules"], dict):
            raise ValueError("Submodules must be a path-to-gitlink-SHA mapping")
        for path, sha in r["submodules"].items():
            if (not isinstance(path, str) or not path or path.startswith("/")
                    or "\\" in path or any(p in {"", ".", "..", ".git"} for p in path.split("/"))
                    or not all(COMPONENT.fullmatch(p) for p in path.split("/"))):
                raise ValueError("Invalid submodule path")
            if not isinstance(sha, str) or not REV.fullmatch(sha):
                raise ValueError("Submodule must be pinned to its exact gitlink SHA")
    return data["repositories"]


def load_manifest(path=MANIFEST):
    return validate(json.loads(Path(path).read_text(encoding="utf-8")))


def render_catalogue(repositories):
    lines = [
        "# Pinned public Git repository catalogue", "",
        "Generated from [public-repositories.lock.json](public-repositories.lock.json).",
        "Do not edit this catalogue independently. A pin is discoverability, not a verified technical claim.",
        "No source code, licensed artwork or paid content is mirrored by this catalogue.", "",
        "| Source ID | Exact Git revision | Canonical public origin | Locked submodules |",
        "|---|---|---|---:|",
    ]
    for r in sorted(repositories, key=lambda x: x["id"]):
        lines.append("| {id} | `{sha}` | [{url}]({url}) | {sub} |".format(
            id=r["id"], sha=r["revision"], url=r["url"], sub=len(r["submodules"])))
    lines.extend(["", "Submodules are checked by gitlink IDs but are **not cloned or executed** by this tool.",
                  "Checkout must be verified against the lock and its pristine working tree.", ""])
    return "\n".join(lines)


def git(args, cwd=None, timeout=300):
    env = dict(os.environ)
    env.update(GIT_TERMINAL_PROMPT="0", GIT_ALLOW_PROTOCOL="https",
               GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull)
    try:
        return subprocess.run(["git", *args], cwd=cwd, env=env,
                              check=True, capture_output=True, text=True,
                              timeout=timeout).stdout.strip()
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
        raise ValueError("Git operation failed or timed out: " + " ".join(args[:3])) from exc


def gitlinks(path):
    raw = git(["ls-tree", "-r", "HEAD"], cwd=path)
    result = {}
    for line in raw.splitlines():
        if not line.startswith("160000 commit "):
            continue
        left, name = line.split("\t", 1)
        result[name] = left.split()[2]
    return result


def inspect_checkout(path, locked):
    path = Path(path)
    if path.is_symlink() or not path.is_dir() or not (path / ".git").is_dir():
        raise ValueError("Missing or unsafe checkout: " + str(path))
    sha = git(["rev-parse", "--verify", "HEAD^{commit}"], cwd=path)
    if sha != locked["revision"]:
        raise ValueError("Pinned revision mismatch for " + locked["id"])
    if git(["rev-parse", "--abbrev-ref", "HEAD"], cwd=path) != "HEAD":
        raise ValueError("Checkout is on a writable branch instead of detached HEAD")
    if git(["status", "--porcelain", "--untracked-files=all"], cwd=path):
        raise ValueError("Dirty checkout; never reset existing user work")
    if git(["remote"], cwd=path):
        raise ValueError("Checkout has remote(s) configured: push/edit guard missing")
    if gitlinks(path) != locked["submodules"]:
        raise ValueError("Pinned submodule gitlinks differ from the locked set")
    return sha


def guard_checkout(path):
    path = Path(path)
    git(["remote", "remove", "origin"], cwd=path)
    git(["config", "--local", "receive.denyCurrentBranch", "refuse"], cwd=path)
    hooks = path / ".git" / "hooks"
    hooks.mkdir(exist_ok=True)
    for name in ("pre-commit", "pre-push"):
        hook = hooks / name
        hook.write_text("#!/bin/sh\necho 'Tycho source snapshot is read-only' >&2\nexit 1\n")
        hook.chmod(0o755)
    for root, folders, files in os.walk(path, followlinks=False):
        folders[:] = [d for d in folders if d != ".git"]
        for name in files:
            p = Path(root) / name
            if not p.is_symlink():
                p.chmod(p.stat().st_mode & ~stat.S_IWUSR & ~stat.S_IWGRP & ~stat.S_IWOTH)


def checkout_one(locked, destination):
    destination = Path(destination)
    if destination.exists() or destination.is_symlink():
        return inspect_checkout(destination, locked)
    if destination.parent.is_symlink() or not destination.parent.is_dir():
        raise ValueError("Unsafe or missing checkout root")
    staging = Path(tempfile.mkdtemp(prefix=".tycho-clone-", dir=destination.parent))
    try:
        git(["clone", "--no-checkout", "--no-recurse-submodules", "--",
             locked["url"], str(staging)])
        try:
            git(["cat-file", "-e", locked["revision"] + "^{commit}"], cwd=staging)
        except ValueError:
            git(["fetch", "--no-tags", "origin", locked["revision"]], cwd=staging)
        git(["checkout", "--detach", locked["revision"]], cwd=staging)
        if gitlinks(staging) != locked["submodules"]:
            raise ValueError("Submodule gitlink mismatch: explicit lock update required")
        guard_checkout(staging)
        inspect_checkout(staging, locked)
        if destination.exists():
            raise ValueError("Destination appeared concurrently; will not overwrite")
        staging.rename(destination)
        return inspect_checkout(destination, locked)
    finally:
        if staging.exists():
            # read-only files can be removed by their owning user on writable dirs
            shutil.rmtree(staging, ignore_errors=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("catalogue", "check", "checkout", "verify"))
    parser.add_argument("--manifest", type=Path, default=MANIFEST)
    parser.add_argument("--root", type=Path, default=Path("source-checkouts"))
    args = parser.parse_args()
    repositories = load_manifest(args.manifest)
    rendered = render_catalogue(repositories)
    target = args.manifest.with_name("PUBLIC-REPOSITORIES.md")
    if args.action == "catalogue":
        target.write_text(rendered, encoding="utf-8")
        print("Wrote", target)
    elif args.action == "check":
        if not target.is_file() or target.read_text(encoding="utf-8") != rendered:
            raise SystemExit("Public repo catalogue is stale")
        print("PASS: locked repositories and generated catalogue match")
    else:
        if args.root.is_symlink() or not args.root.is_dir():
            raise SystemExit("Create an ordinary, dedicated checkout root directory first")
        for r in repositories:
            p = args.root / r["id"]
            if args.action == "checkout":
                sha = checkout_one(r, p)
            else:
                sha = inspect_checkout(p, r)
            print("PASS", r["id"], sha)


if __name__ == "__main__":
    main()
