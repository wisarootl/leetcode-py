import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestKClosestPointsToOrigin:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "points, k, expected",
        [
            # Basic examples
            ([[1, 3], [-2, 2]], 1, [[-2, 2]]),
            ([[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]]),
            ([[0, 1], [1, 0]], 2, [[0, 1], [1, 0]]),
            ([[1, 1], [1, 1], [1, 1]], 2, [[1, 1], [1, 1]]),
            # Edge cases
            ([[0, 0]], 1, [[0, 0]]),  # Origin point
            ([[1, 0], [0, 1], [-1, 0], [0, -1]], 1, [[1, 0]]),  # Unit circle points
            ([[2, 2], [1, 1], [3, 3]], 3, [[1, 1], [2, 2], [3, 3]]),  # All points
            # Negative coordinates
            ([[-1, -1], [-2, -2], [1, 1]], 2, [[-1, -1], [1, 1]]),
            # Large coordinates
            ([[100, 100], [1, 1], [50, 50]], 1, [[1, 1]]),
            # Same distances
            ([[1, 0], [0, 1], [-1, 0], [0, -1]], 2, [[1, 0], [0, 1]]),
        ],
    )
    @logged_test
    def test_k_closest(self, points: list[list[int]], k: int, expected: list[list[int]]):
        result = self.solution.k_closest(points, k)
        # Sort both result and expected for comparison since order doesn't matter
        result_sorted = sorted(result)
        expected_sorted = sorted(expected)
        assert result_sorted == expected_sorted
