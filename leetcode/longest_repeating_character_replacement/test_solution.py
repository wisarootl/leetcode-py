import pytest

from leetcode_py import logged_test

from .helpers import assert_character_replacement, run_character_replacement
from .solution import Solution


class TestLongestRepeatingCharacterReplacement:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, k, expected",
        [
            ("ABAB", 2, 4),
            ("AABABBA", 1, 4),
            ("AAAA", 0, 4),
            ("ABCDE", 0, 1),
            ("ABCDE", 4, 5),
            ("A", 0, 1),
            ("A", 1, 1),
            ("AAAB", 0, 3),
            ("AAAB", 1, 4),
            ("ABABAB", 2, 5),
            ("ABABAB", 3, 6),
            ("ABCDEF", 0, 1),
            ("ABCDEF", 1, 2),
            ("ABCDEF", 5, 6),
            ("AABABBA", 2, 5),
        ],
    )
    def test_character_replacement(self, s: str, k: int, expected: int):
        result = run_character_replacement(Solution, s, k)
        assert_character_replacement(result, expected)
