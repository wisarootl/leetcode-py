import tempfile
from pathlib import Path

from typer.testing import CliRunner

from leetcode_py.cli.main import app

runner = CliRunner()


def test_gen_help():
    result = runner.invoke(app, ["gen", "--help"])
    assert result.exit_code == 0
    assert "--problem-num" in result.stdout
    assert "--problem-slug" in result.stdout
    assert "--problem-tag" in result.stdout


def test_gen_no_options():
    result = runner.invoke(app, ["gen"])
    assert result.exit_code == 1
    assert "Exactly one of --problem-num, --problem-slug, or --problem-tag is required" in result.stderr


def test_gen_multiple_options():
    result = runner.invoke(app, ["gen", "-n", "1", "-s", "two-sum"])
    assert result.exit_code == 1
    assert "Exactly one of --problem-num, --problem-slug, or --problem-tag is required" in result.stderr


def test_gen_by_number():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = runner.invoke(app, ["gen", "-n", "1", "-o", temp_dir, "--force"])
        assert result.exit_code == 0
        assert "Generated problem: two_sum" in result.stdout

        # Check files were created
        problem_dir = Path(temp_dir) / "two_sum"
        assert problem_dir.exists()
        assert (problem_dir / "solution.py").exists()
        assert (problem_dir / "test_solution.py").exists()


def test_gen_by_slug():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = runner.invoke(app, ["gen", "-s", "valid_palindrome", "-o", temp_dir, "--force"])
        assert result.exit_code == 0
        assert "Generated problem: valid_palindrome" in result.stdout

        # Check files were created
        problem_dir = Path(temp_dir) / "valid_palindrome"
        assert problem_dir.exists()
        assert (problem_dir / "solution.py").exists()


def test_gen_by_tag():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = runner.invoke(app, ["gen", "-t", "test", "-o", temp_dir, "--force"])
        assert result.exit_code == 0
        assert "Found" in result.stdout
        assert "problems with tag 'test'" in result.stdout
        assert "Generated problem:" in result.stdout


def test_gen_invalid_number():
    result = runner.invoke(app, ["gen", "-n", "99999"])
    assert result.exit_code == 1
    assert "Problem number 99999 not found" in result.stderr


def test_gen_invalid_tag():
    result = runner.invoke(app, ["gen", "-t", "nonexistent"])
    assert result.exit_code == 1
    assert "No problems found with tag 'nonexistent'" in result.stderr
