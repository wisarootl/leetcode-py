import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_max_sub_array, run_max_sub_array
from .solution import Solution


class TestMaximumSubarray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
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
    def test_max_sub_array(self, nums: list[int], expected: int):
        result = run_max_sub_array(Solution, nums)
        assert_max_sub_array(result, expected)
