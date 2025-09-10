from typing import Any


def run_lru_cache(
    solution_class: type, operations: list[str], inputs: list[list[int]]
) -> tuple[list[int | None], Any]:
    cache = None
    results: list[int | None] = []
    for i, op in enumerate(operations):
        if op == "LRUCache":
            cache = solution_class(inputs[i][0])
            results.append(None)
        elif op == "get" and cache is not None:
            results.append(cache.get(inputs[i][0]))
        elif op == "put" and cache is not None:
            cache.put(inputs[i][0], inputs[i][1])
            results.append(None)
    return results, cache


def assert_lru_cache(result: list[int | None], expected: list[int | None]) -> bool:
    assert result == expected
    return True
