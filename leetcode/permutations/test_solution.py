import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_permute, run_permute
from .solution import Solution


class TestPermutations:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
            ([0, 1], [[0, 1], [1, 0]]),
            ([1], [[1]]),
            ([2, 1], [[2, 1], [1, 2]]),
        ],
    )
    def test_permute(self, nums: list[int], expected: list[list[int]]):
        result = run_permute(Solution, nums)
        assert_permute(result, expected)
