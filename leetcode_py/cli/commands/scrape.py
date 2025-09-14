import json

import typer

from leetcode_py.tools.scraper import LeetCodeScraper

ERROR_EXACTLY_ONE_OPTION = "Error: Exactly one of --problem-num or --problem-slug is required"


def fetch_and_format_problem(
    scraper: LeetCodeScraper, problem_num: int | None, problem_slug: str | None
) -> dict:
    if problem_num is not None:
        problem = scraper.get_problem_by_number(problem_num)
        if not problem:
            typer.echo(f"Error: Problem number {problem_num} not found", err=True)
            raise typer.Exit(1)
    elif problem_slug is not None:
        problem = scraper.get_problem_by_slug(problem_slug)
        if not problem:
            typer.echo(f"Error: Problem slug '{problem_slug}' not found", err=True)
            raise typer.Exit(1)
    else:
        typer.echo(ERROR_EXACTLY_ONE_OPTION, err=True)
        raise typer.Exit(1)

    return scraper.format_problem_info(problem)


def scrape(
    problem_num: int | None = typer.Option(None, "-n", "--problem-num", help="Problem number (e.g., 1)"),
    problem_slug: str | None = typer.Option(
        None, "-s", "--problem-slug", help="Problem slug (e.g., 'two-sum')"
    ),
) -> None:
    options_provided = sum(x is not None for x in [problem_num, problem_slug])
    if options_provided != 1:
        typer.echo(ERROR_EXACTLY_ONE_OPTION, err=True)
        raise typer.Exit(1)

    scraper = LeetCodeScraper()

    try:
        formatted = fetch_and_format_problem(scraper, problem_num, problem_slug)
        typer.echo(json.dumps(formatted, indent=2))

    except Exception as e:
        typer.echo(f"Error fetching problem: {e}", err=True)
        raise typer.Exit(1)
