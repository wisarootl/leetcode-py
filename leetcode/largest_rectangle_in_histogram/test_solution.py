import pytest

from leetcode_py import logged_test

from .helpers import assert_largest_rectangle_area, run_largest_rectangle_area
from .solution import Solution


class TestLargestRectangleInHistogram:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "heights, expected",
        [
            ([2, 1, 5, 6, 2, 3], 10),
            ([2, 4], 4),
            ([1], 1),
            ([0], 0),
            ([1, 1], 2),
            ([0, 0, 0], 0),
            ([1, 2, 3, 4, 5], 9),
            ([5, 4, 3, 2, 1], 9),
            ([3, 3, 3, 3], 12),
            ([2, 1, 2], 3),
            ([1, 3, 1], 3),
            ([6, 7, 5, 2, 4, 5, 9, 3], 16),
            ([4, 2, 0, 3, 2, 5], 6),
            ([1, 2, 2, 1], 4),
            ([0, 9], 9),
            ([9, 0], 9),
        ],
    )
    def test_largest_rectangle_area(self, heights: list[int], expected: int):
        result = run_largest_rectangle_area(Solution, heights)
        assert_largest_rectangle_area(result, expected)
