import pytest

from leetcode_py import logged_test

from .helpers import assert_find_min, run_find_min
from .solution import Solution


class TestFindMinimumInRotatedSortedArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([3, 4, 5, 1, 2], 1),
            ([4, 5, 6, 7, 0, 1, 2], 0),
            ([11, 13, 15, 17], 11),
            ([1], 1),
            ([2, 1], 1),
            ([1, 2, 3], 1),
            ([3, 1, 2], 1),
            ([2, 3, 1], 1),
            ([4, 5, 6, 7, 8, 1, 2, 3], 1),
            ([5, 6, 7, 8, 9, 10, 1, 2, 3, 4], 1),
            ([6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4, 5], 1),
            ([7, 8, 9, 10, 11, 12, 13, 14, 1, 2, 3, 4, 5, 6], 1),
            ([8, 9, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4, 5, 6, 7], 1),
            ([9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 1, 2, 3, 4, 5, 6, 7, 8], 1),
            (
                [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                1,
            ),
        ],
    )
    def test_find_min(self, nums: list[int], expected: int):
        result = run_find_min(Solution, nums)
        assert_find_min(result, expected)
