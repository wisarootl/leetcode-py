from leetcode_py import TreeNode


class Solution:

    # Inorder Recursive
    # Time: O(k)
    # Space: O(h)
    def kth_smallest(self, root: TreeNode[int] | None, k: int) -> int:
        def inorder(node: TreeNode[int] | None):
            if not node:
                return
            yield from inorder(node.left)
            yield node.val
            yield from inorder(node.right)

        for i, val in enumerate(inorder(root)):
            if i == k - 1:
                return val

        raise ValueError(f"Tree has fewer than {k} nodes")


# Binary Tree Traversal Patterns
#
# def inorder(node):
#     if node:
#         inorder(node.left)
#         print(node.val)
#         inorder(node.right)
#
# def preorder(node):
#     if node:
#         print(node.val)
#         preorder(node.left)
#         preorder(node.right)
#
# def postorder(node):
#     if node:
#         postorder(node.left)
#         postorder(node.right)
#         print(node.val)
