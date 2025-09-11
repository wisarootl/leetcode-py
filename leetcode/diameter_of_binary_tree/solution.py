from leetcode_py import TreeNode


class Solution:

    # Time: O(n)
    # Space: O(h)
    def diameter_of_binary_tree(self, root: TreeNode[int] | None) -> int:
        self.max_diameter = 0

        def dfs(node: TreeNode[int] | None) -> int:
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.max_diameter = max(self.max_diameter, left + right)

            return max(left, right) + 1

        dfs(root)
        return self.max_diameter
