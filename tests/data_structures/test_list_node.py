import pytest

from leetcode_py import ListNode


class TestListNode:
    @pytest.mark.parametrize(
        "val,expected_val,expected_next",
        [
            (None, 0, None),  # default
            (5, 5, None),  # with value
        ],
    )
    def test_init(self, val, expected_val, expected_next):
        node = ListNode() if val is None else ListNode(val)
        assert node.val == expected_val
        assert node.next == expected_next

    def test_init_with_next(self):
        next_node = ListNode(2)
        node = ListNode(1, next_node)
        assert node.val == 1
        assert node.next == next_node

    @pytest.mark.parametrize(
        "input_list,expected_result",
        [
            ([], None),
            ([1], "single_node"),
            ([1, 2, 3], "multiple_nodes"),
        ],
    )
    def test_from_list(self, input_list, expected_result):
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

    @pytest.mark.parametrize(
        "input_list,expected_output",
        [
            ([1], [1]),
            ([1, 2, 3], [1, 2, 3]),
        ],
    )
    def test_to_list(self, input_list, expected_output):
        node = ListNode.from_list(input_list)
        assert node is not None
        assert node.to_list() == expected_output

    @pytest.mark.parametrize(
        "input_list,expected_str,expected_repr",
        [
            ([1, 2, 3], "1 -> 2 -> 3", "ListNode([1, 2, 3])"),
        ],
    )
    def test_string_representations(self, input_list, expected_str, expected_repr):
        node = ListNode.from_list(input_list)
        assert node is not None
        assert str(node) == expected_str
        assert repr(node) == expected_repr
        assert node._repr_html_() == expected_str

    @pytest.mark.parametrize(
        "list1,list2,should_equal",
        [
            ([1, 2, 3], [1, 2, 3], True),
            ([1, 2, 3], [1, 2, 4], False),
        ],
    )
    def test_equality(self, list1, list2, should_equal):
        node1 = ListNode.from_list(list1)
        node2 = ListNode.from_list(list2)
        assert (node1 == node2) == should_equal

    @pytest.mark.parametrize("other_value", [[1], "1"])
    def test_equality_different_types(self, other_value):
        node = ListNode(1)
        assert node != other_value

    @pytest.mark.parametrize(
        "test_list",
        [
            [1, 2, 3, 4, 5],
            [1],
            [10, 20, 30],
        ],
    )
    def test_roundtrip_conversion(self, test_list):
        node = ListNode.from_list(test_list)
        assert node is not None
        result = node.to_list()
        assert result == test_list
