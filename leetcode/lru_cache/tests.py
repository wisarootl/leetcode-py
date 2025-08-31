import pytest
from loguru import logger

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
            ),
        ],
    )
    @logged_test
    def test_lru_cache(self, operations: list[str], inputs: list[list[int]], expected: list[int | None]):
        logger.info(f"Testing LRU Cache with operations: {operations}")
        logger.info(f"Inputs: {inputs}")
        logger.info(f"Expected: {expected}")

        cache: LRUCache | None = None
        result: list[int | None] = []
        for i, op in enumerate(operations):
            if op == "LRUCache":
                cache = LRUCache(inputs[i][0])
                result.append(None)
            elif op == "get" and cache is not None:
                result.append(cache.get(inputs[i][0]))
            elif op == "put" and cache is not None:
                cache.put(inputs[i][0], inputs[i][1])
                result.append(None)

        logger.info(f"Result: {result}")
        assert result == expected
