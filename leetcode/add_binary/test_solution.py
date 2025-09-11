import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_add_binary, run_add_binary
from .solution import Solution


class TestAddBinary:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "a, b, expected",
        [
            ("11", "1", "100"),
            ("1010", "1011", "10101"),
            ("0", "0", "0"),
            ("1", "1", "10"),
            ("1111", "1111", "11110"),
            ("1", "0", "1"),
            ("0", "1", "1"),
            ("1", "111", "1000"),
            ("111", "1", "1000"),
            ("1010", "1", "1011"),
            ("1111", "1", "10000"),
        ],
    )
    def test_add_binary(self, a: str, b: str, expected: str):
        result = run_add_binary(Solution, a, b)
        assert_add_binary(result, expected)
