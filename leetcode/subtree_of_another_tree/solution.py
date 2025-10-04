from leetcode_py import TreeNode


class Solution:

    # Time: O(m * n) - where m is nodes in root, n is nodes in sub_root
    # Space: O(h) - where h is height of root tree (recursion stack)
    def is_subtree(self, root: TreeNode[int] | None, sub_root: TreeNode[int] | None) -> bool:
        """
        Check if sub_root is a subtree of root.
        Uses DFS to check every node in root as potential subtree root.
        """
        if not sub_root:
            return True
        if not root:
            return False

        # Check if current root matches sub_root
        if self._is_same_tree(root, sub_root):
            return True

        # Recursively check left and right subtrees
        return self.is_subtree(root.left, sub_root) or self.is_subtree(root.right, sub_root)

    def _is_same_tree(self, p: TreeNode[int] | None, q: TreeNode[int] | None) -> bool:
        """Helper method to check if two trees are identical."""
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return self._is_same_tree(p.left, q.left) and self._is_same_tree(p.right, q.right)
