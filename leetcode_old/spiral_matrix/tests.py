import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestSpiralMatrix:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "matrix, expected",
        [
            # Original cases
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
            ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
            # Single element
            ([[1]], [1]),
            # Single row
            ([[1, 2, 3, 4]], [1, 2, 3, 4]),
            # Single column
            ([[1], [2], [3]], [1, 2, 3]),
            # 2x2 matrix
            ([[1, 2], [3, 4]], [1, 2, 4, 3]),
            # 1x2 matrix
            ([[1, 2]], [1, 2]),
            # 2x1 matrix
            ([[1], [2]], [1, 2]),
            # Larger square matrix
            (
                [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
                [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10],
            ),
        ],
    )
    @logged_test
    def test_spiral_order(self, matrix: list[list[int]], expected: list[int]):
        result = self.solution.spiral_order(matrix)
        assert result == expected
