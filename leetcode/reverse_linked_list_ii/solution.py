from leetcode_py import ListNode


class Solution:
    # Time: O(n)
    # Space: O(1)
    def reverse_between(self, head: ListNode[int] | None, left: int, right: int) -> ListNode[int] | None:
        if not head or left == right:
            return head

        dummy = ListNode[int](0)
        dummy.next = head
        prev = dummy

        # Move to position before left
        for _ in range(left - 1):
            assert prev.next
            prev = prev.next

        # Reverse from left to right using iterative approach
        # Example: [1,2,3,4,5] left=2, right=4 -> [1,4,3,2,5]
        #
        # Initial: prev curr
        #           ↓    ↓
        #           1 -> 2 -> 3 -> 4 -> 5
        #
        assert prev.next
        curr = prev.next  # First node to be reversed (will become last after reversal)

        # Reverse by moving nodes one by one to the front of the section
        for _ in range(right - left):
            assert curr.next
            next_node = curr.next  # Node to move to front
            #
            #        prev curr next_node
            #          ↓    ↓    ↓
            #          1 -> 2 -> 3 -> 4 -> 5
            #
            curr.next = next_node.next
            #         1 -> 2 -----> 4 -> 5
            #                   3 ↗
            #
            next_node.next = prev.next
            #         1 -> 2 -----> 4 -> 5
            #           3 ↗
            #
            prev.next = next_node
            #         1 -> 3 -> 2 -> 4 -> 5
            #         prev  ↑   curr
            #              next_node

        return dummy.next
