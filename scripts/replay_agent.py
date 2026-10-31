#!/usr/bin/env python3
"""Replay a saved answer for harness aggregation."""
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
task_id = os.environ["TYCHO_TASK_ID"]
path = ROOT / "evaluation/agent-benchmark/answers" / (task_id + ".json")
print(path.read_text(encoding="utf-8"))
