import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_k_closest, run_k_closest
from .solution import Solution


class TestKClosestPointsToOrigin:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "points, k, expected",
        [
            ([[1, 3], [-2, 2]], 1, [[-2, 2]]),
            ([[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]]),
            ([[0, 1], [1, 0]], 2, [[0, 1], [1, 0]]),
            ([[1, 1], [1, 1], [1, 1]], 2, [[1, 1], [1, 1]]),
            ([[0, 0]], 1, [[0, 0]]),
            ([[1, 0], [2, 0], [3, 0]], 2, [[1, 0], [2, 0]]),
        ],
    )
    def test_k_closest(self, points: list[list[int]], k: int, expected: list[list[int]]):
        result = run_k_closest(Solution, points, k)
        assert_k_closest(result, expected)
