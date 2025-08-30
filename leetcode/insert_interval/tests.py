import pytest
from loguru import logger

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestInsertInterval:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "intervals, newInterval, expected",
        [
            ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
            ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
            ([], [5, 7], [[5, 7]]),
            ([[1, 5]], [2, 3], [[1, 5]]),
        ],
    )
    @logged_test
    def test_insert(self, intervals: list[list[int]], newInterval: list[int], expected: list[list[int]]):
        logger.info(f"Testing with intervals={intervals}, newInterval={newInterval}")
        result = self.solution.insert(intervals, newInterval)
        logger.success(f"Got result: {result}")
        assert result == expected
