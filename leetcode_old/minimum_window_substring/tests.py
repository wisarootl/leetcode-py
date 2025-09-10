import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestMinimumWindowSubstring:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "s, t, expected",
        [
            # Basic cases
            ("ADOBECODEBANC", "ABC", "BANC"),
            ("a", "a", "a"),
            ("a", "aa", ""),
            # Edge cases
            ("", "a", ""),  # Empty s
            ("a", "", ""),  # Empty t
            ("", "", ""),  # Both empty
            ("ab", "ba", "ab"),  # Same length
            ("abc", "cba", "abc"),  # Entire string needed
            # Duplicates
            ("ADOBECODEBANC", "AABC", "ADOBECODEBA"),  # Correct: needs 2 A's, 1 B, 1 C
            ("aa", "aa", "aa"),
            # No solution
            ("abc", "def", ""),
            ("a", "b", ""),
            # Multiple valid windows
            ("ADOBECODEBANC", "AB", "BA"),  # Correct: "BA" is shorter than "ADOB"
            ("abcdef", "cf", "cdef"),
        ],
    )
    @logged_test
    def test_min_window(self, s: str, t: str, expected: str):
        result = self.solution.min_window(s, t)
        assert result == expected
