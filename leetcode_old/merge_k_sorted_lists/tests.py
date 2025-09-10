import pytest

from leetcode_py import ListNode
from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestMergeKSortedLists:
    def setup_method(self):
        self.solution = Solution()

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
            ([[]], []),
            ([[], [1], []], [1]),
            ([[0]], [0]),
            ([[-10, -5, -1], [-8, -3], [-7, -2, 0]], [-10, -8, -7, -5, -3, -2, -1, 0]),
            ([[1, 2, 3, 4, 5]], [1, 2, 3, 4, 5]),
            ([[10], [9], [8], [7]], [7, 8, 9, 10]),
            ([[1, 100], [2, 99], [3, 98]], [1, 2, 3, 98, 99, 100]),
            ([[], [], []], []),
            ([[0, 0, 0], [0, 0]], [0, 0, 0, 0, 0]),
            ([[1, 3, 5, 7], [2, 4, 6, 8]], [1, 2, 3, 4, 5, 6, 7, 8]),
            (
                [[100, 200, 300], [50, 150, 250], [75, 125, 175]],
                [50, 75, 100, 125, 150, 175, 200, 250, 300],
            ),
        ],
    )
    @logged_test
    def test_merge_k_lists(self, lists_data: list[list[int]], expected_data: list[int]):
        lists = [ListNode.from_list(lst) for lst in lists_data]
        result = self.solution.merge_k_lists(lists)
        expected = ListNode.from_list(expected_data)
        assert result == expected
