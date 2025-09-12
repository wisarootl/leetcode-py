def run_median_finder(solution_class: type, operations: list[str], inputs: list[list[int]]):
    mf = None
    results: list[float | None] = []
    for i, op in enumerate(operations):
        if op == "MedianFinder":
            mf = solution_class()
            results.append(None)
        elif op == "addNum" and mf is not None:
            mf.add_num(inputs[i][0])
            results.append(None)
        elif op == "findMedian" and mf is not None:
            results.append(mf.find_median())
    return results, mf


def assert_median_finder(result: list[float | None], expected: list[float | None]) -> bool:
    assert result == expected
    return True
