"""Configuration layer tests."""

from __future__ import annotations

import pytest
from typer.testing import CliRunner

from influencer_manager.__main__ import app
from influencer_manager.config import Settings, get_settings


def test_defaults_load_without_env(monkeypatch: pytest.MonkeyPatch) -> None:
    for key in [
        "IM_ENV",
        "IM_LOG_LEVEL",
        "GEMINI_API_KEY",
        "GOOGLE_API_KEY",
        "IM_GEMINI_MODEL",
        "IM_IG_ACCESS_TOKEN",
        "IM_IG_USER_ID",
        "IM_GRAPH_API_BASE_URL",
        "IM_GRAPH_API_VERSION",
        "IM_META_APP_ID",
        "IM_META_APP_SECRET",
    ]:
        monkeypatch.delenv(key, raising=False)

    get_settings.cache_clear()
    settings = Settings()

    assert settings.env == "local"
    assert settings.log_level == "INFO"
    assert settings.gemini_api_key is None
    assert settings.gemini_model == "gemini-3-pro-image-preview"
    assert settings.graph_api_base_url == "https://graph.facebook.com"
    assert settings.graph_api_version == "v21.0"


def test_gemini_key_aliasing_prefers_gemini_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("GEMINI_API_KEY", "primary")
    monkeypatch.setenv("GOOGLE_API_KEY", "secondary")

    get_settings.cache_clear()
    settings = Settings()

    assert settings.gemini_api_key == "primary"


def test_require_instagram_raises_when_missing(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("IM_IG_ACCESS_TOKEN", raising=False)
    monkeypatch.delenv("IM_IG_USER_ID", raising=False)

    settings = Settings()

    with pytest.raises(ValueError):
        settings.require_instagram()


def test_config_show_does_not_leak_secrets(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("GEMINI_API_KEY", "supersecret")
    monkeypatch.setenv("IM_IG_ACCESS_TOKEN", "igsecret")
    monkeypatch.setenv("IM_IG_USER_ID", "user123")

    get_settings.cache_clear()
    runner = CliRunner()
    result = runner.invoke(app, ["config", "show"])

    assert result.exit_code == 0
    assert "supersecret" not in result.stdout
    assert "igsecret" not in result.stdout
