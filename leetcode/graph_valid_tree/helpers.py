def run_valid_tree(solution_class: type, n: int, edges: list[list[int]]):
    implementation = solution_class()
    return implementation.valid_tree(n, edges)


def assert_valid_tree(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
