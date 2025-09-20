# Find K Closest Elements

**Difficulty:** Medium
**Topics:** Array, Two Pointers, Binary Search, Sliding Window, Sorting, Heap (Priority Queue)
**Tags:** grind

**LeetCode:** [Problem 658](https://leetcode.com/problems/find-k-closest-elements/description/)

## Problem Description

Given a **sorted** integer array `arr`, two integers `k` and `x`, return the `k` closest integers to `x` in the array. The result should also be sorted in ascending order.

An integer `a` is closer to `x` than an integer `b` if:

- `|a - x| < |b - x|`, or
- `|a - x| == |b - x|` and `a < b`

## Examples

### Example 1:

```
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
```

### Example 2:

```
Input: arr = [1,1,2,3,4,5], k = 4, x = -1
Output: [1,1,2,3]
```

## Constraints

- `1 <= k <= arr.length`
- `1 <= arr.length <= 10^4`
- `arr` is sorted in **ascending** order.
- `-10^4 <= arr[i], x <= 10^4`
