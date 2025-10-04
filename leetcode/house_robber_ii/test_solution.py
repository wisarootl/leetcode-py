import pytest

from leetcode_py import logged_test

from .helpers import assert_rob, run_rob
from .solution import Solution


class TestHouseRobberII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([2, 3, 2], 3),
            ([1, 2, 3, 1], 4),
            ([1, 2, 3], 3),
            ([1], 1),
            ([1, 2], 2),
            ([2, 1, 1, 2], 3),
            ([1, 2, 3, 4, 5], 8),
            ([2, 3, 2, 3, 2], 6),
            ([1, 2, 1, 1], 3),
            ([2, 1, 1, 1], 3),
            ([1, 2, 3, 4, 5, 1, 2, 3, 4, 5], 16),
            ([0], 0),
            ([0, 0], 0),
            ([1, 0, 0, 1], 1),
            ([2, 7, 9, 3, 1], 11),
            ([1, 2, 3, 1, 2, 3], 6),
            ([2, 1, 1, 2, 1, 1], 4),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 30),
            ([100, 1, 1, 100], 101),
            ([1, 100, 1, 1, 100], 200),
        ],
    )
    def test_rob(self, nums: list[int], expected: int):
        result = run_rob(Solution, nums)
        assert_rob(result, expected)
