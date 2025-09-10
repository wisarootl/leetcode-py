import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestLongestPalindrome:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "s, expected",
        [
            ("abccccdd", 7),
            ("a", 1),
            ("Aa", 1),
            ("aabbcc", 6),
            ("abc", 1),
            ("abcdef", 1),
            ("aab", 3),
            ("aaaa", 4),
            ("AaBbCc", 1),
            ("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendure", 73),
            ("bananas", 5),
        ],
    )
    @logged_test
    def test_longest_palindrome(self, s: str, expected: int):
        result = self.solution.longest_palindrome(s)
        assert result == expected
