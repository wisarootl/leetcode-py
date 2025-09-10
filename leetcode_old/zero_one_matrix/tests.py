import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestZeroOneMatrix:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "mat, expected",
        [
            ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
            ([[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[0, 0, 0], [0, 1, 0], [1, 2, 1]]),
            ([[0]], [[0]]),
            ([[1, 1, 1], [1, 1, 1], [1, 1, 0]], [[4, 3, 2], [3, 2, 1], [2, 1, 0]]),
            ([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], [[0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5]]),
            (
                [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0, 1, 1]],
                [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0, 1, 2]],
            ),
        ],
    )
    @logged_test
    def test_update_matrix(self, mat: list[list[int]], expected: list[list[int]]):
        result = self.solution.update_matrix(mat)
        assert result == expected
