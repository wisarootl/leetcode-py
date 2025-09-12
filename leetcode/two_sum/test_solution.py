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
        ],
    )
    def test_two_sum(self, nums: list[int], target: int, expected: list[int]):
        result = run_two_sum(Solution, nums, target)
        assert_two_sum(result, expected)
