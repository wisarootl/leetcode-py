from leetcode_py import TreeNode


class Solution:
    # Time: O(log n) average, O(n) worst case
    # Space: O(1) iterative, O(log n) recursive
    def lowest_common_ancestor(
        self, root: TreeNode[int] | None, p: TreeNode[int], q: TreeNode[int]
    ) -> TreeNode[int] | None:
        while root:
            # Both nodes are in left subtree
            if p.val < root.val and q.val < root.val:
                root = root.left
            # Both nodes are in right subtree
            elif p.val > root.val and q.val > root.val:
                root = root.right
            # Split point - one node on each side or one is the root
            else:
                return root
        return None
