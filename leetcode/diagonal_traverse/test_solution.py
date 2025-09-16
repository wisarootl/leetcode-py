import pytest

from leetcode_py import logged_test

from .helpers import assert_find_diagonal_order, run_find_diagonal_order
from .solution import Solution, SolutionRowShift


class TestDiagonalTraverse:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize("solution_class", [Solution, SolutionRowShift])
    @pytest.mark.parametrize(
        "mat, expected",
        [
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 4, 7, 5, 3, 6, 8, 9]),
            ([[1, 2], [3, 4]], [1, 2, 3, 4]),
            ([[1]], [1]),
            ([[1, 2, 3]], [1, 2, 3]),
            ([[1], [2], [3]], [1, 2, 3]),
            ([[1, 2, 3, 4], [5, 6, 7, 8]], [1, 2, 5, 6, 3, 4, 7, 8]),
            ([[1, 2], [3, 4], [5, 6]], [1, 2, 3, 5, 4, 6]),
            ([[1, 2, 3, 4, 5]], [1, 2, 3, 4, 5]),
            ([[1], [2], [3], [4], [5]], [1, 2, 3, 4, 5]),
            ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 5, 9, 6, 3, 4, 7, 10, 11, 8, 12]),
            ([[-1, 0, 1], [2, -3, 4]], [-1, 0, 2, -3, 1, 4]),
            ([[100]], [100]),
        ],
    )
    def test_find_diagonal_order(self, solution_class, mat: list[list[int]], expected: list[int]):
        result = run_find_diagonal_order(solution_class, mat)
        assert_find_diagonal_order(result, expected)
