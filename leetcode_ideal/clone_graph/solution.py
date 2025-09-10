from collections import deque

from leetcode_py import GraphNode


class Solution:
    # Time: O(V + E)
    # Space: O(V)
    def clone_graph(self, node: GraphNode | None) -> GraphNode | None:
        if node is None:
            return None

        def dfs(node: GraphNode, visited: dict[int, GraphNode]):
            if node.val in visited:
                return visited[node.val]

            clone = GraphNode(node.val)
            visited[node.val] = clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor, visited))

            return clone

        return dfs(node, visited={})


class SolutionDFS:
    # DFS Iterative
    # Time: O(V + E)
    # Space: O(V)
    def clone_graph(self, node: GraphNode | None) -> GraphNode | None:
        if node is None:
            return None

        stack = [node]
        visited = {node.val: GraphNode(node.val)}

        while stack:
            current = stack.pop()
            clone = visited[current.val]

            for neighbor in current.neighbors:
                if neighbor.val not in visited:
                    visited[neighbor.val] = GraphNode(neighbor.val)
                    stack.append(neighbor)
                clone.neighbors.append(visited[neighbor.val])

        return visited[node.val]


class SolutionBFS:
    # BFS
    # Time: O(V + E)
    # Space: O(V)
    def clone_graph(self, node: GraphNode | None) -> GraphNode | None:
        if node is None:
            return None

        queue = deque([node])
        visited = {node.val: GraphNode(node.val)}

        while queue:
            current = queue.popleft()
            clone = visited[current.val]

            for neighbor in current.neighbors:
                if neighbor.val not in visited:
                    visited[neighbor.val] = GraphNode(neighbor.val)
                    queue.append(neighbor)
                clone.neighbors.append(visited[neighbor.val])

        return visited[node.val]
