from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h)
    def is_balanced(self, root: TreeNode | None) -> bool:
        def height(node: TreeNode | None) -> int:
            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        return height(root) != -1
