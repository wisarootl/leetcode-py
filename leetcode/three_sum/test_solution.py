import pytest

from leetcode_py import logged_test

from .helpers import assert_three_sum, run_three_sum
from .solution import Solution


class TestThreeSum:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
            ([0, 1, 1], []),
            ([0, 0, 0], [[0, 0, 0]]),
            ([-1, 0, 1], [[-1, 0, 1]]),
            ([1, 2, -2, -1], []),
            ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
            ([1, -1, -1, 0], [[-1, 0, 1]]),
            (
                [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6],
                [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]],
            ),
            ([3, 0, -2, -1, 1, 2], [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]),
            ([0, 0, 0, 0], [[0, 0, 0]]),
            ([-1, -1, 2], [[-1, -1, 2]]),
            ([1, 1, -2], [[-2, 1, 1]]),
        ],
    )
    def test_three_sum(self, nums: list[int], expected: list[list[int]]):
        result = run_three_sum(Solution, nums)
        assert_three_sum(result, expected)
