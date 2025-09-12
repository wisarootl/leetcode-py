def run_job_scheduling(
    solution_class: type, start_time: list[int], end_time: list[int], profit: list[int]
):
    implementation = solution_class()
    return implementation.job_scheduling(start_time, end_time, profit)


def assert_job_scheduling(result: int, expected: int) -> bool:
    assert result == expected
    return True
