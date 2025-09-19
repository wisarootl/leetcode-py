import pytest

from leetcode_py import logged_test

from .helpers import assert_word_dictionary, run_word_dictionary
from .solution import WordDictionary


class TestDesignAddAndSearchWordsDataStructure:

    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                [
                    "WordDictionary",
                    "addWord",
                    "addWord",
                    "addWord",
                    "search",
                    "search",
                    "search",
                    "search",
                ],
                [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]],
                [None, None, None, None, False, True, True, True],
            ),
            (
                ["WordDictionary", "addWord", "search", "search", "search"],
                [[], ["a"], ["a"], ["."], ["aa"]],
                [None, None, True, True, False],
            ),
            (
                ["WordDictionary", "addWord", "addWord", "search", "search", "search"],
                [[], ["at"], ["and"], ["an"], [".at"], ["an."]],
                [None, None, None, False, False, True],
            ),
            (
                ["WordDictionary", "addWord", "addWord", "search", "search"],
                [[], ["word"], ["world"], ["word"], ["wor."]],
                [None, None, None, True, True],
            ),
            (
                ["WordDictionary", "addWord", "search", "search"],
                [[], ["test"], ["test"], ["t..t"]],
                [None, None, True, True],
            ),
            (
                ["WordDictionary", "addWord", "addWord", "search", "search", "search"],
                [[], ["a"], ["b"], ["a"], ["."], ["c"]],
                [None, None, None, True, True, False],
            ),
            (
                ["WordDictionary", "addWord", "addWord", "search", "search", "search"],
                [[], ["abc"], ["def"], ["..."], ["a.."], ["..f"]],
                [None, None, None, True, True, True],
            ),
            (
                ["WordDictionary", "addWord", "addWord", "search", "search", "search"],
                [
                    [],
                    ["programming"],
                    ["algorithm"],
                    ["prog......."],
                    ["algo....."],
                    ["........ing"],
                ],
                [None, None, None, True, True, True],
            ),
            (
                ["WordDictionary", "addWord", "addWord", "search", "search"],
                [[], ["x"], ["xy"], ["."], [".."]],
                [None, None, None, True, True],
            ),
            (
                ["WordDictionary", "addWord", "addWord", "search", "search", "search"],
                [[], ["hello"], ["world"], ["hi"], ["word"], ["......"]],
                [None, None, None, False, False, False],
            ),
            (
                [
                    "WordDictionary",
                    "addWord",
                    "addWord",
                    "addWord",
                    "search",
                    "search",
                    "search",
                    "search",
                ],
                [[], ["cat"], ["car"], ["card"], ["c.."], ["ca."], ["c..d"], ["....."]],
                [None, None, None, None, True, True, True, False],
            ),
            (
                [
                    "WordDictionary",
                    "addWord",
                    "addWord",
                    "addWord",
                    "search",
                    "search",
                    "search",
                ],
                [
                    [],
                    ["run"],
                    ["runner"],
                    ["running"],
                    ["run"],
                    ["run..."],
                    ["run....."],
                ],
                [None, None, None, None, True, True, False],
            ),
            (
                ["WordDictionary", "addWord", "addWord", "search", "search", "search"],
                [[], ["abc"], ["xyz"], ["..."], [".."], ["...."]],
                [None, None, None, True, False, False],
            ),
        ],
    )
    def test_word_dictionary(
        self,
        operations: list[str],
        inputs: list[list[str]],
        expected: list[bool | None],
    ):
        result = run_word_dictionary(WordDictionary, operations, inputs)
        assert_word_dictionary(result, expected)
