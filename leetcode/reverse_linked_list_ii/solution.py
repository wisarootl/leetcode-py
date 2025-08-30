from leetcode_py.list_node import ListNode


class Solution:
    # Time: O(?)
    # Space: O(?)
    def reverse_between(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Move to position before left
        for _ in range(left - 1):
            assert prev.next is not None
            prev = prev.next

        # Reverse the sublist
        assert prev.next is not None
        curr = prev.next
        for _ in range(right - left):
            assert curr.next is not None
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next
