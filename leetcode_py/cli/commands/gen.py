import json
from pathlib import Path

import typer

from leetcode_py.tools.generator import generate_problem

from ..utils.problem_finder import (
    find_problem_by_number,
    find_problems_by_tag,
    get_all_problems,
    get_problem_json_path,
)
from ..utils.resources import get_template_path
from ..utils.tag_helpers import get_available_tags_help


def _get_problem_difficulty(problem_name: str) -> str | None:
    json_path = get_problem_json_path(problem_name)
    if not json_path.exists():
        return None

    try:
        with open(json_path) as f:
            data = json.load(f)
        return data.get("difficulty")
    except Exception:
        return None


def _validate_single_option(
    problem_nums: list[int],
    problem_slugs: list[str],
    problem_tag: str | None,
    all_problems: bool,
) -> None:
    options_count = sum(
        [
            len(problem_nums) > 0,
            len(problem_slugs) > 0,
            problem_tag is not None,
            all_problems,
        ]
    )

    if options_count != 1:
        typer.echo(
            "Error: Exactly one of --problem-num, --problem-slug, --problem-tag, or --all is required",
            err=True,
        )
        raise typer.Exit(1)


def _resolve_by_numbers(problem_nums: list[int]) -> list[str]:
    problems = []
    for num in problem_nums:
        problem_name = find_problem_by_number(num)
        if not problem_name:
            typer.echo(f"Error: Problem number {num} not found", err=True)
            raise typer.Exit(1)
        problems.append(problem_name)
    return problems


def _resolve_by_tag(problem_tag: str) -> list[str]:
    problems = find_problems_by_tag(problem_tag)
    if not problems:
        typer.echo(f"Error: No problems found with tag '{problem_tag}'", err=True)
        raise typer.Exit(1)
    typer.echo(f"Found {len(problems)} problems with tag '{problem_tag}'")
    return problems


def _filter_by_difficulty(problems: list[str], difficulty: str) -> list[str]:
    filtered_problems = []
    for problem_name in problems:
        problem_difficulty = _get_problem_difficulty(problem_name)
        if problem_difficulty and problem_difficulty.lower() == difficulty.lower():
            filtered_problems.append(problem_name)
    typer.echo(f"Filtered to {len(filtered_problems)} problems with difficulty '{difficulty}'")
    return filtered_problems


def resolve_problems(
    problem_nums: list[int],
    problem_slugs: list[str],
    problem_tag: str | None,
    difficulty: str | None,
    all_problems: bool,
) -> list[str]:
    _validate_single_option(problem_nums, problem_slugs, problem_tag, all_problems)

    if problem_nums:
        problems = _resolve_by_numbers(problem_nums)
    elif problem_slugs:
        problems = problem_slugs
    elif problem_tag:
        problems = _resolve_by_tag(problem_tag)
    else:  # all_problems
        problems = get_all_problems()
        typer.echo(f"Found {len(problems)} problems")

    if difficulty:
        problems = _filter_by_difficulty(problems, difficulty)

    return problems


def generate(
    problem_nums: list[int] = typer.Option(
        [], "-n", "--problem-num", help="Problem number(s) (use multiple -n flags)"
    ),
    problem_slugs: list[str] = typer.Option(
        [], "-s", "--problem-slug", help="Problem slug(s) (use multiple -s flags)"
    ),
    problem_tag: str | None = typer.Option(
        None,
        "-t",
        "--problem-tag",
        help="Problem tag (bulk). Available tags: " + get_available_tags_help(),
    ),
    difficulty: str | None = typer.Option(
        None, "-d", "--difficulty", help="Filter by difficulty (Easy/Medium/Hard)"
    ),
    all_problems: bool = typer.Option(False, "--all", help="Generate all problems"),
    output: str = typer.Option(".", "-o", "--output", help="Output directory"),
    force: bool = typer.Option(False, "--force", help="Force overwrite existing files"),
):
    template_dir = get_template_path()
    output_dir = Path(output)

    # Determine which problems to generate
    problems = resolve_problems(problem_nums, problem_slugs, problem_tag, difficulty, all_problems)

    # Generate each problem
    success_count = 0
    failed_count = 0

    for problem_name in problems:
        json_path = get_problem_json_path(problem_name)
        if not json_path.exists():
            typer.echo(f"Warning: JSON file not found for problem '{problem_name}', skipping", err=True)
            failed_count += 1
            continue

        try:
            generate_problem(json_path, template_dir, output_dir, force)
            success_count += 1
        except typer.Exit:
            # typer.Exit was already handled with proper error message
            failed_count += 1
        except Exception as e:
            typer.echo(f"Error generating problem '{problem_name}': {e}", err=True)
            failed_count += 1

    typer.echo(f"Completed: {success_count} successful, {failed_count} failed")

    if failed_count > 0:
        raise typer.Exit(1)
