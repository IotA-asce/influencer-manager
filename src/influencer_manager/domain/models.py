"""Domain models shared across ports and use cases.

Defines the canonical entities used by the ports described in docs/ARCHITECTURE.md.

TODO: Implementation in Step 3.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, Optional


class JobState(Enum):
    """State machine for publish jobs."""

    PLANNED = "PLANNED"
    GENERATED = "GENERATED"
    STORED = "STORED"
    CONTAINER_CREATED = "CONTAINER_CREATED"
    CONTAINER_READY = "CONTAINER_READY"
    PUBLISHED = "PUBLISHED"
    FAILED_RETRYABLE = "FAILED_RETRYABLE"
    FAILED_TERMINAL = "FAILED_TERMINAL"


@dataclass
class PromptSpec:
    """Prompt specification for image generation requests."""

    text: str
    style_bible_ref: Optional[str]
    aspect_ratio: str
    seed: Optional[int]
    refs: Optional[list[str]]


@dataclass
class GeneratedImage:
    """Output of image generation.

    Holds optional in-memory data or local path alongside metadata for storage/publishing.
    """

    data: Optional[bytes]
    path: Optional[str]
    mime: str
    width: Optional[int]
    height: Optional[int]
    sha256: str


@dataclass
class PostPlan:
    """Plan describing how an image will be published."""

    caption_template: str
    hashtags: list[str]
    scheduled_at: Optional[datetime]
    prompt_spec: PromptSpec


@dataclass
class PublishJob:
    """Job record used for idempotency and tracking publish attempts."""

    job_key: str
    state: JobState
    retry_count: int
    container_id: Optional[str]
    media_id: Optional[str]
    created_at: datetime
    updated_at: datetime


@dataclass
class AuditEvent:
    """Audit log entry for significant actions (generate, store, publish)."""

    event_type: str
    payload: dict[str, Any]
    created_at: datetime
