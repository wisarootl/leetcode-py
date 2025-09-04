import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestMaximumProfitInJobScheduling:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "start_time, end_time, profit, expected",
        [
            # Original examples
            ([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70], 120),
            ([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60], 150),
            ([1, 1, 1], [2, 3, 4], [5, 6, 4], 6),
            # Edge cases
            ([1], [2], [100], 100),  # Single job
            ([1, 2], [2, 3], [50, 100], 150),  # Adjacent jobs
            ([1, 3], [2, 4], [50, 100], 150),  # Overlapping jobs - can take both
            ([1, 3, 5], [2, 4, 6], [10, 20, 30], 60),  # No overlaps - take all
            ([1, 1, 1], [2, 2, 2], [10, 20, 30], 30),  # Same time slots - take best
            ([1, 2, 3, 4], [2, 3, 4, 5], [1, 1, 1, 1], 4),  # All same profit - take all
            ([1, 5, 10], [3, 7, 12], [100, 1, 1], 102),  # High profit + non-overlapping
        ],
    )
    @logged_test
    def test_job_scheduling(
        self, start_time: list[int], end_time: list[int], profit: list[int], expected: int
    ):
        result = self.solution.job_scheduling(start_time, end_time, profit)
        assert result == expected
