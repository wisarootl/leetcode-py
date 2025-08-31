"""Template generation utilities for LeetCode problems."""

import json
import sys
from pathlib import Path
from typing import Any, Dict

import typer
from cookiecutter.main import cookiecutter


class TemplateGenerator:
    """Generator for LeetCode problem templates using cookiecutter."""

    def __init__(self):
        self.common_tags = ["grind-75", "blind-75", "neetcode-150", "top-interview"]

    def check_and_prompt_tags(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Check and prompt for tags if empty."""
        if "tags" in data and (not data["tags"] or data["tags"] == []):
            if sys.stdin.isatty():  # Interactive terminal
                typer.echo("\n📋 No tags specified. Would you like to add any common tags?")
                typer.echo("Available options:")
                for i, tag in enumerate(self.common_tags, 1):
                    typer.echo(f"  {i}. {tag}")
                typer.echo("  0. Skip (no tags)")

                choices_input = typer.prompt(
                    "Select options (comma-separated, e.g. '1,2' or '0' to skip)"
                )

                try:
                    choices = [int(x.strip()) for x in choices_input.split(",")]
                    selected_tags: list[str] = []

                    for choice in choices:
                        if choice == 0:
                            selected_tags = []
                            break
                        elif 1 <= choice <= len(self.common_tags):
                            tag = self.common_tags[choice - 1]
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

    def auto_set_dummy_return(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Auto-set dummy_return based on return_type."""
        if "dummy_return" not in data and "return_type" in data:
            return_type = data["return_type"]
            dummy_map = {"bool": "False", "int": "0", "str": '""', "float": "0.0", "None": "None"}

            if return_type in dummy_map:
                data["dummy_return"] = dummy_map[return_type]
            elif return_type.startswith("list["):
                data["dummy_return"] = "[]"
            elif return_type.startswith("dict["):
                data["dummy_return"] = "{}"
            elif return_type.startswith("set["):
                data["dummy_return"] = "set()"
            elif return_type.startswith("tuple["):
                data["dummy_return"] = "()"
            else:
                data["dummy_return"] = "None"

        return data

    def convert_arrays_to_nested(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Convert arrays to cookiecutter-friendly nested format."""
        extra_context = data.copy()
        array_fields = ["examples", "test_cases", "tags"]
        for field in array_fields:
            if field in data and isinstance(data[field], list):
                extra_context[f"_{field}"] = {"list": data[field]}
                del extra_context[field]
        return extra_context

    def check_overwrite_permission(self, problem_name: str, force: bool, template_dir: Path) -> None:
        """Check if problem exists and get overwrite permission."""
        if force:
            return

        output_dir = template_dir.parent.parent / "leetcode"
        problem_dir = output_dir / problem_name

        if not problem_dir.exists():
            return

        typer.echo(f"⚠️  Warning: Problem '{problem_name}' already exists in leetcode/", err=True)
        typer.echo("This will overwrite existing files. Use --force to skip this check.", err=True)

        if sys.stdin.isatty():  # Interactive terminal
            confirm = typer.confirm("Continue?")
            if not confirm:
                typer.echo("Cancelled.")
                raise typer.Exit(1)
        else:  # Non-interactive mode
            typer.echo("Non-interactive mode: use --force to overwrite.", err=True)
            raise typer.Exit(1)

    def generate_problem(
        self, json_file: str, force: bool = False, template_dir: Path | None = None
    ) -> None:
        """Generate problem from JSON using cookiecutter."""
        json_path = Path(json_file)
        if not json_path.exists():
            typer.echo(f"Error: {json_file} not found", err=True)
            raise typer.Exit(1)

        # Load JSON data
        with open(json_path) as f:
            data = json.load(f)

        # Process data
        data = self.check_and_prompt_tags(data)
        data = self.auto_set_dummy_return(data)

        # Save updated data back to JSON file
        with open(json_path, "w") as f:
            json.dump(data, f)

        # Convert arrays to cookiecutter-friendly nested format
        extra_context = self.convert_arrays_to_nested(data)

        # Check if problem already exists
        problem_name = extra_context.get("problem_name", "unknown")

        # Use provided template_dir or default
        if template_dir is None:
            template_dir = Path(__file__).parent.parent.parent / ".templates" / "leetcode"

        self.check_overwrite_permission(problem_name, force, template_dir)

        # Generate project using cookiecutter
        output_dir = template_dir.parent.parent / "leetcode"

        cookiecutter(
            str(template_dir),
            extra_context=extra_context,
            no_input=True,
            overwrite_if_exists=True,
            output_dir=str(output_dir),
        )

        typer.echo(f"✅ Generated problem: {problem_name}")
