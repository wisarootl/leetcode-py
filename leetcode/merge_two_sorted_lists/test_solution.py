import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_merge_two_lists, run_merge_two_lists
from .solution import Solution


class TestMergeTwoSortedLists:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "list1_vals, list2_vals, expected_vals",
        [
            ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
            ([], [], []),
            ([], [0], [0]),
            ([1], [2], [1, 2]),
            ([2], [1], [1, 2]),
            ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
            ([1, 1, 1], [2, 2, 2], [1, 1, 1, 2, 2, 2]),
            ([0], [], [0]),
            ([1, 2, 3], [], [1, 2, 3]),
            ([5], [1, 2, 3, 4], [1, 2, 3, 4, 5]),
            ([-1, 0, 1], [-2, 2, 3], [-2, -1, 0, 1, 2, 3]),
            ([1, 5, 9], [2, 6, 8], [1, 2, 5, 6, 8, 9]),
            ([10, 20, 30], [15, 25, 35], [10, 15, 20, 25, 30, 35]),
            ([1, 1], [1, 1], [1, 1, 1, 1]),
        ],
    )
    def test_merge_two_lists(
        self, list1_vals: list[int], list2_vals: list[int], expected_vals: list[int]
    ):
        result = run_merge_two_lists(Solution, list1_vals, list2_vals)
        assert_merge_two_lists(result, expected_vals)
