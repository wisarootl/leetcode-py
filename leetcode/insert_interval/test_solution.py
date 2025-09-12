import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_insert, run_insert
from .solution import Solution


class TestInsertInterval:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "intervals, new_interval, expected",
        [
            ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
            ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
            ([], [5, 7], [[5, 7]]),
            ([[1, 5]], [2, 3], [[1, 5]]),
            ([[1, 5]], [6, 8], [[1, 5], [6, 8]]),
            ([[1, 5]], [0, 0], [[0, 0], [1, 5]]),
            ([[3, 5], [12, 15]], [6, 6], [[3, 5], [6, 6], [12, 15]]),
            ([[1, 2], [4, 5]], [3, 3], [[1, 2], [3, 3], [4, 5]]),
            ([[2, 5], [6, 7], [8, 9]], [0, 1], [[0, 1], [2, 5], [6, 7], [8, 9]]),
            ([[1, 3], [6, 9]], [10, 12], [[1, 3], [6, 9], [10, 12]]),
            ([[1, 4], [5, 6]], [2, 3], [[1, 4], [5, 6]]),
            ([[1, 2], [3, 4], [5, 6]], [0, 7], [[0, 7]]),
            ([[2, 3], [5, 6]], [1, 4], [[1, 4], [5, 6]]),
            ([[1, 5], [10, 15]], [6, 9], [[1, 5], [6, 9], [10, 15]]),
        ],
    )
    def test_insert(
        self, intervals: list[list[int]], new_interval: list[int], expected: list[list[int]]
    ):
        result = run_insert(Solution, intervals, new_interval)
        assert_insert(result, expected)
