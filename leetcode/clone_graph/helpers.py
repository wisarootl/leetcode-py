from leetcode_py import GraphNode


def run_clone_graph(solution_class: type, adj_list: list[list[int]]):
    node = GraphNode.from_adjacency_list(adj_list)
    implementation = solution_class()
    return implementation.clone_graph(node)


def assert_clone_graph(result: GraphNode | None, adj_list: list[list[int]]) -> bool:
    original = GraphNode.from_adjacency_list(adj_list)
    if result is None:
        assert original is None
    else:
        assert result.is_clone(original)
    return True
