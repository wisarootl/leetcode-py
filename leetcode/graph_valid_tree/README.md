# Graph Valid Tree

**Difficulty:** Medium
**Topics:** Depth-First Search, Breadth-First Search, Union Find, Graph
**Tags:** blind-75

**LeetCode:** [Problem 261](https://leetcode.com/problems/graph-valid-tree/description/)

## Problem Description

Given `n` nodes labeled from `0` to `n-1` and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

## Examples

### Example 1:

```
Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
```

### Example 2:

```
Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
```

## Constraints

- 0 <= n <= 2000
- 0 <= edges.length <= 5000
- edges[i].length == 2
- 0 <= ai, bi < n
- ai != bi
- There are no self-loops or repeated edges.

**Note:** you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.
