import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestInsertInterval:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "intervals, new_interval, expected",
        [
            ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
            ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
        ],
    )
    @logged_test
    def test_insert(
        self, intervals: list[list[int]], new_interval: list[int], expected: list[list[int]]
    ):
        result = self.solution.insert(intervals, new_interval)
        assert result == expected
