import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_oranges_rotting, run_oranges_rotting
from .solution import Solution


class TestRottingOranges:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
            ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),
            ([[0, 2]], 0),
            ([[0]], 0),
            ([[1]], -1),
            ([[2]], 0),
            ([[1, 2]], 1),
            ([[2, 1]], 1),
            ([[0, 1, 2]], 1),
            ([[2, 2], [1, 1], [0, 0]], 1),
            ([[2, 1, 1], [1, 1, 1], [0, 1, 2]], 2),
        ],
    )
    def test_oranges_rotting(self, grid: list[list[int]], expected: int):
        result = run_oranges_rotting(Solution, grid)
        assert_oranges_rotting(result, expected)
