from leetcode_py import ListNode


class Solution:

    # Time: O(m + n)
    # Space: O(1)
    def merge_two_lists(
        self, list1: ListNode[int] | None, list2: ListNode[int] | None
    ) -> ListNode[int] | None:
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 or list2
        return dummy.next
