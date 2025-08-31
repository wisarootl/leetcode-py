import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestContainerWithMostWater:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "height, expected", [([1, 8, 6, 2, 5, 4, 8, 3, 7], 49), ([1, 1], 1), ([1, 2, 1], 2)]
    )
    @logged_test
    def test_max_area(self, height: list[int], expected: int):
        result = self.solution.max_area(height)
        assert result == expected
