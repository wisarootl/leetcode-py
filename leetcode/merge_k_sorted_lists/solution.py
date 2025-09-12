from leetcode_py import ListNode


class Solution:

    # Time: O(n log k) where n is total nodes, k is number of lists
    # Space: O(log k) for recursion stack
    def merge_k_lists(self, lists: list[ListNode[int] | None]) -> ListNode[int] | None:
        if not lists:
            return None
        return self._divide_conquer(lists, 0, len(lists) - 1)

    def _divide_conquer(
        self, lists: list[ListNode[int] | None], left: int, right: int
    ) -> ListNode[int] | None:
        if left == right:
            return lists[left]

        mid = (left + right) // 2
        l1 = self._divide_conquer(lists, left, mid)
        l2 = self._divide_conquer(lists, mid + 1, right)
        return self._merge_two(l1, l2)

    def _merge_two(self, l1: ListNode[int] | None, l2: ListNode[int] | None) -> ListNode[int] | None:
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 or l2
        return dummy.next
