import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_calculate, run_calculate
from .solution import Solution


class TestBasicCalculator:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("1 + 1", 2),
            (" 2-1 + 2 ", 3),
            ("(1+(4+5+2)-3)+(6+8)", 23),
            ("1", 1),
            ("-1", -1),
            ("-(1+2)", -3),
            ("2147483647", 2147483647),
            ("1-1+1", 1),
            # Additional edge cases from old tests
            ("0", 0),
            ("-0", 0),
            ("1+(2+3)", 6),
            ("(1+2)+3", 6),
            ("1-(2+3)", -4),
            ("(1-2)+3", 2),
            ("-(-1)", 1),
            ("-(-(-1))", -1),
            ("1000000-999999", 1),
            ("10+20-30+40", 40),
            ("((1+2)+(3+4))", 10),
            ("1+(2-(3+4))", -4),
            ("-(1+(2+3))", -6),
            ("   1   +   2   ", 3),
            ("123+456", 579),
            ("-2147483648", -2147483648),
        ],
    )
    def test_calculate(self, s: str, expected: int):
        result = run_calculate(Solution, s)
        assert_calculate(result, expected)

    @logged_test
    @pytest.mark.parametrize(
        "s, error_msg",
        [
            ("(1+2", "Mismatched parentheses"),
            ("1+2)", "Mismatched parentheses"),
            ("((1+2)", "Mismatched parentheses"),
            ("1+2))", "Mismatched parentheses"),
            ("1*2", r"Invalid character: '\*'"),
            ("1/2", "Invalid character: '/'"),
            ("1%2", "Invalid character: '%'"),
            ("1^2", r"Invalid character: '\^'"),
            ("1&2", "Invalid character: '&'"),
            ("a+b", "Invalid character: 'a'"),
            ("1+2.5", r"Invalid character: '\.'"),
        ],
    )
    def test_calculate_invalid_input(self, s: str, error_msg: str):
        with pytest.raises(ValueError, match=error_msg):
            self.solution.calculate(s)
