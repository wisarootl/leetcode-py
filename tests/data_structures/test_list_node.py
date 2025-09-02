from typing import Any

import pytest

from leetcode_py import ListNode


class TestListNode:
    @pytest.mark.parametrize(
        "val, expected_val, expected_next",
        [
            (5, 5, None),  # with value
            ("hello", "hello", None),  # string value
        ],
    )
    def test_init(self, val: Any, expected_val: Any, expected_next: Any) -> None:
        node = ListNode(val)
        assert node.val == expected_val
        assert node.next == expected_next

    def test_init_with_next(self) -> None:
        next_node = ListNode[int](2)
        node = ListNode[int](1, next_node)
        assert node.val == 1
        assert node.next == next_node

    @pytest.mark.parametrize(
        "input_list, expected_result",
        [
            ([], None),
            ([1], "single_node"),
            ([1, 2, 3], "multiple_nodes"),
            (["a", "b"], "string_nodes"),
        ],
    )
    def test_from_list(self, input_list: list[Any], expected_result: str | None) -> None:
        result = ListNode.from_list(input_list)

        if expected_result is None:
            assert result is None
        elif expected_result == "single_node":
            assert result is not None
            assert result.val == 1
            assert result.next is None
        elif expected_result == "multiple_nodes":
            assert result is not None
            assert result.val == 1
            assert result.next is not None
            assert result.next.val == 2
            assert result.next.next is not None
            assert result.next.next.val == 3
            assert result.next.next.next is None
        elif expected_result == "string_nodes":
            assert result is not None
            assert result.val == "a"
            assert result.next is not None
            assert result.next.val == "b"
            assert result.next.next is None

    @pytest.mark.parametrize(
        "input_list, expected_output",
        [
            ([1], [1]),
            ([1, 2, 3], [1, 2, 3]),
            (["x", "y"], ["x", "y"]),
        ],
    )
    def test_to_list(self, input_list: list[Any], expected_output: list[Any]) -> None:
        node = ListNode.from_list(input_list)
        assert node is not None
        assert node.to_list() == expected_output

    @pytest.mark.parametrize(
        "input_list, expected_str, expected_repr",
        [
            ([1, 2, 3], "1 -> 2 -> 3", "ListNode([1, 2, 3])"),
            (["a", "b"], "a -> b", "ListNode(['a', 'b'])"),
        ],
    )
    def test_string_representations(
        self, input_list: list[Any], expected_str: str, expected_repr: str
    ) -> None:
        node = ListNode.from_list(input_list)
        assert node is not None
        assert str(node) == expected_str
        assert repr(node) == expected_repr

    @pytest.mark.parametrize(
        "list1,list2, should_equal",
        [
            ([1, 2, 3], [1, 2, 3], True),
            ([1, 2, 3], [1, 2, 4], False),
        ],
    )
    def test_equality(self, list1: list[int], list2: list[int], should_equal: bool) -> None:
        node1 = ListNode.from_list(list1)
        node2 = ListNode.from_list(list2)
        assert (node1 == node2) == should_equal

    @pytest.mark.parametrize("other_value", [[1], "1"])
    def test_equality_different_types(self, other_value: Any) -> None:
        node = ListNode[int](1)
        assert node != other_value

    @pytest.mark.parametrize(
        "test_list",
        [
            [1, 2, 3, 4, 5],
            [1],
            [10, 20, 30],
            ["hello", "world"],
            [True, False, True],
        ],
    )
    def test_roundtrip_conversion(self, test_list: list[Any]) -> None:
        node = ListNode.from_list(test_list)
        assert node is not None
        result = node.to_list()
        assert result == test_list

    def test_has_cycle_no_cycle(self) -> None:
        # Test linear list has no cycle
        node = ListNode.from_list([1, 2, 3])
        assert node is not None
        assert not node._has_cycle()

    def test_has_cycle_with_cycle(self) -> None:
        # Create a cycle: 1 -> 2 -> 3 -> 2 (cycle back to node 2)
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node1.next = node2
        node2.next = node3
        node3.next = node2  # Create cycle

        assert node1._has_cycle()

    def test_str_with_cycle(self) -> None:
        # Create a cycle and test string representation
        node1 = ListNode(1)
        node2 = ListNode(2)
        node1.next = node2
        node2.next = node1  # Create cycle

        result = str(node1)
        assert "-> ... (cycle back to 1)" in result

    def test_equality_with_cycles(self) -> None:
        # Create two cyclic lists
        node1 = ListNode(1)
        node2 = ListNode(2)
        node1.next = node2
        node2.next = node1  # Create cycle

        node3 = ListNode(1)
        node4 = ListNode(2)
        node3.next = node4
        node4.next = node3  # Create cycle

        # Cyclic lists should not be equal (for simplicity)
        assert node1 != node3

        # Test cyclic vs non-cyclic
        linear_node = ListNode.from_list([1, 2])
        assert node1 != linear_node
