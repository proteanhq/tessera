"""The cx command surface.

Every verb is registered so `cx --help` shows the full library interface from
day one. The implementations land in initiative epic E2, once the domain
reaches M2 and the savepoint recipes exist. Until then each verb exits with a
message saying where it is in the plan.
"""

from __future__ import annotations

import typer

app = typer.Typer(
    help="Walk the Tessera scenario library over Protean.",
    no_args_is_help=True,
    add_completion=False,
)

_PENDING = (
    "Not implemented yet. The cx tool is built in initiative epic E2, "
    "after the finance domain reaches milestone M2."
)


def _pending() -> None:
    typer.echo(_PENDING)
    raise typer.Exit(code=1)


@app.command("list")
def list_scenarios() -> None:
    """List the scenario library, grouped by feature and part."""
    _pending()


@app.command()
def map() -> None:
    """Show the story tree: each scenario's savepoint, story, and seen mark."""
    _pending()


@app.command()
def goto(scenario: str) -> None:
    """Rebuild to a scenario's state, land, and print its interest card."""
    _pending()


@app.command()
def play(scenario: str) -> None:
    """Run a scenario's full beat sequence, pausing for the verdict."""
    _pending()


@app.command()
def walk(
    from_: str = typer.Option(..., "--from", help="Scenario to start the tour from.")
) -> None:
    """Run the guided tour onward from a starting scenario."""
    _pending()


@app.command()
def maraud(scenario: str = typer.Argument(None)) -> None:
    """Goto a scenario, then drop into a live session against that state."""
    _pending()


@app.command()
def snapshot(name: str) -> None:
    """Freeze the live state so roaming never costs a rebuild."""
    _pending()


@app.command()
def restore(name: str) -> None:
    """Thaw a previously frozen live state."""
    _pending()


@app.command()
def where() -> None:
    """Show the current scenario and state."""
    _pending()


@app.command()
def reset() -> None:
    """Reset back to a clean base state."""
    _pending()


if __name__ == "__main__":
    app()
