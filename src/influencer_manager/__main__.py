"""Entry point for the influencer-manager CLI."""

from __future__ import annotations

import typer
from rich.console import Console

from influencer_manager import __version__
from influencer_manager.config import get_settings

app = typer.Typer(help="Influencer Manager command-line interface (scaffolding phase).")
console = Console()
config_app = typer.Typer(help="Configuration inspection utilities.")


@app.command()
def version() -> None:
    """Print the installed package version."""

    console.print(f"influencer-manager {__version__}")


@config_app.command("show")
def config_show() -> None:
    """Display non-sensitive configuration values."""

    settings = get_settings()

    console.print(f"Environment: {settings.env}")
    console.print(f"Log level: {settings.log_level}")
    console.print(f"Gemini model: {settings.gemini_model}")
    console.print(f"Graph API base URL: {settings.graph_api_base_url}")
    console.print(f"Graph API version: {settings.graph_api_version}")


@config_app.command("check")
def config_check(
    feature: str = typer.Option(
        "none",
        "--feature",
        "-f",
        case_sensitive=False,
        help="Check required configuration for a feature (gemini, instagram, all).",
        show_default=True,
    ),
) -> None:
    """Validate configuration for the specified feature."""

    settings = get_settings()

    try:
        if feature.lower() in {"gemini", "all"}:
            settings.require_gemini()
        if feature.lower() in {"instagram", "all"}:
            settings.require_instagram()
    except ValueError as exc:  # pragma: no cover - defensive
        console.print(f"[red]Configuration error:[/red] {exc}")
        raise typer.Exit(code=1) from exc

    console.print("[green]Configuration validated.[/green]")


app.add_typer(config_app, name="config")


def main() -> None:
    """Run the Typer application."""

    app()


if __name__ == "__main__":
    main()
