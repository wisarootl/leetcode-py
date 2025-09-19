import pytest

from leetcode_py import logged_test

from .helpers import assert_max_product, run_max_product
from .solution import Solution


class TestMaximumProductSubarray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([2, 3, -2, 4], 6),
            ([-2, 0, -1], 0),
            ([1], 1),
            ([0], 0),
            ([-1], -1),
            ([2, -1, 3], 3),
            ([-2, -3], 6),
            ([1, 2, 3, 4], 24),
            ([-1, -2, -3], 6),
            ([0, 2], 2),
            ([3, -1, 4], 4),
            ([-2, 3, -4], 24),
            ([2, 3, -2, 4, -1], 48),
            ([1, 0, -1, 2, 3], 6),
            ([-3, 0, 1, -2], 1),
        ],
    )
    def test_max_product(self, nums: list[int], expected: int):
        result = run_max_product(Solution, nums)
        assert_max_product(result, expected)
