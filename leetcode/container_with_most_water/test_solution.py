import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_max_area, run_max_area
from .solution import Solution


class TestContainerWithMostWater:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "height, expected", [([1, 8, 6, 2, 5, 4, 8, 3, 7], 49), ([1, 1], 1), ([1, 2, 1], 2)]
    )
    def test_max_area(self, height: list[int], expected: int):
        result = run_max_area(Solution, height)
        assert_max_area(result, expected)
