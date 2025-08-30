from leetcode_py.list_node import ListNode


class Solution:
    # Time: O(n)
    # Space: O(1)
    def reverse_between(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Move to position before left
        for _ in range(left - 1):
            assert prev.next
            prev = prev.next

        # Reverse from left to right
        assert prev.next
        curr = prev.next
        for _ in range(right - left):
            assert curr.next
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next
