#!/usr/bin/env python3
"""Compatibility wrapper for scraper."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import json
from typing import Optional
import typer
from leetcode_py.tools import LeetCodeScraper

app = typer.Typer(help="Fetch LeetCode problem information")


@app.command()
def fetch(
    number: Optional[int] = typer.Option(None, "-n", "--number", help="Problem number (e.g., 1)"),
    slug: Optional[str] = typer.Option(None, "-s", "--slug", help="Problem slug (e.g., 'two-sum')"),
):
    """Fetch LeetCode problem information and return as JSON."""
    if not number and not slug:
        typer.echo("Error: Must provide either --number or --slug", err=True)
        raise typer.Exit(1)

    if number and slug:
        typer.echo("Error: Cannot provide both --number and --slug", err=True)
        raise typer.Exit(1)

    scraper = LeetCodeScraper()

    if number:
        problem = scraper.get_problem_by_number(number)
    else:
        problem = scraper.get_problem_by_slug(slug)

    if not problem:
        typer.echo(json.dumps({"error": "Problem not found"}))
        raise typer.Exit(1)

    formatted = scraper.format_problem_info(problem)
    typer.echo(json.dumps(formatted, indent=2))


if __name__ == "__main__":
    app()
