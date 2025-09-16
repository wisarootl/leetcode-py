import pytest

from leetcode_py import logged_test

from .helpers import assert_is_anagram, run_is_anagram
from .solution import Solution


class TestValidAnagram:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, t, expected",
        [
            ("anagram", "nagaram", True),
            ("rat", "car", False),
            ("listen", "silent", True),
            ("hello", "bello", False),
            ("", "", True),
            ("a", "a", True),
            ("a", "b", False),
            ("ab", "ba", True),
            ("abc", "bca", True),
            ("abc", "def", False),
            ("aab", "abb", False),
            ("aabbcc", "abcabc", True),
            ("abcd", "abcde", False),
            ("race", "care", True),
            ("elbow", "below", True),
            ("study", "dusty", True),
            ("night", "thing", True),
            ("stressed", "desserts", True),
        ],
    )
    def test_is_anagram(self, s: str, t: str, expected: bool):
        result = run_is_anagram(Solution, s, t)
        assert_is_anagram(result, expected)
