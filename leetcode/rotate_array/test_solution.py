import pytest

from leetcode_py import logged_test

from .helpers import assert_rotate, run_rotate
from .solution import Solution


class TestRotateArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
            ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
            ([1, 2], 1, [2, 1]),
            ([1], 1, [1]),
            ([1, 2, 3], 0, [1, 2, 3]),
            ([1, 2, 3], 3, [1, 2, 3]),
            ([1, 2, 3], 4, [3, 1, 2]),
            ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
            ([1, 2, 3, 4, 5, 6], 4, [3, 4, 5, 6, 1, 2]),
            ([-1, -2, -3, -4], 1, [-4, -1, -2, -3]),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9], 5, [5, 6, 7, 8, 9, 1, 2, 3, 4]),
            ([10, 20, 30], 6, [10, 20, 30]),
            ([5, 4, 3, 2, 1], 10, [5, 4, 3, 2, 1]),
            ([1, 2, 3, 4, 5, 6, 7, 8], 3, [6, 7, 8, 1, 2, 3, 4, 5]),
            ([100], 0, [100]),
        ],
    )
    def test_rotate(self, nums: list[int], k: int, expected: list[int]):
        result = run_rotate(Solution, nums, k)
        assert_rotate(result, expected)
