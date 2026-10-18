#!/usr/bin/env python3
"""One-time idempotent TYCHO-23 priority correction: get researched chapters first.

Safe exact-scope migration: only five approved issue dependency sets are
changed; all other issue metadata, milestones and hierarchy remain untouched.
"""
import json
import os
import re
import time
from urllib.request import Request, urlopen
from urllib.error import HTTPError

REPO = "rouslanbaranov/tycho"
VERSION = "2026-03-10"
CHANGES = {
    # issue: (old blockers, new blockers)
    18: ([17], [39]),     # legacy-model refinements after real end-to-end evidence
    19: ([17], [38]),     # applicability cards from researched mechanism
    23: ([19], [17]),     # a book plan needs the requirements contract, not all cards
    26: ([22, 25], [25]), # research pilots need authoring contracts, not decision service
    38: ([26, 37], [26])  # pilot content can precede full validator infrastructure
}


def github(method, path, token, payload=None):
    url = "https://api.github.com/repos/" + REPO + path
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": VERSION,
        "Authorization": "Bearer " + token,
        "User-Agent": "tycho-book-first-plan",
    }
    request = Request(url, headers=headers, method=method,
                      data=json.dumps(payload).encode() if payload is not None else None)
    for attempt in range(5):
        try:
            with urlopen(request, timeout=35) as response:
                content = response.read()
                return json.loads(content) if content else None
        except HTTPError as exc:
            error_text = exc.read().decode("utf-8", errors="replace")[:400]
            if (exc.code in (429, 502, 503) or
                (exc.code == 403 and "secondary rate limit" in error_text.lower())) and attempt < 4:
                time.sleep(8 * (attempt + 1))
                continue
            raise RuntimeError(method + " " + path + ": HTTP " + str(exc.code) + " " + error_text) from exc


def dependency_section(body):
    match = re.search(r"(## Dependencies\n\n)(.*?)(?=\n## |\Z)", body, re.S)
    if not match:
        raise ValueError("Missing Dependencies section")
    return match


def blocker_numbers(text):
    return [int(n) for n in re.findall(r"#(\d+)\b", text)]


def check_no_cycle(issues):
    planned = {}
    for obj in issues:
        if obj.get("pull_request") or obj["number"] < 17:
            continue
        deptext = dependency_section(obj.get("body") or "").group(2)
        planned[obj["number"]] = list(CHANGES[obj["number"]][1]) if obj["number"] in CHANGES else blocker_numbers(deptext)
    visited, active = set(), set()
    def visit(node):
        if node in active:
            raise ValueError("Dependency cycle at #" + str(node))
        if node in visited:
            return
        active.add(node)
        for child in planned.get(node, []):
            if child not in planned:
                raise ValueError("Bad dependency #" + str(child))
            visit(child)
        active.remove(node)
        visited.add(node)
    for node in planned:
        visit(node)


def main():
    token = os.getenv("GITHUB_TOKEN") or os.getenv("GH_TOKEN")
    if not token:
        raise ValueError("GITHUB_TOKEN is required")
    data = github("GET", "/issues?state=all&per_page=100", token)
    bynumber = {obj["number"]: obj for obj in data if "pull_request" not in obj}
    if not all(num in bynumber for num in set(CHANGES) | {17, 25, 26, 37, 38, 39}):
        raise ValueError("Incomplete issue inventory")
    check_no_cycle(data)

    # Preflight every edited issue before making any write.
    for number, (old, new) in CHANGES.items():
        section = dependency_section(bynumber[number].get("body") or "").group(2)
        present = blocker_numbers(section)
        if present not in (old, new):
            raise ValueError("Unexpected dependency text for #" + str(number) + ": " + str(present))
        actual = github("GET", "/issues/" + str(number) + "/dependencies/blocked_by?per_page=100", token)
        actual_numbers = {entry["number"] for entry in actual}
        if not actual_numbers <= (set(old) | set(new)):
            raise ValueError("Unplanned dependency for #" + str(number) + ": " + str(actual_numbers))

    for number, (old, new) in CHANGES.items():
        issue = github("GET", "/issues/" + str(number), token)
        section = dependency_section(issue["body"])
        declared = blocker_numbers(section.group(2))
        if declared == old and old != new:
            annotation = ", ".join("#" + str(n) for n in new)
            reason = {
                18: "Research-backed legacy methodology follows the first end-to-end pilot",
                19: "Pattern cards use evidence from the first researched mechanism",
                23: "Question-driven book outline needs the validated requirements baseline",
                26: "Bounded pilot contract follows the minimal authoring workflow",
                38: "Pilot research uses manual evidence gates while full automated validators mature",
            }[number]
            fresh = issue["body"][:section.start(2)] + annotation + "\n\nBook-first sequencing rationale: " + reason + ".\n" + issue["body"][section.end(2):]
            github("PATCH", "/issues/" + str(number), token, {"body": fresh})
            print("Updated task dependency wording:", number, flush=True)

        actual = github("GET", "/issues/" + str(number) + "/dependencies/blocked_by?per_page=100", token)
        present = {i["number"]: i["id"] for i in actual}
        for removed in sorted(set(present) - set(new)):
            github("DELETE", "/issues/" + str(number) + "/dependencies/blocked_by/" + str(present[removed]), token)
            print("Removed obsolete blocker", number, "<-", removed, flush=True)
            time.sleep(1.5)
        for missing in sorted(set(new) - set(present)):
            github("POST", "/issues/" + str(number) + "/dependencies/blocked_by", token,
                   {"issue_id": bynumber[missing]["id"]})
            print("Added valid blocker", number, "<-", missing, flush=True)
            time.sleep(1.5)
        verified = github("GET", "/issues/" + str(number) + "/dependencies/blocked_by?per_page=100", token)
        if {x["number"] for x in verified} != set(new):
            raise RuntimeError("Verification failed on #" + str(number))
        current = github("GET", "/issues/" + str(number), token)
        if blocker_numbers(dependency_section(current["body"]).group(2)) != new:
            raise RuntimeError("Text verification failed on #" + str(number))

    print("PASS: book-first dependencies applied and verified for five issues")


if __name__ == "__main__":
    main()
