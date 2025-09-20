# Remove Nth Node From End of List

**Difficulty:** Medium
**Topics:** Linked List, Two Pointers
**Tags:** grind

**LeetCode:** [Problem 19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/)

## Problem Description

Given the `head` of a linked list, remove the `n<sup>th</sup>` node from the end of the list and return its head.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)

```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

### Example 2:

```
Input: head = [1], n = 1
Output: []
```

### Example 3:

```
Input: head = [1,2], n = 1
Output: [1]
```

## Constraints

- The number of nodes in the list is `sz`.
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

**Follow up:** Could you do this in one pass?
