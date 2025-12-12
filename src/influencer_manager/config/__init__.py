"""Configuration entrypoint."""

from __future__ import annotations

from functools import lru_cache

from .settings import Settings

__all__ = ["Settings", "get_settings"]


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return cached application settings."""

    return Settings()
