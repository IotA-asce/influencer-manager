"""Application use cases orchestrating domain flows via ports.

Implements coordination across ImageGeneratorPort, AssetStorePort, InstagramPublisherPort,
JobStorePort, ClockPort, and LoggerPort.

TODO: Implementation in Step 3.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from influencer_manager.domain.models import PostPlan, PublishJob


class GenerateUseCase(Protocol):
    """Generate an image from a prompt specification."""

    def run(self, post_plan: PostPlan) -> PublishJob: ...


class PublishUseCase(Protocol):
    """Publish an existing asset to Instagram."""

    def run(self, post_plan: PostPlan) -> PublishJob: ...


@dataclass
class UseCaseResult:
    """Placeholder result wrapper for use case executions."""

    job: PublishJob
