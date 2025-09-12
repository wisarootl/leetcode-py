def run_calculate(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.calculate(s)


def assert_calculate(result: int, expected: int) -> bool:
    assert result == expected
    return True
