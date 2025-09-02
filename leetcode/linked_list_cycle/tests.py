import pytest

from leetcode_py import ListNode
from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestLinkedListCycle:
    def setup_method(self):
        self.solution = Solution()

    def create_cycle_list(self, values: list[int], pos: int):
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
            ([3, 2, 0, -4], 1, True),
            ([1, 2], 0, True),
            ([1], -1, False),
            ([], -1, False),
            ([1, 2, 3], -1, False),
            ([1, 2, 3, 4, 5], 0, True),
            ([1, 2, 3, 4, 5], 2, True),
            ([1, 2, 3, 4, 5], 4, True),
            ([1], 0, True),
            ([1, 2], 1, True),
            ([1, 2, 3, 4, 5, 6, 7, 8], 3, True),
            ([1, 2, 3, 4, 5, 6, 7, 8], -1, False),
            ([1, 2], -1, False),
            ([5, 10], 0, True),
            ([5, 10], 1, True),
            ([0], -1, False),
            ([-1, -2, -3], 1, True),
            ([100, 200, 300], 0, True),
        ],
    )
    @logged_test
    def test_has_cycle(self, values: list[int], pos: int, expected: bool):
        head = self.create_cycle_list(values, pos)
        result = self.solution.has_cycle(head)
        assert result == expected
