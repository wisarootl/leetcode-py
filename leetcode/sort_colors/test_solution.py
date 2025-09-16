import pytest

from leetcode_py import logged_test

from .helpers import assert_sort_colors, run_sort_colors
from .solution import Solution


class TestSortColors:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
            ([2, 0, 1], [0, 1, 2]),
            ([0], [0]),
            ([1], [1]),
            ([2], [2]),
            ([0, 1, 2], [0, 1, 2]),
            ([2, 2, 2], [2, 2, 2]),
            ([0, 0, 0], [0, 0, 0]),
            ([1, 1, 1], [1, 1, 1]),
            ([2, 1, 0], [0, 1, 2]),
            ([1, 0, 2, 1, 0, 2], [0, 0, 1, 1, 2, 2]),
            ([0, 2, 1, 0, 2, 1], [0, 0, 1, 1, 2, 2]),
            ([2, 2, 1, 0, 0, 1], [0, 0, 1, 1, 2, 2]),
            ([1, 2, 0, 1, 2, 0, 1], [0, 0, 1, 1, 1, 2, 2]),
            ([0, 1, 0, 2, 1, 2, 0], [0, 0, 0, 1, 1, 2, 2]),
        ],
    )
    def test_sort_colors(self, nums: list[int], expected: list[int]):
        result = run_sort_colors(Solution, nums)
        assert_sort_colors(result, expected)
