import pytest

from leetcode_py import logged_test

from .helpers import assert_min_meeting_rooms, run_min_meeting_rooms
from .solution import Solution


class TestMeetingRoomsII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "intervals, expected",
        [
            ([[0, 30], [5, 10], [15, 20]], 2),
            ([[7, 10], [2, 4]], 1),
            ([[1, 5]], 1),
            ([[1, 5], [8, 9]], 1),
            ([[1, 5], [2, 6]], 2),
            ([[0, 1], [1, 2]], 1),
            ([[0, 2], [1, 3]], 2),
            ([[1, 3], [2, 4], [3, 5]], 2),
            ([[1, 2], [3, 4], [5, 6]], 1),
            ([[0, 5], [5, 10], [10, 15]], 1),
            ([[1, 4], [2, 3]], 2),
            ([[1, 10], [2, 3], [4, 5]], 2),
            ([[9, 10], [4, 9], [4, 17]], 2),
            ([[2, 7]], 1),
            ([[1, 13], [13, 15]], 1),
            ([[6, 7], [2, 4], [8, 12]], 1),
            ([[13, 15], [1, 13]], 1),
            ([[0, 30], [5, 10], [15, 20], [25, 35]], 2),
            ([[1, 2], [2, 3], [3, 4], [4, 5]], 1),
            ([[1, 3], [2, 4], [4, 6], [5, 7]], 2),
        ],
    )
    def test_min_meeting_rooms(self, intervals: list[list[int]], expected: int):
        result = run_min_meeting_rooms(Solution, intervals)
        assert_min_meeting_rooms(result, expected)
