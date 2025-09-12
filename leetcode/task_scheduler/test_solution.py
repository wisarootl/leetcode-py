import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_least_interval, run_least_interval
from .solution import Solution, SolutionGreedy


class TestTaskScheduler:

    @logged_test
    @pytest.mark.parametrize("solution_class", [Solution, SolutionGreedy])
    @pytest.mark.parametrize(
        "tasks, n, expected",
        [
            (["A", "A", "A", "B", "B", "B"], 2, 8),
            (["A", "C", "A", "B", "D", "B"], 1, 6),
            (["A", "A", "A", "B", "B", "B"], 3, 10),
            (["A"], 0, 1),
            (["A", "A"], 1, 3),
            (["A", "B"], 0, 2),
        ],
    )
    def test_least_interval(self, tasks: list[str], n: int, expected: int, solution_class: type):
        result = run_least_interval(solution_class, tasks, n)
        assert_least_interval(result, expected)
