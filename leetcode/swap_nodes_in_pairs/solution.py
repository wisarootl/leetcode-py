from leetcode_py import ListNode


class Solution:

    # Time: O(n) - traverse each node once
    # Space: O(1) - constant extra space
    def swap_pairs(self, head: ListNode[int] | None) -> ListNode[int] | None:
        # Create dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Process pairs while they exist
        while prev.next and prev.next.next:
            # Identify nodes to swap
            first = prev.next
            second = prev.next.next

            # Perform swap: prev -> second -> first -> ...
            prev.next = second
            first.next = second.next
            second.next = first

            # Move prev to end of swapped pair
            prev = first

        return dummy.next
