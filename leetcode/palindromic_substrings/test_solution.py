import pytest

from leetcode_py import logged_test

from .helpers import assert_count_substrings, run_count_substrings
from .solution import Solution


class TestPalindromicSubstrings:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("abc", 3),
            ("aaa", 6),
            ("a", 1),
            ("aa", 3),
            ("aba", 4),
            ("abccba", 9),
            ("racecar", 10),
            ("abcdef", 6),
            ("aab", 4),
            ("ababa", 9),
            ("aaaaa", 15),
            ("ab", 2),
            ("abcba", 7),
            ("abacaba", 12),
            ("xyz", 3),
        ],
    )
    def test_count_substrings(self, s: str, expected: int):
        result = run_count_substrings(Solution, s)
        assert_count_substrings(result, expected)
