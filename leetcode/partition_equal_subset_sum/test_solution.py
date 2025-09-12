import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_can_partition, run_can_partition
from .solution import Solution, SolutionBitset


class TestPartitionEqualSubsetSum:

    @logged_test
    @pytest.mark.parametrize("solution_class", [Solution, SolutionBitset])
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 5, 11, 5], True),
            ([1, 2, 3, 5], False),
            ([1, 1], True),
            ([1], False),
            ([2, 2, 1, 1], True),
            ([100], False),
            ([1, 2, 5], False),
        ],
    )
    def test_can_partition(self, nums: list[int], expected: bool, solution_class: type):
        result = run_can_partition(solution_class, nums)
        assert_can_partition(result, expected)
