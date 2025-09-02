import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestSearchInRotatedSortedArray:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, target, expected",
        [
            # Original test cases
            ([4, 5, 6, 7, 0, 1, 2], 0, 4),
            ([4, 5, 6, 7, 0, 1, 2], 3, -1),
            ([1], 0, -1),
            ([1], 1, 0),
            ([3, 1], 1, 1),
            # No rotation (sorted array)
            ([1, 2, 3, 4, 5], 3, 2),
            ([1, 2, 3, 4, 5], 6, -1),
            # Different rotation points
            ([6, 7, 0, 1, 2, 4, 5], 0, 2),
            ([6, 7, 0, 1, 2, 4, 5], 4, 5),
            ([6, 7, 0, 1, 2, 4, 5], 7, 1),
            ([2, 3, 4, 5, 6, 7, 0, 1], 0, 6),
            # Target at boundaries
            ([4, 5, 6, 7, 0, 1, 2], 4, 0),
            ([4, 5, 6, 7, 0, 1, 2], 2, 6),
            # Two elements
            ([2, 1], 1, 1),
            ([2, 1], 2, 0),
            ([1, 3], 3, 1),
        ],
    )
    @logged_test
    def test_search(self, nums: list[int], target: int, expected: int):
        result = self.solution.search(nums, target)
        assert result == expected
