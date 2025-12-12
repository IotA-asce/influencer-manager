"""CLI interface for invoking use cases.

Implements presentation layer that will call Generate/Publish use cases via ports.

TODO: Implementation in Step 3.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass


@dataclass
class CLICommand:
    """Placeholder CLI command definition."""

    name: str
    handler: Callable[..., int]
