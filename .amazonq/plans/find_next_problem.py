#!/usr/bin/env python3
"""Find next problem to update from json_old to json."""

from pathlib import Path


def find_next_problem():
    """Return next problem from json_old that's not in json."""
    json_old_dir = Path(".templates/leetcode/json_old")
    json_dir = Path(".templates/leetcode/json")

    if not json_old_dir.exists():
        return "json_old directory not found"

    if not json_dir.exists():
        return "json directory not found"

    # Get all problems in json_old
    old_problems = {f.stem for f in json_old_dir.glob("*.json")}

    # Get all problems in json
    new_problems = {f.stem for f in json_dir.glob("*.json")}

    # Find problems that need updating
    missing_problems = old_problems - new_problems

    if not missing_problems:
        return "All problems updated!"

    # Return first missing problem (sorted for consistency)
    return sorted(missing_problems)[0]


if __name__ == "__main__":
    print(find_next_problem())
