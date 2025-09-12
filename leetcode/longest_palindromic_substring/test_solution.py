import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_longest_palindrome, run_longest_palindrome
from .solution import Solution, SolutionManacher


class TestLongestPalindromicSubstring:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize("solution_class", [Solution, SolutionManacher])
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
    def test_longest_palindrome(self, solution_class: type, s: str, expected: set[str]):
        result = run_longest_palindrome(solution_class, s)
        assert_longest_palindrome(result, expected)
