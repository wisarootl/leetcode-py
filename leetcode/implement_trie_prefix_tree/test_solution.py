import pytest

from leetcode_py import logged_test

from .helpers import assert_trie_operations, run_trie_operations
from .solution import Trie


class TestImplementTriePrefixTree:

    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["Trie", "insert", "insert", "search", "search", "search"],
                [[], ["app"], ["apple"], ["app"], ["apple"], ["appl"]],
                [None, None, None, True, True, False],
            ),
            (
                ["Trie", "insert", "insert", "insert", "search", "search", "search"],
                [[], ["cat"], ["car"], ["card"], ["cat"], ["car"], ["care"]],
                [None, None, None, None, True, True, False],
            ),
            (
                ["Trie", "insert", "insert", "starts_with", "starts_with", "starts_with"],
                [[], ["test"], ["testing"], ["test"], ["testing"], ["te"]],
                [None, None, None, True, True, True],
            ),
            (
                ["Trie", "insert", "search", "search", "insert", "search", "search"],
                [[], ["abc"], ["abc"], ["ab"], ["ab"], ["ab"], ["abc"]],
                [None, None, True, False, None, True, True],
            ),
            (
                ["Trie", "insert", "search", "starts_with"],
                [[], ["a"], ["a"], ["a"]],
                [None, None, True, True],
            ),
            (
                ["Trie", "search", "starts_with"],
                [[], ["empty"], ["empty"]],
                [None, False, False],
            ),
            (
                ["Trie", "insert", "insert", "search", "search", "starts_with", "starts_with"],
                [[], ["word"], ["world"], ["word"], ["world"], ["wor"], ["wo"]],
                [None, None, None, True, True, True, True],
            ),
            (
                ["Trie", "insert", "insert", "insert", "search", "search", "search", "starts_with"],
                [[], ["aa"], ["aaa"], ["aaaa"], ["aa"], ["aaa"], ["aaaa"], ["a"]],
                [None, None, None, None, True, True, True, True],
            ),
            (
                ["Trie", "insert", "search", "search", "starts_with", "starts_with"],
                [[], ["hello"], ["hello"], ["hell"], ["hello"], ["hel"]],
                [None, None, True, False, True, True],
            ),
            (
                [
                    "Trie",
                    "insert",
                    "insert",
                    "insert",
                    "search",
                    "search",
                    "search",
                    "starts_with",
                    "starts_with",
                ],
                [[], ["she"], ["sells"], ["sea"], ["she"], ["shells"], ["sea"], ["se"], ["s"]],
                [None, None, None, None, True, False, True, True, True],
            ),
            (
                [
                    "Trie",
                    "insert",
                    "insert",
                    "search",
                    "search",
                    "starts_with",
                    "starts_with",
                    "starts_with",
                ],
                [
                    [],
                    ["programming"],
                    ["program"],
                    ["programming"],
                    ["program"],
                    ["prog"],
                    ["programming"],
                    ["programm"],
                ],
                [None, None, None, True, True, True, True, True],
            ),
            (
                ["Trie", "insert", "search", "starts_with", "insert", "search", "starts_with"],
                [[], ["z"], ["z"], ["z"], ["zzz"], ["zzz"], ["zz"]],
                [None, None, True, True, None, True, True],
            ),
        ],
    )
    def test_trie_operations(
        self, operations: list[str], inputs: list[list[str]], expected: list[bool | None]
    ):
        result, _ = run_trie_operations(Trie, operations, inputs)
        assert_trie_operations(result, expected)
