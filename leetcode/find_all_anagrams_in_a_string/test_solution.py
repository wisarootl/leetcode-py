import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_find_anagrams, run_find_anagrams
from .solution import Solution


class TestFindAllAnagramsInAString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, p, expected",
        [
            ("cbaebabacd", "abc", [0, 6]),
            ("abab", "ab", [0, 1, 2]),
            ("a", "aa", []),
            ("aa", "aa", [0]),
            ("abcdefg", "xyz", []),
            ("aab", "ab", [1]),
            ("aaab", "ab", [2]),
            ("baa", "aa", [1]),
            ("abacabad", "aaab", []),
            ("ababacb", "abc", [3, 4]),
            ("abaacbabc", "abc", [3, 4, 6]),
            ("abab", "abab", [0]),
        ],
    )
    def test_find_anagrams(self, s: str, p: str, expected: list[int]):
        result = run_find_anagrams(Solution, s, p)
        assert_find_anagrams(result, expected)
