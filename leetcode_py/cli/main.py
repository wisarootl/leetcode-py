from importlib.metadata import version

import typer

app = typer.Typer(
    help="LeetCode problem generator - Generate and list LeetCode problems",
)


def show_version():
    typer.echo(f"lcpy version {version('leetcode-py')}")
    raise typer.Exit()


@app.callback(invoke_without_command=True)
def main_callback(
    ctx: typer.Context,
    version: bool = typer.Option(False, "--version", "-V", help="Show version and exit"),
):
    if version:
        show_version()

    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help())
        raise typer.Exit()


# Placeholder commands for Phase 1 testing
@app.command()
def gen():
    typer.echo("gen command - coming soon!")


@app.command()
def scrape():
    typer.echo("scrape command - coming soon!")


@app.command()
def list():
    typer.echo("list command - coming soon!")


def main():
    app()
