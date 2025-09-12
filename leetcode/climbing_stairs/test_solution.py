import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_climb_stairs, run_climb_stairs
from .solution import Solution


class TestClimbingStairs:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [(1, 1), (2, 2), (3, 3), (4, 5), (5, 8), (6, 13), (10, 89), (20, 10946), (45, 1836311903)],
    )
    def test_climb_stairs(self, n: int, expected: int):
        result = run_climb_stairs(Solution, n)
        assert_climb_stairs(result, expected)
