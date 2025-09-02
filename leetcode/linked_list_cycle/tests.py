import pytest

from leetcode_py import ListNode
from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestLinkedListCycle:
    def setup_method(self):
        self.solution = Solution()

    def create_cycle_list(self, values: list[int], pos: int) -> ListNode[int] | None:
        if not values:
            return None

        nodes = []
        head = ListNode(values[0])
        nodes.append(head)
        current = head

        for i in range(1, len(values)):
            current.next = ListNode(values[i])
            current = current.next
            nodes.append(current)

        if pos != -1 and pos < len(nodes):
            current.next = nodes[pos]

        return head

    @pytest.mark.parametrize(
        "values, pos, expected",
        [
            # Basic cases
            ([3, 2, 0, -4], 1, True),  # Cycle to middle
            ([1, 2], 0, True),  # Cycle to head
            ([1], -1, False),  # Single node, no cycle
            ([], -1, False),  # Empty list
            ([1, 2, 3], -1, False),  # Linear list
            # Various cycle positions
            ([1, 2, 3, 4, 5], 0, True),  # Cycle to head
            ([1, 2, 3, 4, 5], 2, True),  # Cycle to middle
            ([1, 2, 3, 4, 5], 4, True),  # Cycle to tail
            # Self-loop cases
            ([1], 0, True),  # Single node self-loop
            ([1, 2], 1, True),  # Last node self-loop
            # Longer lists
            ([1, 2, 3, 4, 5, 6, 7, 8], 3, True),  # Long list with cycle
            ([1, 2, 3, 4, 5, 6, 7, 8], -1, False),  # Long list without cycle
            # Two-node cases
            ([1, 2], -1, False),  # Two nodes, no cycle
            ([5, 10], 0, True),  # Two nodes, cycle to first
            ([5, 10], 1, True),  # Two nodes, self-loop on second
            # Edge case values
            ([0], -1, False),  # Zero value
            ([-1, -2, -3], 1, True),  # Negative values
            ([100, 200, 300], 0, True),  # Large values
        ],
    )
    @logged_test
    def test_has_cycle(self, values: list[int], pos: int, expected: bool):
        head = self.create_cycle_list(values, pos)
        result = self.solution.has_cycle(head)
        assert result == expected
