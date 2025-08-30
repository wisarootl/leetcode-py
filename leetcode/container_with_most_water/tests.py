import pytest
from loguru import logger

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestContainerWithMostWater:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "height, expected",
        [
            ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
            ([1, 1], 1),
            ([1, 2, 1], 2),
            ([2, 3, 4, 5, 18, 17, 6], 17),
            ([1, 2, 4, 3], 4),
        ],
    )
    @logged_test
    def test_max_area(self, height: list[int], expected: int):
        logger.info(f"Testing with height={height}")
        result = self.solution.max_area(height)
        logger.success(f"Got result: {result}")
        assert result == expected
