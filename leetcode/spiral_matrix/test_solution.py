import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_spiral_order, run_spiral_order
from .solution import Solution


class TestSpiralMatrix:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "matrix, expected",
        [
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
            ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
            ([[1]], [1]),
            ([[1, 2]], [1, 2]),
            ([[1], [2]], [1, 2]),
            ([[1, 2, 3]], [1, 2, 3]),
            ([[1], [2], [3]], [1, 2, 3]),
        ],
    )
    def test_spiral_order(self, matrix: list[list[int]], expected: list[int]):
        result = run_spiral_order(Solution, matrix)
        assert_spiral_order(result, expected)
