from leetcode_py import ListNode


class Solution:

    # Time: O(max(m, n))
    # Space: O(max(m, n))
    def add_two_numbers(
        self, l1: ListNode[int] | None, l2: ListNode[int] | None
    ) -> ListNode[int] | None:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
