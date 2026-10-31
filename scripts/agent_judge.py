#!/usr/bin/env python3
"""Deterministic rule-based judge for the benchmark harness.

Reads the task JSON from TYCHO_TASK_JSON and the answer JSON on stdin.
This is not a semantic judge and not human review.
"""
import json
import os
import re
import sys

def main():
    task = json.loads(os.environ["TYCHO_TASK_JSON"])
    try:
        answer = json.load(sys.stdin)
    except json.JSONDecodeError:
        print(json.dumps({"pass": False, "error": "invalid-answer-json"}))
        return 0
    abstain = bool(answer.get("abstain"))
    citations = answer.get("citations") or []
    required = task.get("required_evidence") or []
    required_set = set(required)
    valid = [c for c in citations if c in required_set]
    invalid = [c for c in citations if c not in required_set]
    text = str(answer.get("answer", "")).strip()
    if task.get("abstention_expected"):
        ok = abstain and not citations
        return print(json.dumps({
            "pass": ok, "abstain": abstain, "citation_precision": 1.0 if not citations else 0.0,
            "citations": len(citations), "valid_citations": len(valid),
            "invalid_citations": invalid, "reason": "abstention-expected"}))
    support = 1.0 if text and citations and not invalid else 0.0
    coverage = 1.0 if len(valid) >= 1 else 0.0
    ok = bool(support and coverage and not abstain)
    print(json.dumps({
        "pass": ok, "answer_support": support, "coverage": coverage,
        "citation_precision": round(len(valid) / len(citations), 4) if citations else 0.0,
        "valid_citations": len(valid), "invalid_citations": invalid,
        "abstain": abstain, "reason": "rule-based-not-human"}))

if __name__ == "__main__":
    main()
