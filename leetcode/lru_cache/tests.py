import pytest

from leetcode_py.test_utils import logged_test

from .solution import LRUCache, LRUCacheWithDoublyList


class TestLRUCache:
    @pytest.mark.parametrize("lru_class", [LRUCache, LRUCacheWithDoublyList])
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
    @logged_test
    def test_lru_cache(
        self,
        lru_class: type[LRUCache | LRUCacheWithDoublyList],
        operations: list[str],
        inputs: list[list[int]],
        expected: list[int | None],
    ):
        cache = None
        results: list[int | None] = []
        for i, op in enumerate(operations):
            if op == "LRUCache":
                cache = lru_class(inputs[i][0])
                results.append(None)
            elif op == "get" and cache is not None:
                results.append(cache.get(inputs[i][0]))
            elif op == "put" and cache is not None:
                cache.put(inputs[i][0], inputs[i][1])
                results.append(None)
        assert results == expected
