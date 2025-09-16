import pytest

from leetcode_py import logged_test

from .helpers import assert_can_construct, run_can_construct
from .solution import Solution


class TestRansomNote:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "ransom_note, magazine, expected",
        [
            ("a", "b", False),
            ("aa", "ab", False),
            ("aa", "aab", True),
            ("aab", "baa", True),
            ("", "", True),
            ("", "abc", True),
            ("abc", "", False),
            ("abc", "abc", True),
            ("abc", "cba", True),
            ("aaa", "aa", False),
            ("ab", "ba", True),
        ],
    )
    def test_can_construct(self, ransom_note: str, magazine: str, expected: bool):
        result = run_can_construct(Solution, ransom_note, magazine)
        assert_can_construct(result, expected)
