import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestMaximumSubarray:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
            ([1], 1),
            ([5, 4, -1, 7, 8], 23),
            ([-1], -1),
            ([-2, -1], -1),
            ([1, 2, 3, 4, 5], 15),
            ([-5, -2, -8, -1], -1),
        ],
    )
    @logged_test
    def test_max_sub_array(self, nums: list[int], expected: int):
        result = self.solution.max_sub_array(nums)
        assert result == expected
