from pathlib import Path

import typer

from leetcode_py.tools.generator import generate_problem

from ..utils.problem_finder import find_problem_by_number, find_problems_by_tag, get_problem_json_path
from ..utils.resources import get_template_path


def resolve_problems(
    problem_num: int | None, problem_slug: str | None, problem_tag: str | None
) -> list[str]:
    if problem_num is not None:
        problem_name = find_problem_by_number(problem_num)
        if not problem_name:
            typer.echo(f"Error: Problem number {problem_num} not found", err=True)
            raise typer.Exit(1)
        return [problem_name]
    elif problem_slug is not None:
        return [problem_slug]
    elif problem_tag is not None:
        problems = find_problems_by_tag(problem_tag)
        if not problems:
            typer.echo(f"Error: No problems found with tag '{problem_tag}'", err=True)
            raise typer.Exit(1)
        typer.echo(f"Found {len(problems)} problems with tag '{problem_tag}'")
        return problems

    typer.echo(
        "Error: Exactly one of --problem-num, --problem-slug, or --problem-tag is required", err=True
    )
    raise typer.Exit(1)


def generate(
    problem_num: int | None = typer.Option(None, "-n", "--problem-num", help="Problem number"),
    problem_slug: str | None = typer.Option(None, "-s", "--problem-slug", help="Problem slug"),
    problem_tag: str | None = typer.Option(None, "-t", "--problem-tag", help="Problem tag (bulk)"),
    output: str = typer.Option("leetcode", "-o", "--output", help="Output directory"),
    force: bool = typer.Option(False, "--force", help="Force overwrite existing files"),
):
    options_provided = sum(x is not None for x in [problem_num, problem_slug, problem_tag])
    if options_provided != 1:
        typer.echo(
            "Error: Exactly one of --problem-num, --problem-slug, or --problem-tag is required", err=True
        )
        raise typer.Exit(1)

    template_dir = get_template_path()
    output_dir = Path(output)

    # Determine which problems to generate
    problems = resolve_problems(problem_num, problem_slug, problem_tag)

    # Generate each problem
    for problem_name in problems:
        json_path = get_problem_json_path(problem_name)
        if not json_path.exists():
            typer.echo(f"Warning: JSON file not found for problem '{problem_name}', skipping", err=True)
            continue

        try:
            generate_problem(json_path, template_dir, output_dir, force)
        except Exception as e:
            typer.echo(f"Error generating problem '{problem_name}': {e}", err=True)
            if len(problems) == 1:
                raise typer.Exit(1)
