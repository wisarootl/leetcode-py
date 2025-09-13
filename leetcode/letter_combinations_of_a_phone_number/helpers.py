def run_letter_combinations(solution_class: type, digits: str):
    implementation = solution_class()
    return implementation.letter_combinations(digits)


def assert_letter_combinations(result: list[str], expected: list[str]) -> bool:
    result.sort()
    expected.sort()
    assert result == expected
    return True
