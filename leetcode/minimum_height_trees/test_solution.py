import pytest

from leetcode_py import logged_test

from .helpers import assert_find_min_height_trees, run_find_min_height_trees
from .solution import Solution


class TestMinimumHeightTrees:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, edges, expected",
        [
            (4, [[1, 0], [1, 2], [1, 3]], [1]),
            (6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]], [3, 4]),
            (1, [], [0]),
            (2, [[0, 1]], [0, 1]),
            (3, [[0, 1], [1, 2]], [1]),
            (5, [[0, 1], [1, 2], [2, 3], [3, 4]], [2]),
            (7, [[0, 1], [1, 2], [1, 3], [2, 4], [3, 5], [4, 6]], [1, 2]),
            (6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]], [3, 4]),
            (10, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]], [4, 5]),
            (8, [[0, 1], [1, 2], [2, 3], [0, 4], [4, 5], [5, 6], [6, 7]], [0, 4]),
            (9, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8]], [0, 1]),
            (11, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]], [5]),
        ],
    )
    def test_find_min_height_trees(self, n: int, edges: list[list[int]], expected: list[int]):
        result = run_find_min_height_trees(Solution, n, edges)
        assert_find_min_height_trees(result, expected)
