# Number of Connected Components in an Undirected Graph

**Difficulty:** Medium
**Topics:** Depth-First Search, Breadth-First Search, Union Find, Graph
**Tags:** blind-75

**LeetCode:** [Problem 323](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/)

## Problem Description

Given `n` nodes labeled from `0` to `n - 1` and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

## Examples

### Example 1:

```
Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4

Output: 2
```

### Example 2:

```
Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output: 1
```

## Constraints

- 1 <= n <= 2000
- 1 <= edges.length <= 5000
- edges[i].length == 2
- 0 <= ai, bi < n
- ai != bi
- There are no repeated edges.

**Note:** You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
