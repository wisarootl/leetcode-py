import pytest

from leetcode_py import logged_test

from .helpers import assert_erase_overlap_intervals, run_erase_overlap_intervals
from .solution import Solution


class TestNonOverlappingIntervals:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "intervals, expected",
        [
            ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
            ([[1, 2], [1, 2], [1, 2]], 2),
            ([[1, 2], [2, 3]], 0),
            ([[1, 2]], 0),
            ([[1, 2], [1, 3], [2, 3], [3, 4]], 1),
            ([[1, 2], [2, 3], [3, 4], [1, 3], [2, 4]], 2),
            ([[1, 2], [3, 4], [5, 6]], 0),
            ([[1, 2], [1, 3], [1, 4]], 2),
            ([[1, 2], [2, 3], [3, 4], [4, 5]], 0),
            ([[1, 2], [1, 2], [1, 2], [1, 2]], 3),
            ([[1, 3], [2, 4], [3, 5], [4, 6]], 2),
            ([[1, 2], [3, 4], [5, 6], [7, 8]], 0),
            ([[1, 4], [2, 3], [3, 4]], 1),
            ([[1, 2], [1, 2], [1, 2], [2, 3]], 2),
            ([[1, 2], [2, 3], [1, 3], [3, 4]], 1),
        ],
    )
    def test_erase_overlap_intervals(self, intervals: list[list[int]], expected: int):
        result = run_erase_overlap_intervals(Solution, intervals)
        assert_erase_overlap_intervals(result, expected)
