def run_least_interval(solution_class: type, tasks: list[str], n: int):
    implementation = solution_class()
    return implementation.least_interval(tasks, n)


def assert_least_interval(result: int, expected: int) -> bool:
    assert result == expected
    return True
