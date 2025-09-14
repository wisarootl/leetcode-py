"""Tests for list command."""

from typer.testing import CliRunner

from leetcode_py.cli.main import app

runner = CliRunner()


def test_list_help():
    result = runner.invoke(app, ["list", "--help"])
    assert result.exit_code == 0
    assert "--tag" in result.stdout
    assert "--difficulty" in result.stdout


def test_list_all_problems():
    result = runner.invoke(app, ["list"])
    assert result.exit_code == 0
    assert "LeetCode Problems" in result.stdout
    assert "Number" in result.stdout
    assert "Title" in result.stdout
    assert "Difficulty" in result.stdout


def test_list_by_tag():
    result = runner.invoke(app, ["list", "-t", "grind-75"])
    assert result.exit_code == 0
    assert "LeetCode Problems" in result.stdout
    assert "Two Sum" in result.stdout


def test_list_by_difficulty():
    result = runner.invoke(app, ["list", "-d", "Easy"])
    assert result.exit_code == 0
    assert "LeetCode Problems" in result.stdout
    assert "Easy" in result.stdout
    assert "Two Sum" in result.stdout


def test_list_invalid_tag():
    result = runner.invoke(app, ["list", "-t", "nonexistent-tag"])
    assert result.exit_code == 1
    assert "No problems found with tag 'nonexistent-tag'" in result.stderr


def test_list_combined_filters():
    result = runner.invoke(app, ["list", "-t", "grind-75", "-d", "Easy"])
    assert result.exit_code == 0
    assert "LeetCode Problems" in result.stdout
    assert "Two Sum" in result.stdout
