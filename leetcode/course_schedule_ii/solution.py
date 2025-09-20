from collections import deque


class Solution:

    # TOPOLOGICAL SORT using Kahn's Algorithm (BFS-based)
    # Keywords: DAG, in-degree, adjacency list, cycle detection, dependency resolution
    # Time: O(V + E) where V = num_courses, E = len(prerequisites)
    # Space: O(V + E) for adjacency list and in_degree array
    def find_order(self, num_courses: int, prerequisites: list[list[int]]) -> list[int]:
        """
        Topological Sort: Linear ordering of vertices in DAG where all edges go from left to right.

        Algorithm: Kahn's Algorithm (BFS approach)
        1. Build adjacency list and calculate in-degrees
        2. Start with nodes having 0 in-degree (no dependencies)
        3. Remove nodes and update in-degrees of neighbors
        4. If all nodes processed → valid ordering, else cycle exists

        Keywords: Directed Acyclic Graph (DAG), in-degree, out-degree, dependency graph,
                 prerequisite resolution, cycle detection, BFS traversal
        """
        # Build adjacency list and in-degree count
        graph: list[list[int]] = [[] for _ in range(num_courses)]
        in_degree = [0] * num_courses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        # Start with courses having no prerequisites
        queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
        result = []

        while queue:
            course = queue.popleft()
            result.append(course)

            # Remove this course and update in-degrees
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Check if all courses can be taken (no cycle)
        return result if len(result) == num_courses else []
