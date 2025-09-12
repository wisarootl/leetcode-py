def run_is_valid(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.is_valid(s)


def assert_is_valid(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
