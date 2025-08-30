92. Reverse Linked List II
    Solved
    Medium
    Topics
    premium lock icon
    Companies
    Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

Follow up: Could you do it in one pass?

Seen this question in a real interview before?
1/5
Yes
No
Accepted
1,153,915/2.3M
Acceptance Rate
50.0%
Topics
Linked List

# Definition for singly-linked list.

# class ListNode:

# def **init**(self, val=0, next=None):

# self.val = val

# self.next = next

class Solution:
def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
