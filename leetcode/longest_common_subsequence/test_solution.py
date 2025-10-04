import pytest

from leetcode_py import logged_test

from .helpers import assert_longest_common_subsequence, run_longest_common_subsequence
from .solution import Solution


class TestLongestCommonSubsequence:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "text1, text2, expected",
        [
            ("abcde", "ace", 3),
            ("abc", "abc", 3),
            ("abc", "def", 0),
            ("", "", 0),
            ("a", "a", 1),
            ("a", "b", 0),
            ("ab", "ba", 1),
            ("abc", "bca", 2),
            ("abcdef", "ace", 3),
            ("abcdef", "adf", 3),
            ("abcdef", "xyz", 0),
            ("abcdef", "abcdef", 6),
            ("abcdef", "fedcba", 1),
            ("abcdef", "aceg", 3),
            ("abcdef", "bdf", 3),
            ("abcdef", "bdfh", 3),
            ("abcdef", "bdfhj", 3),
            ("abcdef", "bdfhjl", 3),
        ],
    )
    def test_longest_common_subsequence(self, text1: str, text2: str, expected: int):
        result = run_longest_common_subsequence(Solution, text1, text2)
        assert_longest_common_subsequence(result, expected)
