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
        ],
    )
    def test_lru_cache(
        self,
        operations: list[str],
        inputs: list[list[int]],
        expected: list[int | None],
        solution_class: type,
    ):
        result, _ = run_lru_cache(solution_class, operations, inputs)
        assert_lru_cache(result, expected)
