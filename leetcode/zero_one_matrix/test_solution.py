import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_update_matrix, run_update_matrix
from .solution import Solution


class TestZeroOneMatrix:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "mat, expected",
        [
            ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
            ([[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[0, 0, 0], [0, 1, 0], [1, 2, 1]]),
            ([[0]], [[0]]),
            ([[1, 0]], [[1, 0]]),
            ([[1, 1], [1, 0]], [[2, 1], [1, 0]]),
            ([[0, 1, 0], [1, 1, 1], [0, 1, 0]], [[0, 1, 0], [1, 2, 1], [0, 1, 0]]),
            ([[1, 0, 1], [1, 1, 1], [1, 1, 1]], [[1, 0, 1], [2, 1, 2], [3, 2, 3]]),
            ([[0, 1, 0, 0], [1, 1, 1, 0], [1, 1, 1, 0]], [[0, 1, 0, 0], [1, 2, 1, 0], [2, 2, 1, 0]]),
        ],
    )
    def test_update_matrix(self, mat: list[list[int]], expected: list[list[int]]):
        result = run_update_matrix(Solution, mat)
        assert_update_matrix(result, expected)
