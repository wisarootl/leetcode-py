import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_lru_cache, run_lru_cache
from .solution import LRUCache, LRUCacheWithDoublyList


class TestLRUCache:

    @logged_test
    @pytest.mark.parametrize("solution_class", [LRUCache, LRUCacheWithDoublyList])
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
                [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
                [None, None, None, 1, None, -1, None, -1, 3, 4],
            ),
            (
                ["LRUCache", "get", "put", "get", "put", "put", "get", "get"],
                [[2], [2], [2, 6], [1], [1, 5], [1, 2], [1], [2]],
                [None, -1, None, -1, None, None, 2, 6],
            ),
            (
                ["LRUCache", "put", "get", "put", "get", "get"],
                [[1], [2, 1], [2], [3, 2], [2], [3]],
                [None, None, 1, None, -1, 2],
            ),
            (["LRUCache", "get"], [[1], [1]], [None, -1]),
            (["LRUCache", "put", "get"], [[1], [1, 100], [1]], [None, None, 100]),
            (
                ["LRUCache", "put", "put", "get", "get"],
                [[2], [1, 1], [2, 2], [1], [2]],
                [None, None, None, 1, 2],
            ),
            (
                ["LRUCache", "put", "put", "put", "get", "get", "get"],
                [[2], [1, 1], [2, 2], [3, 3], [1], [2], [3]],
                [None, None, None, None, -1, 2, 3],
            ),
            (
                ["LRUCache", "put", "get", "put", "get", "put", "get"],
                [[3], [1, 1], [1], [2, 2], [2], [3, 3], [3]],
                [None, None, 1, None, 2, None, 3],
            ),
            (
                ["LRUCache", "put", "put", "put", "put", "get", "get"],
                [[3], [1, 1], [2, 2], [3, 3], [4, 4], [4], [3]],
                [None, None, None, None, None, 4, 3],
            ),
            (
                ["LRUCache", "put", "put", "get", "put", "get", "get"],
                [[2], [2, 1], [1, 1], [2], [4, 1], [1], [2]],
                [None, None, None, 1, None, -1, 1],
            ),
            (
                ["LRUCache", "put", "put", "get", "put", "put", "get"],
                [[2], [2, 1], [2, 2], [2], [1, 1], [4, 1], [2]],
                [None, None, None, 2, None, None, -1],
            ),
            (
                ["LRUCache", "put", "put", "put", "get", "put", "get", "get", "get", "get"],
                [[3], [1, 1], [2, 2], [3, 3], [2], [4, 4], [1], [3], [4], [2]],
                [None, None, None, None, 2, None, -1, 3, 4, 2],
            ),
        ],
    )
    def test_lru_cache(
        self,
        solution_class: type,
        operations: list[str],
        inputs: list[list[int]],
        expected: list[int | None],
    ):
        result, _ = run_lru_cache(solution_class, operations, inputs)
        assert_lru_cache(result, expected)
