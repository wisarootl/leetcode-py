#!/usr/bin/env python3
import sys
from pathlib import Path

import json5


def main():
    # Load tags file
    tags_file = Path("leetcode_py/cli/resources/leetcode/json/tags.json5")
    problems_dir = Path("leetcode_py/cli/resources/leetcode/json/problems")

    with open(tags_file) as f:
        tags_data = json5.load(f)

    # Get all existing problem JSON files
    existing_problems = {p.stem for p in problems_dir.glob("*.json")}

    # Check each tag's problems
    missing_problems = []
    for tag_name, problems in tags_data.items():
        if isinstance(problems, list):
            for problem in problems:
                if isinstance(problem, str):  # Skip dict entries like {"tag": "grind-75"}
                    if problem not in existing_problems:
                        missing_problems.append((tag_name, problem))

    if missing_problems:
        print("❌ Found problems in tags that don't have JSON files:")
        for tag_name, problem in missing_problems:
            print(f"  {tag_name}: {problem}")
        sys.exit(1)
    else:
        print("✅ All tagged problems have corresponding JSON files!")
        sys.exit(0)


if __name__ == "__main__":
    main()
