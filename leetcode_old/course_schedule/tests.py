import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestCourseSchedule:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "num_courses, prerequisites, expected",
        [
            # Basic cases
            (2, [[1, 0]], True),
            (2, [[1, 0], [0, 1]], False),
            (1, [], True),
            (3, [[1, 0], [2, 1]], True),
            (4, [[1, 0], [2, 1], [3, 2], [1, 3]], False),
            # Edge cases
            (0, [], True),
            (5, [], True),
            (3, [[0, 1], [0, 2], [1, 2]], True),
            # Self-loop
            (2, [[0, 0]], False),
            (3, [[1, 1]], False),
            # Complex valid cases
            (6, [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3], [5, 4]], True),
            (4, [[0, 1], [0, 2], [1, 3], [2, 3]], True),
            # Complex cycles
            (3, [[0, 1], [1, 2], [2, 0]], False),
            (5, [[1, 0], [2, 1], [3, 2], [4, 3], [0, 4]], False),
            (4, [[1, 0], [2, 0], [0, 3], [3, 1]], False),
        ],
    )
    @logged_test
    def test_can_finish(self, num_courses: int, prerequisites: list[list[int]], expected: bool):
        result = self.solution.can_finish(num_courses, prerequisites)
        assert result == expected
