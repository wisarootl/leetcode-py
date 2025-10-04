"""Shared utilities for problem list management."""

from leetcode_py.cli.utils.problem_finder import _build_problem_number_cache


def get_existing_problems():
    """Get problem numbers from existing JSON files."""
    cache = _build_problem_number_cache()
    return set(cache.keys())
