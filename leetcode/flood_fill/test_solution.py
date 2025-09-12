import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_flood_fill, run_flood_fill
from .solution import Solution


class TestFloodFill:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "image, sr, sc, color, expected",
        [
            ([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2, [[2, 2, 2], [2, 2, 0], [2, 0, 1]]),
            ([[0, 0, 0], [0, 0, 0]], 0, 0, 0, [[0, 0, 0], [0, 0, 0]]),
            ([[0, 0, 0], [0, 1, 1]], 1, 1, 1, [[0, 0, 0], [0, 1, 1]]),
            ([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 1, [[1, 1, 1], [1, 1, 0], [1, 0, 1]]),
            ([[1]], 0, 0, 2, [[2]]),
            ([[0, 1], [1, 0]], 0, 0, 3, [[3, 1], [1, 0]]),
            ([[1, 1], [1, 1]], 0, 0, 2, [[2, 2], [2, 2]]),
            ([[0, 1, 0], [1, 0, 1], [0, 1, 0]], 1, 1, 2, [[0, 1, 0], [1, 2, 1], [0, 1, 0]]),
            ([[2, 2, 2], [2, 2, 0], [2, 0, 1]], 0, 0, 3, [[3, 3, 3], [3, 3, 0], [3, 0, 1]]),
            ([[1, 0, 1], [0, 1, 0], [1, 0, 1]], 1, 1, 5, [[1, 0, 1], [0, 5, 0], [1, 0, 1]]),
            (
                [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]],
                1,
                1,
                2,
                [[0, 0, 0, 0], [0, 2, 2, 0], [0, 2, 2, 0], [0, 0, 0, 0]],
            ),
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1, 0, [[1, 2, 3], [4, 0, 6], [7, 8, 9]]),
        ],
    )
    def test_flood_fill(
        self, image: list[list[int]], sr: int, sc: int, color: int, expected: list[list[int]]
    ):
        result = run_flood_fill(Solution, image, sr, sc, color)
        assert_flood_fill(result, expected)
