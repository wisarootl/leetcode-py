from leetcode_py import ListNode


class Solution:
    # Time: O(n)
    # Space: O(1)
    def reverse_list(self, head: ListNode[int] | None) -> ListNode[int] | None:
        if not head:
            return None

        # Iterative approach using three pointers
        # Example: [1,2,3] -> [3,2,1]
        #
        # Initial: prev curr
        #          None  ↓
        #                1 -> 2 -> 3 -> None
        #
        prev: ListNode[int] | None = None
        curr: ListNode[int] | None = head

        while curr:
            # Store next node before breaking the link
            next_node = curr.next
            #
            #         prev curr next_node
            #         None  ↓    ↓
            #               1 -> 2 -> 3 -> None
            #

            # Reverse the current link
            curr.next = prev
            #         None <- 1    2 -> 3 -> None
            #         prev   curr  next_node
            #

            # Move pointers forward
            prev = curr
            curr = next_node
            #                1 <- 2    3 -> None
            #                    prev curr
            #

        #                1 <- 2 <- 3   None
        #                         prev curr
        # prev now points to new head of reversed list
        return prev
