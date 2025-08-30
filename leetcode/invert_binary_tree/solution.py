from leetcode_py.tree_node import TreeNode


class Solution:
    # Time: O(n) - visit each node once
    # Space: O(h) - recursion stack depth equals tree height
    def invert_tree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return root

        root.left, root.right = self.invert_tree(root.right), self.invert_tree(root.left)
        return root
