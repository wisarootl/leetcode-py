import pytest

from leetcode_py.test_utils import logged_test

from .solution import LRUCache


class TestLRUCache:
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
                [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
                [None, None, None, 1, None, -1, None, -1, 3, 4],
            )
        ],
    )
    @logged_test
    def test_lru_cache(self, operations: list[str], inputs: list[list[int]], expected: list[int | None]):
        cache: LRUCache | None = None
        results: list[int | None] = []
        for i, op in enumerate(operations):
            if op == "LRUCache":
                cache = LRUCache(inputs[i][0])
                results.append(None)
            elif op == "get" and cache is not None:
                results.append(cache.get(inputs[i][0]))
            elif op == "put" and cache is not None:
                cache.put(inputs[i][0], inputs[i][1])
                results.append(None)
        assert results == expected
