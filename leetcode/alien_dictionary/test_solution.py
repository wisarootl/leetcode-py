import pytest

from leetcode_py import logged_test

from .helpers import assert_alien_order, run_alien_order
from .solution import Solution


class TestAlienDictionary:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "words, expected",
        [
            (["wrt", "wrf", "er", "ett", "rftt"], "wertf"),
            (["z", "x"], "zx"),
            (["z", "x", "z"], ""),
            (["z", "z"], "z"),
            (["abc", "ab"], ""),
            (["ab", "adc"], "abdc"),
            (["ac", "ab", "zc", "zb"], "acbz"),
            (["z"], "z"),
            (["za", "zb", "ca", "cb"], "zcab"),
            (["zy", "zx"], "zyx"),
            (["a", "b", "ca", "cc"], "abc"),
            (["abc", "bcd", "cde"], "abcde"),
            (["a", "aa"], "a"),
            (["ab", "abc"], "abc"),
            (["abc", "ab"], ""),
            (["a", "b", "c", "d"], "abcd"),
            (["d", "c", "b", "a"], "dcba"),
            (["ac", "ab", "b"], "acb"),
        ],
    )
    def test_alien_order(self, words: list[str], expected: str):
        result = run_alien_order(Solution, words)
        assert_alien_order(result, expected)
