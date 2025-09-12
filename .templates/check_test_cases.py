#!/usr/bin/env python3

import json
from pathlib import Path
from typing import Optional
import typer


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
            # Parse the test_cases string to count actual test cases
            try:
                # Remove outer brackets and split by top-level commas
                cases_str = test_cases.strip()
                if cases_str.startswith("[") and cases_str.endswith("]"):
                    cases_str = cases_str[1:-1]  # Remove outer brackets

                # Count test cases by counting commas at parenthesis depth 0
                depth = 0
                case_count = 1 if cases_str.strip() else 0

                for char in cases_str:
                    if char in "([{":
                        depth += 1
                    elif char in ")]}":
                        depth -= 1
                    elif char == "," and depth == 0:
                        case_count += 1

                total += case_count
            except Exception:
                # Fallback to old method if parsing fails
                total += test_cases.count("(") - test_cases.count("([") + test_cases.count("[(")
    return total


def main(
    threshold: int = typer.Option(
        10, "--threshold", "-t", help="Show files with test cases <= threshold"
    ),
    max_results: str = typer.Option(
        1, "--max", "-m", help="Maximum number of results to show ('none' for no limit)"
    ),
):
    """Check test case counts in LeetCode JSON templates."""
    json_dir = Path(".templates/leetcode/json")
    all_files = []

    for json_file in json_dir.glob("*.json"):
        try:
            with open(json_file) as f:
                data = json.load(f)

            test_count = count_test_cases(data)
            all_files.append((json_file.name, test_count))
        except Exception as e:
            typer.echo(f"Error reading {json_file.name}: {e}", err=True)

    # Sort by test count
    all_files.sort(key=lambda x: x[1])

    # Filter by threshold
    filtered_files = [f for f in all_files if f[1] <= threshold]

    # Apply max results limit
    if max_results.lower() not in ["none", "null", "-1"]:
        try:
            max_count = int(max_results)
            if max_count > 0:
                filtered_files = filtered_files[:max_count]
        except ValueError:
            typer.echo(f"Invalid max_results value: {max_results}", err=True)
            raise typer.Exit(1)

    typer.echo(f"Problems with ≤{threshold} test cases ({len(filtered_files)} total):")
    for filename, count in filtered_files:
        typer.echo(f"{filename}: {count} test cases")

    # Exit with non-zero code if any files found
    if filtered_files:
        raise typer.Exit(1)


if __name__ == "__main__":
    typer.run(main)
