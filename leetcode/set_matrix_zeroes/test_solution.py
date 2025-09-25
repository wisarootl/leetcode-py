import pytest

from leetcode_py import logged_test

from .helpers import assert_set_zeroes, run_set_zeroes
from .solution import Solution


class TestSetMatrixZeroes:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "matrix, expected",
        [
            ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
            (
                [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
                [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
            ),
            ([[1]], [[1]]),
            ([[0]], [[0]]),
            ([[1, 0]], [[0, 0]]),
            ([[0, 1]], [[0, 0]]),
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            ([[1, 2, 0], [4, 5, 6], [7, 8, 9]], [[0, 0, 0], [4, 5, 0], [7, 8, 0]]),
            ([[0, 2, 3], [4, 5, 6], [7, 8, 9]], [[0, 0, 0], [0, 5, 6], [0, 8, 9]]),
            ([[1, 2, 3], [4, 0, 6], [7, 8, 0]], [[1, 0, 0], [0, 0, 0], [0, 0, 0]]),
            ([[1, 2], [0, 4], [5, 6]], [[0, 2], [0, 0], [0, 6]]),
            ([[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]),
            ([[0, 2, 0], [4, 5, 6]], [[0, 0, 0], [0, 5, 0]]),
            ([[-1, 2, 3], [4, 0, -6]], [[-1, 0, 3], [0, 0, 0]]),
            (
                [[1, 2, 3, 4], [0, 5, 0, 7], [8, 9, 10, 11]],
                [[0, 2, 0, 4], [0, 0, 0, 0], [0, 9, 0, 11]],
            ),
        ],
    )
    def test_set_zeroes(self, matrix: list[list[int]], expected: list[list[int]]):
        result = run_set_zeroes(Solution, matrix)
        assert_set_zeroes(result, expected)
