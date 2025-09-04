import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution, SolutionManacher


class TestLongestPalindromicSubstring:
    def setup_method(self):
        self.solution = Solution()
        self.solution_manacher = SolutionManacher()

    @pytest.mark.parametrize(
        "solution_class",
        [Solution, SolutionManacher],
    )
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("babad", {"bab", "aba"}),
            ("cbbd", {"bb"}),
            ("a", {"a"}),
            ("ac", {"a", "c"}),
            ("racecar", {"racecar"}),
            ("abcdef", {"a", "b", "c", "d", "e", "f"}),
            ("aabbaa", {"aabbaa"}),
            ("abacabad", {"abacaba"}),
            ("aaaaaaaa", {"aaaaaaaa"}),
            ("noon", {"noon"}),
            ("abccba", {"abccba"}),
            ("", {""}),
            ("aa", {"aa"}),
            ("aba", {"aba"}),
            ("abcba", {"abcba"}),
            ("forgeeksskeegfor", {"geeksskeeg"}),
            ("bananas", {"anana"}),
            (
                "abcdefghijklmnopqrstuvwxyz",
                {
                    "a",
                    "b",
                    "c",
                    "d",
                    "e",
                    "f",
                    "g",
                    "h",
                    "i",
                    "j",
                    "k",
                    "l",
                    "m",
                    "n",
                    "o",
                    "p",
                    "q",
                    "r",
                    "s",
                    "t",
                    "u",
                    "v",
                    "w",
                    "x",
                    "y",
                    "z",
                },
            ),
        ],
    )
    @logged_test
    def test_longest_palindrome(self, solution_class, s: str, expected: set[str]):
        solution = solution_class()
        result = solution.longest_palindrome(s)
        assert result in expected
