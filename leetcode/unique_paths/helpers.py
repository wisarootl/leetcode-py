def run_unique_paths(solution_class: type, m: int, n: int):
    implementation = solution_class()
    return implementation.unique_paths(m, n)


def assert_unique_paths(result: int, expected: int) -> bool:
    assert result == expected
    return True
