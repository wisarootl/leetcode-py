# 54. Spiral Matrix

**Difficulty:** Medium
**Topics:** Array, Matrix, Simulation
**Tags:** grind-75
**LeetCode:** [Problem 54](https://leetcode.com/problems/spiral-matrix/description/)

## Problem Description

Given an m x n matrix, return all elements of the matrix in spiral order.

## Examples

### Example 1:

```
1 → 2 → 3
        ↓
4 → 5   6
↑       ↓
7 ← 8 ← 9

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

### Example 2:

```
1 → 2 → 3 → 4
            ↓
5 → 6 → 7   8
↑           ↓
9 ← 10← 11← 12

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

## Constraints

- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 10
- -100 <= matrix[i][j] <= 100
