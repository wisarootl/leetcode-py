# Group Anagrams

**Difficulty:** Medium
**Topics:** Array, Hash Table, String, Sorting
**Tags:** grind

**LeetCode:** [Problem 49](https://leetcode.com/problems/group-anagrams/description/)

## Problem Description

Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.

An **anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Examples

### Example 1:

```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
- There is no string in strs that can be rearranged to form "bat".
- The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
- The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
```

### Example 2:

```
Input: strs = [""]
Output: [[""]]
```

### Example 3:

```
Input: strs = ["a"]
Output: [["a"]]
```

## Constraints

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.
