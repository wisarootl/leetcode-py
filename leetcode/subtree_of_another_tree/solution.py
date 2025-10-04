from leetcode_py import TreeNode


class Solution:

    # Time: O(m * n) - where m is nodes in root, n is nodes in subRoot
    # Space: O(h) - where h is height of root tree (recursion stack)
    def is_subtree(self, root: TreeNode[int] | None, subRoot: TreeNode[int] | None) -> bool:
        """
        Check if subRoot is a subtree of root.
        Uses DFS to check every node in root as potential subtree root.
        """
        if not subRoot:
            return True
        if not root:
            return False

        # Check if current root matches subRoot
        if self._is_same_tree(root, subRoot):
            return True

        # Recursively check left and right subtrees
        return self.is_subtree(root.left, subRoot) or self.is_subtree(root.right, subRoot)

    def _is_same_tree(self, p: TreeNode[int] | None, q: TreeNode[int] | None) -> bool:
        """Helper method to check if two trees are identical."""
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return self._is_same_tree(p.left, q.left) and self._is_same_tree(p.right, q.right)
