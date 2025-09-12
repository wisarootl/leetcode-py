import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_can_partition, run_can_partition
from .solution import Solution, SolutionBitset


class TestPartitionEqualSubsetSum:
    def setup_method(self):
        self.solution = Solution()

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
            ([1, 3, 5, 7], True),
            ([2, 2, 3, 5], False),
            ([1, 2, 3, 4, 5, 6, 7], True),
            ([3, 3, 3, 4, 5], True),
            ([1, 1, 1, 1], True),
            ([23, 13, 11, 7, 6, 5, 5], True),
            ([1, 5, 3], False),
            ([4, 4, 4, 4, 4, 4], True),
        ],
    )
    def test_can_partition(self, solution_class: type, nums: list[int], expected: bool):
        result = run_can_partition(solution_class, nums)
        assert_can_partition(result, expected)
