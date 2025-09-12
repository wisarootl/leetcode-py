def run_can_construct(solution_class: type, ransom_note: str, magazine: str):
    implementation = solution_class()
    return implementation.can_construct(ransom_note, magazine)


def assert_can_construct(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
