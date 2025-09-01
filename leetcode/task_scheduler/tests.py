import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution, SolutionGreedy


class TestTaskScheduler:
    @pytest.mark.parametrize("solution_class", [Solution, SolutionGreedy])
    @pytest.mark.parametrize(
        "tasks, n, expected",
        [
            (["A", "A", "A", "B", "B", "B"], 2, 8),
            (["A", "C", "A", "B", "D", "B"], 1, 6),
            (["A", "A", "A", "B", "B", "B"], 3, 10),
            (["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2, 16),
            (["A"], 2, 1),
        ],
    )
    @logged_test
    def test_least_interval(
        self,
        tasks: list[str],
        n: int,
        expected: int,
        solution_class: type[Solution | SolutionGreedy],
    ):
        solution = solution_class()
        result = solution.least_interval(tasks, n)
        assert result == expected
