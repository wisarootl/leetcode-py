from collections import deque

from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h)
    def right_side_view(self, root: TreeNode[int] | None) -> list[int]:
        result: list[int] = []

        def dfs(node: TreeNode[int] | None, level: int) -> None:
            if not node:
                return
            if level == len(result):
                result.append(node.val)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        dfs(root, 0)
        return result


class SolutionDFS:
    # Time: O(n)
    # Space: O(h)
    def right_side_view(self, root: TreeNode[int] | None) -> list[int]:
        if not root:
            return []

        result: list[int] = []
        stack = [(root, 0)]

        while stack:
            node, level = stack.pop()
            if level == len(result):
                result.append(node.val)
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))

        return result


class SolutionBFS:
    # Time: O(n)
    # Space: O(w)
    def right_side_view(self, root: TreeNode[int] | None) -> list[int]:
        if not root:
            return []

        result: list[int] = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i == level_size - 1:  # rightmost node
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
