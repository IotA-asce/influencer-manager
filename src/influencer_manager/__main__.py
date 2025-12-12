"""Entry point for the influencer-manager CLI."""

from __future__ import annotations

import typer
from rich.console import Console

from influencer_manager import __version__

app = typer.Typer(help="Influencer Manager command-line interface (scaffolding phase).")
console = Console()


@app.command()
def version() -> None:
    """Print the installed package version."""

    console.print(f"influencer-manager {__version__}")


def main() -> None:
    """Run the Typer application."""

    app()


if __name__ == "__main__":
    main()
