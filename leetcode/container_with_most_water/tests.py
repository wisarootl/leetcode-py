import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestContainerWithMostWater:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "height, expected",
        [
            # Original cases
            ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
            ([1, 1], 1),
            ([1, 2, 1], 2),
            # Edge cases
            ([2, 1], 1),
            ([1, 2], 1),
            ([0, 2], 0),
            ([2, 0], 0),
            # Increasing heights
            ([1, 2, 3, 4, 5], 6),
            # Decreasing heights
            ([5, 4, 3, 2, 1], 6),
            # Same heights
            ([3, 3, 3, 3], 9),
            # Large differences
            ([1, 1000, 1], 2),
            ([1000, 1, 1000], 2000),
            # Multiple peaks
            ([2, 3, 4, 5, 18, 17, 6], 17),
        ],
    )
    @logged_test
    def test_max_area(self, height: list[int], expected: int):
        result = self.solution.max_area(height)
        assert result == expected
