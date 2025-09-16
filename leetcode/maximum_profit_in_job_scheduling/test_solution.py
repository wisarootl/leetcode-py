import pytest

from leetcode_py import logged_test

from .helpers import assert_job_scheduling, run_job_scheduling
from .solution import Solution


class TestMaximumProfitInJobScheduling:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "start_time, end_time, profit, expected",
        [
            ([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70], 120),
            ([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60], 150),
            ([1, 1, 1], [2, 3, 4], [5, 6, 4], 6),
            ([1, 2], [2, 3], [100, 200], 300),
            (
                [6, 15, 7, 11, 1, 3, 16, 2],
                [19, 18, 19, 16, 10, 8, 19, 8],
                [2, 9, 1, 19, 5, 7, 3, 19],
                41,
            ),
            ([1], [2], [100], 100),
            ([1, 2, 3], [2, 3, 4], [1, 1, 1], 3),
            ([1, 3, 6, 7, 8, 12], [4, 5, 10, 11, 12, 16], [20, 20, 100, 70, 60, 120], 240),
            ([1, 4, 6], [3, 5, 7], [50, 10, 40], 100),
            ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [10, 20, 30, 40, 50], 50),
            ([5, 4, 3, 2, 1], [6, 5, 4, 3, 2], [1, 2, 3, 4, 5], 15),
            ([1, 1000000000], [2, 1000000001], [1, 10000], 10001),
        ],
    )
    def test_job_scheduling(
        self, start_time: list[int], end_time: list[int], profit: list[int], expected: int
    ):
        result = run_job_scheduling(Solution, start_time, end_time, profit)
        assert_job_scheduling(result, expected)
