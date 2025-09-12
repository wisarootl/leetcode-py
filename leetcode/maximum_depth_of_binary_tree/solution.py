from leetcode_py import TreeNode


class Solution:

    # Time: O(n)
    # Space: O(h)
    def max_depth(self, root: TreeNode[int] | None) -> int:
        if not root:
            return 0

        left_depth = self.max_depth(root.left)
        right_depth = self.max_depth(root.right)

        return 1 + max(left_depth, right_depth)
