import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestMergeIntervals:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "intervals, expected",
        [
            # Original test cases
            ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
            ([[1, 4], [4, 5]], [[1, 5]]),
            ([[4, 7], [1, 4]], [[1, 7]]),
            # Edge cases
            ([[1, 1]], [[1, 1]]),  # Single point interval
            ([[1, 2], [3, 4]], [[1, 2], [3, 4]]),  # No overlap
            ([[1, 4], [2, 3]], [[1, 4]]),  # Complete overlap
            ([[1, 10], [2, 6], [8, 10], [15, 18]], [[1, 10], [15, 18]]),  # Multiple merges
            ([[0, 0], [1, 1], [2, 2]], [[0, 0], [1, 1], [2, 2]]),  # All single points
            ([[1, 3], [2, 6], [8, 10], [9, 12], [15, 18]], [[1, 6], [8, 12], [15, 18]]),  # Chain merge
            ([[4, 5], [4, 6]], [[4, 6]]),  # Same start time
        ],
    )
    @logged_test
    def test_merge(self, intervals: list[list[int]], expected: list[list[int]]):
        result = self.solution.merge(intervals)
        assert result == expected
