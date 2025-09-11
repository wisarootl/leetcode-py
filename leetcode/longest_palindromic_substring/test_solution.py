import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_longest_palindrome, run_longest_palindrome
from .solution import Solution


class TestLongestPalindromicSubstring:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("babad", {"bab", "aba"}),
            ("cbbd", {"bb"}),
            ("a", {"a"}),
            ("ac", {"a", "c"}),
            ("racecar", {"racecar"}),
            ("aabbaa", {"aabbaa"}),
            ("abacabad", {"abacaba"}),
            ("noon", {"noon"}),
            ("abccba", {"abccba"}),
            ("aa", {"aa"}),
            ("aba", {"aba"}),
            ("abcba", {"abcba"}),
        ],
    )
    def test_longest_palindrome(self, s: str, expected: set[str]):
        result = run_longest_palindrome(Solution, s)
        assert_longest_palindrome(result, expected)
