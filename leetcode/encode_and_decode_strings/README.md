# Encode and Decode Strings

**Difficulty:** Medium
**Topics:** Array, String, Design
**Tags:** blind-75

**LeetCode:** [Problem 271](https://leetcode.com/problems/encode-and-decode-strings/description/)

## Problem Description

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

## Examples

### Example 1:

```
Input: dummy_input = ["Hello","World"]
Output: "Hello,World"
Explanation: Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2
Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
```

## Constraints

- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] contains any possible characters out of 256 valid ASCII characters.

**Note:**

- The string may contain any possible characters out of 256 valid ASCII characters. Your algorithm should be generalized enough to work on any possible characters.
- Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
- Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode algorithm.
