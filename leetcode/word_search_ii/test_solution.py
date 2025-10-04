import pytest

from leetcode_py import logged_test

from .helpers import assert_find_words, run_find_words
from .solution import Solution


class TestWordSearchII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "board, words, expected",
        [
            (
                [
                    ["o", "a", "a", "n"],
                    ["e", "t", "a", "e"],
                    ["i", "h", "k", "r"],
                    ["i", "f", "l", "v"],
                ],
                ["oath", "pea", "eat", "rain"],
                ["eat", "oath"],
            ),
            ([["a", "b"], ["c", "d"]], ["abcb"], []),
            ([["a"]], ["a"], ["a"]),
            ([["a"]], ["b"], []),
            ([["a", "a"], ["a", "a"]], ["aaaa"], ["aaaa"]),
            ([["a", "a"], ["a", "a"]], ["aa"], ["aa"]),
            (
                [["a", "b"], ["c", "d"]],
                ["ab", "cd", "ac", "bd"],
                ["ab", "cd", "ac", "bd"],
            ),
            ([["a", "b"], ["c", "d"]], ["abcd"], []),
            (
                [
                    ["o", "a", "a", "n"],
                    ["e", "t", "a", "e"],
                    ["i", "h", "k", "r"],
                    ["i", "f", "l", "v"],
                ],
                ["oath", "pea", "eat", "rain", "oathf"],
                ["oath", "oathf", "eat"],
            ),
            (
                [["a", "b", "c"], ["a", "e", "d"], ["a", "f", "g"]],
                ["abcdefg", "gfedcbaaa", "eaabcdgfa", "befa", "dgc", "ade"],
                ["abcdefg", "befa", "eaabcdgfa", "gfedcbaaa"],
            ),
            ([["a", "b"], ["c", "d"]], ["abdc"], ["abdc"]),
            (
                [
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ],
                [
                    "a",
                    "aa",
                    "aaa",
                    "aaaa",
                    "aaaaa",
                    "aaaaaa",
                    "aaaaaaa",
                    "aaaaaaaa",
                    "aaaaaaaaa",
                    "aaaaaaaaaa",
                ],
                [
                    "a",
                    "aa",
                    "aaa",
                    "aaaa",
                    "aaaaa",
                    "aaaaaa",
                    "aaaaaaa",
                    "aaaaaaaa",
                    "aaaaaaaaa",
                    "aaaaaaaaaa",
                ],
            ),
        ],
    )
    def test_find_words(self, board: list[list[str]], words: list[str], expected: list[str]):
        result = run_find_words(Solution, board, words)
        assert_find_words(result, expected)
