import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestTrappingRainWater:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "height, expected",
        [
            # Original examples
            ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
            ([4, 2, 0, 3, 2, 5], 9),
            ([3, 0, 2, 0, 4], 7),
            # Edge cases
            ([], 0),
            ([1], 0),
            ([1, 2], 0),
            ([2, 1], 0),
            # No water trapped
            ([1, 2, 3, 4, 5], 0),
            ([5, 4, 3, 2, 1], 0),
            # Simple cases
            ([3, 0, 3], 3),
            ([2, 1, 2], 1),
            ([5, 2, 7, 2, 6, 1, 5, 3, 2, 4], 14),
            # All same height
            ([3, 3, 3, 3], 0),
            # Valley pattern
            ([3, 2, 1, 2, 3], 4),
            # Multiple peaks
            ([0, 2, 0, 4, 0, 3, 0, 4, 0, 2, 0], 13),
        ],
    )
    @logged_test
    def test_trap(self, height: list[int], expected: int):
        result = self.solution.trap(height)
        assert result == expected
