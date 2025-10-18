class Solution:

    # Time: O(n + e)
    # Space: O(n + e)
    def count_components(self, n: int, edges: list[list[int]]) -> int:
        # Build adjacency list
        graph: list[list[int]] = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        components = 0

        def dfs(node: int) -> None:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        # Count connected components
        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1

        return components
