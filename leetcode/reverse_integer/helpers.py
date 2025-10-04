def run_reverse(solution_class: type, x: int):
    implementation = solution_class()
    return implementation.reverse(x)


def assert_reverse(result: int, expected: int) -> bool:
    assert result == expected
    return True
