#!/usr/bin/env python3
"""Generate LeetCode problem from JSON using cookiecutter."""

import json
from pathlib import Path

import typer
from cookiecutter.main import cookiecutter


def check_and_prompt_tags(data: dict) -> dict:
    """Check if tags are empty and prompt user for common options."""
    import sys

    common_tags = ["grind-75", "blind-75", "neetcode-150", "top-interview"]

    if "tags" in data and (not data["tags"] or data["tags"] == []):
        if sys.stdin.isatty():  # Interactive terminal
            typer.echo("\n📋 No tags specified. Would you like to add any common tags?")
            typer.echo("Available options:")
            for i, tag in enumerate(common_tags, 1):
                typer.echo(f"  {i}. {tag}")
            typer.echo("  0. Skip (no tags)")

            choices_input = typer.prompt("Select options (comma-separated, e.g. '1,2' or '0' to skip)")

            try:
                choices = [int(x.strip()) for x in choices_input.split(",")]
                selected_tags = []

                for choice in choices:
                    if choice == 0:
                        selected_tags = []
                        break
                    elif 1 <= choice <= len(common_tags):
                        tag = common_tags[choice - 1]
                        if tag not in selected_tags:
                            selected_tags.append(tag)

                data["tags"] = selected_tags
                if selected_tags:
                    typer.echo(f"✅ Added tags: {', '.join(selected_tags)}")
                else:
                    typer.echo("✅ No tags added")

            except ValueError:
                typer.echo("⚠️  Invalid input, skipping tags")
                data["tags"] = []

    return data


def convert_arrays_to_nested(data: dict) -> dict:
    """Convert array fields to cookiecutter-friendly nested format."""
    extra_context = data.copy()
    array_fields = ["examples", "test_cases", "tags"]
    for field in array_fields:
        if field in data and isinstance(data[field], list):
            extra_context[f"_{field}"] = {"list": data[field]}
            del extra_context[field]
    return extra_context


def check_overwrite_permission(question_name: str, force: bool) -> None:
    """Check if user wants to overwrite existing problem."""
    import sys

    if force:
        return

    output_dir = Path(__file__).parent.parent.parent / "leetcode"
    problem_dir = output_dir / question_name

    if not problem_dir.exists():
        return

    typer.echo(f"⚠️  Warning: Question '{question_name}' already exists in leetcode/", err=True)
    typer.echo("This will overwrite existing files. Use --force to skip this check.", err=True)

    if sys.stdin.isatty():  # Interactive terminal
        confirm = typer.confirm("Continue?")
        if not confirm:
            typer.echo("Cancelled.")
            raise typer.Exit(1)
    else:  # Non-interactive mode
        typer.echo("Non-interactive mode: use --force to overwrite.", err=True)
        raise typer.Exit(1)


def generate_problem(json_file: str, force: bool = False) -> None:
    """Generate LeetCode problem from JSON file."""
    json_path = Path(json_file)
    if not json_path.exists():
        typer.echo(f"Error: {json_file} not found", err=True)
        raise typer.Exit(1)

    # Load JSON data
    with open(json_path) as f:
        data = json.load(f)

    # Check and prompt for tags if empty
    data = check_and_prompt_tags(data)

    # Save updated data back to JSON file
    with open(json_path, 'w') as f:
        json.dump(data, f, indent=4)

    # Convert arrays to cookiecutter-friendly nested format
    extra_context = convert_arrays_to_nested(data)

    # Check if problem already exists
    question_name = extra_context.get("question_name", "unknown")
    check_overwrite_permission(question_name, force)

    # Generate project using cookiecutter
    template_dir = Path(__file__).parent
    output_dir = template_dir.parent.parent / "leetcode"

    cookiecutter(
        str(template_dir),
        extra_context=extra_context,
        no_input=True,
        overwrite_if_exists=True,
        output_dir=str(output_dir),
    )

    typer.echo(f"✅ Generated problem: {question_name}")


if __name__ == "__main__":
    typer.run(generate_problem)
