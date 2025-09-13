from leetcode_py import TreeNode


class Solution:
    """
    Construct Binary Tree from Preorder and Inorder Traversal

    Algorithm Explanation:
    - Preorder: Root -> Left -> Right (first element is always root)
    - Inorder: Left -> Root -> Right (root splits left/right subtrees)

    Example: preorder=[3,9,20,15,7], inorder=[9,3,15,20,7]

    Step 1: Root = 3 (first in preorder)
            Find 3 in inorder at index 1
            Left subtree: inorder[0:1] = [9]
            Right subtree: inorder[2:] = [15,20,7]

    Step 2: Build left subtree with preorder=[9], inorder=[9]
            Root = 9, no children

    Step 3: Build right subtree with preorder=[20,15,7], inorder=[15,20,7]
            Root = 20, left=[15], right=[7]

    Final tree:
           3
          / \
         9   20
            /  \
           15   7
    """

    # Time: O(n) - hashmap lookup O(1) for each of n nodes
    # Space: O(n) - hashmap + recursion stack
    def build_tree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder or not inorder:
            return None

        inorder_map = {val: i for i, val in enumerate(inorder)}
        self.preorder_index = 0

        def build(left: int, right: int) -> TreeNode | None:
            # left, right: boundaries in inorder array for current subtree
            if left > right:
                return None

            root_val = preorder[self.preorder_index]
            self.preorder_index += 1
            root = TreeNode(root_val)

            mid = inorder_map[root_val]  # root position in inorder
            # Left subtree: inorder[left:mid-1]
            root.left = build(left, mid - 1)
            # Right subtree: inorder[mid+1:right]
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)
