import pytest

from leetcode_py import logged_test

from .helpers import assert_count_components, run_count_components
from .solution import Solution


class TestNumberOfConnectedComponentsInAnUndirectedGraph:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, edges, expected",
        [
            (5, [[0, 1], [1, 2], [3, 4]], 2),
            (5, [[0, 1], [1, 2], [2, 3], [3, 4]], 1),
            (1, [], 1),
            (2, [[0, 1]], 1),
            (2, [], 2),
            (3, [[0, 1]], 2),
            (3, [[0, 1], [1, 2]], 1),
            (4, [[0, 1], [2, 3]], 2),
            (4, [[0, 1], [1, 2], [2, 3]], 1),
            (6, [[0, 1], [1, 2], [3, 4]], 3),
            (0, [], 0),
            (7, [[0, 1], [1, 2], [3, 4], [4, 5]], 3),
            (8, [[0, 1], [1, 2], [2, 3], [4, 5], [5, 6], [6, 7]], 2),
            (5, [[0, 1], [0, 2], [0, 3], [0, 4]], 1),
            (6, [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5]], 1),
            (10, [], 10),
            (4, [[0, 1], [0, 2], [1, 2]], 2),
            (5, [[0, 1], [2, 3], [4, 4]], 3),
        ],
    )
    def test_count_components(self, n: int, edges: list[list[int]], expected: int):
        result = run_count_components(Solution, n, edges)
        assert_count_components(result, expected)
