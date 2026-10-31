#!/usr/bin/env python3
"""Batch harness for the 100-question external-agent benchmark.

Each question is dispatched to an independent subprocess in a fresh environment.
The harness is read-only and does not call a model itself.
"""
import argparse
import concurrent.futures
import json
import os
import shlex
import statistics
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {"id", "question", "layer_expected", "difficulty",
            "required_evidence", "expected_answer_points",
            "abstention_expected", "token_budget", "time_budget_s",
            "rubric_weights"}


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def validate(corpus):
    errors = []
    items = corpus.get("questions", [])
    if len(items) != 100:
        errors.append("expected 100 questions, got %d" % len(items))
    ids = [x.get("id") for x in items]
    if len(set(ids)) != len(ids):
        errors.append("duplicate ids")
    for item in items:
        missing = REQUIRED - set(item)
        if missing:
            errors.append("%s missing %s" % (item.get("id"), sorted(missing)))
        for key in ("required_evidence", "expected_answer_points",
                    "rubric_weights"):
            if not isinstance(item.get(key), list):
                errors.append("%s %s must be a list" % (item.get("id"), key))
    return errors


def run_one(item, agent_cmd, judge_cmd, timeout):
    log_path = ROOT / "evaluation/agent-benchmark/logs" / (item["id"] + ".jsonl")
    log_path.parent.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ)
    env["TYCHO_TASK_JSON"] = json.dumps(item, ensure_ascii=False)
    env["TYCHO_QUESTION"] = item["question"]
    env["TYCHO_TASK_ID"] = item["id"]
    env["TYCHO_SESSION_LOG"] = str(log_path)
    env["TYCHO_SNAPSHOT"] = "e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa"
    started = time.perf_counter()
    try:
        proc = subprocess.run(
            shlex.split(agent_cmd), cwd=ROOT, env=env, text=True,
            capture_output=True, timeout=timeout)
        elapsed = time.perf_counter() - started
        return {"id": item["id"], "ok": proc.returncode == 0,
                "stdout": proc.stdout[-200000:], "stderr": proc.stderr[-20000:],
                "elapsed_s": round(elapsed, 3),
                "log": str(log_path), "judge": None}
    except subprocess.TimeoutExpired as exc:
        return {"id": item["id"], "ok": False, "error": "timeout",
                "stdout": (exc.stdout or "")[-20000:],
                "stderr": (exc.stderr or "")[-20000:], "elapsed_s": timeout}


def derive_telemetry(log_path):
    records = []
    try:
        with open(log_path, encoding="utf-8") as fh:
            for line in fh:
                try:
                    records.append(json.loads(line))
                except ValueError:
                    pass
    except OSError:
        pass
    counts = {}
    pages, sections = set(), set()
    for rec in records:
        tool = rec.get("command") or rec.get("tool") or "unknown"
        counts[tool] = counts.get(tool, 0) + 1
        value = rec.get("value")
        if tool == "page" and value:
            pages.add(value)
        if tool == "read" and value:
            sections.add(value)
    return {"calls": len(records), "ok": sum(1 for r in records if r.get("ok")),
            "failed": sum(1 for r in records if r.get("ok") is False),
            "by_tool": counts, "unique_pages": len(pages),
            "unique_sections": len(sections)}


def parse_answer(row):
    try:
        value = json.loads(row.get("stdout", ""))
    except (TypeError, ValueError):
        return None
    return value if isinstance(value, dict) else None


def aggregate(rows, corpus):
    by_id = {x["id"]: x for x in corpus["questions"]}
    scores = []
    tokens = []
    calls = []
    for row in rows:
        ans = parse_answer(row) or {}
        judge = row.get("judge") or {}
        if isinstance(judge, dict):
            scores.append(judge.get("pass", False))
        usage = ans.get("token_usage") or {}
        val = usage.get("total")
        if isinstance(val, (int, float)):
            tokens.append(float(val))
        tele = row.get("telemetry") or {}
        if isinstance(tele.get("calls"), (int, float)):
            calls.append(float(tele["calls"]))
    mean = statistics.mean(tokens) if tokens else None
    sd = statistics.pstdev(tokens) if len(tokens) > 1 else None
    anomalies = []
    for row in rows:
        ans = parse_answer(row) or {}
        usage = ans.get("token_usage") or {}
        val = usage.get("total")
        if mean is not None and sd and isinstance(val, (int, float)):
            z = (val - mean) / sd
            if abs(z) >= 2:
                anomalies.append({"id": row["id"], "token_z": round(z, 2),
                                  "tokens": val})
    return {"questions": len(rows),
            "dispatched_ok": sum(1 for x in rows if x.get("ok")),
            "judged": len(scores),
            "pass_rate": round(sum(bool(x) for x in scores) / len(scores), 4)
            if scores else None,
            "mean_tokens": round(mean, 1) if mean is not None else None,
            "mean_calls": round(statistics.mean(calls), 2) if calls else None,
            "token_anomalies": anomalies,
            "layers": {layer: sum(1 for q in corpus["questions"]
                                 if q["layer_expected"] == layer)
                       for layer in sorted({q["layer_expected"]
                                            for q in corpus["questions"]})}}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--corpus", type=Path, required=True)
    ap.add_argument("--agent-command", required=True)
    ap.add_argument("--judge-command")
    ap.add_argument("--jobs", type=int, default=1)
    ap.add_argument("--timeout", type=int, default=900)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--out", type=Path, default=ROOT / "evaluation/agent-benchmark/results.json")
    ap.add_argument("--validate-only", action="store_true")
    args = ap.parse_args(argv)
    corpus = load_json(args.corpus)
    errors = validate(corpus)
    if errors:
        print(json.dumps({"ok": False, "errors": errors}, indent=2))
        return 2
    if args.validate_only:
        print(json.dumps({"ok": True, "questions": len(corpus["questions"])}, indent=2))
        return 0
    questions = corpus["questions"]
    if args.limit:
        questions = questions[:args.limit]
    rows = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.jobs)) as pool:
        futures = [pool.submit(run_one, item, args.agent_command,
                               args.judge_command, args.timeout)
                   for item in questions]
        for future in concurrent.futures.as_completed(futures):
            rows.append(future.result())
    rows.sort(key=lambda x: x["id"])
    for row in rows:
        row["telemetry"] = derive_telemetry(row.get("log", ""))
    # Judge is an external command that receives the answer on stdin.
    for row in rows:
        if not args.judge_command or not row.get("ok"):
            continue
        item = next(q for q in corpus["questions"] if q["id"] == row["id"])
        env = dict(os.environ)
        env["TYCHO_TASK_JSON"] = json.dumps(item, ensure_ascii=False)
        try:
            proc = subprocess.run(
                shlex.split(args.judge_command), cwd=ROOT, env=env,
                input=row.get("stdout", ""), text=True,
                capture_output=True, timeout=args.timeout)
            row["judge"] = json.loads(proc.stdout) if proc.returncode == 0 else {
                "error": proc.stderr[-2000:]}
        except (subprocess.TimeoutExpired, ValueError) as exc:
            row["judge"] = {"error": str(exc)}
    out = {"status": "ai-benchmark-not-human", "corpus": str(args.corpus),
           "agent_command": args.agent_command, "rows": rows,
           "summary": aggregate(rows, corpus),
           "limits": ("Harness only; independent agents and judges are external. "
                      "No human review. Token values are self-reported unless "
                      "the provider usage is included.")}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
