# Daily Temperatures

**Difficulty:** Medium
**Topics:** Array, Stack, Monotonic Stack
**Tags:** grind

**LeetCode:** [Problem 739](https://leetcode.com/problems/daily-temperatures/description/)

## Problem Description

Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `ith` day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

## Examples

### Example 1:

```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

**Explanation:**

- For input `[73,74,75,71,69,72,76,73]`, the output should be `[1,1,4,2,1,1,0,0]`.
- For example, the first temperature is 73. The next warmer temperature is 74, which is 1 day later, so we put 1.
- The second temperature is 74. The next warmer temperature is 75, which is 1 day later, so we put 1.
- The third temperature is 75. The next warmer temperature is 76, which is 4 days later, so we put 4.

### Example 2:

```
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```

### Example 3:

```
Input: temperatures = [30,60,90]
Output: [1,1,0]
```

## Constraints

- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`
