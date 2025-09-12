def run_trap(solution_class: type, height: list[int]):
    implementation = solution_class()
    return implementation.trap(height)


def assert_trap(result: int, expected: int) -> bool:
    assert result == expected
    return True
