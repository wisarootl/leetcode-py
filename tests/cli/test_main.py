from typer.testing import CliRunner

from leetcode_py.cli.main import app

runner = CliRunner()


def test_cli_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "LeetCode problem generator" in result.stdout
    assert "Generate and list LeetCode problems" in result.stdout


def test_cli_version():
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "lcpy version" in result.stdout


def test_cli_version_short():
    result = runner.invoke(app, ["-V"])
    assert result.exit_code == 0
    assert "lcpy version" in result.stdout


def test_cli_no_args():
    result = runner.invoke(app, [])
    assert result.exit_code == 0
    assert "Usage:" in result.stdout


def test_scrape_command():
    result = runner.invoke(app, ["scrape"])
    assert result.exit_code == 0
    assert "scrape command - coming soon!" in result.stdout


def test_list_command():
    result = runner.invoke(app, ["list"])
    assert result.exit_code == 0
    assert "list command - coming soon!" in result.stdout


def test_invalid_command():
    result = runner.invoke(app, ["invalid"])
    assert result.exit_code == 2
    # Check stderr instead of stdout for error messages
    assert "No such command" in result.stderr or "invalid" in result.stderr
