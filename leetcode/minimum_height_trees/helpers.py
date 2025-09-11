def run_find_min_height_trees(solution_class: type, n: int, edges: list[list[int]]):
    implementation = solution_class()
    return implementation.find_min_height_trees(n, edges)


def assert_find_min_height_trees(result: list[int], expected: list[int]) -> bool:
    assert sorted(result) == sorted(expected)
    return True
