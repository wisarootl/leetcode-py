import pytest

from leetcode_py import ListNode
from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestMiddleOfTheLinkedList:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "head_list, expected_list",
        [
            ([1, 2, 3, 4, 5], [3, 4, 5]),  # odd length
            ([1, 2, 3, 4, 5, 6], [4, 5, 6]),  # even length
            ([1], [1]),  # single node
            ([1, 2], [2]),  # two nodes
            ([1, 2, 3], [2, 3]),  # three nodes
            ([1, 2, 3, 4], [3, 4]),  # four nodes
            ([10, 20, 30, 40, 50, 60, 70], [40, 50, 60, 70]),  # larger odd
            ([5, 15, 25, 35], [25, 35]),  # larger even
        ],
    )
    @logged_test
    def test_middle_node(self, head_list: list[int], expected_list: list[int]):
        head = ListNode.from_list(head_list)
        expected = ListNode.from_list(expected_list)
        result = self.solution.middle_node(head)
        assert result == expected
