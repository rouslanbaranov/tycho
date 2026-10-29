#!/usr/bin/env python3
"""Validate the feature branch for one GitHub sub-issue or activated parent issue.

A PR head must be feature/TYCHO-<issue-number>-<slug> where the slug exactly
matches the descriptive portion of the corresponding GitHub sub-issue title.
Requires the built-in GITHUB_TOKEN (Issues: read) in CI. Unit-testable offline.
"""
import argparse
import json
import os
import re
import sys
from urllib.error import HTTPError
from urllib.request import Request, urlopen

BRANCH_PATTERN = re.compile(r"^feature/TYCHO-(\d+)-([a-z0-9]+(?:-[a-z0-9]+)*)$")
ISSUE_TITLE_PATTERN = re.compile(
    r"^\[(?:E\d{2}-\d{2}|FUTURE|SIM-[A-Z])\]\s+(.+)$")


def title_slug(issue_title):
    match = ISSUE_TITLE_PATTERN.fullmatch(issue_title.strip())
    if not match:
        raise ValueError(
            "Issue is not an executable [E##-##], [FUTURE] or [SIM-X] sub-issue")
    slug = re.sub(r"[^a-z0-9]+", "-", match.group(1).lower()).strip("-")
    if not slug:
        raise ValueError("Empty issue title slug")
    return slug


def validate(branch, issue_title):
    match = BRANCH_PATTERN.fullmatch(branch)
    if not match:
        raise ValueError("Branch must match feature/TYCHO-<issue-number>-<task-desc-slug>")
    number = int(match.group(1))
    if number < 1 or str(number) != match.group(1):
        raise ValueError("Issue number must be a positive unpadded decimal integer")
    expected = title_slug(issue_title)
    if match.group(2) != expected:
        raise ValueError("Slug mismatch: expected feature/TYCHO-" + str(number) + "-" + expected)
    return number


def fetch_issue(repo, number, token):
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo):
        raise ValueError("Unexpected repository identifier")
    if not token:
        raise ValueError("Missing GITHUB_TOKEN for issue-title verification")
    request = Request(
        "https://api.github.com/repos/" + repo + "/issues/" + str(number),
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": "Bearer " + token,
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "tycho-branch-name-check",
        },
    )
    try:
        with urlopen(request, timeout=20) as response:
            issue = json.loads(response.read())
    except HTTPError as exc:
        raise ValueError("Cannot read issue #" + str(number) +
                         " (HTTP " + str(exc.code) + ")") from exc
    if "pull_request" in issue:
        raise ValueError("Branch issue number points to a pull request")
    return issue


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--branch", help="Override GITHUB_HEAD_REF for offline checks")
    parser.add_argument("--issue-title", help="Use title directly for offline tests")
    args = parser.parse_args()
    branch = args.branch or os.environ.get("GITHUB_HEAD_REF")
    if not branch:
        parser.error("No PR head branch (GITHUB_HEAD_REF) supplied")
    match = BRANCH_PATTERN.fullmatch(branch)
    if not match:
        raise ValueError("Invalid branch format: " + branch)
    issue_number = int(match.group(1))
    title = args.issue_title
    if title is None:
        repo = os.environ.get("GITHUB_REPOSITORY", "")
        issue = fetch_issue(repo, issue_number,
                            os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN"))
        title = issue["title"]
    validate(branch, title)
    print("PASS: branch matches issue #" + str(issue_number) + " and its descriptive slug")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError) as error:
        print("FAIL: " + str(error), file=sys.stderr)
        sys.exit(1)
