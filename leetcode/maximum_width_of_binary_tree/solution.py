from collections import deque

from leetcode_py import TreeNode


class Solution:

    # Time: O(n)
    # Space: O(w) where w is maximum width
    def width_of_binary_tree(self, root: TreeNode[int] | None) -> int:
        if not root:
            return 0

        max_width = 1
        queue = deque([(root, 0)])

        while queue:
            level_size = len(queue)
            _, first_pos = queue[0]
            last_pos = first_pos

            for _ in range(level_size):
                node, pos = queue.popleft()
                last_pos = pos

                if node.left:
                    queue.append((node.left, 2 * pos))
                if node.right:
                    queue.append((node.right, 2 * pos + 1))

            max_width = max(max_width, last_pos - first_pos + 1)

        return max_width
