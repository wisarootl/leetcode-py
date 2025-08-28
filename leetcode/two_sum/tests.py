import pytest
from loguru import logger

from .solution import Solution


class TestTwoSum:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, target, expected",
        [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
        ],
    )
    def test_two_sum(self, nums, target, expected):
        result = self.solution.two_sum(nums, target)
        assert result == expected
        logger.success("test")
