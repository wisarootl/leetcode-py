# Merge Intervals

**Difficulty:** Medium
**Topics:** Array, Sorting
**Tags:** grind-75

**LeetCode:** [Problem 56](https://leetcode.com/problems/merge-intervals/description/)

## Problem Description

Given an array of `intervals` where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

## Examples

### Example 1:

```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
```

**Explanation:** Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

### Example 2:

```
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
```

**Explanation:** Intervals [1,4] and [4,5] are considered overlapping.

### Example 3:

```
Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
```

**Explanation:** Intervals [1,4] and [4,7] are considered overlapping.

## Constraints

- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= starti <= endi <= 10^4`
