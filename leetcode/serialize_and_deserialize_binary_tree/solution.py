from leetcode_py import TreeNode


class Codec:
    # Preorder with Null Markers
    # Time: O(n)
    # Space: O(n)
    def __init__(self) -> None:
        pass

    # Time: O(n)
    # Space: O(n)
    def serialize(self, root: TreeNode[int] | None) -> str:
        vals = []

        def dfs(node: TreeNode[int] | None):
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
    def deserialize(self, data: str) -> TreeNode[int] | None:
        vals = iter(data.split(","))

        def dfs():
            val = next(vals)
            if val == "#":
                return None
            node = TreeNode[int](int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
