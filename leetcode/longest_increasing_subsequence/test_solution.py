import pytest

from leetcode_py import logged_test

from .helpers import assert_length_of_lis, run_length_of_lis
from .solution import Solution


class TestLongestIncreasingSubsequence:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([10, 9, 2, 5, 3, 7, 101, 18], 4),
            ([0, 1, 0, 3, 2, 3], 4),
            ([7, 7, 7, 7, 7, 7, 7], 1),
            ([1, 3, 6, 7, 9, 4, 10, 5, 6], 6),
            ([10, 22, 9, 33, 21, 50, 41, 60], 5),
            ([1], 1),
            ([1, 2], 2),
            ([2, 1], 1),
            ([1, 2, 3, 4, 5], 5),
            ([5, 4, 3, 2, 1], 1),
            ([4, 10, 4, 3, 8, 9], 3),
            ([2, 2], 1),
            ([1, 3, 2, 4], 3),
            ([10, 9, 2, 5, 3, 4], 3),
            ([1, 2, 3, 2, 3, 4, 5], 5),
        ],
    )
    def test_length_of_lis(self, nums: list[int], expected: int):
        result = run_length_of_lis(Solution, nums)
        assert_length_of_lis(result, expected)
