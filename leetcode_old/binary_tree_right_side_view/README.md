# Binary Tree Right Side View

**Difficulty:** Medium
**Topics:** Tree, Depth-First Search, Breadth-First Search, Binary Tree
**Tags:** grind-75

**LeetCode:** [Problem 199](https://leetcode.com/problems/binary-tree-right-side-view/description/)

## Problem Description

Given the `root` of a binary tree, imagine yourself standing on the **right side** of it, return _the values of the nodes you can see ordered from top to bottom_.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2024/11/24/tmpd5jn43fs-1.png)

```
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2024/11/24/tmpkpe40xeh-1.png)

```
Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]
```

### Example 3:

```
Input: root = [1,null,3]
Output: [1,3]
```

### Example 4:

```
Input: root = []
Output: []
```

## Constraints

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`
