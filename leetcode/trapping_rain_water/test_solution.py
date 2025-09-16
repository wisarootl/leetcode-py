import pytest

from leetcode_py import logged_test

from .helpers import assert_trap, run_trap
from .solution import Solution


class TestTrappingRainWater:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "height, expected",
        [
            ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
            ([4, 2, 0, 3, 2, 5], 9),
            ([3, 0, 2, 0, 4], 7),
            ([0], 0),
            ([1], 0),
            ([1, 2], 0),
            ([2, 1], 0),
            ([3, 2, 0, 4], 4),
            ([5, 4, 1, 2], 1),
            ([2, 0, 2], 2),
            ([1, 0, 1], 1),
            ([0, 2, 0], 0),
            ([1, 2, 1], 0),
            ([5, 2, 7, 2, 6, 1, 5, 3, 2, 1], 11),
            ([0, 0, 0, 0], 0),
        ],
    )
    def test_trap(self, height: list[int], expected: int):
        result = run_trap(Solution, height)
        assert_trap(result, expected)
