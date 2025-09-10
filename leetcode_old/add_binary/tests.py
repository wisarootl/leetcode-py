import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestAddBinary:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            ("11", "1", "100"),
            ("1010", "1011", "10101"),
            ("0", "0", "0"),
            ("1", "1", "10"),
            ("1111", "1111", "11110"),
        ],
    )
    @logged_test
    def test_add_binary(self, a: str, b: str, expected: str):
        result = self.solution.add_binary(a, b)
        assert result == expected
