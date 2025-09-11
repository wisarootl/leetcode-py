def run_first_bad_version(solution_class: type, n: int, bad: int):
    solution = solution_class(bad)
    return solution.first_bad_version(n)


def assert_first_bad_version(result: int, expected: int) -> bool:
    assert result == expected
    return True
