import pytest
from loguru import logger

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestSpiralMatrix:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "matrix, expected",
        [
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
            ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
            ([[1]], [1]),
            ([[1, 2], [3, 4]], [1, 2, 4, 3]),
            ([[1, 2, 3]], [1, 2, 3]),
            ([[1], [2], [3]], [1, 2, 3]),
            ([[1, 2], [3, 4], [5, 6]], [1, 2, 4, 6, 5, 3]),
            ([[1, 2, 3, 4, 5]], [1, 2, 3, 4, 5]),
            ([[1], [2], [3], [4], [5]], [1, 2, 3, 4, 5]),
            ([[1, 2, 3, 4], [5, 6, 7, 8]], [1, 2, 3, 4, 8, 7, 6, 5]),
            ([], []),
            ([[]], []),
        ],
    )
    @logged_test
    def test_spiral_order(self, matrix: list[list[int]], expected: list[int]):
        logger.info(f"Testing with matrix={matrix}")
        result = self.solution.spiral_order(matrix)
        logger.success(f"Got result: {result}")
        assert result == expected


class TestSpiralMatrixInvalid:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "matrix",
        [
            [[1, 2, 3], [4, 5], [6, 7, 8]],
            [[1], [2, 3], [4, 5, 6]],
            [[1, 2], [3, 4, 5]],
            [[1, 2, 3, 4], [5, 6]],
        ],
    )
    def test_invalid_matrix(self, matrix: list[list[int]]):
        with pytest.raises(ValueError, match="Invalid matrix: all rows must have same length"):
            self.solution.spiral_order(matrix)
