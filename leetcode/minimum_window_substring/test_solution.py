import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_min_window, run_min_window
from .solution import Solution


class TestMinimumWindowSubstring:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, t, expected",
        [
            ("ADOBECODEBANC", "ABC", "BANC"),
            ("a", "a", "a"),
            ("a", "aa", ""),
            ("ab", "b", "b"),
            ("abc", "cba", "abc"),
        ],
    )
    def test_min_window(self, s: str, t: str, expected: str):
        result = run_min_window(Solution, s, t)
        assert_min_window(result, expected)
