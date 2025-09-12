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
        ],
    )
    def test_merge_two_lists(
        self, list1_vals: list[int], list2_vals: list[int], expected_vals: list[int]
    ):
        result = run_merge_two_lists(Solution, list1_vals, list2_vals)
        assert_merge_two_lists(result, expected_vals)
