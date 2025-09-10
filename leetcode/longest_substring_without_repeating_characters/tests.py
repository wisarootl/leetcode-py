import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestLongestSubstringWithoutRepeatingCharacters:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "s, expected",
        [
            ("abcabcbb", 3),  # "abc"
            ("bbbbb", 1),  # "b"
            ("pwwkew", 3),  # "wke"
            ("", 0),  # empty
            ("a", 1),  # single char
            ("au", 2),  # "au"
            ("dvdf", 3),  # "vdf"
            ("abcdef", 6),  # no repeats
            ("aab", 2),  # "ab"
            ("cdd", 2),  # "cd"
            ("abba", 2),  # "ab" or "ba"
            ("tmmzuxt", 5),  # "mzuxt"
            (" ", 1),  # space char
            ("!@#$%", 5),  # symbols
            ("abcabcabcabc", 3),  # repeating pattern
        ],
    )
    @logged_test
    def test_length_of_longest_substring(self, s: str, expected: int):
        result = self.solution.length_of_longest_substring(s)
        assert result == expected
