# Balanced Binary Tree

**Difficulty:** Easy
**Topics:** Tree, Depth-First Search, Binary Tree
**Tags:** grind-75

**LeetCode:** [Problem 110](https://leetcode.com/problems/balanced-binary-tree/description/)

## Problem Description

Given a binary tree, determine if it is **height-balanced**.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg)

```
Input: root = [3,9,20,null,null,15,7]
Output: true
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg)

```
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
```

### Example 3:

```
Input: root = []
Output: true
```

## Constraints

- The number of nodes in the tree is in the range `[0, 5000]`.
- `-10^4 <= Node.val <= 10^4`
