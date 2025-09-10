import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestSortColors:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
            ([2, 0, 1], [0, 1, 2]),
            ([0], [0]),
            ([1], [1]),
            ([2], [2]),
            ([0, 1, 2], [0, 1, 2]),
        ],
    )
    @logged_test
    def test_sort_colors(self, nums: list[int], expected: list[int]):
        nums_copy = nums.copy()
        self.solution.sort_colors(nums_copy)
        assert nums_copy == expected
