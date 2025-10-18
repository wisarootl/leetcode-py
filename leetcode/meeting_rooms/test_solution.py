import pytest

from leetcode_py import logged_test

from .helpers import assert_can_attend_meetings, run_can_attend_meetings
from .solution import Solution


class TestMeetingRooms:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "intervals, expected",
        [
            ([[0, 30], [5, 10], [15, 20]], False),
            ([[7, 10], [2, 4]], True),
            ([], True),
            ([[1, 5]], True),
            ([[1, 5], [8, 9]], True),
            ([[1, 5], [2, 6]], False),
            ([[0, 1], [1, 2]], True),
            ([[0, 2], [1, 3]], False),
            ([[1, 3], [2, 4], [3, 5]], False),
            ([[1, 2], [3, 4], [5, 6]], True),
            ([[0, 5], [5, 10], [10, 15]], True),
            ([[1, 4], [2, 3]], False),
            ([[1, 10], [2, 3], [4, 5]], False),
            ([[9, 10], [4, 9], [4, 17]], False),
            ([[2, 7]], True),
            ([[1, 13], [13, 15]], True),
            ([[6, 7], [2, 4], [8, 12]], True),
            ([[13, 15], [1, 13]], True),
        ],
    )
    def test_can_attend_meetings(self, intervals: list[list[int]], expected: bool):
        result = run_can_attend_meetings(Solution, intervals)
        assert_can_attend_meetings(result, expected)
