from collections import deque

from leetcode_py import TreeNode

# Note: "Fringe" is the general CS term for the data structure holding nodes to be explored.
# Stack (LIFO) → DFS, Queue (FIFO) → BFS, Priority Queue → A*/Best-first search


class Solution:
    # DFS recursive
    # Time: O(n)
    # Space: O(h) where h is height of tree
    def invert_tree(self, root: TreeNode[int] | None) -> TreeNode[int] | None:
        if not root:
            return None

        root.left, root.right = self.invert_tree(root.right), self.invert_tree(root.left)
        return root


class SolutionDFS:
    # DFS iterative
    # Time: O(n)
    # Space: O(h) where h is height of tree
    def invert_tree(self, root: TreeNode[int] | None) -> TreeNode[int] | None:
        if not root:
            return None

        stack: list[TreeNode[int] | None] = [root]
        while stack:
            node = stack.pop()
            if node is None:
                continue
            node.left, node.right = node.right, node.left

            stack.append(node.left)
            stack.append(node.right)

        return root


class SolutionBFS:
    # Time: O(n)
    # Space: O(w) where w is maximum width of tree
    def invert_tree(self, root: TreeNode[int] | None) -> TreeNode[int] | None:
        if not root:
            return None

        queue: deque[TreeNode[int] | None] = deque([root])
        while queue:
            node = queue.popleft()
            if node is None:
                continue
            node.left, node.right = node.right, node.left

            queue.append(node.left)
            queue.append(node.right)

        return root
