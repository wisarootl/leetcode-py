from leetcode_py import TreeNode


class Solution:

    # Time: O(min(m, n)) where m and n are the number of nodes in the two trees
    # Space: O(min(m, n)) for the recursion stack
    def is_same_tree(self, p: TreeNode[int] | None, q: TreeNode[int] | None) -> bool:
        # Base case: both nodes are None
        if p is None and q is None:
            return True

        # Base case: one node is None, the other is not
        if p is None or q is None:
            return False

        # Check if current nodes have the same value
        if p.val != q.val:
            return False

        # Recursively check left and right subtrees
        return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)
