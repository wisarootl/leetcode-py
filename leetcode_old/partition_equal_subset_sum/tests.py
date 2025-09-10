import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution, SolutionBitset


class TestPartitionEqualSubsetSum:
    @pytest.mark.parametrize("solution_class", [Solution, SolutionBitset])
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 5, 11, 5], True),
            ([1, 2, 3, 5], False),
            ([1, 1], True),
            ([1], False),
            ([2, 2, 1, 1], True),
            # Edge cases
            ([100], False),
            ([1, 1, 1, 1], True),
            ([2, 3, 5], True),
            # Large numbers
            ([50, 50], True),
            ([99, 1], False),
            ([100, 100], True),
            # Multiple solutions
            ([1, 2, 3, 4], True),
            ([3, 3, 3, 4, 5], True),
            # No solution cases
            ([1, 3, 5], False),
            ([7, 11, 13], False),
            # Larger arrays
            ([1, 1, 1, 1, 1, 1, 1, 1], True),
            ([2, 4, 6, 8, 10], False),
            ([5, 10, 15, 20], True),
            # Very large numbers (testing Python's arbitrary precision)
            ([1000, 1000], True),
            ([5000, 5000], True),
            ([9999, 1], False),
            ([10000, 10000], True),
            # Extremely large numbers (beyond 64-bit)
            ([2**16, 2**16], True),  # 65536 each, target = 65536
            ([2**20, 2**20], True),  # 1048576 each, target = 1048576
            ([2**20 + 1, 2**20 - 1], False),  # sum = 2^21, target = 2^20, cannot partition
        ],
    )
    @logged_test
    def test_can_partition(
        self,
        nums: list[int],
        expected: bool,
        solution_class: type[Solution | SolutionBitset],
    ):
        solution = solution_class()
        result = solution.can_partition(nums)
        assert result == expected
