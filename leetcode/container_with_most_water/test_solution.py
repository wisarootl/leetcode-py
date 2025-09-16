import pytest

from leetcode_py import logged_test

from .helpers import assert_max_area, run_max_area
from .solution import Solution


class TestContainerWithMostWater:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "height, expected",
        [
            ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
            ([1, 1], 1),
            ([1, 2, 1], 2),
            ([2, 1], 1),
            ([1, 2, 4, 3], 4),
            ([1, 3, 2, 5, 25, 24, 5], 24),
            ([2, 3, 4, 5, 18, 17, 6], 17),
            ([1, 2, 3, 4, 5], 6),
            ([5, 4, 3, 2, 1], 6),
            ([0, 2], 0),
            ([3, 9, 3, 4, 7, 2, 12, 6], 45),
            ([1, 0, 0, 0, 0, 0, 0, 2, 2], 8),
        ],
    )
    def test_max_area(self, height: list[int], expected: int):
        result = run_max_area(Solution, height)
        assert_max_area(result, expected)
