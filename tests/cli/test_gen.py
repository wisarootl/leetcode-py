import re
import tempfile
from pathlib import Path

import pytest
from typer.testing import CliRunner

from leetcode_py.cli.main import app

runner = CliRunner()


def test_gen_help():
    result = runner.invoke(app, ["gen", "--help"])
    assert result.exit_code == 0
    # Remove ANSI color codes for reliable string matching
    clean_output = re.sub(r"\x1b\[[0-9;]*m", "", result.stdout)
    assert "--problem-num" in clean_output
    assert "--problem-slug" in clean_output
    assert "--problem-tag" in clean_output
    assert "--difficulty" in clean_output
    assert "--all" in clean_output


def test_gen_no_options():
    result = runner.invoke(app, ["gen"])
    assert result.exit_code == 1
    assert (
        "Exactly one of --problem-num, --problem-slug, --problem-tag, or --all is required"
        in result.stderr
    )


@pytest.mark.parametrize(
    "args",
    [
        ["-n", "1", "-s", "two-sum"],
        ["-n", "1", "-t", "grind-75"],
        ["-s", "two-sum", "-t", "grind-75"],
        ["-n", "1", "--all"],
    ],
)
def test_gen_multiple_options(args):
    result = runner.invoke(app, ["gen"] + args)
    assert result.exit_code == 1
    assert (
        "Exactly one of --problem-num, --problem-slug, --problem-tag, or --all is required"
        in result.stderr
    )


@pytest.mark.parametrize(
    "args,expected_problems,expected_count",
    [
        (["-n", "1"], ["two_sum"], "1 successful, 0 failed"),
        (["-n", "1", "-n", "125"], ["two_sum", "valid_palindrome"], "2 successful, 0 failed"),
    ],
)
def test_gen_by_numbers(args, expected_problems, expected_count):
    with tempfile.TemporaryDirectory() as temp_dir:
        result = runner.invoke(app, ["gen"] + args + ["-o", temp_dir, "--force"])
        assert result.exit_code == 0

        for problem in expected_problems:
            assert f"Generated problem: {problem}" in result.stdout
            problem_dir = Path(temp_dir) / problem
            assert problem_dir.exists()
            assert (problem_dir / "solution.py").exists()

        assert f"Completed: {expected_count}" in result.stdout


@pytest.mark.parametrize(
    "args,expected_problems,expected_count",
    [
        (["-s", "valid_palindrome"], ["valid_palindrome"], "1 successful, 0 failed"),
        (
            ["-s", "two_sum", "-s", "valid_palindrome"],
            ["two_sum", "valid_palindrome"],
            "2 successful, 0 failed",
        ),
    ],
)
def test_gen_by_slugs(args, expected_problems, expected_count):
    with tempfile.TemporaryDirectory() as temp_dir:
        result = runner.invoke(app, ["gen"] + args + ["-o", temp_dir, "--force"])
        assert result.exit_code == 0

        for problem in expected_problems:
            assert f"Generated problem: {problem}" in result.stdout
            problem_dir = Path(temp_dir) / problem
            assert problem_dir.exists()
            assert (problem_dir / "solution.py").exists()

        assert f"Completed: {expected_count}" in result.stdout


def test_gen_by_tag():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = runner.invoke(app, ["gen", "-t", "grind-75", "-o", temp_dir, "--force"])
        assert result.exit_code == 0
        assert "Found" in result.stdout
        assert "problems with tag 'grind-75'" in result.stdout
        assert "Generated problem:" in result.stdout
        assert "successful" in result.stdout


def test_gen_with_difficulty_filter():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = runner.invoke(app, ["gen", "-t", "grind-75", "-d", "Easy", "-o", temp_dir, "--force"])
        assert result.exit_code == 0
        assert "Found" in result.stdout
        assert "Filtered to" in result.stdout
        assert "problems with difficulty 'Easy'" in result.stdout


@pytest.mark.parametrize(
    "args,expected_error",
    [
        (["-n", "99999"], "Problem number 99999 not found"),
        (["-t", "nonexistent"], "No problems found with tag 'nonexistent'"),
    ],
)
def test_gen_invalid_inputs(args, expected_error):
    result = runner.invoke(app, ["gen"] + args)
    assert result.exit_code == 1
    assert expected_error in result.stderr


def test_gen_existing_problem_without_force():
    with tempfile.TemporaryDirectory() as temp_dir:
        # First generation should succeed
        result1 = runner.invoke(app, ["gen", "-n", "1", "-o", temp_dir, "--force"])
        assert result1.exit_code == 0

        # Second generation without --force should fail
        result2 = runner.invoke(app, ["gen", "-n", "1", "-o", temp_dir])
        assert result2.exit_code == 1
        assert "already exists" in result2.stderr
        assert "Completed: 0 successful, 1 failed" in result2.stdout


def test_gen_mixed_success_failure():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create one problem first
        runner.invoke(app, ["gen", "-n", "1", "-o", temp_dir, "--force"])

        # Try to generate existing + new problem without force
        result = runner.invoke(app, ["gen", "-n", "1", "-n", "125", "-o", temp_dir])
        assert result.exit_code == 1
        assert "already exists" in result.stderr
        assert "Generated problem: valid_palindrome" in result.stdout
        assert "Completed: 1 successful, 1 failed" in result.stdout


def test_gen_default_output_directory():
    # Test that default output is current directory
    result = runner.invoke(app, ["gen", "--help"])
    assert result.exit_code == 0
    # The help should show the default value
    assert "Output directory" in result.stdout
