import pytest

from leetcode_py import logged_test

from .helpers import assert_longest_consecutive, run_longest_consecutive
from .solution import Solution


class TestLongestConsecutiveSequence:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([100, 4, 200, 1, 3, 2], 4),
            ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
            ([1, 0, 1, 2], 3),
            ([], 0),
            ([1], 1),
            ([1, 2, 3, 4, 5], 5),
            ([5, 4, 3, 2, 1], 5),
            ([1, 3, 5, 7, 9], 1),
            ([1, 2, 0, 1], 3),
            ([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6], 7),
            ([-1, -2, -3, -4, -5], 5),
            ([1000000000, -1000000000], 1),
            ([1, 2, 3, 5, 6, 7, 8], 4),
            ([10, 5, 12, 3, 55, 30, 4, 11, 2], 4),
            ([1, 9, 3, 10, 4, 20, 2], 4),
        ],
    )
    def test_longest_consecutive(self, nums: list[int], expected: int):
        result = run_longest_consecutive(Solution, nums)
        assert_longest_consecutive(result, expected)
