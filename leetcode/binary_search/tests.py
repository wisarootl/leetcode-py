import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestBinarySearch:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, target, expected",
        [
            # Original examples
            ([-1, 0, 3, 5, 9, 12], 9, 4),
            ([-1, 0, 3, 5, 9, 12], 2, -1),
            # Single element
            ([5], 5, 0),
            ([5], -5, -1),
            # Target at boundaries
            ([1, 3, 5, 7, 9], 1, 0),
            ([1, 3, 5, 7, 9], 9, 4),
            # Target not found
            ([1, 3, 5, 7, 9], 4, -1),
            # Two elements
            ([1, 3], 1, 0),
            ([1, 3], 3, 1),
            ([1, 3], 2, -1),
            # Negative numbers
            ([-5, -2, 0, 3, 7], -2, 1),
            ([-5, -2, 0, 3, 7], 0, 2),
            ([-5, -2, 0, 3, 7], -1, -1),
        ],
    )
    @logged_test
    def test_search(self, nums: list[int], target: int, expected: int):
        result = self.solution.search(nums, target)
        assert result == expected
