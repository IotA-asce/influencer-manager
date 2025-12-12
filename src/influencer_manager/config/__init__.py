"""Configuration entrypoint."""

from __future__ import annotations

from functools import lru_cache

from .settings import Settings

__all__ = ["get_settings", "Settings"]


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return cached application settings."""

    return Settings()
