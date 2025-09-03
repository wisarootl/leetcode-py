from leetcode_py import ListNode


class Solution:
    # Time: O(n)
    # Space: O(1)
    def has_cycle(self, head: ListNode[int] | None) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            assert slow is not None
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return True

        return False
