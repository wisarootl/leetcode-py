def run_climb_stairs(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.climb_stairs(n)


def assert_climb_stairs(result: int, expected: int) -> bool:
    assert result == expected
    return True
