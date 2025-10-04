#!/usr/bin/env python3

import json
from typing import Any

import typer

from leetcode_py.cli.utils.resources import get_problems_json_path


def count_test_cases_for_problem(json_data: dict[str, Any]) -> int:
    """Count total test cases across all test methods for a problem."""
    total = 0

    # Handle both direct test_methods and nested _test_methods.list
    test_methods = json_data.get("test_methods", [])
    if not test_methods and "_test_methods" in json_data:
        test_methods = json_data["_test_methods"].get("list", [])

    for method in test_methods:
        test_cases = method.get("test_cases", "")

        if isinstance(test_cases, dict) and "list" in test_cases:
            total += len(test_cases["list"])
    return total


def check_test_cases(
    threshold: int = typer.Option(
        10, "--threshold", "-t", help="Show problems with test cases <= threshold"
    ),
    max_results: str = typer.Option(
        "10", "--max", "-m", help="Maximum number of results to show ('none' for no limit)"
    ),
) -> None:
    """Check test case counts in LeetCode problems."""
    problems_dir = get_problems_json_path()
    all_problems: list[tuple[str, int]] = []
    errors_found = False

    for problem_file in problems_dir.glob("*.json"):
        try:
            with open(problem_file) as f:
                data = json.load(f)

            test_count = count_test_cases_for_problem(data)
            all_problems.append((problem_file.name, test_count))
        except Exception as e:
            typer.echo(f"Error reading problem {problem_file.name}: {e}", err=True)
            errors_found = True
            # Continue processing other files instead of stopping

    # Don't exit immediately - show results for files that worked
    if errors_found:
        typer.echo("\nNote: Some files had errors and were skipped.", err=True)

    # Sort by test count
    all_problems.sort(key=lambda x: x[1])

    # Filter by threshold
    filtered_problems = [p for p in all_problems if p[1] <= threshold]

    # Apply max results limit
    if max_results.lower() not in ["none", "null", "-1"]:
        try:
            max_count = int(max_results)
            if max_count > 0:
                filtered_problems = filtered_problems[:max_count]
        except ValueError:
            typer.echo(f"Invalid max_results value: {max_results}", err=True)
            raise typer.Exit(1)

    typer.echo(f"Problems with ≤{threshold} test cases ({len(filtered_problems)} total):")
    for problem_name, count in filtered_problems:
        typer.echo(f"{problem_name}: {count} test cases")

    # Exit with non-zero code if any problems found or if there were errors
    if filtered_problems or errors_found:
        raise typer.Exit(1)


app = typer.Typer()
app.command()(check_test_cases)

if __name__ == "__main__":
    app()
