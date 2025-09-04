import pytest

from leetcode_py import ListNode
from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestReverseLinkedList:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "head_list, expected_list",
        [
            ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),  # Basic case
            ([1, 2], [2, 1]),  # Two nodes
            ([1], [1]),  # Single node
            ([], []),  # Empty list
            ([1, 2, 3], [3, 2, 1]),  # Odd length
            ([1, 2, 3, 4], [4, 3, 2, 1]),  # Even length
            ([-1, -2, -3], [-3, -2, -1]),  # Negative values
            ([0], [0]),  # Zero value
            ([5000, -5000], [-5000, 5000]),  # Boundary values
            ([1, 1, 1], [1, 1, 1]),  # Duplicate values
        ],
    )
    @logged_test
    def test_reverse_list(self, head_list: list[int], expected_list: list[int]):
        # Convert input list to linked list structure
        # e.g., [1,2,3] -> 1->2->3->None
        head = ListNode.from_list(head_list)

        # Convert expected result list to linked list for comparison
        # e.g., [3,2,1] -> 3->2->1->None
        expected = ListNode.from_list(expected_list)

        # Call the reverse_list method to reverse the linked list
        # This should transform 1->2->3->None into 3->2->1->None
        result = self.solution.reverse_list(head)

        # Verify that the reversed linked list matches expected output
        # ListNode supports direct equality comparison
        assert result == expected
