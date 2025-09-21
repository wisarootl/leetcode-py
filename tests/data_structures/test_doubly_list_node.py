from typing import Any

import pytest

from leetcode_py.data_structures.doubly_list_node import DoublyListNode


class TestDoublyListNode:
    @pytest.mark.parametrize(
        "val, expected_val, expected_prev, expected_next",
        [
            (5, 5, None, None),
            ("hello", "hello", None, None),
        ],
    )
    def test_init(self, val: Any, expected_val: Any, expected_prev: Any, expected_next: Any) -> None:
        node = DoublyListNode(val)
        assert node.val == expected_val
        assert node.prev == expected_prev
        assert node.next == expected_next

    def test_init_with_prev_next(self) -> None:
        prev_node = DoublyListNode[int](1)
        next_node = DoublyListNode[int](3)
        node = DoublyListNode[int](2, prev_node, next_node)
        assert node.val == 2
        assert node.prev == prev_node
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
        result = DoublyListNode.from_list(input_list)

        if expected_result is None:
            assert result is None
        elif expected_result == "single_node":
            assert result is not None
            assert result.val == 1
            assert result.prev is None
            assert result.next is None
        elif expected_result == "multiple_nodes":
            assert result is not None
            assert result.val == 1
            assert result.prev is None
            assert result.next is not None
            assert result.next.val == 2
            assert result.next.prev == result
            assert result.next.next is not None
            assert result.next.next.val == 3
            assert result.next.next.prev == result.next
            assert result.next.next.next is None
        elif expected_result == "string_nodes":
            assert result is not None
            assert result.val == "a"
            assert result.prev is None
            assert result.next is not None
            assert result.next.val == "b"
            assert result.next.prev == result
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
        node = DoublyListNode.from_list(input_list)
        assert node is not None
        assert node.to_list() == expected_output

    @pytest.mark.parametrize(
        "input_list, expected_str, expected_repr",
        [
            ([1, 2, 3], "1 <-> 2 <-> 3", "DoublyListNode([1, 2, 3])"),
            (["a", "b"], "a <-> b", "DoublyListNode(['a', 'b'])"),
        ],
    )
    def test_string_representations(
        self, input_list: list[Any], expected_str: str, expected_repr: str
    ) -> None:
        node = DoublyListNode.from_list(input_list)
        assert node is not None
        assert str(node) == expected_str
        assert repr(node) == expected_repr

    @pytest.mark.parametrize(
        "list1, list2, should_equal",
        [
            ([1, 2, 3], [1, 2, 3], True),
            ([1, 2, 3], [1, 2, 4], False),
        ],
    )
    def test_equality(self, list1: list[int], list2: list[int], should_equal: bool) -> None:
        node1 = DoublyListNode.from_list(list1)
        node2 = DoublyListNode.from_list(list2)
        assert (node1 == node2) == should_equal

    @pytest.mark.parametrize("other_value", [[1], "1"])
    def test_equality_different_types(self, other_value: Any) -> None:
        node = DoublyListNode[int](1)
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
        node = DoublyListNode.from_list(test_list)
        assert node is not None
        result = node.to_list()
        assert result == test_list

    def test_has_cycle_no_cycle(self) -> None:
        node = DoublyListNode.from_list([1, 2, 3])
        assert node is not None
        assert not node._has_cycle()

    def test_has_cycle_with_cycle(self) -> None:
        node1 = DoublyListNode(1)
        node2 = DoublyListNode(2)
        node3 = DoublyListNode(3)
        node1.next = node2
        node2.prev = node1
        node2.next = node3
        node3.prev = node2
        node3.next = node2  # Create cycle

        assert node1._has_cycle()

    def test_str_with_cycle(self) -> None:
        node1 = DoublyListNode(1)
        node2 = DoublyListNode(2)
        node1.next = node2
        node2.prev = node1
        node2.next = node1  # Create cycle

        result = str(node1)
        assert "<-> ... (cycle back to 1)" in result

    def test_equality_with_cycles(self) -> None:
        node1 = DoublyListNode(1)
        node2 = DoublyListNode(2)
        node1.next = node2
        node2.prev = node1
        node2.next = node1  # Create cycle

        node3 = DoublyListNode(1)
        node4 = DoublyListNode(2)
        node3.next = node4
        node4.prev = node3
        node4.next = node3  # Create cycle

        assert node1 != node3

        linear_node = DoublyListNode.from_list([1, 2])
        assert node1 != linear_node

    def test_to_list_with_cycle(self) -> None:
        node1 = DoublyListNode(1)
        node2 = DoublyListNode(2)
        node1.next = node2
        node2.prev = node1
        node2.next = node1  # Create cycle

        result = node1.to_list()
        assert result == [1, 2]

    def test_str_long_list(self) -> None:
        long_list = list(range(1001))
        node = DoublyListNode.from_list(long_list)
        assert node is not None
        result = str(node)
        assert "<-> ... (long list)" in result

    def test_repr_html_no_graphviz(self, monkeypatch) -> None:
        node = DoublyListNode.from_list([1, 2, 3])
        assert node is not None

        # Mock graphviz.Digraph to raise ImportError
        def mock_digraph(*args, **kwargs):
            raise ImportError("No module named 'graphviz'")

        monkeypatch.setattr(
            "leetcode_py.data_structures.doubly_list_node.graphviz.Digraph", mock_digraph
        )
        result = node._repr_html_()
        assert "<pre>" in result
        assert "1 <-> 2 <-> 3" in result

    def test_repr_html_with_graphviz(self) -> None:
        node = DoublyListNode.from_list([1, 2])
        assert node is not None

        result = node._repr_html_()
        assert isinstance(result, str)
        # Either SVG rendering works or fallback to text
        if "<svg" in result or "svg" in result.lower():
            # Graphviz worked successfully
            assert True
        elif "<pre>" in result:
            # Fallback was used (graphviz executable not found) - this is expected
            assert "1 <-> 2" in result
        else:
            pytest.fail("Unexpected HTML output format")

    def test_repr_html_with_cycle(self) -> None:
        node1 = DoublyListNode(1)
        node2 = DoublyListNode(2)
        node1.next = node2
        node2.prev = node1
        node2.next = node1  # Create cycle

        result = node1._repr_html_()
        assert isinstance(result, str)
        # Either SVG rendering works or fallback to text
        if "<svg" in result or "svg" in result.lower():
            # Graphviz worked successfully
            assert True
        elif "<pre>" in result:
            # Fallback was used (graphviz executable not found) - this is expected
            assert "<-> ... (cycle back to 1)" in result
        else:
            pytest.fail("Unexpected HTML output format")
