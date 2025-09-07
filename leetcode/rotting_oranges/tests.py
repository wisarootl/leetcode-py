import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestTestRottingOranges:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "grid, expected",
        [
            # Original examples
            ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
            ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),
            ([[0, 2]], 0),
            # Single cell cases
            ([[0]], 0),
            ([[1]], -1),
            ([[2]], 0),
            # Two cell cases
            ([[1, 2]], 1),
            ([[2, 1]], 1),
            ([[0, 1, 2]], 1),
            # Multiple rotten sources
            ([[2, 2], [1, 1], [0, 0]], 1),
            ([[2, 1, 1], [1, 1, 1], [0, 1, 2]], 2),
            # All empty grid
            ([[0, 0, 0], [0, 0, 0]], 0),
            # All rotten grid
            ([[2, 2, 2], [2, 2, 2]], 0),
            # All fresh grid (impossible)
            ([[1, 1, 1], [1, 1, 1]], -1),
            # Large grid with barriers
            ([[2, 1, 0, 0, 1], [1, 0, 0, 0, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 2]], 3),
            # Cross pattern
            ([[0, 1, 0], [1, 2, 1], [0, 1, 0]], 1),
            # Diagonal (no spread)
            ([[2, 0, 1], [0, 0, 0], [1, 0, 1]], -1),
            # Ring pattern
            ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], -1),
            # Multiple disconnected fresh groups
            ([[2, 1, 0, 1], [0, 0, 0, 0], [1, 0, 0, 2]], -1),
            # Linear spread
            ([[2, 1, 1, 1, 1]], 4),
            # Vertical spread
            ([[2], [1], [1], [1]], 3),
            # Corner cases
            ([[2, 0, 0], [0, 0, 0], [0, 0, 1]], -1),
            ([[1, 0, 0], [0, 0, 0], [0, 0, 2]], -1),
            # Complex maze-like
            ([[2, 1, 1, 0, 1], [1, 0, 1, 0, 1], [1, 1, 1, 0, 2]], 4),
        ],
    )
    @logged_test
    def test_oranges_rotting(self, grid: list[list[int]], expected: int):
        result = self.solution.oranges_rotting(grid)
        assert result == expected
