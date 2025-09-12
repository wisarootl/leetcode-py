import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_two_sum, run_two_sum
from .solution import Solution


class TestTwoSum:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, target, expected",
        [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
            ([2, 5, 5, 11], 10, [1, 2]),
            ([1, 2, 3, 4, 5], 8, [2, 4]),
            ([0, 4, 3, 0], 0, [0, 3]),
            ([-1, -2, -3, -4, -5], -8, [2, 4]),
            ([1, 3, 4, 2], 6, [2, 3]),
            ([5, 75, 25], 100, [1, 2]),
            ([-3, 4, 3, 90], 0, [0, 2]),
            ([1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 2], 6, [5, 11]),
            ([2, 1, 9, 4, 4, 56, 90, 3], 8, [3, 4]),
            ([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], 185, [3, 4]),
            ([-1000000000, 1000000000], 0, [0, 1]),
            ([0, 1], 1, [0, 1]),
            ([1, 2], 5, []),
            ([3, 5, 7], 1, []),
            ([10, 20, 30], 15, []),
        ],
    )
    def test_two_sum(self, nums: list[int], target: int, expected: list[int]):
        result = run_two_sum(Solution, nums, target)
        assert_two_sum(result, expected)
