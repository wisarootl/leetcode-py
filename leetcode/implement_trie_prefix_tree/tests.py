import pytest

from leetcode_py.test_utils import logged_test

from .solution import Trie


class TestImplementTriePrefixTree:
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["Trie", "insert", "search", "search", "starts_with", "insert", "search"],
                [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
                [None, None, True, False, True, None, True],
            ),
            (
                ["Trie", "insert", "insert", "search", "search", "starts_with", "starts_with"],
                [[], ["hello"], ["world"], ["hello"], ["hi"], ["hel"], ["wor"]],
                [None, None, None, True, False, True, True],
            ),
            (
                ["Trie", "insert", "insert", "search", "search", "starts_with", "starts_with"],
                [[], ["a"], ["aa"], ["a"], ["aa"], ["a"], ["aa"]],
                [None, None, None, True, True, True, True],
            ),
            (
                ["Trie", "insert", "search", "starts_with", "insert", "search", "starts_with"],
                [[], ["test"], ["testing"], ["test"], ["testing"], ["testing"], ["test"]],
                [None, None, False, True, None, True, True],
            ),
            (["Trie", "search", "starts_with"], [[], ["empty"], ["empty"]], [None, False, False]),
            (
                ["Trie", "insert", "insert", "search", "search", "starts_with"],
                [[], ["cat"], ["car"], ["cat"], ["card"], ["ca"]],
                [None, None, None, True, False, True],
            ),
            (
                ["Trie", "insert", "search", "insert", "search", "starts_with"],
                [[], ["abc"], ["ab"], ["ab"], ["ab"], ["a"]],
                [None, None, False, None, True, True],
            ),
            (
                ["Trie", "insert", "insert", "insert", "search", "starts_with"],
                [[], [""], ["a"], ["ab"], [""], [""]],
                [None, None, None, None, True, True],
            ),
            (
                ["Trie", "insert", "search", "starts_with", "insert", "search"],
                [[], ["z"], ["z"], ["z"], ["zzz"], ["zzz"]],
                [None, None, True, True, None, True],
            ),
            (
                ["Trie", "insert", "insert", "search", "search", "starts_with", "starts_with"],
                [[], ["prefix"], ["prefixsuffix"], ["prefix"], ["prefixsuffix"], ["pre"], ["prefixs"]],
                [None, None, None, True, True, True, True],
            ),
            (
                ["Trie", "insert", "insert", "search", "starts_with"],
                [[], ["word"], ["word"], ["word"], ["wor"]],
                [None, None, None, True, True],
            ),
            (
                ["Trie", "insert", "search", "search", "starts_with", "starts_with"],
                [[], ["Word"], ["word"], ["Word"], ["W"], ["w"]],
                [None, None, False, True, True, False],
            ),
            (
                ["Trie", "insert", "insert", "search", "search", "search", "starts_with", "starts_with"],
                [[], ["a"], ["b"], ["a"], ["b"], ["c"], ["a"], ["b"]],
                [None, None, None, True, True, False, True, True],
            ),
            (
                [
                    "Trie",
                    "insert",
                    "insert",
                    "insert",
                    "insert",
                    "search",
                    "search",
                    "search",
                    "search",
                    "search",
                    "starts_with",
                    "starts_with",
                ],
                [
                    [],
                    ["car"],
                    ["card"],
                    ["care"],
                    ["careful"],
                    ["car"],
                    ["card"],
                    ["care"],
                    ["careful"],
                    ["ca"],
                    ["car"],
                    ["care"],
                ],
                [None, None, None, None, None, True, True, True, True, False, True, True],
            ),
        ],
    )
    @logged_test
    def test_trie_operations(
        self, operations: list[str], inputs: list[list[str]], expected: list[bool | None]
    ):
        trie: Trie | None = None
        results: list[bool | None] = []
        for i, op in enumerate(operations):
            if op == "Trie":
                trie = Trie()
                results.append(None)
            elif op == "insert" and trie is not None:
                trie.insert(inputs[i][0])
                results.append(None)
            elif op == "search" and trie is not None:
                results.append(trie.search(inputs[i][0]))
            elif op == "starts_with" and trie is not None:
                results.append(trie.starts_with(inputs[i][0]))
        assert results == expected
