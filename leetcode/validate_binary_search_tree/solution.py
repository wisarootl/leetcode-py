from collections import deque

from leetcode_py import TreeNode


class Solution:

    @classmethod
    def validate(cls, node: TreeNode[int] | None, min_val: float, max_val: float) -> bool:
        if not node:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False
        return cls.validate(node.left, min_val, node.val) and cls.validate(node.right, node.val, max_val)

    # Time: O(n)
    # Space: O(h)
    def is_valid_bst(self, root: TreeNode[int] | None) -> bool:
        return self.validate(root, float("-inf"), float("inf"))


class SolutionDFS:
    # Time: O(n)
    # Space: O(h)
    def is_valid_bst(self, root: TreeNode[int] | None) -> bool:
        if not root:
            return True

        stack = [(root, float("-inf"), float("inf"))]

        while stack:
            node, min_val, max_val = stack.pop()
            if node.val <= min_val or node.val >= max_val:
                return False
            if node.right:
                stack.append((node.right, node.val, max_val))
            if node.left:
                stack.append((node.left, min_val, node.val))

        return True


class SolutionBFS:
    # Time: O(n)
    # Space: O(w) where w is max width
    def is_valid_bst(self, root: TreeNode[int] | None) -> bool:
        if not root:
            return True

        queue = deque([(root, float("-inf"), float("inf"))])

        while queue:
            node, min_val, max_val = queue.popleft()
            if node.val <= min_val or node.val >= max_val:
                return False
            if node.right:
                queue.append((node.right, node.val, max_val))
            if node.left:
                queue.append((node.left, min_val, node.val))

        return True
