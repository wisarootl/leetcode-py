import pytest

from leetcode_py import logged_test

from .helpers import assert_search, run_search
from .solution import Solution


class TestSearchInRotatedSortedArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, target, expected",
        [
            ([4, 5, 6, 7, 0, 1, 2], 0, 4),
            ([4, 5, 6, 7, 0, 1, 2], 3, -1),
            ([1], 0, -1),
            ([1], 1, 0),
            ([3, 1], 1, 1),
            ([1, 3], 3, 1),
            ([2, 1], 2, 0),
            ([5, 1, 3], 3, 2),
            ([4, 5, 6, 7, 8, 1, 2, 3], 8, 4),
            ([6, 7, 0, 1, 2, 3, 4, 5], 6, 0),
            ([7, 0, 1, 2, 3, 4, 5, 6], 7, 0),
            ([0, 1, 2, 3, 4, 5, 6, 7], 4, 4),
            ([3, 4, 5, 6, 7, 0, 1, 2], 2, 7),
            ([9, 0, 2, 7, 8], 3, -1),
            ([8, 9, 2, 3, 4], 9, 1),
        ],
    )
    def test_search(self, nums: list[int], target: int, expected: int):
        result = run_search(Solution, nums, target)
        assert_search(result, expected)
