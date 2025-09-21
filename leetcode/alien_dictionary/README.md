# Alien Dictionary

**Difficulty:** Hard
**Topics:** Array, String, Depth-First Search, Breadth-First Search, Graph, Topological Sort
**Tags:** grind-75, grind

**LeetCode:** [Problem 269](https://leetcode.com/problems/alien-dictionary/description/)

## Problem Description

There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings `words` from the alien language's dictionary, where the strings in `words` are **sorted lexicographically** by the rules of this new language.

Return _a string of the unique letters in the new alien language sorted in **lexicographically increasing order** by the new language's rules. If there is no solution, return_ `""`\*. If there are multiple solutions, return **any of them\***.

## Examples

### Example 1:

```
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
```

### Example 2:

```
Input: words = ["z","x"]
Output: "zx"
```

### Example 3:

```
Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".
```

## Constraints

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- `words[i]` consists of only lowercase English letters.
