#!/usr/bin/env python3

import json
from pathlib import Path

def count_test_cases(json_data):
    """Count total test cases across all test methods."""
    total = 0

    # Handle both direct test_methods and nested _test_methods.list
    test_methods = json_data.get("test_methods", [])
    if not test_methods and "_test_methods" in json_data:
        test_methods = json_data["_test_methods"].get("list", [])

    for method in test_methods:
        test_cases = method.get("test_cases", "")
        if test_cases.strip():
            # Count tuples/lists in test_cases string
            total += max(test_cases.count("("), test_cases.count("["))
    return total

def main():
    json_dir = Path(".templates/leetcode/json")
    files_with_few_tests = []

    for json_file in json_dir.glob("*.json"):
        try:
            with open(json_file) as f:
                data = json.load(f)

            test_count = count_test_cases(data)
            if test_count <= 10:
                files_with_few_tests.append((json_file.name, test_count))
        except Exception as e:
            print(f"Error reading {json_file.name}: {e}")

    # Sort by test count
    files_with_few_tests.sort(key=lambda x: x[1])

    print(f"Files with ≤10 test cases ({len(files_with_few_tests)} total):")
    for filename, count in files_with_few_tests:
        print(f"{filename}: {count} test cases")

if __name__ == "__main__":
    main()
