import pytest

from leetcode_py import logged_test

from .helpers import assert_find_order, run_find_order
from .solution import Solution


class TestCourseScheduleII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "num_courses, prerequisites, expected",
        [
            (2, [[1, 0]], [0, 1]),
            (4, [[1, 0], [2, 0], [3, 1], [3, 2]], [0, 2, 1, 3]),
            (1, [], [0]),
            (3, [[1, 0], [2, 1]], [0, 1, 2]),
            (2, [[1, 0], [0, 1]], []),
            (3, [[0, 1], [0, 2], [1, 2]], [2, 1, 0]),
            (4, [[1, 0], [2, 1], [3, 2]], [0, 1, 2, 3]),
            (3, [[1, 0], [1, 2], [0, 1]], []),
            (5, [[1, 4], [2, 4], [3, 1], [3, 2]], [4, 1, 2, 3, 0]),
            (6, [[3, 0], [3, 1], [4, 1], [4, 2], [5, 3], [5, 4]], [0, 1, 2, 3, 4, 5]),
            (0, [], []),
            (3, [], [0, 1, 2]),
            (4, [[0, 1], [1, 2], [2, 3], [3, 0]], []),
            (5, [[0, 1], [1, 2], [2, 3], [3, 4]], [0, 1, 2, 3, 4]),
            (3, [[0, 1], [1, 0], [2, 1]], []),
            (4, [[1, 0], [2, 0], [3, 0]], [0, 1, 2, 3]),
            (5, [[1, 0], [2, 1], [3, 2], [4, 3], [0, 4]], []),
            (
                7,
                [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2]],
                [0, 1, 2, 3, 4, 5, 6],
            ),
        ],
    )
    def test_find_order(self, num_courses: int, prerequisites: list[list[int]], expected: list[int]):
        result = run_find_order(Solution, num_courses, prerequisites)
        assert_find_order(result, expected)
