# 01 Matrix

**Difficulty:** Medium
**Topics:** Array, Dynamic Programming, Breadth-First Search, Matrix
**Tags:** grind-75

**LeetCode:** [Problem 542](https://leetcode.com/problems/zero-one-matrix/description/)

## Problem Description

Given an `m x n` binary matrix `mat`, return the distance of the nearest `0` for each cell.

The distance between two cells sharing a common edge is `1`.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/04/24/01-1-grid.jpg)

```
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2021/04/24/01-2-grid.jpg)

```
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
```

## Constraints

- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 10^4`
- `1 <= m * n <= 10^4`
- `mat[i][j]` is either `0` or `1`
- There is at least one `0` in `mat`

**Note:** This question is the same as 1765: [Map of Highest Peak](https://leetcode.com/problems/map-of-highest-peak/)
