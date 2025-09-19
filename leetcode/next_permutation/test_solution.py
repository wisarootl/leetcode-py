import pytest

from leetcode_py import logged_test

from .helpers import assert_next_permutation, run_next_permutation
from .solution import Solution


class TestNextPermutation:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 3], [1, 3, 2]),
            ([3, 2, 1], [1, 2, 3]),
            ([1, 1, 5], [1, 5, 1]),
            ([1], [1]),
            ([1, 2], [2, 1]),
            ([2, 1], [1, 2]),
            ([1, 3, 2], [2, 1, 3]),
            ([2, 3, 1], [3, 1, 2]),
            ([1, 2, 3, 4], [1, 2, 4, 3]),
            ([4, 3, 2, 1], [1, 2, 3, 4]),
            ([1, 1, 1], [1, 1, 1]),
            ([1, 2, 1], [2, 1, 1]),
            ([5, 4, 7, 5, 3, 2], [5, 5, 2, 3, 4, 7]),
            ([1, 3, 2, 1], [2, 1, 1, 3]),
            ([2, 1, 3], [2, 3, 1]),
        ],
    )
    def test_next_permutation(self, nums: list[int], expected: list[int]):
        result = run_next_permutation(Solution, nums)
        assert_next_permutation(result, expected)
