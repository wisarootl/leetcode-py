from collections import defaultdict, deque


class Solution:
    # Time: O(V)
    # Space: O(V)
    def find_min_height_trees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]

        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        leaves = deque([i for i in range(n) if len(graph[i]) == 1])

        remaining = n
        while remaining > 2:
            size = len(leaves)
            remaining -= size
            for _ in range(size):
                leaf = leaves.popleft()
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    leaves.append(neighbor)

        return list(leaves)
