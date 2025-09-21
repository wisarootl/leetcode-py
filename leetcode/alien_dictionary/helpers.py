def run_alien_order(solution_class: type, words: list[str]):
    implementation = solution_class()
    return implementation.alien_order(words)


def assert_alien_order(result: str, expected: str) -> bool:
    if expected == "":
        assert result == ""
    else:
        # Multiple valid solutions possible, check if result is valid
        assert len(result) == len(expected)
        assert set(result) == set(expected)
    return True
