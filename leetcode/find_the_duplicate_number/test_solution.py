import pytest

from leetcode_py import logged_test

from .helpers import assert_find_duplicate, run_find_duplicate
from .solution import Solution


class TestFindTheDuplicateNumber:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 3, 4, 2, 2], 2),
            ([3, 1, 3, 4, 2], 3),
            ([3, 3, 3, 3, 3], 3),
            ([1, 1], 1),
            ([2, 2, 2], 2),
            ([1, 2, 3, 4, 4], 4),
            ([4, 3, 2, 1, 2], 2),
            ([2, 5, 9, 6, 9, 3, 8, 9, 7, 1], 9),
            ([1, 4, 4, 2, 4], 4),
            ([3, 1, 3, 4, 2], 3),
            ([1, 3, 4, 2, 2], 2),
            ([2, 1, 3, 4, 5, 6, 7, 8, 9, 9], 9),
            ([5, 2, 1, 3, 5, 7, 6, 4], 5),
            ([1, 2, 2], 2),
            ([1, 1, 2], 1),
            ([2, 1, 1], 1),
            ([1, 2, 3, 3], 3),
            ([4, 1, 2, 3, 4], 4),
        ],
    )
    def test_find_duplicate(self, nums: list[int], expected: int):
        result = run_find_duplicate(Solution, nums)
        assert_find_duplicate(result, expected)
