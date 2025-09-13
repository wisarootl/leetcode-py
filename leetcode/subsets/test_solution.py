import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_subsets, run_subsets
from .solution import Solution


class TestSubsets:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
            ([0], [[], [0]]),
            ([1], [[], [1]]),
            ([1, 2], [[], [1], [2], [1, 2]]),
            ([4, 1, 0], [[], [4], [4, 1], [4, 1, 0], [4, 0], [1], [1, 0], [0]]),
            ([-1, 0, 1], [[], [-1], [-1, 0], [-1, 0, 1], [-1, 1], [0], [0, 1], [1]]),
            ([5], [[], [5]]),
            ([2, 1, 3], [[], [2], [2, 1], [2, 1, 3], [2, 3], [1], [1, 3], [3]]),
            ([10], [[], [10]]),
            ([-10, 10], [[], [-10], [-10, 10], [10]]),
            (
                [1, 2, 3, 4],
                [
                    [],
                    [1],
                    [1, 2],
                    [1, 2, 3],
                    [1, 2, 3, 4],
                    [1, 2, 4],
                    [1, 3],
                    [1, 3, 4],
                    [1, 4],
                    [2],
                    [2, 3],
                    [2, 3, 4],
                    [2, 4],
                    [3],
                    [3, 4],
                    [4],
                ],
            ),
            ([5, 2], [[], [5], [5, 2], [2]]),
        ],
    )
    def test_subsets(self, nums: list[int], expected: list[list[int]]):
        result = run_subsets(Solution, nums)
        assert_subsets(result, expected)
