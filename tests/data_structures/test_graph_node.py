import pytest

from leetcode_py.data_structures.graph_node import GraphNode


class TestGraphNode:
    @pytest.mark.parametrize(
        "val, neighbors, expected_val, expected_neighbors",
        [
            (None, None, 0, []),
            (5, None, 5, []),
            (1, [GraphNode(2)], 1, 1),  # 1 neighbor count
        ],
    )
    def test_init(self, val, neighbors, expected_val, expected_neighbors) -> None:
        if val is None:
            node = GraphNode()
        elif neighbors is None:
            node = GraphNode(val)
        else:
            node = GraphNode(val, neighbors)

        assert node.val == expected_val
        if isinstance(expected_neighbors, int):
            assert len(node.neighbors) == expected_neighbors
        else:
            assert node.neighbors == expected_neighbors

    def test_repr(self) -> None:
        node1 = GraphNode(1)
        node2 = GraphNode(2)
        node1.neighbors = [node2]
        node2.neighbors = [node1]
        assert repr(node1) == "GraphNode({1: [2], 2: [1]})"

    def test_str(self) -> None:
        node1 = GraphNode(1)
        node2 = GraphNode(2)
        node1.neighbors = [node2]
        node2.neighbors = [node1]
        expected = "{1: [2], 2: [1]}"
        assert str(node1) == expected

    @pytest.mark.parametrize(
        "val1, val2, expected",
        [
            (1, 1, True),
            (1, 2, False),
        ],
    )
    def test_eq_single_nodes(self, val1, val2, expected) -> None:
        node1 = GraphNode(val1)
        node2 = GraphNode(val2)
        assert (node1 == node2) == expected

    @pytest.mark.parametrize("other", ["not a node", 1, None])
    def test_eq_with_non_graph_node(self, other) -> None:
        node = GraphNode(1)
        assert node != other

    def test_eq_simple_graph(self) -> None:
        # Graph 1: 1-2
        node1_a = GraphNode(1)
        node2_a = GraphNode(2)
        node1_a.neighbors = [node2_a]
        node2_a.neighbors = [node1_a]

        # Graph 2: 1-2
        node1_b = GraphNode(1)
        node2_b = GraphNode(2)
        node1_b.neighbors = [node2_b]
        node2_b.neighbors = [node1_b]

        assert node1_a == node1_b

    def test_eq_different_neighbor_count(self) -> None:
        node1_a = GraphNode(1)
        node2_a = GraphNode(2)
        node1_a.neighbors = [node2_a]

        node1_b = GraphNode(1)
        node2_b = GraphNode(2)
        node3_b = GraphNode(3)
        node1_b.neighbors = [node2_b, node3_b]

        assert node1_a != node1_b

    @pytest.mark.parametrize(
        "adj_list, expected_val, expected_neighbors",
        [
            ([], None, None),
            ([[]], 1, []),
            ([[2], [1]], 1, [2]),
            ([[2, 4], [1, 3], [2, 4], [1, 3]], 1, [2, 4]),
        ],
    )
    def test_from_adjacency_list(self, adj_list, expected_val, expected_neighbors) -> None:
        result = GraphNode.from_adjacency_list(adj_list)

        if expected_val is None:
            assert result is None
        else:
            assert result is not None
            assert result.val == expected_val
            if expected_neighbors == []:
                assert result.neighbors == []
            else:
                neighbor_vals = sorted([n.val for n in result.neighbors])
                assert neighbor_vals == expected_neighbors

    @pytest.mark.parametrize(
        "node, expected",
        [
            (None, []),
            (GraphNode(1), [[]]),
        ],
    )
    def test_to_adjacency_list(self, node, expected) -> None:
        result = GraphNode.to_adjacency_list(node)
        assert result == expected

    def test_to_adjacency_list_two_nodes(self) -> None:
        node1 = GraphNode(1)
        node2 = GraphNode(2)
        node1.neighbors = [node2]
        node2.neighbors = [node1]

        result = GraphNode.to_adjacency_list(node1)
        assert result == [[2], [1]]

    @pytest.mark.parametrize(
        "original",
        [
            [],
            [[]],
            [[2], [1]],
            [[2, 4], [1, 3], [2, 4], [1, 3]],
        ],
    )
    def test_roundtrip_conversion(self, original) -> None:
        graph = GraphNode.from_adjacency_list(original)
        result = GraphNode.to_adjacency_list(graph)
        assert result == original

    def test_cycle_handling(self) -> None:
        # Create a cycle: 1-2-3-1
        node1 = GraphNode(1)
        node2 = GraphNode(2)
        node3 = GraphNode(3)

        node1.neighbors = [node2]
        node2.neighbors = [node1, node3]
        node3.neighbors = [node2, node1]

        # Should not infinite loop
        adj_list = GraphNode.to_adjacency_list(node1)
        assert len(adj_list) == 3

        # Recreate and compare
        recreated = GraphNode.from_adjacency_list(adj_list)
        assert node1 == recreated

    @pytest.mark.parametrize(
        "original, clone, expected",
        [
            (None, None, False),  # None case
            (GraphNode(1), None, False),  # Clone is None
        ],
    )
    def test_is_clone_edge_cases(self, original, clone, expected) -> None:
        if original is None:
            # Can't call is_clone on None
            assert True
        else:
            assert original.is_clone(clone) == expected

    def test_is_clone_same_object(self) -> None:
        # Same object should not be a clone
        node = GraphNode(1)
        assert not node.is_clone(node)

    def test_is_clone_different_structure(self) -> None:
        # Different structures should not be clones
        node1 = GraphNode(1)
        node2 = GraphNode(2)
        assert not node1.is_clone(node2)

    def test_is_clone_proper_clone(self) -> None:
        # Create original graph: 1-2
        original1 = GraphNode(1)
        original2 = GraphNode(2)
        original1.neighbors = [original2]
        original2.neighbors = [original1]

        # Create clone: 1-2 (different objects)
        clone1 = GraphNode(1)
        clone2 = GraphNode(2)
        clone1.neighbors = [clone2]
        clone2.neighbors = [clone1]

        assert original1.is_clone(clone1)

    def test_is_clone_complex_graph(self) -> None:
        # Create triangle: 1-2-3-1
        original1 = GraphNode(1)
        original2 = GraphNode(2)
        original3 = GraphNode(3)
        original1.neighbors = [original2, original3]
        original2.neighbors = [original1, original3]
        original3.neighbors = [original1, original2]

        # Create clone
        clone1 = GraphNode(1)
        clone2 = GraphNode(2)
        clone3 = GraphNode(3)
        clone1.neighbors = [clone2, clone3]
        clone2.neighbors = [clone1, clone3]
        clone3.neighbors = [clone1, clone2]

        assert original1.is_clone(clone1)

    def test_repr_html(self) -> None:
        # Test _repr_html_ method
        node1 = GraphNode(1)
        node2 = GraphNode(2)
        node1.neighbors = [node2]
        node2.neighbors = [node1]

        result = node1._repr_html_()
        assert isinstance(result, str)
        # Should return SVG content from graphviz

    def test_from_adjacency_list_invalid_neighbor(self) -> None:
        # Test adjacency list with invalid neighbor reference
        adj_list = [[2, 5], [1]]  # Node 1 references non-existent node 5
        result = GraphNode.from_adjacency_list(adj_list)
        assert result is not None
        assert result.val == 1
        # Should only have valid neighbors
        neighbor_vals = [n.val for n in result.neighbors]
        assert 2 in neighbor_vals
        assert 5 not in neighbor_vals  # Invalid neighbor should be skipped
