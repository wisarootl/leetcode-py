import pytest

from leetcode_py import logged_test

from .helpers import assert_merge_k_lists, run_merge_k_lists
from .solution import Solution


class TestMergeKSortedLists:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "lists_data, expected_data",
        [
            ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
            ([], []),
            ([[]], []),
            ([[1]], [1]),
            ([[1, 2], [3, 4]], [1, 2, 3, 4]),
            ([[5], [1, 3], [2, 4, 6]], [1, 2, 3, 4, 5, 6]),
            ([[-1, 0, 1], [-2, 2]], [-2, -1, 0, 1, 2]),
            ([[1, 1, 1], [2, 2, 2]], [1, 1, 1, 2, 2, 2]),
            ([[], [1], []], [1]),
            ([[0, 0, 0], [1, 1, 1]], [0, 0, 0, 1, 1, 1]),
            ([[10], [5], [1]], [1, 5, 10]),
            ([[1, 2, 3, 4, 5]], [1, 2, 3, 4, 5]),
            ([[-10, -5], [-8, -3], [-6, -1]], [-10, -8, -6, -5, -3, -1]),
            ([[100]], [100]),
            ([[1, 3, 5], [2, 4, 6], [7, 8, 9]], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ],
    )
    def test_merge_k_lists(self, lists_data: list[list[int]], expected_data: list[int]):
        result = run_merge_k_lists(Solution, lists_data)
        assert_merge_k_lists(result, expected_data)
