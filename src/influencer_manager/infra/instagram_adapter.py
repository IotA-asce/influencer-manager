"""Adapter implementing InstagramPublisherPort for container creation and publishing.

TODO: Implementation in Step 3.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class InstagramPublisherAdapter:
    """Stub Instagram publishing adapter."""

    def create_image_container(self, image_url: str, caption: str) -> str:
        """Create an Instagram media container.

        TODO: Implementation in Step 3.
        """

        raise NotImplementedError

    def get_container_status(self, container_id: str) -> str:
        """Poll container status.

        TODO: Implementation in Step 3.
        """

        raise NotImplementedError

    def publish_container(self, container_id: str) -> str:
        """Publish a ready container.

        TODO: Implementation in Step 3.
        """

        raise NotImplementedError

    def get_publishing_limit(self) -> Optional[int]:
        """Return remaining publishing capacity or limit window value.

        TODO: Implementation in Step 3.
        """

        raise NotImplementedError
