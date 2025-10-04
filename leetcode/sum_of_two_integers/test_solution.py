import pytest

from leetcode_py import logged_test

from .helpers import assert_get_sum, run_get_sum
from .solution import Solution


class TestSumOfTwoIntegers:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (1, 2, 3),
            (2, 3, 5),
            (-1, 1, 0),
            (0, 0, 0),
            (100, 200, 300),
            (-100, -200, -300),
            (1, -1, 0),
            (999, 1, 1000),
            (-999, -1, -1000),
            (0, 1, 1),
            (1, 0, 1),
            (5, -3, 2),
            (-5, 3, -2),
            (1000, 0, 1000),
            (0, 1000, 1000),
        ],
    )
    def test_get_sum(self, a: int, b: int, expected: int):
        result = run_get_sum(Solution, a, b)
        assert_get_sum(result, expected)
