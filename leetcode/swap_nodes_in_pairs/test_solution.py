import pytest

from leetcode_py import logged_test

from .helpers import assert_swap_pairs, run_swap_pairs
from .solution import Solution


class TestSwapNodesInPairs:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "head_list, expected",
        [
            ([1, 2, 3, 4], [2, 1, 4, 3]),
            ([], []),
            ([1], [1]),
            ([1, 2, 3], [2, 1, 3]),
            ([1, 2], [2, 1]),
            ([1, 2, 3, 4, 5], [2, 1, 4, 3, 5]),
            ([1, 2, 3, 4, 5, 6], [2, 1, 4, 3, 6, 5]),
            ([5, 4, 3, 2, 1], [4, 5, 2, 3, 1]),
            ([10, 20], [20, 10]),
            ([100], [100]),
            ([0, 1, 2, 3], [1, 0, 3, 2]),
            ([7, 8, 9, 10, 11, 12, 13], [8, 7, 10, 9, 12, 11, 13]),
        ],
    )
    def test_swap_pairs(self, head_list: list[int], expected: list[int]):
        result = run_swap_pairs(Solution, head_list)
        assert_swap_pairs(result, expected)
