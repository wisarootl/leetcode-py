import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestNumberOfIslands:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "grid, expected",
        [
            # Basic examples
            (
                [
                    ["1", "1", "1", "1", "0"],
                    ["1", "1", "0", "1", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "0", "0", "0"],
                ],
                1,
            ),
            (
                [
                    ["1", "1", "0", "0", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "1", "0", "0"],
                    ["0", "0", "0", "1", "1"],
                ],
                3,
            ),
            # Edge cases
            ([["1"]], 1),
            ([["0"]], 0),
            ([["1", "0", "1"], ["0", "1", "0"], ["1", "0", "1"]], 5),
            # All water
            ([["0", "0", "0"], ["0", "0", "0"]], 0),
            # All land
            ([["1", "1", "1"], ["1", "1", "1"]], 1),
            # Single row
            ([["1", "0", "1", "0", "1"]], 3),
            # Single column
            ([["1"], ["0"], ["1"], ["0"], ["1"]], 3),
            # L-shaped island
            ([["1", "1", "0"], ["1", "0", "0"], ["1", "1", "1"]], 1),
            # Diagonal pattern (no connections)
            ([["1", "0", "0"], ["0", "1", "0"], ["0", "0", "1"]], 3),
            # Large grid with multiple islands
            (
                [
                    ["1", "0", "0", "1", "1", "0"],
                    ["0", "0", "0", "0", "1", "0"],
                    ["0", "0", "1", "0", "0", "0"],
                    ["1", "1", "0", "0", "0", "1"],
                ],
                5,
            ),
            # Snake-like island
            ([["1", "1", "0"], ["0", "1", "0"], ["0", "1", "1"]], 1),
        ],
    )
    @logged_test
    def test_num_islands(self, grid: list[list[str]], expected: int):
        result = self.solution.num_islands(grid)
        assert result == expected
