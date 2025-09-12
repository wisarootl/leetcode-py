import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_product_except_self, run_product_except_self
from .solution import Solution


class TestProductOfArrayExceptSelf:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 3, 4], [24, 12, 8, 6]),
            ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
            ([2, 3, 4, 5], [60, 40, 30, 24]),
            ([1, 1], [1, 1]),
            ([5, 2], [2, 5]),
            ([0, 1, 2, 3], [6, 0, 0, 0]),
            ([1, 0, 3, 4], [0, 12, 0, 0]),
        ],
    )
    def test_product_except_self(self, nums: list[int], expected: list[int]):
        result = run_product_except_self(Solution, nums)
        assert_product_except_self(result, expected)
