import pytest

from leetcode_py import logged_test

from .helpers import assert_reverse, run_reverse
from .solution import Solution


class TestReverseInteger:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "x, expected",
        [
            (123, 321),
            (-123, -321),
            (120, 21),
            (0, 0),
            (1, 1),
            (-1, -1),
            (10, 1),
            (-10, -1),
            (100, 1),
            (-100, -1),
            (1534236469, 0),
            (-1534236469, 0),
            (2147483647, 0),
            (-2147483648, 0),
            (1463847412, 2147483641),
            (-1463847412, -2147483641),
            (123456789, 987654321),
            (-123456789, -987654321),
            (1000000003, 0),
            (-1000000003, 0),
        ],
    )
    def test_reverse(self, x: int, expected: int):
        result = run_reverse(Solution, x)
        assert_reverse(result, expected)
