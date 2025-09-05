import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestStringToIntegerAtoi:
    def setup_method(self):
        self.solution = Solution()

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
            # Edge cases
            ("+-12", 0),
            ("-+12", 0),
            ("++1", 0),
            ("--1", 0),
            ("   +0 123", 0),
            ("0000000000012345678", 12345678),
            ("-000000000000001", -1),
            ("   +000", 0),
            ("123-", 123),
            ("   13  5", 13),
            (".1", 0),
            ("1a33", 1),
            ("  -0012a42", -12),
            ("21474836460", 2147483647),
            ("-21474836480", -2147483648),
        ],
    )
    @logged_test
    def test_my_atoi(self, s: str, expected: int):
        result = self.solution.my_atoi(s)
        assert result == expected
