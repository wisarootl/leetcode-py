# Decode Ways

**Difficulty:** Medium
**Topics:** String, Dynamic Programming
**Tags:** blind-75

**LeetCode:** [Problem 91](https://leetcode.com/problems/decode-ways/description/)

## Problem Description

You have intercepted a secret message encoded as a string of numbers. The message is decoded via the mapping: `"1" -> 'A', "2" -> 'B', ..., "26" -> 'Z'`. Given a string `s` containing only digits, return the number of ways to decode it. Return `0` if it cannot be decoded.

## Examples

### Example 1:

```
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
```

### Example 2:

```
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
```

### Example 3:

```
Input: s = "06"
Output: 0
Explanation: leading zero makes it invalid.
```

## Constraints

- 1 <= s.length <= 100
- s contains only digits and may contain leading zero(s)
