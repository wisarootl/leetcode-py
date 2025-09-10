import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestThreeSum:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
            ([0, 1, 1], []),
            ([0, 0, 0], [[0, 0, 0]]),
            ([-1, 0, 1], [[-1, 0, 1]]),
            ([1, 2, -2, -1], []),
            ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
            # Edge cases
            ([1, 2, 3], []),  # All positive
            ([-3, -2, -1], []),  # All negative
            ([0, 0, 0, 0], [[0, 0, 0]]),  # Multiple zeros
            ([-1, -1, 2, 2], [[-1, -1, 2]]),  # Duplicate pairs
            ([3, 0, -2, -1, 1, 2], [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]),  # Multiple solutions
            (
                [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6],
                [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]],
            ),  # Many duplicates
            ([1, -1, 0], [[-1, 0, 1]]),  # Simple case
            ([2, -1, -1], [[-1, -1, 2]]),  # Solution with duplicates
        ],
    )
    @logged_test
    def test_three_sum(self, nums: list[int], expected: list[list[int]]):
        result = self.solution.three_sum(nums)
        # Sort both result and expected for comparison since order doesn't matter
        result_sorted = [sorted(triplet) for triplet in result]
        expected_sorted = [sorted(triplet) for triplet in expected]
        result_sorted.sort()
        expected_sorted.sort()
        assert result_sorted == expected_sorted
