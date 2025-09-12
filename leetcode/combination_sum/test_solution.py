import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_combination_sum, run_combination_sum
from .solution import Solution


class TestCombinationSum:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "candidates, target, expected",
        [
            ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
            ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
            ([2], 1, []),
            ([2, 3], 1, []),
            ([3, 5], 3, [[3]]),
            ([2, 4], 6, [[2, 2, 2], [2, 4]]),
            ([5], 5, [[5]]),
            ([2, 3, 4], 6, [[2, 2, 2], [2, 4], [3, 3]]),
            ([4, 2, 8], 8, [[2, 2, 2, 2], [2, 2, 4], [4, 4], [8]]),
            ([3, 4, 5], 9, [[3, 3, 3], [4, 5]]),
            ([6, 3, 2], 6, [[2, 2, 2], [3, 3], [6]]),
            ([2, 7], 9, [[2, 7]]),
        ],
    )
    def test_combination_sum(self, candidates: list[int], target: int, expected: list[list[int]]):
        result = run_combination_sum(Solution, candidates, target)
        assert_combination_sum(result, expected)
