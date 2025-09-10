import pytest

from leetcode_py import TreeNode
from leetcode_py.test_utils import logged_test

from .solution import Codec


class TestSerializeAndDeserializeBinaryTree:
    def setup_method(self):
        self.codec = Codec()

    @pytest.mark.parametrize(
        "root_list",
        [
            # Original test cases
            ([1, 2, 3, None, None, 4, 5]),
            ([]),
            ([1]),
            ([1, 2]),
            ([1, None, 2]),
            ([1, 2, 3, 4, 5, 6, 7]),
            ([5, 2, 3, None, None, 2, 4, 3, 1]),
            # Edge cases
            ([0]),  # Single node with value 0
            ([-1]),  # Single node with negative value
            ([1000]),  # Single node with max value
            ([-1000]),  # Single node with min value
            # Skewed trees
            ([1, 2, None, 3, None, 4, None]),  # Left skewed
            ([1, None, 2, None, 3, None, 4]),  # Right skewed
            # Trees with negative values
            ([-5, -3, -8, -2, -1, -7, -9]),
            ([0, -1, 1, -2, None, None, 2]),
            # Larger trees
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),
            # Trees with mixed null patterns
            ([1, None, 2, None, 3, None, 4, None, 5]),
            ([1, 2, None, 3, None, 4, None, 5]),
            ([5, 4, 7, 3, None, 2, None, -1, None, 9]),
            # Duplicate values
            ([1, 1, 1, 1, 1, 1, 1]),
            ([2, 2, None, 2, None]),
            # Complex asymmetric trees
            ([10, 5, 15, None, 6, 12, 20, None, None, None, 13, 18, 25]),
            ([50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]),
        ],
    )
    @logged_test
    def test_serialize_deserialize(self, root_list: list[int | None]):
        root = TreeNode.from_list(root_list) if root_list else None
        serialized = self.codec.serialize(root)
        deserialized = self.codec.deserialize(serialized)
        if root is None:
            assert deserialized is None
        else:
            assert deserialized is not None
            assert deserialized.to_list() == root.to_list()

    @logged_test
    def test_multiple_serialize_deserialize_cycles(self):
        """Test that multiple serialize/deserialize cycles preserve the tree"""
        root_list = [1, 2, 3, None, None, 4, 5]
        root = TreeNode.from_list(root_list)

        # Perform multiple cycles
        current = root
        for _ in range(3):
            serialized = self.codec.serialize(current)
            current = self.codec.deserialize(serialized)

        assert current is not None
        assert current.to_list() == root_list

    @logged_test
    def test_serialization_format(self):
        """Test that serialization produces expected string format"""
        # Simple tree: [1, 2, 3]
        root = TreeNode.from_list([1, 2, 3])
        serialized = self.codec.serialize(root)

        # Should be preorder: root, left, right with # for null
        assert serialized == "1,2,#,#,3,#,#"

        # Empty tree
        serialized_empty = self.codec.serialize(None)
        assert serialized_empty == "#"

    @logged_test
    def test_deserialization_edge_cases(self):
        """Test deserialization with various string inputs"""
        # Single null
        assert self.codec.deserialize("#") is None

        # Single node
        single = self.codec.deserialize("42,#,#")
        assert single is not None
        assert single.val == 42
        assert single.left is None
        assert single.right is None
