import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestMinimumHeightTrees:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "n, edges, expected",
        [
            (4, [[1, 0], [1, 2], [1, 3]], [1]),
            (6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]], [3, 4]),
            (1, [], [0]),
        ],
    )
    @logged_test
    def test_find_min_height_trees(self, n: int, edges: list[list[int]], expected: list[int]):
        result = self.solution.find_min_height_trees(n, edges)
        assert sorted(result) == sorted(expected)
