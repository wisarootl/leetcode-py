import pytest

from leetcode_py import logged_test

from .helpers import assert_rob, run_rob
from .solution import Solution


class TestHouseRobber:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 3, 1], 4),
            ([2, 7, 9, 3, 1], 12),
            ([1], 1),
            ([2, 1], 2),
            ([5, 1, 3, 9], 14),
            ([2, 7, 9, 3, 1, 5, 8], 20),
            ([0, 0, 0], 0),
            ([5], 5),
            ([1, 2], 2),
            ([2, 1, 1, 2], 4),
            ([5, 5, 10, 100, 10, 5], 110),
            ([100, 1, 1, 100], 200),
            ([1, 3, 1, 3, 100], 103),
            ([400, 0, 400], 800),
            ([1, 2, 3, 4, 5], 9),
        ],
    )
    def test_rob(self, nums: list[int], expected: int):
        result = run_rob(Solution, nums)
        assert_rob(result, expected)
