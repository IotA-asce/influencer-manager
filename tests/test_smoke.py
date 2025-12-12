"""Basic smoke tests for the scaffolded package."""

import influencer_manager


def test_version_present() -> None:
    """Ensure package exposes a version string."""

    assert hasattr(influencer_manager, "__version__")
    assert isinstance(influencer_manager.__version__, str)
