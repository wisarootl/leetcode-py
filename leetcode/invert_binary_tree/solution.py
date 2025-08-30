from leetcode_py.tree_node import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h)
    def invert_tree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None

        root.left, root.right = self.invert_tree(root.right), self.invert_tree(root.left)
        return root
