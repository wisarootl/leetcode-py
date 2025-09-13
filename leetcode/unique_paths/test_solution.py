import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_unique_paths, run_unique_paths
from .solution import Solution, SolutionMath


class TestUniquePaths:
    @logged_test
    @pytest.mark.parametrize("solution_class", [Solution, SolutionMath])
    @pytest.mark.parametrize(
        "m, n, expected",
        [
            (3, 7, 28),
            (3, 2, 3),
            (1, 1, 1),
            (1, 10, 1),
            (10, 1, 1),
            (2, 2, 2),
            (3, 3, 6),
            (4, 4, 20),
            (5, 5, 70),
            (2, 3, 3),
            (3, 4, 10),
            (4, 5, 35),
            (6, 3, 21),
            (7, 3, 28),
            (10, 10, 48620),
        ],
    )
    def test_unique_paths(self, solution_class, m: int, n: int, expected: int):
        result = run_unique_paths(solution_class, m, n)
        assert_unique_paths(result, expected)
