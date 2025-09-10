import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestInsertInterval:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "intervals, new_interval, expected",
        [
            # Original cases
            ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
            ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
            # Empty intervals
            ([], [5, 7], [[5, 7]]),
            # Insert at beginning
            ([[3, 5], [6, 9]], [1, 2], [[1, 2], [3, 5], [6, 9]]),
            # Insert at end
            ([[1, 3], [6, 9]], [10, 12], [[1, 3], [6, 9], [10, 12]]),
            # No overlap
            ([[1, 2], [4, 5]], [3, 3], [[1, 2], [3, 3], [4, 5]]),
            # Complete overlap
            ([[1, 5]], [2, 3], [[1, 5]]),
            # Merge all intervals
            ([[1, 2], [3, 4], [5, 6]], [0, 7], [[0, 7]]),
            # Adjacent intervals
            ([[1, 3], [6, 9]], [4, 5], [[1, 3], [4, 5], [6, 9]]),
            # Touch boundaries
            ([[1, 3], [6, 9]], [3, 6], [[1, 9]]),
        ],
    )
    @logged_test
    def test_insert(
        self, intervals: list[list[int]], new_interval: list[int], expected: list[list[int]]
    ):
        result = self.solution.insert(intervals, new_interval)
        assert result == expected
