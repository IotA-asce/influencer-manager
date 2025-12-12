"""Adapter for Gemini image generation implementing ImageGeneratorPort.

TODO: Implementation in Step 3.
"""

from __future__ import annotations

from dataclasses import dataclass

from influencer_manager.domain.models import GeneratedImage, PromptSpec


@dataclass
class GeminiImageGenerator:
    """Stub Gemini adapter."""

    def generate_image(self, prompt: PromptSpec, refs: list[str] | None = None) -> GeneratedImage:
        """Generate an image from the given prompt.

        TODO: Implementation in Step 3.
        """

        raise NotImplementedError
