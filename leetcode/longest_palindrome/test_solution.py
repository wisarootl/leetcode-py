import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_longest_palindrome, run_longest_palindrome
from .solution import Solution


class TestLongestPalindrome:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("abccccdd", 7),
            ("a", 1),
            ("Aa", 1),
            ("aabbcc", 6),
            ("", 0),
            ("aA", 1),
            ("abcdef", 1),
            ("aabbccdd", 8),
            ("aaaa", 4),
            ("abcdefg", 1),
            ("AAaa", 4),
            ("racecar", 7),
            ("abcABC", 1),
        ],
    )
    def test_longest_palindrome(self, s: str, expected: int):
        result = run_longest_palindrome(Solution, s)
        assert_longest_palindrome(result, expected)
