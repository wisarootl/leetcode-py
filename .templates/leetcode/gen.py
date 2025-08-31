#!/usr/bin/env python3
"""Compatibility wrapper for generator."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import typer
from leetcode_py.tools import TemplateGenerator

app = typer.Typer(help="Generate LeetCode problem templates")


@app.command()
def generate(
    json_file: str = typer.Argument(help="Path to JSON problem definition"),
    force: bool = typer.Option(False, "--force", help="Force overwrite existing files")
):
    """Generate LeetCode problem from JSON using cookiecutter."""
    generator = TemplateGenerator()
    template_dir = Path(__file__).parent
    generator.generate_problem(json_file, force, template_dir)


if __name__ == "__main__":
    app()
