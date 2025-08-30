#!/usr/bin/env python3
"""Reusable file comparison tool for template validation."""

import difflib
from pathlib import Path

import typer


def compare_files(file1: Path, file2: Path, label1: str, label2: str) -> bool:
    """Compare two files and show differences. Returns True if identical."""
    print(f"\n{'='*60}")
    print(f"COMPARING: {file1.name}")
    print(f"{label1}: {file1}")
    print(f"{label2}: {file2}")
    print(f"{'='*60}")

    if not file1.exists():
        print(f"❌ MISSING: {file1} does not exist")
        return False

    if not file2.exists():
        print(f"❌ MISSING: {file2} does not exist")
        return False

    content1 = file1.read_text().splitlines(keepends=True)
    content2 = file2.read_text().splitlines(keepends=True)

    diff = list(
        difflib.unified_diff(
            content1,
            content2,
            fromfile=f"{label1}/{file1.name}",
            tofile=f"{label2}/{file2.name}",
            lineterm="",
        )
    )

    if not diff:
        print("✅ FILES IDENTICAL")
        return True
    else:
        print("❌ DIFFERENCES FOUND:")
        for line in diff:
            print(line)
        return False


def main(
    mode: str = typer.Argument(help="Compare template files or generated files (template|generated)"),
    problem: str = typer.Option("invert_binary_tree", help="Problem name for comparison"),
):
    """Compare files for template validation."""
    if mode not in ["template", "generated"]:
        print(f"❌ ERROR: Invalid mode '{mode}'. Use 'template' or 'generated'")
        return

    base_dir = Path(__file__).parent.parent.parent

    files_to_compare = ["solution.py", "tests.py", "README.md", "playground.ipynb", "__init__.py"]

    if mode == "template":
        # Compare reference vs template source
        dir1 = base_dir / "leetcode" / ".example" / problem
        dir2 = base_dir / ".templates" / "leetcode" / ".example" / "{{cookiecutter.problem_name}}"
        label1, label2 = "Reference", "Template"
        print("TEMPLATE SOURCE ANALYSIS")

    elif mode == "generated":
        # Compare reference vs currently generated
        dir1 = base_dir / "leetcode" / ".example" / problem
        dir2 = base_dir / "leetcode" / problem
        label1, label2 = "Reference", "Generated"
        print("GENERATED FILES VALIDATION")

        if not dir2.exists():
            print(f"\n❌ ERROR: Generated directory does not exist: {dir2}")
            print(f"Run: make p-gen PROBLEM={problem}")
            return

    print(f"{label1}: {dir1}")
    print(f"{label2}: {dir2}")

    identical_count = 0
    for filename in files_to_compare:
        file1 = dir1 / filename
        file2 = dir2 / filename
        if compare_files(file1, file2, label1, label2):
            identical_count += 1

    print(f"\n{'='*60}")
    print(f"SUMMARY: {identical_count}/{len(files_to_compare)} files identical")
    print("- ✅ = Files identical")
    print("- ❌ = Differences found or missing files")


if __name__ == "__main__":
    typer.run(main)
