#!/usr/bin/env python3
"""Safely reconcile the Tycho delivery issue hierarchy and declared dependencies.

GitHub Issues are the source of truth. This tool only creates missing links; it
never creates issues, replaces an existing parent, closes tasks or removes links.
Dry-run is the default. Requires a token with Issues:write for --apply.
"""
import argparse
import json
import os
import re
import sys
import time
from urllib.error import HTTPError
from urllib.request import Request, urlopen

API_VERSION = "2026-03-10"
EPIC_RE = re.compile(r"^\[EPIC (E\d{2})\] ")
TASK_RE = re.compile(r"^\[(E\d{2})-\d{2}\] ")
PARENT_RE = re.compile(r"Parent epic: #(\d+) \((E\d{2})\)")
REF_RE = re.compile(r"#(\d+)\b")


def request(repo, method, path, token, payload=None):
    body = json.dumps(payload).encode("utf-8") if payload is not None else None
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": API_VERSION,
        "User-Agent": "tycho-issue-plan-reconciler",
    }
    if token:
        headers["Authorization"] = "Bearer " + token
    url = "https://api.github.com/repos/" + repo + path
    for attempt in range(6):
        try:
            with urlopen(Request(url, data=body, headers=headers, method=method), timeout=35) as response:
                raw = response.read()
                return json.loads(raw) if raw else None
        except HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")[:500]
            throttled = exc.code in (429, 502, 503) or (
                exc.code == 403 and (
                    "secondary rate limit" in detail.lower()
                    or "abuse detection" in detail.lower()
                )
            )
            if throttled and attempt < 5:
                delay = min(90, 8 * (attempt + 1))
                print("Rate-limit/transient response; retrying in", delay, "seconds", flush=True)
                time.sleep(delay)
                continue
            raise RuntimeError(method + " " + path + ": HTTP " + str(exc.code) + " " + detail) from exc


def dependency_refs(issue):
    block = (issue.get("body") or "").split("## Dependencies", 1)
    if len(block) < 2:
        raise ValueError("Missing Dependencies section: #" + str(issue["number"]))
    section = block[1].split("\n## ", 1)[0]
    return [int(n) for n in REF_RE.findall(section)]


def load_and_validate(repo, token):
    issues = request(repo, "GET", "/issues?state=all&per_page=100", token)
    numbers = {i["number"]: i for i in issues if "pull_request" not in i}
    if len(numbers) != 94 or set(numbers) != set(range(1, 95)):
        raise ValueError("Expected the reviewed 94-issue plan (#1–#94), not a changed inventory")
    if not numbers[1]["title"].startswith("[PROGRAM]"):
        raise ValueError("Program #1 has changed")
    epics = {}
    for number in range(2, 17):
        issue = numbers[number]
        match = EPIC_RE.match(issue["title"])
        if not match:
            raise ValueError("Unexpected epic title #" + str(number))
        if issue.get("parent_issue_url") != issue["url"].rsplit("/", 1)[0] + "/1":
            raise ValueError("Epic #" + str(number) + " is not a child of program #1")
        epics[match.group(1)] = issue
    if len(epics) != 15:
        raise ValueError("Expected 15 unique epic codes")

    parents, dependencies = {}, {}
    for number in range(17, 95):
        issue = numbers[number]
        title_match = TASK_RE.match(issue["title"])
        parent_match = PARENT_RE.search(issue.get("body") or "")
        if not title_match or not parent_match:
            raise ValueError("Missing or invalid parent/identity for task #" + str(number))
        code = title_match.group(1)
        expected = epics.get(code)
        if not expected or expected["number"] != int(parent_match.group(1)) or code != parent_match.group(2):
            raise ValueError("Conflicting parent declaration for #" + str(number))
        if issue["milestone"]["number"] != expected["milestone"]["number"]:
            raise ValueError("Task/epic milestone mismatch for #" + str(number))
        parents[number] = expected["number"]
        referenced = dependency_refs(issue)
        if len(referenced) != len(set(referenced)):
            raise ValueError("Repeated dependency for #" + str(number))
        if any(ref not in range(17, 95) or ref == number for ref in referenced):
            raise ValueError("Invalid or self-referential dependency for #" + str(number))
        dependencies[number] = referenced

    visited, active = set(), set()

    def visit(number):
        if number in active:
            raise ValueError("Dependency cycle at #" + str(number))
        if number in visited:
            return
        active.add(number)
        for ref in dependencies[number]:
            visit(ref)
        active.remove(number)
        visited.add(number)

    for number in dependencies:
        visit(number)
    return numbers, parents, dependencies


def reconcile_parents(repo, token, numbers, parents, apply, delay):
    changes = []
    for child, parent in sorted(parents.items()):
        found = numbers[child].get("parent_issue_url")
        wanted = numbers[parent]["url"]
        if found and found != wanted:
            raise ValueError("Existing parent conflict for #" + str(child) + ": " + found)
        if not found:
            changes.append((child, parent))
    print("Missing parent links:", len(changes), flush=True)
    if apply:
        for index, (child, parent) in enumerate(changes, 1):
            request(repo, "POST", "/issues/" + str(parent) + "/sub_issues", token,
                    {"sub_issue_id": numbers[child]["id"]})
            print("Linked #" + str(child) + " under #" + str(parent) +
                  " (" + str(index) + "/" + str(len(changes)) + ")", flush=True)
            if index < len(changes):
                time.sleep(delay)
    return len(changes)


def reconcile_dependencies(repo, token, numbers, dependencies, apply, delay):
    existing = {}
    additions = []
    for number, refs in sorted(dependencies.items()):
        if not refs:
            continue
        active = request(repo, "GET", "/issues/" + str(number) +
                         "/dependencies/blocked_by?per_page=100", token)
        current_ids = {entry["id"] for entry in active}
        existing[number] = current_ids
        for ref in refs:
            if numbers[ref]["id"] not in current_ids:
                additions.append((number, ref))
    print("Missing native blocked-by links:", len(additions), flush=True)
    if apply:
        for index, (issue, blocker) in enumerate(additions, 1):
            request(repo, "POST", "/issues/" + str(issue) +
                    "/dependencies/blocked_by", token,
                    {"issue_id": numbers[blocker]["id"]})
            print("Blocked-by #" + str(issue) + " -> #" + str(blocker) +
                  " (" + str(index) + "/" + str(len(additions)) + ")", flush=True)
            if index < len(additions):
                time.sleep(delay)
    return len(additions)


def verify_parents(repo, token, parents):
    missing = []
    for parent in range(1, 17):
        children = request(repo, "GET", "/issues/" + str(parent) +
                           "/sub_issues?per_page=100", token)
        found = {item["number"] for item in children}
        expected = set(range(2, 17)) if parent == 1 else {
            child for child, owner in parents.items() if owner == parent
        }
        if found != expected:
            missing.append((parent, sorted(expected - found), sorted(found - expected)))
    if missing:
        raise ValueError("Hierarchy validation failed: " + str(missing))
    print("Verified native hierarchy: 1 program, 15 epics and 78 child issues")


def verify_dependencies(repo, token, numbers, dependencies):
    missing = []
    for issue, refs in dependencies.items():
        if not refs:
            continue
        active = request(repo, "GET", "/issues/" + str(issue) +
                         "/dependencies/blocked_by?per_page=100", token)
        found = {item["id"] for item in active}
        if any(numbers[ref]["id"] not in found for ref in refs):
            missing.append(issue)
    if missing:
        raise ValueError("Native dependency verification failed for: " + str(missing))
    print("Verified declared native dependencies:", sum(map(len, dependencies.values())))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Create missing links")
    parser.add_argument("--dependencies", action="store_true", help="Also create native blocked-by links")
    parser.add_argument("--delay", type=float, default=1.4, help="Seconds between write calls")
    args = parser.parse_args()
    repo = os.environ.get("GITHUB_REPOSITORY", "rouslanbaranov/tycho")
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if args.apply and not token:
        parser.error("--apply requires GH_TOKEN or GITHUB_TOKEN")
    if args.delay < 1:
        parser.error("--delay must be at least 1 second")
    numbers, parents, dependencies = load_and_validate(repo, token)
    print("Validated: 94 issues, 15 epics, 78 tasks, 112 declared dependencies")
    reconcile_parents(repo, token, numbers, parents, args.apply, args.delay)
    if args.apply:
        verify_parents(repo, token, parents)
    if args.dependencies:
        reconcile_dependencies(repo, token, numbers, dependencies, args.apply, args.delay)
        if args.apply:
            verify_dependencies(repo, token, numbers, dependencies)
    print("Reconciliation complete" if args.apply else "Dry-run complete; nothing changed")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, RuntimeError) as error:
        print("ERROR:", error, file=sys.stderr)
        sys.exit(1)
