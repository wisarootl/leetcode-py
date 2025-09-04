import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestLargestRectangleInHistogram:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "heights, expected",
        [
            # Basic examples
            ([2, 1, 5, 6, 2, 3], 10),
            ([2, 4], 4),
            # Edge cases
            ([1], 1),
            ([0], 0),
            ([1, 1], 2),
            ([0, 0, 0], 0),
            # Patterns
            ([1, 2, 3, 4, 5], 9),
            ([5, 4, 3, 2, 1], 9),
            ([3, 3, 3, 3], 12),
            ([2, 1, 2], 3),
            ([1, 3, 1], 3),
            # Complex cases
            ([6, 7, 5, 2, 4, 5, 9, 3], 16),
            ([4, 2, 0, 3, 2, 5], 6),
            ([1, 2, 2, 1], 4),
            ([0, 9], 9),
            ([9, 0], 9),
            # Large rectangles
            ([2, 1, 5, 6, 2, 3, 1, 5, 6, 2], 10),
            ([1, 8, 6, 2, 5, 4, 8, 3, 7], 16),
            ([50, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 50),
            ([1, 1, 1, 1, 1, 50, 1, 1, 1, 1, 1], 50),
            ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 50], 50),
        ],
    )
    @logged_test
    def test_largest_rectangle_area(self, heights: list[int], expected: int):
        result = self.solution.largest_rectangle_area(heights)
        assert result == expected
