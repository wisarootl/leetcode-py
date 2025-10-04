from leetcode_py import ListNode


class Solution:

    # Time: O(n)
    # Space: O(1)
    def reverse_k_group(self, head: ListNode[int] | None, k: int) -> ListNode[int] | None:
        if not head or k == 1:
            return head

        # Check if we have at least k nodes
        curr: ListNode[int] | None = head
        count = 0
        while curr and count < k:
            curr = curr.next
            count += 1

        if count == k:
            # Reverse the first k nodes
            prev = self.reverse_k_group(curr, k)  # Recursively reverse remaining groups
            curr = head

            while count > 0 and curr is not None:
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
                count -= 1

            head = prev

        return head
