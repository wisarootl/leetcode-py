from typing import Any

import pytest

from leetcode_py import TreeNode
from leetcode_py.data_structures.tree_node import build_anytree


class TestTreeNode:
    @pytest.mark.parametrize(
        "val, expected_val",
        [
            (5, 5),  # integer value
            ("hello", "hello"),  # string value
        ],
    )
    def test_init(self, val: Any, expected_val: Any) -> None:
        node = TreeNode(val)
        assert node.val == expected_val
        assert node.left is None
        assert node.right is None

    def test_init_with_children(self) -> None:
        left = TreeNode[int](1)
        right = TreeNode[int](2)
        node = TreeNode[int](0, left, right)
        assert node.val == 0
        assert node.left == left
        assert node.right == right

    def test_from_list_empty(self) -> None:
        result: TreeNode[Any] | None = TreeNode.from_list([])
        assert result is None

    def test_from_list_none_root(self) -> None:
        result = TreeNode.from_list([None])
        assert result is None

    def test_from_list_single(self) -> None:
        result = TreeNode.from_list([1])
        assert result is not None
        assert result.val == 1
        assert result.left is None
        assert result.right is None

    def test_from_list_complete_tree(self) -> None:
        result = TreeNode.from_list([1, 2, 3, 4, 5, 6, 7])
        assert result is not None
        assert result.val == 1
        assert result.left is not None
        assert result.left.val == 2
        assert result.right is not None
        assert result.right.val == 3
        assert result.left.left is not None
        assert result.left.left.val == 4
        assert result.left.right is not None
        assert result.left.right.val == 5
        assert result.right.left is not None
        assert result.right.left.val == 6
        assert result.right.right is not None
        assert result.right.right.val == 7

    def test_from_list_sparse_tree(self) -> None:
        result = TreeNode.from_list([1, None, 2])
        assert result is not None
        assert result.val == 1
        assert result.left is None
        assert result.right is not None
        assert result.right.val == 2
        assert result.right.left is None
        assert result.right.right is None

    @pytest.mark.parametrize(
        "input_list, expected_output",
        [
            ([1], [1]),
            ([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]),
            ([1, None, 2], [1, None, 2]),
            (["a", "b", "c"], ["a", "b", "c"]),
        ],
    )
    def test_to_list(self, input_list: list[Any], expected_output: list[Any]) -> None:
        node = TreeNode.from_list(input_list)
        assert node is not None
        assert node.to_list() == expected_output

    @pytest.mark.parametrize(
        "input_list, expected_values",
        [
            ([1], ["1"]),
            ([1, 2, 3], ["1", "2", "3"]),
            (["x", "y"], ["x", "y"]),
        ],
    )
    def test_str_representation(self, input_list: list[Any], expected_values: list[str]) -> None:
        node = TreeNode.from_list(input_list)
        assert node is not None
        result = str(node)
        for val in expected_values:
            assert val in result

    def test_repr_representation(self) -> None:
        node = TreeNode.from_list([1, 2, 3])
        assert node is not None
        assert repr(node) == "TreeNode([1, 2, 3])"

    def test_repr_html_generates_svg(self) -> None:
        node = TreeNode.from_list([1, 2, 3])
        assert node is not None
        result = node._repr_html_()
        assert isinstance(result, str)
        assert "svg" in result.lower()

    @pytest.mark.parametrize(
        "list1,list2, should_equal",
        [
            ([1, 2, 3], [1, 2, 3], True),
            ([1, 2, 3], [1, 3, 2], False),
        ],
    )
    def test_equality(
        self, list1: list[int | None], list2: list[int | None], should_equal: bool
    ) -> None:
        node1 = TreeNode.from_list(list1)
        node2 = TreeNode.from_list(list2)
        assert node1 is not None
        assert node2 is not None
        assert (node1 == node2) == should_equal

    @pytest.mark.parametrize("other_value", [[1], "1"])
    def test_equality_different_types(self, other_value: Any) -> None:
        node = TreeNode[int](1)
        assert node != other_value

    @pytest.mark.parametrize(
        "test_list",
        [
            [1, 2, 3, 4, 5, None, 6],
            [1],
            [1, None, 2],
            ["root", "left", "right"],
            [True, False, None, True],
        ],
    )
    def test_roundtrip_conversion(self, test_list: list[Any]) -> None:
        node = TreeNode.from_list(test_list)
        assert node is not None
        result = node.to_list()
        assert result == test_list

    def test_build_anytree_none(self) -> None:
        result = build_anytree(None)
        assert result is None

    def test_build_anytree_single_node(self) -> None:
        node = TreeNode[int](1)
        result = build_anytree(node)
        assert result is not None
        assert result.name == "1"
        assert len(result.children) == 0

    def test_str_with_none_tree(self) -> None:
        # Create a scenario where build_anytree returns None
        # This happens when we have a node but build_anytree fails
        import unittest.mock

        with unittest.mock.patch(
            "leetcode_py.data_structures.tree_node.build_anytree", return_value=None
        ):
            node = TreeNode[int](1)
            result = str(node)
            assert result == "None"
