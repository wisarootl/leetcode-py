# Odd Even Linked List

**Difficulty:** Medium
**Topics:** Linked List
**Tags:** grind

**LeetCode:** [Problem 328](https://leetcode.com/problems/odd-even-linked-list/description/)

## Problem Description

Given the `head` of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return _the reordered list_.

The **first** node is considered **odd**, and the **second** node is **even**, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in `O(1)` extra space complexity and `O(n)` time complexity.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/03/10/oddeven-linked-list.jpg)

```
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2021/03/10/oddeven2-linked-list.jpg)

```
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
```

## Constraints

- The number of nodes in the linked list is in the range [0, 10^4]
- -10^6 <= Node.val <= 10^6
