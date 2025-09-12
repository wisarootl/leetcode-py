def run_my_atoi(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.my_atoi(s)


def assert_my_atoi(result: int, expected: int) -> bool:
    assert result == expected
    return True
