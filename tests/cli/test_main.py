import pytest
from typer.testing import CliRunner

from leetcode_py.cli.main import app

runner = CliRunner()


def test_cli_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "LeetCode problem generator" in result.stdout
    assert "gen" in result.stdout
    assert "scrape" in result.stdout
    assert "list" in result.stdout


def test_cli_version():
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "lcpy version" in result.stdout


def test_cli_version_short():
    result = runner.invoke(app, ["-V"])
    assert result.exit_code == 0
    assert "lcpy version" in result.stdout


@pytest.mark.parametrize("command", ["gen", "scrape", "list"])
def test_command_help(command):
    result = runner.invoke(app, [command, "--help"])
    assert result.exit_code == 0
    assert "Usage:" in result.stdout


def test_invalid_command():
    result = runner.invoke(app, ["invalid"])
    assert result.exit_code != 0


def test_no_args_shows_help():
    result = runner.invoke(app, [])
    assert result.exit_code == 0
    assert "LeetCode problem generator" in result.stdout
    assert "Commands" in result.stdout


def test_cli_structure():
    """Test that all expected commands are available."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0

    # Check all main commands are listed
    commands = ["gen", "scrape", "list"]
    for cmd in commands:
        assert cmd in result.stdout


def test_version_format():
    """Test version output format."""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0

    # Should contain version info
    output = result.stdout.strip()
    assert output.startswith("lcpy version")
    assert len(output.split()) >= 3  # "lcpy version X.Y.Z"
