import pytest

from leetcode_py import logged_test

from .helpers import assert_least_interval, run_least_interval
from .solution import Solution


class TestTaskScheduler:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "tasks, n, expected",
        [
            (["A", "A", "A", "B", "B", "B"], 2, 8),
            (["A", "C", "A", "B", "D", "B"], 1, 6),
            (["A", "A", "A", "B", "B", "B"], 3, 10),
            (["A"], 0, 1),
            (["A", "A"], 1, 3),
            (["A", "B"], 0, 2),
            (["A", "A", "A"], 0, 3),
            (["A", "B", "C", "D", "E", "F"], 2, 6),
            (["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2, 16),
            (["A", "A", "B", "B"], 2, 5),
            (["A", "B", "A", "B"], 1, 4),
            (["A", "A", "A", "A"], 3, 13),
        ],
    )
    def test_least_interval(self, tasks: list[str], n: int, expected: int):
        result = run_least_interval(Solution, tasks, n)
        assert_least_interval(result, expected)
