"""Shared utilities for problem list management."""

import json
from pathlib import Path


def get_existing_problems():
    """Get problem numbers from existing JSON files."""
    # Get the project root (3 levels up from this file)
    project_root = Path(__file__).parent.parent.parent
    json_dir = project_root / "leetcode_py/cli/resources/leetcode/json/problems"
    existing_problems = set()

    for json_file in json_dir.glob("*.json"):
        try:
            with open(json_file, "r") as f:
                data = json.load(f)
                problem_number = int(data.get("problem_number", 0))
                if problem_number > 0:
                    existing_problems.add(problem_number)
        except (json.JSONDecodeError, ValueError, KeyError):
            continue

    return existing_problems
