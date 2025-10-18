import pytest

from leetcode_py import logged_test

from .helpers import assert_valid_tree, run_valid_tree
from .solution import Solution


class TestGraphValidTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, edges, expected",
        [
            (5, [[0, 1], [0, 2], [0, 3], [1, 4]], True),
            (5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], False),
            (1, [], True),
            (2, [[0, 1]], True),
            (2, [], False),
            (3, [[0, 1], [1, 2]], True),
            (3, [[0, 1], [0, 2], [1, 2]], False),
            (4, [[0, 1], [2, 3]], False),
            (4, [[0, 1], [1, 2], [2, 3]], True),
            (4, [[0, 1], [1, 2], [2, 3], [3, 0]], False),
            (0, [], True),
            (6, [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5]], True),
            (6, [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 5]], False),
            (5, [[0, 1], [0, 2], [0, 3], [0, 4]], True),
            (3, [[0, 1]], False),
            (4, [[0, 1], [0, 2], [0, 3], [1, 2]], False),
            (7, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]], True),
            (5, [[0, 1], [1, 2], [3, 4]], False),
        ],
    )
    def test_valid_tree(self, n: int, edges: list[list[int]], expected: bool):
        result = run_valid_tree(Solution, n, edges)
        assert_valid_tree(result, expected)
