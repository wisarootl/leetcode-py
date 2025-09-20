from leetcode_py import ListNode


class Solution:

    # Time: O(n) - single pass through list
    # Space: O(1) - only pointer manipulation
    def odd_even_list(self, head: ListNode[int] | None) -> ListNode[int] | None:
        """
        Group odd-indexed nodes followed by even-indexed nodes.

        Example: [1,2,3,4,5] → [1,3,5,2,4]

        Step 1: Separate odd and even chains
        odd:  1 → 3 → 5 → None
        even: 2 → 4 → None

        Step 2: Connect odd tail to even head
        1 → 3 → 5 → 2 → 4 → None
        """
        if not head or not head.next:
            return head

        odd = head
        even: ListNode[int] | None = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head
