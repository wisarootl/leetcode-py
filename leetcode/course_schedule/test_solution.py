import pytest

from leetcode_py import logged_test

from .helpers import assert_can_finish, run_can_finish
from .solution import Solution


class TestCourseSchedule:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "num_courses, prerequisites, expected",
        [
            (2, [[1, 0]], True),
            (2, [[1, 0], [0, 1]], False),
            (1, [], True),
            (3, [[1, 0], [2, 1]], True),
            (4, [[1, 0], [2, 1], [3, 2], [1, 3]], False),
            (3, [[0, 1], [0, 2], [1, 2]], True),
            (4, [[0, 1], [1, 2], [2, 3], [3, 1]], False),
            (6, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]], True),
            (3, [[1, 0], [2, 0]], True),
            (5, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]], False),
            (4, [[1, 0], [2, 0], [3, 1], [3, 2]], True),
            (5, [[1, 0], [2, 1], [3, 2], [4, 3], [0, 4]], False),
        ],
    )
    def test_can_finish(self, num_courses: int, prerequisites: list[list[int]], expected: bool):
        result = run_can_finish(Solution, num_courses, prerequisites)
        assert_can_finish(result, expected)
