def run_add_binary(solution_class: type, a: str, b: str):
    implementation = solution_class()
    return implementation.add_binary(a, b)


def assert_add_binary(result: str, expected: str) -> bool:
    assert result == expected
    return True
