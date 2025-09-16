import json
from pathlib import Path

import black
import typer
from cookiecutter.main import cookiecutter

from leetcode_py.cli.utils.problem_finder import get_tags_for_problem


def load_json_data(json_path: Path) -> dict:
    if not json_path.exists():
        typer.echo(f"Error: {json_path} not found", err=True)
        raise typer.Exit(1)

    try:
        with open(json_path) as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        typer.echo(f"Error reading {json_path}: {e}", err=True)
        raise typer.Exit(1)


def check_problem_exists(problem_name: str, output_dir: Path, force: bool) -> None:
    if not force:
        problem_dir = output_dir / problem_name
        if problem_dir.exists():
            typer.echo(
                f"Error: Problem '{problem_name}' already exists. Use --force to overwrite.", err=True
            )
            raise typer.Exit(1)


def format_python_files(problem_dir: Path) -> None:
    if not problem_dir.exists():
        return

    py_files = list(problem_dir.glob("*.py"))
    for py_file in py_files:
        try:
            content = py_file.read_text()
            formatted = black.format_str(content, mode=black.FileMode())
            py_file.write_text(formatted)
        except Exception:
            # Silently continue if formatting fails
            pass


def merge_tags(data: dict) -> dict:
    """Merge tags from get_tags_for_problem with existing JSON tags."""
    problem_name = data.get("problem_name", "")
    if not problem_name:
        return data

    # Get tags from tag system
    system_tags = get_tags_for_problem(problem_name)

    # Get existing tags from JSON
    existing_tags = data.get("_tags", {}).get("list", [])

    # Merge and deduplicate tags
    all_tags = list(set(system_tags + existing_tags))

    # Update data with merged tags
    if all_tags:
        data["_tags"] = {"list": all_tags}

    return data


def generate_from_template(data: dict, template_dir: Path, output_dir: Path) -> None:
    """Generate problem files using cookiecutter template."""
    try:
        # Merge tags before generating
        data = merge_tags(data)

        cookiecutter(
            str(template_dir),
            extra_context=data,
            no_input=True,
            overwrite_if_exists=True,
            output_dir=str(output_dir),
        )
        problem_name = data.get("problem_name", "unknown")
        format_python_files(output_dir / problem_name)
        typer.echo(f"✅ Generated problem: {problem_name}")
    except Exception as e:
        typer.echo(f"Error generating template: {e}", err=True)
        raise typer.Exit(1)


def generate_problem(json_path: Path, template_dir: Path, output_dir: Path, force: bool = False) -> None:
    data = load_json_data(json_path)
    problem_name = data.get("problem_name", "unknown")
    check_problem_exists(problem_name, output_dir, force)
    generate_from_template(data, template_dir, output_dir)
