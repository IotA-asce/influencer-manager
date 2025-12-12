.PHONY: fmt lint fix test type check

fmt:
uv run ruff format .

lint:
uv run ruff check .

fix:
uv run ruff check --fix .

test:
uv run pytest

type:
uv run mypy src

check: lint fmt test type
