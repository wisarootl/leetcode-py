import json
import re

import pytest
from typer.testing import CliRunner

from leetcode_py.cli.main import app

runner = CliRunner()


def test_scrape_help():
    result = runner.invoke(app, ["scrape", "--help"])
    assert result.exit_code == 0
    # Remove ANSI color codes for reliable string matching
    clean_output = re.sub(r"\x1b\[[0-9;]*m", "", result.stdout)
    assert "--problem-num" in clean_output
    assert "--problem-slug" in clean_output


def test_scrape_no_options():
    result = runner.invoke(app, ["scrape"])
    assert result.exit_code == 1
    assert "Exactly one of --problem-num or --problem-slug is required" in result.stderr


def test_scrape_multiple_options():
    result = runner.invoke(app, ["scrape", "-n", "1", "-s", "two-sum"])
    assert result.exit_code == 1
    assert "Exactly one of --problem-num or --problem-slug is required" in result.stderr


@pytest.mark.parametrize(
    "args, expected_number, expected_title, expected_slug, expected_difficulty",
    [
        (["-n", "1"], "1", "Two Sum", "two-sum", "Easy"),
        (["-s", "two-sum"], "1", "Two Sum", "two-sum", "Easy"),
    ],
)
def test_scrape_success_real_api(
    args, expected_number, expected_title, expected_slug, expected_difficulty
):
    result = runner.invoke(app, ["scrape"] + args)

    assert result.exit_code == 0

    # Parse JSON output
    data = json.loads(result.stdout)

    # Verify problem data
    assert data["number"] == expected_number
    assert data["title"] == expected_title
    assert data["slug"] == expected_slug
    assert data["difficulty"] == expected_difficulty

    # Verify structure for number-based test only
    if "-n" in args:
        assert "Array" in data["topics"]
        assert "Hash Table" in data["topics"]
        assert data["description"]  # Should have description
        assert data["examples"]  # Should have examples
        assert data["constraints"]  # Should have constraints


@pytest.mark.parametrize(
    "args, expected_error",
    [
        (["-n", "999999"], "Problem number 999999 not found"),
        (["-s", "nonexistent-problem"], "Problem slug 'nonexistent-problem' not found"),
    ],
)
def test_scrape_not_found_real_api(args, expected_error):
    result = runner.invoke(app, ["scrape"] + args)

    assert result.exit_code == 1
    assert expected_error in result.stderr
