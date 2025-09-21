from __future__ import annotations

from pprint import pformat

import graphviz

from ._utils import handle_graphviz_fallback


class GraphNode:
    """
    Graph node for undirected graph problems.

    Each node contains a value and a list of neighbors.
    """

    def __init__(self, val: int = 0, neighbors: list[GraphNode] | None = None) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def _dfs_traverse(self, visit_fn) -> set[int]:
        """Generic DFS traversal with custom visit function."""
        visited = set()

        def dfs(node: GraphNode) -> None:
            if node.val in visited:
                return
            visited.add(node.val)
            visit_fn(node)
            for neighbor in node.neighbors:
                dfs(neighbor)

        dfs(self)
        return visited

    def _get_adjacency_dict(self) -> dict[int, list[int]]:
        """Get adjacency dictionary representation."""
        adj_dict = {}

        def visit(node: GraphNode) -> None:
            adj_dict[node.val] = sorted([n.val for n in node.neighbors])

        self._dfs_traverse(visit)
        return dict(sorted(adj_dict.items()))

    def __eq__(self, other: object) -> bool:
        """Compare two graph nodes by adjacency list structure."""
        if not isinstance(other, GraphNode):
            return False
        return self.to_adjacency_list(self) == self.to_adjacency_list(other)

    def is_clone(self, other: GraphNode | None) -> bool:
        """
        Check if other is a proper clone (same structure, different objects).
        """
        if other is None:
            return False

        # First check if structures are equal
        if self != other:
            return False

        # Then check all nodes are different objects
        visited: set[int] = set()

        def dfs_check_identity(node1: GraphNode, node2: GraphNode) -> bool:
            if node1.val in visited:
                return True

            visited.add(node1.val)

            # Same object = not a clone
            if node1 is node2:
                return False

            # Check neighbors (sorted for consistency)
            neighbors1 = sorted(node1.neighbors, key=lambda x: x.val)
            neighbors2 = sorted(node2.neighbors, key=lambda x: x.val)

            for n1, n2 in zip(neighbors1, neighbors2):
                if not dfs_check_identity(n1, n2):
                    return False
            return True

        return dfs_check_identity(self, other)

    def __str__(self) -> str:
        """Human-readable string representation using pprint."""
        return pformat(self._get_adjacency_dict(), width=40)

    def _repr_html_(self) -> str:
        """HTML representation for Jupyter notebooks using Graphviz."""
        try:
            dot = graphviz.Graph(engine="neato")
            dot.attr("node", shape="circle", style="filled", fillcolor="lightblue")
            dot.attr("edge", color="gray")

            edges = set()

            def visit(node: GraphNode) -> None:
                dot.node(str(node.val), str(node.val))
                for neighbor in node.neighbors:
                    edge = (min(node.val, neighbor.val), max(node.val, neighbor.val))
                    if edge not in edges:
                        edges.add(edge)
                        dot.edge(str(node.val), str(neighbor.val))

            self._dfs_traverse(visit)
            return dot.pipe(format="svg", encoding="utf-8")
        except (ImportError, AttributeError, graphviz.ExecutableNotFound) as e:
            return handle_graphviz_fallback(e, str(self))

    def __repr__(self) -> str:
        """Developer representation showing adjacency dict."""
        return f"GraphNode({self._get_adjacency_dict()})"

    @classmethod
    def from_adjacency_list(cls, adj_list: list[list[int]]) -> GraphNode | None:
        """
        Create a graph from adjacency list representation.

        Args:
            adj_list: List where adj_list[i] contains neighbors of node (i+1)

        Returns:
            First node of the graph, or None if empty
        """
        if not adj_list:
            return None

        # Create all nodes first
        nodes: dict[int, GraphNode] = {}
        for i in range(len(adj_list)):
            nodes[i + 1] = cls(val=i + 1)

        # Connect neighbors
        for i, neighbors in enumerate(adj_list):
            node_val = i + 1
            for neighbor_val in neighbors:
                if neighbor_val in nodes:
                    nodes[node_val].neighbors.append(nodes[neighbor_val])

        return nodes.get(1)

    @staticmethod
    def to_adjacency_list(node: GraphNode | None) -> list[list[int]]:
        """
        Convert graph to adjacency list representation.

        Args:
            node: Starting node of the graph

        Returns:
            Adjacency list where result[i] contains neighbors of node (i+1)
        """
        if node is None:
            return []

        adj_dict = node._get_adjacency_dict()
        if not adj_dict:
            return []

        max_val = max(adj_dict.keys())
        return [adj_dict.get(i + 1, []) for i in range(max_val)]
