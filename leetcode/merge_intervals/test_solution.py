import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_merge, run_merge
from .solution import Solution


class TestMergeIntervals:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "intervals, expected",
        [
            ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
            ([[1, 4], [4, 5]], [[1, 5]]),
            ([[4, 7], [1, 4]], [[1, 7]]),
            ([[1, 3]], [[1, 3]]),
            ([[1, 4], [2, 3]], [[1, 4]]),
            ([[1, 2], [3, 4], [5, 6]], [[1, 2], [3, 4], [5, 6]]),
            ([[0, 0]], [[0, 0]]),
            ([[1, 10], [2, 3], [4, 5], [6, 7], [8, 9]], [[1, 10]]),
            ([[1, 3], [2, 6], [8, 10], [9, 12], [15, 18]], [[1, 6], [8, 12], [15, 18]]),
            ([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]], [[1, 10]]),
            ([[1, 4], [0, 4]], [[0, 4]]),
            ([[1, 4], [0, 0], [3, 5]], [[0, 0], [1, 5]]),
        ],
    )
    def test_merge(self, intervals: list[list[int]], expected: list[list[int]]):
        result = run_merge(Solution, intervals)
        assert_merge(result, expected)
