def run_daily_temperatures(solution_class: type, temperatures: list[int]):
    implementation = solution_class()
    return implementation.daily_temperatures(temperatures)


def assert_daily_temperatures(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
