# Reverse Bits

**Difficulty:** Easy
**Topics:** Divide and Conquer, Bit Manipulation
**Tags:** blind-75

**LeetCode:** [Problem 190](https://leetcode.com/problems/reverse-bits/description/)

## Problem Description

Reverse bits of a given 32 bits signed integer.

## Examples

### Example 1:

```
Input: n = 43261596
Output: 964176192
Explanation:

| Integer    | Binary                              |
|------------|-------------------------------------|
| 43261596   | 00000010100101000001111010011100    |
| 964176192  | 00111001011110000010100101000000    |
```

### Example 2:

```
Input: n = 2147483644
Output: 1073741822
Explanation:

| Integer     | Binary                              |
|-------------|-------------------------------------|
| 2147483644  | 01111111111111111111111111111100    |
| 1073741822  | 00111111111111111111111111111110    |
```

## Constraints

- 0 <= n <= 2^31 - 2
- n is even.

**Follow up:** If this function is called many times, how would you optimize it?
