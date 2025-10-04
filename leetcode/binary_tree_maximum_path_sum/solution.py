from leetcode_py import TreeNode


class Solution:

    # Time: O(n) where n is the number of nodes
    # Space: O(h) where h is the height of the tree (recursion stack)
    def max_path_sum(self, root: TreeNode[int] | None) -> int:
        """
        Find the maximum path sum in a binary tree.

        A path is a sequence of nodes where each pair of adjacent nodes
        has an edge connecting them. A node can only appear once in the path.
        The path doesn't need to pass through the root.

        Uses DFS with post-order traversal to calculate:
        1. Maximum path sum that can be extended upward from current node
        2. Maximum path sum that includes current node as the highest point
        """
        if not root:
            return 0

        max_sum = float("-inf")

        def dfs(node: TreeNode[int] | None) -> int:
            nonlocal max_sum

            if not node:
                return 0

            # Get maximum path sum from left and right subtrees
            # If negative, we don't include them (take 0 instead)
            left_max = max(0, dfs(node.left))
            right_max = max(0, dfs(node.right))

            # Current path sum if this node is the highest point
            # (left path + current node + right path)
            current_path_sum = node.val + left_max + right_max

            # Update global maximum
            max_sum = max(max_sum, current_path_sum)

            # Return maximum path sum that can be extended upward
            # (either left or right path + current node)
            return node.val + max(left_max, right_max)

        dfs(root)
        return int(max_sum)
