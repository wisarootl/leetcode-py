import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestProductOfArrayExceptSelf:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 3, 4], [24, 12, 8, 6]),
            ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
            ([2, 3, 4, 5], [60, 40, 30, 24]),
            # Edge cases
            ([1, 1], [1, 1]),  # Minimum length
            ([5, 2], [2, 5]),  # Two elements
            ([0, 0], [0, 0]),  # All zeros
            ([1, 0], [0, 1]),  # Single zero
            ([0, 1, 2], [2, 0, 0]),  # Zero at start
            ([1, 2, 0], [0, 0, 2]),  # Zero at end
            # Negative numbers
            ([-1, -2], [-2, -1]),
            ([-1, -2, -3], [6, 3, 2]),
            ([1, -2, 3], [-6, 3, -2]),
            # All ones
            ([1, 1, 1, 1], [1, 1, 1, 1]),
            # Large numbers
            ([10, 3, 5, 6, 2], [180, 600, 360, 300, 900]),
        ],
    )
    @logged_test
    def test_product_except_self(self, nums: list[int], expected: list[int]):
        result = self.solution.product_except_self(nums)
        assert result == expected
