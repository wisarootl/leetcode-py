import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestClimbingStairs:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "n, expected",
        [(1, 1), (2, 2), (3, 3), (4, 5), (5, 8), (6, 13), (10, 89), (20, 10946), (45, 1836311903)],
    )
    @logged_test
    def test_climb_stairs(self, n: int, expected: int):
        result = self.solution.climb_stairs(n)
        assert result == expected
