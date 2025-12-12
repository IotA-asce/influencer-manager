"""Adapter implementing AssetStorePort for storing generated assets.

TODO: Implementation in Step 3.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class AssetStoreAdapter:
    """Stub asset store adapter."""

    def put_bytes(self, key: str, data: bytes, content_type: str) -> str:
        """Persist bytes and return a public URL.

        TODO: Implementation in Step 3.
        """

        raise NotImplementedError

    def get_url(self, key: str) -> str | None:
        """Return a public URL for the given key.

        TODO: Implementation in Step 3.
        """

        raise NotImplementedError
