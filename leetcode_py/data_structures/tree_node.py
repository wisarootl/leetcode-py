from typing import Any, Generic, TypeVar

import graphviz
from anytree import Node, RenderTree

from ._utils import handle_graphviz_fallback

# TODO: Remove TypeVar when minimum Python version is 3.12+ (use class TreeNode[T]: syntax)
T = TypeVar("T")


def build_anytree(node: "TreeNode[Any] | None", parent: Node | None = None) -> Node | None:
    if not node:
        return Node("None", parent=parent) if parent else None
    current = Node(str(node.val), parent=parent)
    if node.left or node.right:
        build_anytree(node.left, current)
        build_anytree(node.right, current)
    return current


def add_nodes(dot: graphviz.Digraph, node: "TreeNode[Any] | None", node_id: int = 0) -> int:
    if not node:
        return node_id

    dot.node(str(node_id), str(node.val))
    current_id = node_id
    next_id = node_id + 1

    if node.left:
        dot.edge(str(current_id), str(next_id))
        next_id = add_nodes(dot, node.left, next_id) + 1

    if node.right:
        dot.edge(str(current_id), str(next_id))
        next_id = add_nodes(dot, node.right, next_id) + 1

    return next_id - 1


class TreeNode(Generic[T]):
    def __init__(self, val: T, left: "TreeNode[T] | None" = None, right: "TreeNode[T] | None" = None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, arr: list[T | None]) -> "TreeNode[T] | None":
        """Convert array representation to binary tree."""
        if not arr or arr[0] is None:
            return None

        root = cls(arr[0])
        queue = [root]
        i = 1

        while queue and i < len(arr):
            node = queue.pop(0)

            if i < len(arr) and arr[i] is not None:
                left_val = arr[i]
                assert left_val is not None
                node.left = cls(left_val)
                queue.append(node.left)
            i += 1

            if i < len(arr) and arr[i] is not None:
                right_val = arr[i]
                assert right_val is not None
                node.right = cls(right_val)
                queue.append(node.right)
            i += 1

        return root

    def to_list(self) -> list[T | None]:
        """Convert binary tree to array representation."""
        result: list[T | None] = []
        queue: list[TreeNode[T] | None] = [self]

        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        # Remove trailing None values
        while result and result[-1] is None:
            result.pop()

        return result

    def __str__(self) -> str:
        tree = build_anytree(self)
        if not tree:
            return str(None)
        return "\n".join([f"{pre}{node.name}" for pre, _, node in RenderTree(tree)])

    def _repr_html_(self) -> str:
        try:
            dot = graphviz.Digraph()
            dot.attr(rankdir="TB")

            add_nodes(dot, self)
            return dot.pipe(format="svg", encoding="utf-8")
        except (ImportError, AttributeError, graphviz.ExecutableNotFound) as e:
            return handle_graphviz_fallback(e, str(self))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TreeNode):
            return False
        return self.to_list() == other.to_list()

    def find_node(self, val: T) -> "TreeNode[T] | None":
        """Find node with given value."""
        if self.val == val:
            return self
        if self.left:
            left_result = self.left.find_node(val)
            if left_result:
                return left_result
        if self.right:
            return self.right.find_node(val)
        return None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"
