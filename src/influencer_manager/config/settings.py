"""Application configuration settings."""

from __future__ import annotations

from typing import Optional

from pydantic import AliasChoices, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Centralized application settings sourced from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        env_prefix="IM_",
    )

    env: str = "local"
    log_level: str = "INFO"
    gemini_api_key: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices("GEMINI_API_KEY", "GOOGLE_API_KEY"),
    )
    gemini_model: str = "gemini-3-pro-image-preview"
    ig_access_token: Optional[str] = None
    ig_user_id: Optional[str] = None
    graph_api_base_url: str = "https://graph.facebook.com"
    graph_api_version: str = "v21.0"
    meta_app_id: Optional[str] = None
    meta_app_secret: Optional[str] = None

    def require_gemini(self) -> None:
        """Validate that Gemini configuration is present."""

        if not self.gemini_api_key:
            raise ValueError(
                "Missing Gemini credentials. Set GEMINI_API_KEY or GOOGLE_API_KEY to enable generation."
            )

    def require_instagram(self) -> None:
        """Validate that Instagram configuration is present."""

        if not self.ig_access_token or not self.ig_user_id:
            raise ValueError(
                "Missing Instagram credentials. Set IM_IG_ACCESS_TOKEN and IM_IG_USER_ID to enable publishing."
            )
