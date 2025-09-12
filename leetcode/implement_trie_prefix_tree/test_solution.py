import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_trie_operations, run_trie_operations
from .solution import Trie


class TestImplementTriePrefixTree:

    @logged_test
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
        ],
    )
    def test_trie_operations(
        self, operations: list[str], inputs: list[list[str]], expected: list[bool | None]
    ):
        result, _ = run_trie_operations(Trie, operations, inputs)
        assert_trie_operations(result, expected)
