from leetcode_py import ListNode


class Solution:

    # Time: O(n) where n is the number of nodes
    # Space: O(1) - only using constant extra space
    def reorder_list(self, head: ListNode[int] | None) -> None:
        """
        Reorder a linked list in-place: L0→L1→...→Ln-1→Ln becomes L0→Ln→L1→Ln-1→L2→Ln-2→...

        Algorithm:
        1. Find the middle of the list using slow/fast pointers
        2. Reverse the second half of the list
        3. Merge the first half and reversed second half alternately

        This approach uses O(1) space and O(n) time.
        """
        if not head or not head.next:
            return

        # Step 1: Find the middle of the list
        slow = fast = head
        while fast.next and fast.next.next:
            assert slow.next
            slow = slow.next
            fast = fast.next.next

        # Split the list into two halves
        second_half = slow.next
        slow.next = None  # Break the connection

        # Step 2: Reverse the second half
        prev = None
        current = second_half
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        second_half = prev

        # Step 3: Merge the two halves alternately
        first_half = head
        while second_half:
            # Store next nodes
            first_next = first_half.next
            second_next = second_half.next

            # Reorder: first -> second -> first_next
            first_half.next = second_half
            second_half.next = first_next

            # Move to next nodes
            first_half = first_next  # type: ignore[assignment]
            second_half = second_next
