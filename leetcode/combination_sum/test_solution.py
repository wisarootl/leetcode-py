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
        ],
    )
    def test_combination_sum(self, candidates: list[int], target: int, expected: list[list[int]]):
        result = run_combination_sum(Solution, candidates, target)
        assert_combination_sum(result, expected)
