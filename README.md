# influencer-manager

Automation pipeline to generate campaign-ready images and publish them to Instagram.

Current status: scaffolding / baseline.

See [docs/BASELINE.md](docs/BASELINE.md) for the initial audit snapshot.

## Architecture
- Blueprint: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
- Requirements: [docs/REQUIREMENTS.md](docs/REQUIREMENTS.md)
- Architectural Decisions: [docs/adr](docs/adr)

## Prerequisites
- [uv](https://docs.astral.sh/uv/) (Python toolchain and package manager)
- Python 3.11 (managed automatically via `uv python install 3.11` or `.python-version`)

## Setup
Install dependencies (including development tools):

```bash
uv sync --dev
# First sync will generate `uv.lock`; commit it to capture resolved versions.
```

If you're behind a corporate proxy, export proxy variables so `uv` can reach PyPI:

```bash
export HTTP_PROXY=http://proxy.example.com:3128
export HTTPS_PROXY=http://proxy.example.com:3128
uv sync --dev
```

## Usage
Run the CLI stub:

```bash
uv run python -m influencer_manager --help
uv run python -m influencer_manager version
```

## Quality
Common development commands are available via `make`:

- `make fmt` — format code with Ruff
- `make lint` — lint code with Ruff
- `make fix` — apply autofixes with Ruff
- `make test` — run pytest with coverage
- `make type` — run mypy type checks

## Environment variables
Future integrations (e.g., API tokens, secrets) will be loaded via `.env` and `python-dotenv`.
Do not commit secrets. Provide a sample file when wiring real features.
