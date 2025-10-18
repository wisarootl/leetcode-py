class Solution:

    # Time: O(n + e)
    # Space: O(n + e)
    def valid_tree(self, n: int, edges: list[list[int]]) -> bool:
        # Edge case: empty graph is a valid tree
        if n == 0:
            return True

        # A valid tree must have exactly n-1 edges
        if len(edges) != n - 1:
            return False

        # Build adjacency list
        graph: list[list[int]] = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # DFS to check connectivity
        visited = set()

        def dfs(node: int) -> None:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        # Start DFS from node 0
        dfs(0)

        # Check if all nodes are visited (connected)
        return len(visited) == n
