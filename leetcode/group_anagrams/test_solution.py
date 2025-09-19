import pytest

from leetcode_py import logged_test

from .helpers import assert_group_anagrams, run_group_anagrams
from .solution import Solution


class TestGroupAnagrams:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "strs, expected",
        [
            (
                ["eat", "tea", "tan", "ate", "nat", "bat"],
                [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
            ),
            ([""], [[""]]),
            (["a"], [["a"]]),
            (["abc", "bca", "cab", "xyz"], [["abc", "bca", "cab"], ["xyz"]]),
            (["ab", "ba"], [["ab", "ba"]]),
            (["abc"], [["abc"]]),
            (["listen", "silent", "hello"], [["listen", "silent"], ["hello"]]),
            (["aab", "aba", "baa"], [["aab", "aba", "baa"]]),
            (["race", "care", "acre"], [["race", "care", "acre"]]),
            (["", "b"], [[""], ["b"]]),
            (["a", "aa", "aaa"], [["a"], ["aa"], ["aaa"]]),
            (["abc", "def", "ghi"], [["abc"], ["def"], ["ghi"]]),
            (["abcd", "dcba", "lls", "sll"], [["abcd", "dcba"], ["lls", "sll"]]),
            (["ac", "c"], [["ac"], ["c"]]),
            (["huh", "tit"], [["huh"], ["tit"]]),
        ],
    )
    def test_group_anagrams(self, strs: list[str], expected: list[list[str]]):
        result = run_group_anagrams(Solution, strs)
        assert_group_anagrams(result, expected)
