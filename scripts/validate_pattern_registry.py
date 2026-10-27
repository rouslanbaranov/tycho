#!/usr/bin/env python3
"""Validate the versioned System Design pattern registry.

Checks JSON Schema, the 145-entry catalog partition, aliases, ownership
references and coverage consistency. Structural checks only: this does not
prove technical truth, source reading, authoring quality or independent review.
"""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = Path("edition/patterns/registry.v1.json")
SCHEMA = Path("schemas/pattern-registry.v1.schema.json")
TICK = chr(96)
FENCE = re.compile(r"^\s*([" + TICK + r"]{3,}|~{3,})[^\r\n]*$")
HEAD = re.compile(r"^\s{0,3}(#{1,6})\s+(.+?)\s*$")
INLINE = re.compile("[" + TICK + "][^" + TICK + r"\n]*[" + TICK + "]")
SEVERITY = {
    "sufficient": 0,
    "partial-reviewed": 1,
    "partial-bounded": 2,
    "partial": 3,
    "name-only": 4,
    "contradictory": 5,
    "missing": 6,
    "not-yet-assessed": 7,
}
EVIDENCE_STATES = ("sufficient", "partial-reviewed", "partial-bounded", "partial")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def engine():
    try:
        from jsonschema import Draft202012Validator, FormatChecker
    except ImportError as exc:
        raise RuntimeError(
            "Install validation dependencies: python3 -m pip install "
            "-r requirements-validation.txt"
        ) from exc
    return Draft202012Validator, FormatChecker


def normalize_alias(value):
    value = unicodedata.normalize("NFKD", value).lower()
    return re.sub(r"[^a-z0-9]+", " ", value).strip()


def slug_heading(label):
    text = re.sub(r"<[^>]*>", "", label)
    text = INLINE.sub(lambda match: match.group(0).strip(TICK), text)
    text = text.strip().rstrip("#").strip().lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    return re.sub(r"\s+", "-", text)


def heading_slugs(path):
    seen = Counter()
    slugs = set()
    fenced = None
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        match = FENCE.match(line)
        if match:
            marker = match.group(1)
            if fenced is None:
                fenced = (marker[0], len(marker))
            elif marker[0] == fenced[0] and len(marker) >= fenced[1]:
                fenced = None
            continue
        if fenced is not None:
            continue
        heading = HEAD.match(line)
        if not heading:
            continue
        key = slug_heading(heading.group(2))
        if not key:
            continue
        number = seen[key]
        slugs.add(key if number == 0 else key + "-" + str(number))
        seen[key] += 1
    return slugs


def route_documents(root):
    path = Path(root) / "generated/route-index.v1.json"
    if not path.is_file():
        return {}
    data = load_json(path)
    return {item["id"]: item["path"] for item in data.get("documents", [])}


def registered_sources(root):
    data = load_json(Path(root) / "sources/register.json")
    return {item["id"] for item in data.get("sources", [])}


def expected_overall(technical, decision):
    if technical == "not-applicable" and decision == "not-applicable":
        return "not-applicable"
    if technical == "not-applicable":
        return decision
    if decision == "not-applicable":
        return technical
    return technical if SEVERITY[technical] >= SEVERITY[decision] else decision


def validate_data(data, root=ROOT):
    root = Path(root).resolve()
    Draft, Format = engine()
    schema = load_json(root / SCHEMA)
    Draft.check_schema(schema)
    validator = Draft(schema, format_checker=Format())
    errors = sorted(
        validator.iter_errors(data),
        key=lambda error: (list(map(str, error.path)), error.message),
    )
    if errors:
        first = errors[0]
        path = "/".join(map(str, first.path)) or "(root)"
        raise ValueError(
            "registry-schema: " + str(len(errors)) + " error(s), first at "
            + path + ": " + first.message
        )

    promotion_data = load_json(root / "edition/patterns/sufficient-promotions.v1.json")
    promotions = {item["pattern_id"]: item
                  for item in promotion_data["promotions"]}
    patterns = data["patterns"]
    families = data["families"]
    require(len(patterns) == 145, "registry-pattern-count")
    require(len(families) == 11, "registry-family-count")

    family_ids = [item["id"] for item in families]
    require(len(set(family_ids)) == 11, "registry-duplicate-family")
    require(sorted(item["number"] for item in families) == list(range(1, 12)),
            "registry-family-number")
    chapters = [item["chapter"] for item in families]
    require(len(set(chapters)) == 11, "registry-duplicate-chapter")
    family_by_id = {item["id"]: item for item in families}

    membership = {}
    for family in families:
        for pattern_id in family["pattern_ids"]:
            require(pattern_id not in membership,
                    "registry-duplicate-membership: " + pattern_id)
            membership[pattern_id] = family["id"]
    pattern_ids = [item["id"] for item in patterns]
    require(len(set(pattern_ids)) == 145, "registry-duplicate-pattern-id")
    require(set(membership) == set(pattern_ids), "registry-family-partition")

    orders = [item["catalog_order"] for item in patterns]
    require(orders == list(range(1, 146)), "registry-catalog-order")
    priorities = Counter(item["priority"] for item in patterns)
    require(priorities["core"] == 123 and priorities["advanced"] == 22,
            "registry-priority-count")

    alias_owner = {}
    sections = set()
    for pattern in patterns:
        pattern_id = pattern["id"]
        require(membership[pattern_id] == pattern["family"],
                "registry-family-mismatch: " + pattern_id)
        require(family_by_id[pattern["family"]]["chapter"]
                == pattern["atlas_owner"]["chapter"],
                "registry-atlas-chapter-mismatch: " + pattern_id)

        normalized = set()
        for value in [pattern["catalog_name"], *pattern["aliases"]]:
            key = normalize_alias(value)
            require(bool(key), "registry-empty-alias: " + pattern_id)
            if key in normalized:
                continue
            normalized.add(key)
            owner = alias_owner.get(key)
            require(owner is None or owner == pattern_id,
                    "registry-alias-collision: " + value)
            alias_owner[key] = pattern_id

        section_key = (pattern["atlas_owner"]["chapter"], pattern["atlas_section"])
        require(section_key not in sections,
                "registry-duplicate-atlas-section: " + pattern_id)
        sections.add(section_key)

    documents = route_documents(root)
    sources = registered_sources(root)
    for pattern in patterns:
        pattern_id = pattern["id"]
        owner = pattern["technical_owner"]
        if owner["document_id"] is None:
            require(owner["path"] is None and owner["anchor"] is None,
                    "registry-owner-shape: " + pattern_id)
            require(owner["state"] != "sufficient",
                    "registry-sufficient-without-owner: " + pattern_id)
        else:
            require(owner["path"] is not None,
                    "registry-owner-path: " + pattern_id)
            if documents:
                require(owner["document_id"] in documents,
                        "registry-unknown-owner-id: " + pattern_id)
                require(documents[owner["document_id"]] == owner["path"],
                        "registry-owner-path-mismatch: " + pattern_id)
            if owner["anchor"] is not None:
                page = root / owner["path"]
                require(page.is_file() and not page.is_symlink(),
                        "registry-owner-page-missing: " + pattern_id)
                require(owner["anchor"] in heading_slugs(page),
                        "registry-owner-anchor: " + pattern_id)

        for unit in pattern["source_units"]:
            require(unit["source_id"] in sources,
                    "registry-unknown-source: " + pattern_id)

        coverage = pattern["coverage"]
        require(coverage["overall"]
                == expected_overall(coverage["technical"], coverage["decision"]),
                "registry-coverage-overall: " + pattern_id)
        if coverage["technical"] == "sufficient":
            require(owner["state"] == "sufficient",
                    "registry-technical-state: " + pattern_id)
        if coverage["decision"] == "sufficient":
            require(pattern["atlas_owner"]["state"] == "sufficient",
                    "registry-atlas-state: " + pattern_id)
        if coverage["technical"] in EVIDENCE_STATES:
            require(owner["state"] == coverage["technical"],
                    "registry-owner-evidence-state: " + pattern_id)
        if coverage["decision"] in EVIDENCE_STATES:
            require(pattern["atlas_owner"]["state"] == coverage["decision"],
                    "registry-atlas-evidence-state: " + pattern_id)
        if "partial-reviewed" in (coverage["technical"], coverage["decision"]):
            require(data["review"]["independent_review"] is True,
                    "registry-reviewed-without-independent-review: " + pattern_id)
        if "sufficient" in (coverage["technical"], coverage["decision"]):
            require(any(unit["status"] == "read"
                        for unit in pattern["source_units"]),
                    "registry-sufficient-without-read-source: " + pattern_id)
            require(pattern_id in promotions
                    and promotions[pattern_id]["technical"] == "pass"
                    and promotions[pattern_id]["decision"] == "pass",
                    "registry-sufficient-without-promotion: " + pattern_id)
        if pattern["review_status"] == "independent-reviewed":
            require(data["review"]["independent_review"] is True,
                    "registry-independent-review-claim: " + pattern_id)

    require(data["source_policy"]["unread_citations"] == "forbidden",
            "registry-source-policy")
    require(data["atlas"]["volume_path"] == "book/volumes/v11-pattern-atlas",
            "registry-atlas-volume-path")
    for family in families:
        require(family["chapter_path"].startswith(
            data["atlas"]["volume_path"] + "/"),
            "registry-chapter-path: " + family["chapter"])

    return {
        "patterns": len(patterns),
        "families": len(families),
        "core": priorities["core"],
        "advanced": priorities["advanced"],
        "kinds": dict(sorted(Counter(item["kind"] for item in patterns).items())),
        "technical_owners": sum(
            item["technical_owner"]["document_id"] is not None for item in patterns
        ),
        "atlas_sections": len(sections),
        "source_units": sum(len(item["source_units"]) for item in patterns),
        "coverage": dict(sorted(Counter(
            item["coverage"]["overall"] for item in patterns
        ).items())),
        "scope": "catalog membership and structural references; not technical truth",
    }


def validate(root=ROOT):
    root = Path(root).resolve()
    data = load_json(root / REGISTRY)
    return validate_data(data, root)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        result = validate(args.root)
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as exc:
        print("FAIL:", exc, file=sys.stderr)
        sys.exit(1)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("PASS: pattern registry", result["patterns"], "entries,",
              result["families"], "families")
    return 0


if __name__ == "__main__":
    sys.exit(main())
