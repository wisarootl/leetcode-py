from leetcode_py import TreeNode


class Solution:

    # Time: O(n) - visit each node once
    # Space: O(h) - recursion depth + path storage, where h is tree height
    def path_sum(self, root: TreeNode[int] | None, target_sum: int) -> list[list[int]]:
        result: list[list[int]] = []

        def dfs(node: TreeNode[int] | None, remaining: int, path: list[int]) -> None:
            if not node:
                return

            # Add current node to path
            path.append(node.val)

            # Check if leaf node with target sum
            if not node.left and not node.right and remaining == node.val:
                result.append(path[:])

            # Recurse on children with updated remaining sum
            dfs(node.left, remaining - node.val, path)
            dfs(node.right, remaining - node.val, path)

            # Backtrack: remove current node from path
            path.pop()

        dfs(root, target_sum, [])
        return result
