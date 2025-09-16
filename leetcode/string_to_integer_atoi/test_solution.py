import pytest

from leetcode_py import logged_test

from .helpers import assert_my_atoi, run_my_atoi
from .solution import Solution


class TestStringToIntegerAtoi:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("42", 42),
            ("   -042", -42),
            ("1337c0d3", 1337),
            ("0-1", 0),
            ("words and 987", 0),
            ("", 0),
            ("   ", 0),
            ("+1", 1),
            ("-1", -1),
            ("2147483647", 2147483647),
            ("-2147483648", -2147483648),
            ("2147483648", 2147483647),
            ("-2147483649", -2147483648),
        ],
    )
    def test_my_atoi(self, s: str, expected: int):
        result = run_my_atoi(Solution, s)
        assert_my_atoi(result, expected)
