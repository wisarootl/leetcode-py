"""List command for displaying available LeetCode problems."""

import typer
from rich.console import Console
from rich.table import Table

from ..utils.problem_finder import find_problems_by_tag, get_all_problems, get_tags_for_problem
from ..utils.tag_helpers import get_available_tags_help

console = Console()


def list_problems(
    tag: str | None = typer.Option(
        None, "-t", "--tag", help="Filter by tag. Available tags: " + get_available_tags_help()
    ),
    difficulty: str | None = typer.Option(
        None, "-d", "--difficulty", help="Filter by difficulty (Easy/Medium/Hard)"
    ),
) -> None:

    # Get problems based on filters
    if tag:
        problems = find_problems_by_tag(tag)
        if not problems:
            typer.echo(f"Error: No problems found with tag '{tag}'", err=True)
            raise typer.Exit(1)
    else:
        problems = get_all_problems()

    if not problems:
        typer.echo("No problems found", err=True)
        raise typer.Exit(1)

    # Create table
    table = Table(title="LeetCode Problems")
    table.add_column("Number", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta")
    table.add_column("Difficulty", style="green")
    table.add_column("Tags", style="blue")

    # Get problem data and sort by number
    problem_list = []
    for problem_name in problems:
        try:
            problem_data = _get_problem_data(problem_name)

            # Apply difficulty filter
            if difficulty and problem_data.get("difficulty", "").lower() != difficulty.lower():
                continue

            problem_list.append((problem_data, problem_name))
        except Exception:
            # Skip problems that can't be loaded
            continue

    # Sort by problem number (convert to int for proper numerical sorting)
    problem_list.sort(
        key=lambda x: int(x[0].get("number", "999999")) if x[0].get("number", "?").isdigit() else 999999
    )

    # Update table title with count
    table.title = f"LeetCode Problems ({len(problem_list)} problems)"

    # Add sorted problems to table
    for problem_data, problem_name in problem_list:
        table.add_row(
            problem_data.get("number", "?"),
            problem_data.get("title", problem_name),
            problem_data.get("difficulty", "Unknown"),
            ", ".join(problem_data.get("tags", [])),
        )

    console.print(table)


def _get_problem_data(problem_name: str) -> dict:
    import json

    from ..utils.problem_finder import get_problem_json_path

    json_path = get_problem_json_path(problem_name)
    if not json_path.exists():
        return {"title": problem_name, "tags": get_tags_for_problem(problem_name)}

    try:
        with open(json_path) as f:
            data = json.load(f)

        return {
            "number": data.get("problem_number", "?"),
            "title": data.get("problem_title", problem_name),
            "difficulty": data.get("difficulty", "Unknown"),
            "tags": get_tags_for_problem(problem_name),
        }
    except Exception:
        return {"title": problem_name, "tags": get_tags_for_problem(problem_name)}
