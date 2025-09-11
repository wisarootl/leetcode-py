import pytest

from leetcode_py.test_utils import logged_test

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
        ],
    )
    def test_merge_k_lists(self, lists_data: list[list[int]], expected_data: list[int]):
        result = run_merge_k_lists(Solution, lists_data)
        assert_merge_k_lists(result, expected_data)
