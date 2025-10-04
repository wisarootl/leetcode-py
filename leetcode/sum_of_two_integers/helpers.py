def run_get_sum(solution_class: type, a: int, b: int):
    implementation = solution_class()
    return implementation.getSum(a, b)


def assert_get_sum(result: int, expected: int) -> bool:
    assert result == expected
    return True
