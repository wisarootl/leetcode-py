from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h)
    def lowest_common_ancestor(
        self, root: TreeNode[int], p: TreeNode[int], q: TreeNode[int]
    ) -> TreeNode[int]:
        result = self._lca(root, p, q)
        assert result is not None
        return result

    def _lca(
        self, root: TreeNode[int] | None, p: TreeNode[int], q: TreeNode[int]
    ) -> TreeNode[int] | None:
        if not root or root == p or root == q:
            return root

        left = self._lca(root.left, p, q)
        right = self._lca(root.right, p, q)

        if left and right:
            return root
        return left or right
