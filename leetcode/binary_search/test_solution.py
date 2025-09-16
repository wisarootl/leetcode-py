import pytest

from leetcode_py import logged_test

from .helpers import assert_search, run_search
from .solution import Solution


class TestBinarySearch:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, target, expected",
        [
            ([-1, 0, 3, 5, 9, 12], 9, 4),
            ([-1, 0, 3, 5, 9, 12], 2, -1),
            ([5], 5, 0),
            ([5], -5, -1),
            ([1, 3, 5, 7, 9], 1, 0),
            ([1, 3, 5, 7, 9], 9, 4),
            ([1, 3, 5, 7, 9], 4, -1),
            ([1, 3], 1, 0),
            ([1, 3], 3, 1),
            ([1, 3], 2, -1),
            ([-5, -2, 0, 3, 7], -2, 1),
            ([-5, -2, 0, 3, 7], 0, 2),
            ([-5, -2, 0, 3, 7], -1, -1),
        ],
    )
    def test_search(self, nums: list[int], target: int, expected: int):
        result = run_search(Solution, nums, target)
        assert_search(result, expected)
