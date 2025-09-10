import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_lru_cache, run_lru_cache


class TestLRUCache:
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
        operations: list[str],
        inputs: list[list[int]],
        expected: list[int | None],
    ):
        from .solution import LRUCache

        result, _ = run_lru_cache(LRUCache, operations, inputs)
        assert_lru_cache(result, expected)

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
    def test_lru_cache_with_doubly_list(
        self,
        operations: list[str],
        inputs: list[list[int]],
        expected: list[int | None],
    ):
        from .solution import LRUCacheWithDoublyList

        result, _ = run_lru_cache(LRUCacheWithDoublyList, operations, inputs)
        assert_lru_cache(result, expected)
