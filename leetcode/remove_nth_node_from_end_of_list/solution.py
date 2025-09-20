from leetcode_py import ListNode


class Solution:

    # Time: O(L) where L is the length of the list
    # Space: O(1)
    def remove_nth_from_end(self, head: ListNode[int] | None, n: int) -> ListNode[int] | None:
        dummy = ListNode(0)
        dummy.next = head
        fast: ListNode[int] | None = dummy
        slow: ListNode[int] | None = dummy

        # Move fast pointer n+1 steps ahead
        for _ in range(n + 1):
            assert fast
            fast = fast.next

        # Move both pointers until fast reaches end
        while fast:
            fast = fast.next
            assert slow
            slow = slow.next

        # Remove the nth node
        assert slow and slow.next
        slow.next = slow.next.next
        return dummy.next
