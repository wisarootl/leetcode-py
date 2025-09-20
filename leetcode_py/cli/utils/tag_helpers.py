"""Helper functions for working with tags."""

from .resources import get_tags_path


def get_available_tags_help() -> str:
    """Get available tags for help text."""
    try:
        import json5

        tags_file = get_tags_path()
        with open(tags_file) as f:
            tags_data = json5.load(f)
        available_tags = list(tags_data.keys())
        return ", ".join(available_tags)
    except Exception:
        return "grind-75, blind-75, neetcode-150"
