from leetcode_py import ListNode


class Solution:

    # Time: O(n)
    # Space: O(1)
    def middle_node(self, head: ListNode[int] | None) -> ListNode[int] | None:
        slow = fast = head
        while fast and fast.next:
            assert slow is not None
            slow = slow.next
            fast = fast.next.next
        return slow
