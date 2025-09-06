import pytest

from leetcode_py import ListNode
from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestMergeTwoSortedLists:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "list1_vals, list2_vals, expected_vals",
        [
            ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
            ([], [], []),
            ([], [0], [0]),
            ([0], [], [0]),
            ([1], [2], [1, 2]),
            ([2], [1], [1, 2]),
            ([1, 1, 1], [2, 2, 2], [1, 1, 1, 2, 2, 2]),
            ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
            ([-10, -5, 0], [-8, -3, 1], [-10, -8, -5, -3, 0, 1]),
            ([5], [1, 2, 3, 4], [1, 2, 3, 4, 5]),
            ([1, 2, 3, 4], [5], [1, 2, 3, 4, 5]),
        ],
    )
    @logged_test
    def test_merge_two_lists(
        self, list1_vals: list[int], list2_vals: list[int], expected_vals: list[int]
    ):
        list1 = ListNode.from_list(list1_vals)
        list2 = ListNode.from_list(list2_vals)
        expected = ListNode.from_list(expected_vals)
        result = self.solution.merge_two_lists(list1, list2)
        assert result == expected
