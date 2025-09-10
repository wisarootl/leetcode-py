import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestValidAnagram:
    def setup_method(self):
        self.solution = Solution()

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
    @logged_test
    def test_is_anagram(self, s: str, t: str, expected: bool):
        result = self.solution.is_anagram(s, t)
        assert result == expected
