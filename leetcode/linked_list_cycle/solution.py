from leetcode_py import ListNode


class Solution:
    # Time: O(n)
    # Space: O(1)
    def has_cycle(self, head: ListNode[int] | None) -> bool:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next  # type: ignore[union-attr]
            fast = fast.next.next
            if slow is fast:
                return True  # Cycle detected

        return False  # No cycle
