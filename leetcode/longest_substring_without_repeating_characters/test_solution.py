import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_length_of_longest_substring, run_length_of_longest_substring
from .solution import Solution


class TestLongestSubstringWithoutRepeatingCharacters:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("abcabcbb", 3),
            ("bbbbb", 1),
            ("pwwkew", 3),
            ("", 0),
            ("a", 1),
            ("au", 2),
            ("dvdf", 3),
            ("abcdef", 6),
            ("aab", 2),
            ("tmmzuxt", 5),
            (" ", 1),
            ("  ", 1),
            ("abba", 2),
        ],
    )
    def test_length_of_longest_substring(self, s: str, expected: int):
        result = run_length_of_longest_substring(Solution, s)
        assert_length_of_longest_substring(result, expected)
