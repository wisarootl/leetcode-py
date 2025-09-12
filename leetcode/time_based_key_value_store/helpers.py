def run_time_map_operations(solution_class: type, operations: list[str], inputs: list[list]):
    time_map = None
    results: list[str | None] = []
    for i, op in enumerate(operations):
        if op == "TimeMap":
            time_map = solution_class()
            results.append(None)
        elif op == "set" and time_map is not None:
            time_map.set(*inputs[i])
            results.append(None)
        elif op == "get" and time_map is not None:
            results.append(time_map.get(*inputs[i]))
    return results, time_map


def assert_time_map_operations(result: list, expected: list) -> bool:
    results, _ = result
    assert results == expected
    return True
