from leetcode_py import TreeNode


class Codec:
    # Preorder with Null Markers
    # Time: O(n)
    # Space: O(n)
    def serialize(self, root: TreeNode | None) -> str:
        vals = []

        def dfs(node: TreeNode | None):
            if not node:
                vals.append("#")
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(vals)

    # Time: O(n)
    # Space: O(n)
    def deserialize(self, data: str) -> TreeNode | None:
        vals = iter(data.split(","))

        def dfs():
            val = next(vals)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


# Binary Tree Serialization Techniques

# Example Tree:
#       1
#      / \
#     2   3
#        / \
#       4   5

# 1. Preorder with Null Markers (This Implementation)
# Visit: root → left → right, mark nulls with '#'
# Result: "1,2,#,#,3,4,#,#,5,#,#"
# Pros: Self-contained, unambiguous, O(n) reconstruction
# Cons: Longer string due to null markers

# 2. Level-order (BFS) with Null Markers
# Visit level by level, mark nulls with '#'
# Result: "1,2,3,#,#,4,5"
# Pros: Simple format like preorder, level-by-level intuitive
# Cons: Still requires queue processing

# 3. Postorder with Null Markers
# Visit: left → right → root
# Result: "#,#,2,#,#,4,#,#,5,3,1"
# Pros: Bottom-up reconstruction
# Cons: Less intuitive than preorder

# 4. Inorder + Preorder (Two Arrays)
# Inorder: [2,1,4,3,5], Preorder: [1,2,3,4,5]
# Pros: Works for any binary tree structure
# Cons: Requires two arrays, only works with unique values

# 5. Parenthetical Preorder
# Same traversal as #1 but with parentheses format: value(left)(right)
# Result: "1(2()())(3(4()())(5()()))"
# Pros: Human readable structure, shows nesting clearly
# Cons: Complex parsing, verbose

# 6. Parenthetical Postorder
# Same traversal as #3 but with parentheses format: (left)(right)value
# Result: "(()()2)((()()4)(()()5)3)1"
# Pros: Bottom-up readable structure
# Cons: Even more complex parsing
